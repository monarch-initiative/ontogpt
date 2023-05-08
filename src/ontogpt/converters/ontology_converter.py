"""Ontology converter."""
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from linkml_runtime import SchemaView
from linkml_runtime.utils.formatutils import camelcase
from oaklib.datamodels.obograph import Graph
from oaklib.datamodels.vocabulary import IS_A
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.templates.halo import Ontology, OntologyElement

this_path = Path(__file__).parent
logger = logging.getLogger(__name__)


@dataclass
class OntologyConverter:
    """Converts an OAK ontology to an OntoGPT schema."""

    adapter: OboGraphInterface = None
    schemaview: SchemaView = None
    fixed_slot_values: Dict[str, str] = field(default_factory=lambda: {})

    def __post_init__(self):
        templates_path = this_path.parent / "templates"
        path_to_template = str(templates_path / "halo.yaml")
        self.schemaview = SchemaView(path_to_template)

    def extract_seed_ontology(self, seeds: List[str], predicates: List[str]) -> Ontology:
        """Extract an ontology from a given text.

        :param text:
        :return:
        """
        ancestors = list(set(list(self.adapter.ancestors(seeds, predicates, reflexive=True))))
        seed_graph = self.adapter.extract_graph(ancestors, predicates, dangling=False)
        logger.info(len(seed_graph.nodes))
        seed_ontology = self.from_obograph(seed_graph)
        return seed_ontology

    def from_adapter(self) -> Ontology:
        """Convert an OAK adapter to an Ontology.

        :param adapter:
        :return:
        """
        graph = self.adapter.as_obograph()
        return self.from_obograph(graph)

    def from_obograph(self, graph: Graph) -> Ontology:
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
                logging.info(f"Equiv[{element.name}] = {element.equivalent_to}")
        for element in element_index.values():
            ontology.elements.append(element)
        return ontology

    def node_to_name(self, curie: str, label: Optional[str] = None) -> str:
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
