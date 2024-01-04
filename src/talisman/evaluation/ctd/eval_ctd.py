"""
Chemical to Disease (CTD) evaluation.

This relation extraction test is based on the
Biocreative V Chemical to Disease Relation (BC5CDR)
data, as described below.

Biocreative results here:
https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDR_overview.final.pdf

A total of 18 teams successfully submitted CID results in 46 runs. As
shown in Table 3 (only the best run of each team is included),
the Fscore ranges from 32.01% to 57.03% (team 288) with an average of
43.37%. All teams outperformed the baseline results by the simple abstract-level
co-occurrence method (16.43% in precision, 76.45% in recall and 27.05% in F-score).

Note: the CTD training set has some oddities,
e.g., scopolamine induces drug overdose.
This evaluation does not account for these oddities.

"""
import gzip
import logging
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from random import shuffle
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import yaml
from bioc import biocxml
from oaklib import BasicOntologyInterface, get_adapter
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import chunk_text
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.evaluation_engine import SimilarityScore, SPIRESEvaluationEngine
from ontogpt.templates.ctd import (
    ChemicalToDiseaseDocument,
    ChemicalToDiseaseRelationship,
    Publication,
    TextWithTriples,
)

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"
TEST_SET_BIOC = DATABASE_DIR / "CDR_TestSet.BioC.xml.gz"
TRAIN_SET_BIOC = DATABASE_DIR / "CDR_TrainSet.BioC.xml.gz"

RMAP = {"CID": "induces"}

logger = logging.getLogger(__name__)


def negated(ChemicalToDiseaseRelationship) -> bool:
    return (
        ChemicalToDiseaseRelationship.qualifier
        and ChemicalToDiseaseRelationship.qualifier.lower() == "not"
    )


class PredictionRE(BaseModel):
    """A prediction for a relationship extraction task."""

    test_object: Optional[TextWithTriples] = None
    """source of truth to evaluate against"""

    true_positives: Optional[List[Tuple]] = None
    num_true_positives: Optional[int] = None
    false_positives: Optional[List[Tuple]] = None
    num_false_positives: Optional[int] = None
    false_negatives: Optional[List[Tuple]] = None
    num_false_negatives: Optional[int] = None
    scores: Optional[Dict[str, SimilarityScore]] = None
    predicted_object: Optional[TextWithTriples] = None
    named_entities: Optional[List[Any]] = None

    def calculate_scores(self, labelers: Optional[List[BasicOntologyInterface]] = None):
        self.scores = {}

        def label(x):
            if labelers:
                for labeler in labelers:
                    lbl = labeler.label(x)
                    if lbl:
                        return f"{x} {lbl}"
            return x

        def all_objects(dm: Optional[TextWithTriples]):
            if dm is not None:
                return list(
                    set(link.subject for link in dm.triples if not negated(link))
                    | set(link.object for link in dm.triples if not negated(link))
                )
            else:
                return list()

        def pairs(dm: TextWithTriples) -> Set:
            if dm.triples is not None:
                return set(
                    (label(link.subject), label(link.object))
                    for link in dm.triples
                    if not negated(link)
                )
            else:
                return set()

        self.scores["similarity"] = SimilarityScore.from_set(
            all_objects(self.test_object),
            all_objects(self.predicted_object),
            labelers=labelers,
        )
        if self.predicted_object is not None and self.test_object is not None:
            pred_pairs = pairs(self.predicted_object)
            test_pairs = pairs(self.test_object)
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

    training: Optional[List[TextWithTriples]] = None
    predictions: Optional[List[PredictionRE]] = None
    test: Optional[List[TextWithTriples]] = None


@dataclass
class EvalCTD(SPIRESEvaluationEngine):
    subject_prefix = "MESH"
    object_prefix = "MESH"

    def __post_init__(self):
        self.extractor = SPIRESEngine(template="ctd.ChemicalToDiseaseDocument", model=self.model)
        # synonyms are derived entirely from training set
        self.extractor.load_dictionary(DATABASE_DIR / "synonyms.yaml")

    def load_test_cases(self) -> Iterable[ChemicalToDiseaseDocument]:
        return self.load_cases(TEST_SET_BIOC)

    def load_training_cases(self) -> Iterable[ChemicalToDiseaseDocument]:
        return self.load_cases(TRAIN_SET_BIOC)

    def load_cases(self, path: Path) -> Iterable[ChemicalToDiseaseDocument]:
        logger.info(f"Loading {path}")
        with gzip.open(str(path), "rb") as f:
            collection = biocxml.load(f)
            triples_by_text = defaultdict(list)
            for document in collection.documents:
                doc = {}
                for p in document.passages:
                    doc[p.infons["type"]] = p.text
                title = doc["title"]
                abstract = doc["abstract"]
                logger.debug(f"Title: {title} Abstract: {abstract}")
                for r in document.relations:
                    i = r.infons
                    t = ChemicalToDiseaseRelationship.model_validate(
                        {
                            "subject": f"{self.subject_prefix}:{i['Chemical']}",
                            "predicate": RMAP[i["relation"]],
                            "object": f"{self.object_prefix}:{i['Disease']}",
                        }
                    )
                    triples_by_text[(title, abstract)].append(t)
        i = 0
        for (title, abstract), triples in triples_by_text.items():
            i = i + 1
            pub = Publication.model_validate(
                {
                    "id": str(i),
                    "title": title,
                    "abstract": abstract,
                }
            )
            logger.debug(f"Triples: {len(triples)} for Title: {title} Abstract: {abstract}")
            yield ChemicalToDiseaseDocument.model_validate({"publication": pub, "triples": triples})

    def create_training_set(self, num=100):
        ke = self.extractor
        docs = list(self.load_test_cases())
        shuffle(docs)
        for doc in docs[0:num]:
            text = doc.text
            prompt = ke.get_completion_prompt(None, text)
            completion = ke.serialize_object()
            yield dict(prompt=prompt, completion=completion)

    def eval(self) -> EvaluationObjectSetRE:
        """Evaluate the ability to extract relations."""
        labeler = get_adapter("sqlite:obo:mesh")
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
            text = f"Title: {doc.publication.title} Abstract: {doc.publication.abstract}"
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
                    logger.info(
                        f"{len(extraction.extracted_object.triples)}\
                            triples from window: {chunked_text}"
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

            def included(t: ChemicalToDiseaseRelationship):
                if not [var for var in (t.subject, t.object, t.predicate) if var is None]:
                    return (
                        t
                        and t.subject
                        and t.object
                        and t.subject.startswith("MESH:")
                        and t.object.startswith("MESH:")
                        and t.predicate.lower() == "induces"
                    )
                else:
                    return t

            predicted_obj.triples = [t for t in predicted_obj.triples if included(t)]
            duplicate_triples = []
            unique_predicted_triples = [
                t
                for t in predicted_obj.triples
                if t not in duplicate_triples and not duplicate_triples.append(t)  # type: ignore
            ]
            predicted_obj.triples = unique_predicted_triples
            logger.info(
                f"{len(predicted_obj.triples)} filtered triples (CID only, between MESH only)"
            )
            pred = PredictionRE(
                predicted_object=predicted_obj, test_object=doc, named_entities=named_entities
            )
            named_entities.clear()
            logger.info("PRED")
            logger.info(yaml.dump(data=pred.model_dump()))
            logger.info("Calc scores")
            pred.calculate_scores(labelers=[labeler])
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
