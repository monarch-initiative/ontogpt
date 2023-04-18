"""
Uses code-davinci-002.

Note also that fine-tuning can't be done with code-davinci-002, see:
https://community.openai.com/t/finetuning-code-davinci/23132/2
"""
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import openai
import pydantic
import tiktoken
import yaml
from linkml.utils.schema_fixer import uncamel
from linkml_runtime.utils.formatutils import camelcase
from oaklib.datamodels.obograph import Graph
from oaklib.datamodels.vocabulary import IS_A
from oaklib.interfaces.obograph_interface import OboGraphInterface
from tiktoken import Encoding

from ontogpt.clients import OpenAIClient
from ontogpt.engines.knowledge_engine import FIELD, KnowledgeEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.templates.halo import Ontology, OntologyElement

this_path = Path(__file__).parent
logger = logging.getLogger(__name__)


ELEMENT_NAME = str

INSTRUCTIONS = """
## Instructions:
## Add an additional element to the YAML below, which is for elements
## in an industrial ontology. Complete as far as possible the following
## fields:
"""


class StructuredPrompt(pydantic.BaseModel):
    header: str = None
    body: str = None
    main_prompt: str = None

    @property
    def text(self) -> str:
        return f"{self.header}\n{self.body}\n{self.main_prompt}"


