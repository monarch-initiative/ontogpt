"""
MAXO annotation evaluation.

Annotations in the Medical Action Ontology (MAXO)
may be between a MAXO term and a phenotype,
denoted with a Human Phenotype Ontology (HP) term,
or between a MAXO term and a disease,
denoted with a Mondo Disease Ontology (MONDO) term.

See:
https://github.com/monarch-initiative/maxo-annotations/

This evaluation uses the maxo template to extract
annotations from the text provided in each test case
(see the test_cases directory) and compares them to
the annotations accompanying the case. The existing
annotations are from the set of manual annotations
in the above repository
(see
https://github.com/monarch-initiative/maxo-annotations/
blob/master/annotations/maxo-annotations.tsv)
though the annotations are not considered disease-specific
for the purposes of this evaluation.

Note that this evaluation does not consider predicates,
only extraction of any relation involving a grounded MAXO
action and a grounded HP phenotype.

"""

import logging
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from random import shuffle
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import yaml
from oaklib import BasicOntologyInterface, get_adapter
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import chunk_text
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.evaluation_engine import SimilarityScore, SPIRESEvaluationEngine
from ontogpt.templates.maxo import MaxoAnnotations, ActionAnnotationRelationship, Publication

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "test_cases"

# This does not do much now but can be expanded to
# additional predicate types
RMAP = {"TREATS": "TREATS"}

logger = logging.getLogger(__name__)


class PredictionRE(BaseModel):
    """A prediction for a relationship extraction task."""

    test_object: Optional[MaxoAnnotations] = None
    """Source of truth to evaluate against."""

    true_positives: Optional[List[Tuple]] = None
    num_true_positives: Optional[int] = None
    false_positives: Optional[List[Tuple]] = None
    num_false_positives: Optional[int] = None
    false_negatives: Optional[List[Tuple]] = None
    num_false_negatives: Optional[int] = None
    scores: Optional[Dict[str, SimilarityScore]] = None
    predicted_object: Optional[MaxoAnnotations] = None
    named_entities: Optional[List[Any]] = None

    def calculate_scores(self, labelers: Optional[List[BasicOntologyInterface]] = None):
        self.scores = {}

        def label(x):
            if labelers:
                for labeler in labelers:
                    if type(labeler) == list:
                        lbl = labeler[0].label(x)
                    else:
                        lbl = labeler.label(x)
                    if lbl:
                        return f"{x} {lbl}"
            return x

        def all_objects(dm: Optional[MaxoAnnotations]):
            if dm is not None:
                # set conversion requires lists to be flattened
                # and made generic, or they become invalid
                dm_flat_triples = []
                for triple in dm.triples:
                    if triple.subject is not None and triple.object is not None:
                        if type(triple.object) == list:
                            flat_object = triple.object[0]
                        else:
                            flat_object = triple.object
                        triple_flat = {
                            "subject": triple.subject,
                            # "predicate": triple.predicate,
                            "object": flat_object,
                        }

                        dm_flat_triples.append(triple_flat)
                return list(
                    set(link["subject"] for link in dm_flat_triples)
                    | set(link["object"] for link in dm_flat_triples)
                )
            else:
                return list()

        def pairs(dm: MaxoAnnotations) -> Set:
            if dm.triples is not None:
                return set(
                    (label(link.subject), label(link.object[0]))
                    for link in dm.triples
                    if link.object is not None
                )
            else:
                return set()

        self.scores["similarity"] = SimilarityScore.from_set(
            all_objects(self.test_object),
            all_objects(self.predicted_object),
            labelers=labelers,
        )
        if self.predicted_object is not None:
            pred_pairs = pairs(self.predicted_object)
        else:
            pred_pairs = set()
        if self.test_object is not None:
            test_pairs = pairs(self.test_object)
        else:
            test_pairs = set()
        self.true_positives = list(pred_pairs.intersection(test_pairs))
        self.false_positives = list(pred_pairs.difference(test_pairs))
        self.false_negatives = list(test_pairs.difference(pred_pairs))
        self.num_false_negatives = len(self.false_negatives)
        self.num_false_positives = len(self.false_positives)
        self.num_true_positives = len(self.true_positives)


class EvaluationObjectSetRE(BaseModel):
    """A result of predicting relation extractions."""

    precision: float = 0
    recall: float = 0
    f1: float = 0

    training: Optional[List[MaxoAnnotations]] = None
    predictions: Optional[List[PredictionRE]] = None
    test: Optional[List[MaxoAnnotations]] = None


