"""
Main Knowledge Extractor class.

This works by recursively constructing structured prompt-completions where
a pseudo-YAML structure is requested, where the YAML
structure corresponds to a template class.

Described in the SPIRES manuscript.
See https://arxiv.org/abs/2304.02711
"""

import json
import logging
import re
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

import pydantic
import yaml
from linkml_runtime.linkml_model import ClassDefinition, SlotDefinition
from oaklib import BasicOntologyInterface

from ontogpt.engines.knowledge_engine import (
    ANNOTATION_KEY_PROMPT,
    ANNOTATION_KEY_PROMPT_SKIP,
    EXAMPLE,
    FIELD,
    OBJECT,
    KnowledgeEngine,
    chunk_text,
)
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.templates.core import ExtractionResult

this_path = Path(__file__).parent

CODE_FENCE = "```"

RESPONSE_ATOM = Union[str, "ResponseAtom"]  # type: ignore
RESPONSE_DICT = Dict[FIELD, Union[RESPONSE_ATOM, List[RESPONSE_ATOM]]]


@dataclass
class SPIRESEngine(KnowledgeEngine):
    """Knowledge extractor."""

    recurse: bool = True
    """If true, then complex non-named entity objects are always recursively parsed.
    If this is false AND the complex object is a pair, then token-based splitting is
    instead used.
    TODO: deprecate this, it's not clear that token-based splitting is better, due to
    the inability to control which tokens GPT will use"""

    sentences_per_window: Optional[int] = None
    """If set, this will split the text into chains of sentences,
    where this determines the maximum number of sentences per chain.
    The results are then merged together."""

    def extract_from_text(
        self,
        text: str,
        cls: ClassDefinition = None,
        object: OBJECT = None,
        show_prompt: bool = False,
    ) -> ExtractionResult:
        """
        Extract annotations from the given text.

        :param text:
        :param cls:
        :param object: optional stub object
        :return:
        """
        self.extracted_named_entities = []  # Clear the named entity buffer

        if self.sentences_per_window:
            chunks = chunk_text(text, self.sentences_per_window)
            extracted_object = None
            for chunk in chunks:
                raw_text = self._raw_extract(chunk, cls=cls, object=object, show_prompt=show_prompt)
                logging.info(f"RAW TEXT: {raw_text}")
                next_object = self.parse_completion_payload(
                    raw_text, cls, object=object  # type: ignore
                )
                if extracted_object is None:
                    extracted_object = next_object
                else:
                    for k, v in next_object.items():
                        if isinstance(v, list):
                            extracted_object[k] += v
                        else:
                            if k not in extracted_object:
                                extracted_object[k] = v
                            else:
                                extracted_object[k] = v
        else:
            raw_text = self._raw_extract(text=text, cls=cls, object=object, show_prompt=show_prompt)
            logging.info(f"RAW TEXT: {raw_text}")
            extracted_object = self.parse_completion_payload(
                raw_text, cls, object=object  # type: ignore
            )

        return ExtractionResult(
            input_text=text,
            raw_completion_output=raw_text,
            prompt=self.last_prompt,
            extracted_object=extracted_object,
            named_entities=self.extracted_named_entities,
            # Note these are the named entities from the last extraction,
            # not the full list of all named entities across all extractions
        )

    def _extract_from_text_to_dict(self, text: str, cls: ClassDefinition = None) -> RESPONSE_DICT:
        raw_text = self._raw_extract(text=text, cls=cls)
        return self._parse_response_to_dict(raw_text, cls)

    def generate_and_extract(
        self, entity: str, prompt_template: str = "", show_prompt: bool = False, **kwargs
    ) -> ExtractionResult:
        """
        Generate a description using an LLM and then extract from it using SPIRES.

        :param entity:
        :param kwargs:
        :return:
        """
        if prompt_template == "":
            prompt_template = "Generate a comprehensive description of {entity}.\n"
        prompt = prompt_template.format(entity=entity)
        if self.client is not None:
            payload = self.client.complete(prompt=prompt, show_prompt=show_prompt)
        else:
            payload = ""
        return self.extract_from_text(payload, **kwargs)

    def iteratively_generate_and_extract(
        self,
        entity: str,
        cache_path: Union[str, Path],
        iteration_slots: List[str],
        adapter: BasicOntologyInterface = None,
        clear=False,
        max_iterations=10,
        prompt_template=None,
        show_prompt: bool = False,
        **kwargs,
    ) -> Iterator[ExtractionResult]:
        def _remove_parenthetical_context(s: str):
            return re.sub(r"\(.*\)", "", s)

        iteration = 0
        if isinstance(cache_path, str):
            cache_path = Path(cache_path)
        if cache_path:
            if cache_path.exists() and not clear:
                db = yaml.safe_load(cache_path.open())
                if "entities_in_queue" not in db:
                    db["entities_in_queue"] = []
            else:
                db = {"processed_entities": [], "entities_in_queue": [], "results": []}
        if entity not in db["processed_entities"]:
            db["entities_in_queue"].append(entity)
        if prompt_template is None:
            prompt_template = (
                "Generate a comprehensive description of {entity}. "
                + "The description should include the information on"
                + " and ".join(iteration_slots)
                + ".\n"
            )
        while db["entities_in_queue"] and iteration < max_iterations:
            iteration += 1
            next_entity = db["entities_in_queue"].pop(0)
            logging.info(f"ITERATION {iteration}, entity={next_entity}")
            # check if entity matches a curie pattern using re
            if re.match(r"^[A-Z]+:[A-Z0-9]+$", next_entity):
                curie = next_entity
                next_entity = adapter.label(next_entity)
            else:
                curie = None
            result = self.generate_and_extract(
                next_entity, prompt_template=prompt_template, show_prompt=show_prompt, **kwargs
            )
            if curie:
                if result.extracted_object:
                    result.extracted_object.id = curie
            db["results"].append(result)
            db["processed_entities"].append(next_entity)
            yield result
            for s in iteration_slots:
                # if s not in result.extracted_object:
                #    raise ValueError(f"Slot {s} not found in {result.extracted_object}")
                vals = getattr(result.extracted_object, s, [])
                if not vals:
                    logging.info("dead-end: no values found for slot")
                    continue
                if not isinstance(vals, list):
                    vals = [vals]
                for val in vals:
                    entity = val
                    if result.named_entities is not None:
                        for ne in result.named_entities:
                            if ne.id == val:
                                entity = ne.label
                                if ne.id.startswith("AUTO"):
                                    # Sometimes the value of some slots will lack
                                    context = next_entity
                                    context = re.sub(r"\(.*\)", "", context)
                                    entity = f"{entity} ({context})"
                                else:
                                    entity = ne.id
                                break
                    queue_deparenthesized = [
                        _remove_parenthetical_context(e) for e in db["entities_in_queue"]
                    ]
                    if (
                        entity not in db["processed_entities"]
                        and entity not in db["entities_in_queue"]
                        and _remove_parenthetical_context(entity) not in queue_deparenthesized
                    ):
                        db["entities_in_queue"].append(entity)
            with open(cache_path, "w") as f:
                # TODO: consider a more robust backend e.g. mongo
                f.write(dump_minimal_yaml(db))

    def generalize(
        self,
        object: Union[pydantic.BaseModel, dict],
        examples: List[EXAMPLE],
        show_prompt: bool = False,
    ) -> ExtractionResult:
        """
        Generalize the given examples.

        :param object:
        :param examples:
        :return:
        """
        cls = self.template_class
        sv = self.schemaview
        prompt = "example:\n"
        for example in examples:
            prompt += f"{self.serialize_object(example)}\n\n"
        prompt += "\n\n===\n\n"
        if isinstance(object, pydantic.BaseModel):
            object = object.model_dump()
        for k, v in object.items():
            if v:
                slot = sv.induced_slot(k, cls.name)
                prompt += f"{k}: {self._serialize_value(v, slot)}\n"
        logging.debug(f"PROMPT: {prompt}")
        payload = self.client.complete(prompt, show_prompt)
        prediction = self.parse_completion_payload(payload, object=object)
        return ExtractionResult(
            input_text=prompt,
            raw_completion_output=payload,
            # prompt=self.last_prompt,
            results=[prediction],
            named_entities=self.named_entities,
        )

    def map_terms(
        self, terms: List[str], ontology: str, show_prompt: bool = False
    ) -> Dict[str, str]:
        """
        Map the given terms to the given ontology.

        EXPERIMENTAL

        currently GPT-3 does not do so well with this task.

        :param terms:
        :param ontology:
        :return:
        """
        # TODO: make a separate config
        examples = {
            "go": {
                "nucleui": "nucleus",
                "mitochondrial": "mitochondrion",
                "signaling": "signaling pathway",
                "cysteine biosynthesis": "cysteine biosynthetic process",
                "alcohol dehydrogenase": "alcohol dehydrogenase activity",
            },
            "uberon": {
                "feet": "pes",
                "forelimb, left": "left forelimb",
                "hippocampus": "Ammons horn",
            },
        }
        ontology = ontology.lower()
        if ontology in examples:
            example = examples[ontology]
        else:
            example = examples["uberon"]
        prompt = "Normalize the following semicolon separated\
            list of terms to the {ontology.upper()} ontology\n\n"
        prompt += "For example:\n\n"
        for k, v in example.items():
            prompt += f"{k}: {v}\n"
        prompt += "===\n\nTerms:"
        prompt += "; ".join(terms)
        prompt += "===\n\n"
        payload = self.client.complete(prompt, show_prompt)
        # outer parse
        best_results: List[str] = []
        for sep in ["\n", "; "]:
            results = payload.split(sep)
            if len(results) > len(best_results):
                best_results = results

        def normalize(s: str) -> str:
            s = s.strip()
            s.replace("_", " ")
            return s.lower()

        mappings = {}
        for result in best_results:
            if ":" not in result:
                logging.error(f"Count not parse result: {result}")
                continue
            k, v = result.strip().split(":", 1)
            k = k.strip()
            v = v.strip()
            for t in terms:
                if normalize(t) == normalize(k):
                    mappings[t] = v
                    break
        for t in terms:
            if t not in mappings:
                logging.warning(f"Could not map term: {t}")
        return mappings

    def serialize_object(self, example: EXAMPLE, cls: ClassDefinition = None) -> str:
        if cls is None:
            cls = self.template_class
        if isinstance(example, str):
            return example
        if isinstance(example, pydantic.BaseModel):
            example = example.model_dump()
        lines = []
        sv = self.schemaview
        for k, v in example.items():
            if not v:
                continue
            slot = sv.induced_slot(k, cls.name)
            v_serialized = self._serialize_value(v, slot)
            lines.append(f"{k}: {v_serialized}")
        return "\n".join(lines)

    def _serialize_value(self, val: Any, slot: SlotDefinition) -> str:
        if val is None:
            return ""
        if isinstance(val, list):
            return "; ".join([self._serialize_value(v, slot) for v in val if v])
        if isinstance(val, dict):
            return " - ".join([self._serialize_value(v, slot) for v in val.values() if v])
        sv = self.schemaview
        if slot.range in sv.all_classes():
            if self.labelers:
                labelers = list(self.labelers)
            else:
                labelers = []
            labelers += self.get_annotators(sv.get_class(slot.range))
            if labelers:
                for labeler in labelers:
                    label = labeler.label(val)
                    if label:
                        return label
        return val

    def _raw_extract(
        self,
        text,
        cls: ClassDefinition = None,
        object: OBJECT = None,
        show_prompt: bool = False,
    ) -> str:
        """
        Extract annotations from the given text.

        :param text:
        :return:
        """
        prompt = self.get_completion_prompt(cls=cls, text=text, object=object)
        self.last_prompt = prompt
        payload = self.client.complete(prompt=prompt, show_prompt=show_prompt)
        return payload

    def get_completion_prompt(
        self, cls: ClassDefinition = None, text: str = "", object: OBJECT = None
    ) -> str:
        """Get the prompt for the given template."""
        if cls is None:
            cls = self.template_class
        if not text or ("\n" in text or len(text) > 60):
            prompt = (
                "From the text below, extract the following entities in the following format:\n\n"
            )
        else:
            prompt = "Split the following piece of text into fields in the following format:\n\n"
        for slot in self.schemaview.class_induced_slots(cls.name):
            if ANNOTATION_KEY_PROMPT_SKIP in slot.annotations:
                continue
            if ANNOTATION_KEY_PROMPT in slot.annotations:
                slot_prompt = slot.annotations[ANNOTATION_KEY_PROMPT].value
            elif slot.description:
                slot_prompt = slot.description
            else:
                if slot.multivalued:
                    slot_prompt = f"semicolon-separated list of {slot.name}s"
                else:
                    slot_prompt = f"the value for {slot.name}"
            if slot.range in self.schemaview.all_enums():
                enum_def = self.schemaview.get_enum(slot.range)
                pvs = [str(k) for k in enum_def.permissible_values.keys()]
                slot_prompt += f"Must be one of: {', '.join(pvs)}"
            prompt += f"{slot.name}: <{slot_prompt}>\n"
        # prompt += "Do not answer if you don't know\n\n"
        prompt = f"{prompt}\n\nText:\n{text}\n\n===\n\n"
        if object:
            if cls is None:
                cls = self.template_class
            if isinstance(object, pydantic.BaseModel):
                object = object.model_dump()
            for k, v in object.items():
                if v:
                    slot = self.schemaview.induced_slot(k, cls.name)
                    prompt += f"{k}: {self._serialize_value(v, slot)}\n"
        return prompt

    def _parse_response_to_dict(
        self, results: str, cls: ClassDefinition = None
    ) -> Optional[RESPONSE_DICT]:
        """
        Parse the pseudo-YAML response from OpenAI into a dictionary object.

        E.g.

            foo: a; b; c

        becomes

            {"foo": ["a", "b", "c"]}

        The response may already be in markdown and/or JSON,
        in which case we need to recognize the format.
        JSON may be parsed as-is but may be malformed or over-processed
        as compared to our template (e.g., it may separate key-value pairs
        where we expect them to be concatenated)

        :param results:
        :return:
        """
        promptable_slots = self.promptable_slots(cls)
        is_json = False

        # First remove any code fences
        # and any adjacent strings on the same line
        results = re.sub(r"```[^`\n]*", "", results, flags=re.DOTALL)

        # Try to parse as JSON
        # The JSON may still be malformed.
        # If so, it's not JSON and we need to parse it as YAML-like
        # So just to be sure we remove the JSON delimiters in that case
        try:
            ann = json.loads(results)
            is_json = True
        except json.decoder.JSONDecodeError:
            for ch in ["{", "}", '"']:
                results = results.replace(ch, "")

        if is_json:
            for entry in ann:
                if isinstance(ann[entry], list):
                    values = "; ".join(ann[entry])
                elif isinstance(ann[entry], dict):
                    values = "; ".join([f"{k} - {v}" for k, v in ann[entry].items()])
                else:
                    values = ann[entry]
                line = f"{entry}: {values}"
                r = self._parse_line_to_dict(line, cls)
                if r is not None:
                    field, val = r
                    ann[field] = val
        else:
            # First split the text into sections, denoted by presence of multiple newlines
            # Each section may still have multiple fields, but we don't know how
            # they will be formatted
            sections = results.replace("*","").split("\n\n")
            ann = {}
            for section in sections:
                lines = section.splitlines()
                continued_line = ""
                for line in lines:
                    line = line.replace("*","").strip()
                    # The line may be split into multiple lines,
                    # and we can only tell if there's a delimiter at the end of this one
                    # (though it may just be a misplaced delimiter)
                    # TODO: this could be a different delimiter, globally defined
                    if line.endswith(";"):
                        logging.info(f"This line ends in a delimiter, assuming continuation: {line}")
                        continued_line = line
                        continue
                    # If there's nothing after the colon,
                    # we may be continuing as a numeric list or the like
                    if ":" in line and not line.split(":", 1)[1].strip():
                        logging.info(f"This line looks empty, assuming continuation: {line}")
                        if len(continued_line) > 0:
                            logging.info(f"Finishing previous continued line: {continued_line}")
                            r = self._parse_line_to_dict(continued_line, cls)
                            if r is not None:
                                field, val = r
                                ann[field] = val
                        continued_line = line
                        continue
                    # We may be continuing a numeric list
                    if (line.split("."))[0].isdigit():
                        logging.info(
                            f"Line '{line}' is a numeric item; continuing from {continued_line}"
                        )
                        # Remove the leading numeral from the line
                        line = line.split(".", 1)[1].strip()
                        continued_line = continued_line + line + ";"
                        continue
                    if not line:
                        continue
                    if line.startswith(CODE_FENCE):
                        continue
                    if ":" not in line:
                        if len(promptable_slots) == 1:
                            slot = promptable_slots[0]
                            logging.info(
                                f"Coercing to YAML-like with key {slot.name}: Original line: {line}"
                            )
                            line = f"{slot.name}: {line}"
                        elif len(continued_line) > 0:
                            logging.info(f"Line '{line}' continuing from {continued_line}")
                            line = continued_line + ";" + line
                        if ":" not in line:
                            logging.error(f"Line '{line}' does not contain a colon; ignoring")
                            continue
                    else:
                        # We made it this far but may still have a continued line
                        # So parse that first
                        if len(continued_line) > 0:
                            line = continued_line
                    r = self._parse_line_to_dict(line, cls)
                    continued_line = ""
                    if r is not None:
                        field, val = r
                        ann[field] = val
                if len(continued_line) > 0:
                    logging.info(f"Finishing continued line: {continued_line}")
                    r = self._parse_line_to_dict(continued_line, cls)
                    if r is not None:
                        field, val = r
                        ann[field] = val
        return ann

    def _parse_line_to_dict(
        self, line: str, cls: ClassDefinition = None
    ) -> Optional[Tuple[FIELD, RESPONSE_ATOM]]:
        if cls is None:
            cls = self.template_class
        sv = self.schemaview
        # each line is a key-value pair
        logging.info(f"PARSING LINE: {line}")
        field, val = line.split(":", 1)
        # Field nornalization:
        # The LLM may mutate the output format somewhat,
        # randomly pluralizing or replacing spaces with underscores
        field = field.lower().replace(" ", "_")
        logging.debug(f"  FIELD: {field}")
        cls_slots = sv.class_slots(cls.name)
        slot = None
        if field in cls_slots:
            slot = sv.induced_slot(field, cls.name)
        else:

            # Try removing pluralization
            if field.endswith("s"):
                field = field[:-1]

            if field in cls_slots:
                slot = sv.induced_slot(field, cls.name)
        if not slot:
            logging.error(f"Cannot find slot for {field} in {line}")
            return None
        if not val:
            msg = f"Empty value in key-value line: {line}"
            if slot.required:
                raise ValueError(msg)
            if slot.recommended:
                logging.warning(msg)
            return None
        inlined = slot.inlined
        slot_range = sv.get_class(slot.range)
        if not inlined:
            if slot.range in sv.all_classes():
                inlined = sv.get_identifier_slot(slot_range.name) is None
        val = val.strip()
        if slot.multivalued:
            vals = [v.strip() for v in val.split(";")]
        else:
            vals = [val]
        vals = [val for val in vals if val]
        logging.debug(f"SLOT: {slot.name} INL: {inlined} VALS: {vals}")
        if inlined:
            transformed = False
            slots_of_range = sv.class_slots(slot_range.name)
            if self.recurse or len(slots_of_range) > 2:
                logging.debug(f"  RECURSING ON SLOT: {slot.name}, range={slot_range.name}")
                vals = [
                    self._extract_from_text_to_dict(v, slot_range) for v in vals  # type: ignore
                ]
            else:
                for sep in [" - ", ":", "/", "*", "-"]:
                    if all([sep in v for v in vals]):
                        vals = [
                            dict(zip(slots_of_range, v.split(sep, 1))) for v in vals  # type: ignore
                        ]
                        for v in vals:
                            for k in v.keys():  # type: ignore
                                v[k] = v[k].strip()  # type: ignore
                        transformed = True
                        break
                if not transformed:
                    logging.warning(f"Did not find separator in {vals} for line {line}")
                    return None
        # transform back from list to single value if not multivalued
        if slot.multivalued:
            final_val = vals
        else:
            if len(vals) != 1:
                logging.error(f"Expected 1 value for {slot.name} in '{line}' but got {vals}")
            final_val = vals[0]  # type: ignore
        return field, final_val

    def parse_completion_payload(
        self, results: str, cls: ClassDefinition = None, object: dict = None
    ) -> pydantic.BaseModel:
        """
        Parse the completion payload into a pydantic class.

        :param results:
        :param cls:
        :param object: stub object
        :return:
        """
        raw = self._parse_response_to_dict(results, cls)
        logging.debug(f"RAW: {raw}")
        if object:
            raw = {**object, **raw}
        self._auto_add_ids(raw, cls)
        return self.ground_annotation_object(raw, cls)

    def _auto_add_ids(self, ann: RESPONSE_DICT, cls: ClassDefinition = None) -> None:
        if ann is None:
            return
        if cls is None:
            cls = self.template_class
        for slot in self.schemaview.class_induced_slots(cls.name):
            if slot.identifier:
                if slot.name not in ann:
                    auto_id = str(uuid.uuid4())
                    auto_prefix = self.auto_prefix
                    if slot.range == "uriorcurie" or slot.range == "uri":
                        ann[slot.name] = f"{auto_prefix}:{auto_id}"
                    else:
                        ann[slot.name] = auto_id

    def ground_annotation_object(
        self, ann: RESPONSE_DICT, cls: ClassDefinition = None
    ) -> Optional[pydantic.BaseModel]:
        """Ground the direct parse of the OpenAI payload.

        The raw openAI payload is a YAML-like string, which is parsed to
        a response dictionary.

        This dictionary is then grounded, using this method

        :param ann: Raw annotation object
        :param cls: schema class the ground object should instantiate
        :return: Grounded annotation object
        """
        logging.debug(f"Grounding annotation object {ann}")
        if cls is None:
            cls = self.template_class
        sv = self.schemaview
        new_ann: Dict[str, Any] = {}
        if ann is None:
            logging.error(f"Cannot ground None annotation, cls={cls.name}")
            return None
        for field, vals in ann.items():
            if isinstance(vals, list):
                multivalued = True
            else:
                multivalued = False
                vals = [vals]
            slot = sv.induced_slot(field, cls.name)
            rng_cls = sv.get_class(slot.range)
            enum_def = None
            if slot.range:
                if slot.range in self.schemaview.all_enums():
                    enum_def = self.schemaview.get_enum(slot.range)
            new_ann[field] = []
            logging.debug(f"FIELD: {field} SLOT: {slot.name}")
            for val in vals:
                if not val:
                    continue
                logging.debug(f"   VAL: {val}")
                if isinstance(val, tuple):
                    # special case for pairs
                    sub_slots = sv.class_induced_slots(rng_cls.name)
                    obj = {}
                    for i in range(0, len(val)):
                        sub_slot = sub_slots[i]
                        sub_rng = sv.get_class(sub_slot.range)
                        if not sub_rng:
                            logging.error(f"Cannot find range for {sub_slot.name}")
                        result = self.normalize_named_entity(val[i], sub_slot.range)
                        obj[sub_slot.name] = result
                elif isinstance(val, dict):
                    # recurse
                    obj = self.ground_annotation_object(val, rng_cls)
                else:
                    obj = self.normalize_named_entity(val, slot.range)  # type: ignore
                if enum_def:
                    found = False
                    logging.info(f"Looking for {obj} in {enum_def.name}")
                    for k, _pv in enum_def.permissible_values.items():
                        if type(obj) is str and type(k) is str:
                            if obj.lower() == k.lower():  # type: ignore
                                obj = k  # type: ignore
                                found = True
                                break
                    if not found:
                        logging.info(f"Cannot find enum value for {obj} in {enum_def.name}")
                        obj = None
                if multivalued:
                    new_ann[field].append(obj)
                else:
                    new_ann[field] = obj
        logging.debug(f"Creating object from dict {new_ann}")
        logging.info(new_ann)
        py_cls = self.template_module.__dict__[cls.name]
        return py_cls(**new_ann)