@dataclass
class HALOEngine(KnowledgeEngine):
    """Engine for Hallucinating Latent Ontologies."""

    engine: str = "code-davinci-002"
    ontology: Ontology = None
    traverse_slots: List[FIELD] = field(
        default_factory=lambda: ["subtypes", "parts", "subclass_of", "part_of"]
    )
    fixed_slot_values: Dict[str, str] = None
    adapter: OboGraphInterface = None
    visited: Set[ELEMENT_NAME] = field(default_factory=lambda: set())
    candidates: List[ELEMENT_NAME] = None
    always_extend: bool = False
    expand_horizon: bool = False

    element_scores: Dict[ELEMENT_NAME, float] = field(default_factory=lambda: {})
    """Ranks each element by estimated informativeness for training."""

    tokenizer_encoding: Encoding = field(default_factory=lambda: tiktoken.get_encoding("gpt2"))

    def __post_init__(self):
        self.template_class = self._get_template_class("halo.OntologyElement")
        self.client = OpenAIClient(model=self.engine)
        self.api_key = self._get_openai_api_key()
        openai.api_key = self.api_key

    def seed(self, seed_ontology: Ontology):
        """Seed the engine with an initial ontology.

        :param seed_ontology:
        :return:
        """
        self.ontology = seed_ontology
        if not self.expand_horizon:
            self.visited = {x.name for x in self.ontology.elements}

    def seed_from_file(self, file_path: str) -> Ontology:
        """Seed the engine with an initial ontology from a file.

        :param file_path:
        :return:
        """
        ontology = Ontology(**yaml.safe_load(open(file_path)))
        self.seed(ontology)
        logger.info(f"Seeded with {len(ontology.elements)} elements")
        return ontology

    def hallucinate(
        self, seed_elements: List[ELEMENT_NAME] = None, num_iterations=10
    ) -> List[OntologyElement]:
        """Run the HALO engine for a given number of iterations.

        Each iteration will expand the initial seed ontology.

        :param num_iterations:
        :return:
        """
        added = []
        if seed_elements:
            for e in seed_elements:
                added.append(self.hallucinate_element(e))
        for i in range(num_iterations):
            logger.info(f"Running HALO iteration {i}")
            elt = self.hallucinate_once()
            if elt:
                added.append(elt)
            else:
                break
        return added

    def hallucinate_once(self) -> Optional[OntologyElement]:
        """Run the HALO engine once.

        Finds a candidate element to expand,
        then runs HALO on that element by generating
        a prompt for it.

        :return:
        """
        candidate_elements = self.get_candidate_elements()
        logger.info(f"Found {len(candidate_elements)} candidate elements")
        logger.info(f"Candidate elements: {candidate_elements}  // visited={self.visited}")
        if not candidate_elements:
            return None
        element = candidate_elements[0]
        logger.info(f"Selected element {element}")
        return self.hallucinate_element(element)

    def get_candidate_elements(self) -> List[ELEMENT_NAME]:
        """Get candidate elements to expand.

        Has side effect of removing candidate cache if visited
        :return:
        """
        if self.candidates is None:
            # TODO: exclude seed set that is not on the horizon
            self.candidates = [x.name for x in self.ontology.elements]
        self.candidates = [c for c in self.candidates if c not in self.visited]
        return self.candidates

    def extend_candidates(self, elements: List[ELEMENT_NAME]) -> List[ELEMENT_NAME]:
        """Extend candidates by all entities in the signature of the specified elements.

        :return:
        """
        visited = self.visited
        if not self.traverse_slots:
            raise ValueError("No slots to traverse")
        for element_name in elements:
            visited.add(element_name)
            logger.info(f"Extending candidates for {element_name}; visited={visited}")
            element = self.get_element(element_name)
            for slot_name in self.traverse_slots:
                refs = getattr(element, slot_name)
                for ref in refs:
                    if ref not in visited:
                        if not self.candidates:
                            self.candidates = []
                        self.candidates.append(ref)
                        logger.info(f" -- Added {ref} to candidates")
        return self.candidates

    def get_element(self, element_name: ELEMENT_NAME) -> Optional[OntologyElement]:
        """Get an element by name.

        :param element_name:
        :return:
        """
        for e in self.ontology.elements:
            if e.name == element_name:
                return e

    def old_get_candidate_elements(self) -> List[ELEMENT_NAME]:
        """Get candidate elements for HALO.

        :return:
        """
        candidate_elements = set()
        visited = self.visited
        if not self.traverse_slots:
            raise ValueError("No slots to traverse")
        for element in self.ontology.elements:
            all_slots_have_refs = True
            for slot_name in self.traverse_slots:
                refs = getattr(element, slot_name)
                if len(refs) == 0 and element.name not in visited:
                    candidate_elements.add(element.name)
                    all_slots_have_refs = False
                for ref in refs:
                    if ref not in visited:
                        candidate_elements.add(ref)
                        visited.add(ref)
            if all_slots_have_refs and not self.always_extend:
                visited.add(element.name)
        return list(candidate_elements)

    def hallucinate_element(self, element: ELEMENT_NAME) -> OntologyElement:
        """Generate an ontology element based on its name.

        :param element: example: LeftDigit1OfHand
        :return:
        """
        logger.info(f"Hallucinating element {element}")
        example_elements = self.get_example_elements(element)
        example_element_names = [x.name for x in example_elements]
        logger.info(f"Found {len(example_elements)} example elements: {example_element_names}")
        # TODO: set bound dynamically
        prompt = self.generate_prompt(element, example_elements[0:10])
        # logger.info(f"Generated prompt: {prompt}")
        payload = self.client.complete(prompt.text)
        objs = self.integrate_payload(prompt, payload)
        logger.info(f"Integrated {len(objs)} objects")
        obj = objs[0]
        self.extend_candidates([obj.name])
        return obj

    def get_example_elements(self, element: ELEMENT_NAME) -> List[OntologyElement]:
        """Get example elements for HALO.

        :param element:
        :return:
        """
        name = uncamel(element)
        toks = set(self.tokenizer_encoding.encode(name))
        score_element_pairs = [(self.get_element_score(e, toks), e) for e in self.ontology.elements]
        score_element_pairs.sort(key=lambda x: x[0], reverse=True)
        logger.info(f"Scores[{element}: {[x for x, _ in score_element_pairs]}")
        logger.info(f"Sorted elements: {score_element_pairs}")
        return [x for _, x in score_element_pairs]

    def get_element_score(self, element: OntologyElement, tokens: Set[int]) -> float:
        """Calculate a score for an element based on how informative it is for few-shot learning.

        :param element:
        :param tokens: tokenized form of the element name
        :return:
        """
        element_name = element.name
        if element_name in self.element_scores:
            score = self.element_scores[element_name]
        else:
            score = 0
            for _, v in element.dict().items():
                if v:
                    score += 1
            self.element_scores[element_name] = score
        element_tokens = set(self.tokenizer_encoding.encode(element_name))
        jaccard = len(tokens.intersection(element_tokens)) / len(tokens.union(element_tokens))
        return score / 100 + jaccard

    def generate_prompt(
        self, seed_element: ELEMENT_NAME, example_elements: List[OntologyElement]
    ) -> StructuredPrompt:
        """Generate a prompt for HALO.

        :param seed_element:
        :param example_elements:
        :return:
        """
        prompt = StructuredPrompt()
        prompt.header = INSTRUCTIONS
        for slot in self.schemaview.class_induced_slots("OntologyElement"):
            desc = slot.description
            if not desc:
                logger.warning(f"No description for slot {slot.name}")
                desc = ""
            prompt.header += f"## {slot.name}: {desc}\n"
        prompt.body = "\n## Examples:\n"
        for element in example_elements:
            prompt.body += dump_minimal_yaml(element)
        stub_object = {
            "name": seed_element,
        }
        for k, v in self.fixed_slot_values.items():
            stub_object[k] = v
        prompt.main_prompt = yaml.dump([stub_object])
        logger.info(
            f"Generated prompt: {len(prompt.text)} = {len(prompt.header)} +\
                {len(prompt.body)} + {len(prompt.main_prompt)}"
        )
        return prompt

    def integrate_payload(
        self, prompt: StructuredPrompt, payload: Dict[str, Any]
    ) -> List[OntologyElement]:
        """Integrate the payload from HALO into the ontology.

        :param payload:
        :param element:
        :return:
        """
        effective_payload = prompt.main_prompt + payload
        # logger.info(f"## EFFECTIVE: {effective_payload}")
        try:
            objs = yaml.safe_load(effective_payload)
        except:
            # codex does not give reliable YAML
            objs = self.parse_what_you_can(effective_payload)
        logger.info(f"## PARSED: {len(objs)}")
        elt = self.integrate_object(objs[0])
        logger.info(f" * INTEGRATED: {elt}")
        return [elt]

    def integrate_object(self, obj: Dict[str, Any], strict=True) -> Optional[OntologyElement]:
        obj = self.repair_dict(obj)
        try:
            elt = OntologyElement(**obj)
        except pydantic.ValidationError as e:
            logger.warning(f"## COULD NOT PARSE: {obj} /// {e}")
            if strict:
                raise e
            return None
        self.add_element(elt)
        return elt

    def repair_dict(self, obj: dict) -> dict:
        slots = self.schemaview.class_slots("OntologyElement")
        nu_obj = {}
        for k, v in obj.items():
            if k not in slots:
                logger.warning(f"Could not find slot {k} in slots")
                continue
            slot = self.schemaview.induced_slot(k, "OntologyElement")
            if slot.multivalued and not isinstance(v, list):
                logger.warning(f"Coercing {v} to list")
                v = [v]
            elif not slot.multivalued and isinstance(v, list):
                logger.warning(f"Coercing {v} len {len(v)} to single value")
                v = v[0]
            nu_obj[k] = v
        return nu_obj

    def old_integrate_payload(self, prompt: StructuredPrompt, payload: Dict[str, Any]):
        """Integrate the payload from HALO into the ontology.

        :param payload:
        :param element:
        :return:
        """
        allowed_slots = self.schemaview.class_slots("OntologyElement")
        effective_payload = prompt.main_prompt + payload
        # logger.info(f"## EFFECTIVE: {effective_payload}")
        try:
            objs = yaml.safe_load(effective_payload)
        except:
            # codex does not give reliable YAML
            objs = self.parse_what_you_can(effective_payload)
        logger.info(f"## PARSED: {len(objs)}")
        added = []
        n = 0
        for obj in objs:
            n += 1
            slots_populated = [k for k, v in obj.items() if v]
            diff = set(slots_populated).difference(allowed_slots)
            if diff:
                logger.info(f"## SKIPPING SLOTS {diff}")
            obj = {k: v for k, v in obj.items() if k in allowed_slots}
            try:
                elt = OntologyElement(**obj)
            except pydantic.ValidationError as e:
                logger.info(f"## COULD NOT PARSE: {obj} /// {e}")
                return added
            logger.info(f"Elt: {elt.name} // {slots_populated} // {obj}")
            if self.add_element(elt):
                logger.info(f" - Added {elt.name}")
                added.append(elt)
            else:
                logger.info(f" - already got {elt.name}")
                if n == 1:
                    logger.error(f"Failed to add first element {elt.name}")
        logger.info(f"Added {len(added)} elements")
        return added

    def parse_what_you_can(self, yaml_str: str) -> List[Dict[str, Any]]:
        """Parse as much of the YAML as possible.

        :param yaml_str:
        :return:
        """
        objs = None
        chunk = ""
        for line in yaml_str.split("\n"):
            chunk += line + "\n"
            try:
                objs = yaml.safe_load(chunk)
            except:
                pass
        if objs is None:
            raise ValueError(f"Could not parse YAML {yaml_str}")
        return objs

    def add_element(self, element: OntologyElement) -> bool:
        """Add an element to the ontology.

        :param obj:
        :return:
        """
        existing = self.get_element(element.name)
        if existing:
            return False
        self.ontology.elements.append(element)
        return True

    def xxextract_seed_ontology(self, seeds: List[str], predicates: List[str]) -> Ontology:
        """Extract an ontology from a given text.

        :param text:
        :return:
        """
        ancestors = list(set(list(self.adapter.ancestors(seeds, predicates, reflexive=True))))
        seed_graph = self.adapter.extract_graph(ancestors, predicates, dangling=False)
        logger.info(len(seed_graph.nodes))
        seed_ontology = self.ontology_from_obograph(seed_graph)
        return seed_ontology

    def xxontology_from_obograph(self, graph: Graph) -> Ontology:
        """Convert an OBO Graph to an Ontology.

        :param graph:
        :return:
        """
        adapter = self.adapter
        ontology = Ontology()
        element_index = {}
        node_to_element_name = {}
        id2slot = {}
        inverses = {}
        for slot in self.schemaview.class_induced_slots(OntologyElement.__name__):
            if slot.inverse:
                inverses[slot.name] = slot.inverse
                inverses[slot.inverse] = slot.name
            if slot.slot_uri:
                id2slot[slot.slot_uri] = slot
        logger.info(list(id2slot.keys()))
        logger.info(inverses)
        for node in graph.nodes:
            meta = node.meta
            if not node.lbl:
                continue
            if not meta:
                # logger.warning(f"Node {node.id} has no meta")
                continue
            element = OntologyElement(
                name=self.node_to_name(node.id, node.lbl),
                synonyms=[synonym.val for synonym in meta.synonyms],
                description=meta.definition.val if meta.definition else None,
            )
            for k, v in self.fixed_slot_values.items():
                setattr(element, k, v)
            element_index[element.name] = element
            node_to_element_name[node.id] = element.name
        for edge in graph.edges:
            if edge.pred == "is_a":
                pred = IS_A
            else:
                try:
                    pred = adapter.uri_to_curie(edge.pred)
                except:
                    pred = edge.pred
            if pred not in id2slot:
                continue
            if edge.sub not in node_to_element_name:
                continue
            if edge.obj not in node_to_element_name:
                continue
            subject = node_to_element_name[edge.sub]
            object = node_to_element_name[edge.obj]
            slot = id2slot[pred]
            getattr(element_index[subject], slot.name).append(object)
            if slot.name in inverses:
                inverse = inverses[slot.name]
                getattr(element_index[object], inverse).append(subject)
        for ldef in adapter.logical_definitions([node.id for node in graph.nodes]):
            if ldef.definedClassId in node_to_element_name:
                element = element_index[node_to_element_name[ldef.definedClassId]]
                if not ldef.genusIds:
                    continue
                if not ldef.restrictions:
                    continue
                genus_elts = [node_to_element_name[g] for g in ldef.genusIds]
                differentia = [
                    f"{adapter.label(r.propertyId)} some {self.node_to_name(r.fillerId)}"
                    for r in ldef.restrictions
                ]
                element.equivalent_to = (
                    f"{' and '.join(genus_elts)} and {' and '.join(differentia)}"
                )
                logger.info(f"Equiv[{element.name}] = {element.equivalent_to}")
        for element in element_index.values():
            ontology.elements.append(element)
        return ontology

    def xxnode_to_name(self, curie: str, label: Optional[str] = None) -> str:
        """Convert a node to a name.

        :param curie:
        :param label:
        :return:
        """
        if label is None:
            label = self.adapter.label(curie)
        if label is None:
            logger.warning(f"Node {curie} has no label")
            label = curie
        return camelcase(label)