@dataclass
class EvalMAXO(SPIRESEvaluationEngine):
    subject_prefix = "MAXO"
    object_prefix = "HP"

    def __post_init__(self):
        self.extractor = SPIRESEngine(template="maxo", model=self.model)

    def load_test_cases(self) -> Iterable[MaxoAnnotations]:
        return self.load_cases(DATABASE_DIR)

    # Load cases from YAML
    # One-to-many relationships are parsed as one-to-one, as we
    # may only match part of the set.
    # They still need to be list members to validate, though.
    def load_cases(self, path: Path) -> Iterable[MaxoAnnotations]:
        logger.info(f"Loading {path}")

        triples_by_text = defaultdict(list)

        for casefile in path.glob("*.yaml"):
            logger.info(f"Loading case {casefile}")
            with open(casefile, "r") as file:
                doc = yaml.safe_load(file)
            input_text = doc["input_text"]
            logger.debug(f"Text: {input_text}")
            try:
                for r in doc["extracted_object"]["diagnostic_procedure_to_symptom"]:
                    for object in r["object"]:
                        t = ActionAnnotationRelationship.model_validate(
                            {
                                "subject": f"{r['subject']}",
                                "predicate": RMAP[r["predicate"]],
                                "object": [object],
                            }
                        )
                        triples_by_text[input_text].append(t)
            except KeyError:  # some of the test cases may only have other relations
                logger.info(f"Ignored {casefile} - no Diagnostic Procedure to Symptom relations")
                continue
        i = 0
        for input_text, triples in triples_by_text.items():
            i = i + 1
            title = input_text[:40]
            pub = Publication.model_validate(
                {
                    "id": str(i),
                    "title": title,
                    "abstract": input_text,
                }
            )
            logger.debug(f"Triples: {len(triples)} for Title: {title}")
            yield MaxoAnnotations.model_validate({"publication": pub, "triples": triples})

    def eval(self) -> EvaluationObjectSetRE:
        """Evaluate the ability to extract relations."""
        maxo_labeler = get_adapter("sqlite:obo:maxo")
        hp_labeler = get_adapter("sqlite:obo:hp")

        if self.num_tests and isinstance(self.num_tests, int):
            num_test = self.num_tests
        else:
            num_test = 1
        ke = self.extractor
        docs = list(self.load_test_cases())
        shuffle(docs)
        eos = EvaluationObjectSetRE(
            test=docs[:num_test],
            training=[],
            predictions=[],
        )
        n = 1
        for doc in eos.test:
            logger.info(f"Iteration {n} of {num_test}")
            n += 1
            logger.info(doc)
            text = doc.publication.abstract
            predicted_obj = None
            named_entities: List[str] = []  # This stores the NEs for the whole document
            ke.named_entities = []  # This stores the NEs the extractor knows about

            if self.chunking:
                text_list = chunk_text(text)
            else:
                text_list = iter([text])

            for chunked_text in text_list:
                extraction = ke.extract_from_text(chunked_text)

                if extraction.extracted_object is not None:
                    # Process all multi-object triples to 1 to 1 triples
                    # so they may be more directly compared
                    for extracted_triple in extraction.extracted_object.action_annotation_relationships:
                        new_triple = extracted_triple
                        for object in extracted_triple.object:
                            new_triple.object = [object]
                            extraction.extracted_object.triples.append(new_triple)

                    logger.info(
                        f"{len(extraction.extracted_object.triples)} triples from: {chunked_text}"
                    )
                if not predicted_obj and extraction.extracted_object is not None:
                    predicted_obj = extraction.extracted_object
                else:
                    if predicted_obj is not None and extraction.extracted_object is not None:
                        predicted_obj.triples.extend(extraction.extracted_object.triples)
                        logger.info(
                            f"{len(predicted_obj.triples)} total triples, after concatenation"
                        )
                        logger.debug(f"concatenated triples: {predicted_obj.triples}")
                if extraction.named_entities is not None:
                    for entity in extraction.named_entities:
                        if entity not in named_entities:
                            named_entities.append(entity)

            def included(t: ActionAnnotationRelationship):
                if not [var for var in (t.subject, t.object, t.predicate) if var is None]:
                    return (
                        t
                        and t.subject
                        and t.object
                        and t.subject.startswith("MAXO:")
                        and t.object[0].startswith("HP:")
                        # and t.predicate.lower() == "treats"
                    )
                else:
                    return False

            if predicted_obj is not None:
                predicted_obj.triples = [t for t in predicted_obj.triples if included(t)]
                duplicate_triples = []
                unique_predicted_triples = [
                    t
                    for t in predicted_obj.triples
                    if t not in duplicate_triples
                    and not duplicate_triples.append(t)  # type: ignore
                ]
                predicted_obj.triples = unique_predicted_triples
                logger.info(f"{len(predicted_obj.triples)} filtered triples")
            pred = PredictionRE(
                predicted_object=predicted_obj, test_object=doc, named_entities=named_entities
            )
            named_entities.clear()
            logger.info("PRED")
            logger.info(yaml.dump(data=pred.model_dump()))
            logger.info("Calc scores")
            pred.calculate_scores(labelers=[maxo_labeler, hp_labeler])
            logger.info(yaml.dump(data=pred.model_dump()))
            eos.predictions.append(pred)
        self.calc_stats(eos)
        return eos

    def calc_stats(self, eos: EvaluationObjectSetRE):
        num_true_positives = sum(p.num_true_positives for p in eos.predictions)
        num_false_positives = sum(p.num_false_positives for p in eos.predictions)
        num_false_negatives = sum(p.num_false_negatives for p in eos.predictions)
        if num_true_positives + num_false_positives == 0:
            logger.warning("No true positives or false positives")
            return
        eos.precision = num_true_positives / (num_true_positives + num_false_positives)
        eos.recall = num_true_positives / (num_true_positives + num_false_negatives)
        if eos.precision + eos.recall == 0:
            logger.warning("No precision or recall")
            return
        eos.f1 = 2 * (eos.precision * eos.recall) / (eos.precision + eos.recall)
