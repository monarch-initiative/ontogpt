"""
Chemical and Disease named entity recognition (NER) evaluation.

This NER test is based on the
Biocreative V Chemical to Disease Relation (BC5CDR)
data, as described below.

Biocreative results here:
https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDR_overview.final.pdf

In the original task, only disease names were considered in NER evaluation.
(i.e., the task was disease named entity recognition, or DNER).
Across 16 teams, the best systems achieved an F-score of 86.46.
From the paper:
"The average precision, recall and F-score were 78.99%, 74.81% and 76.03%,
respectively. All teams but one achieved a higher F-score than our baseline
dictionary method, which obtained an F-score of 52.30%. While we did not
perform any additional development on DNorm [the benchmark method] to adapt
it to this dataset, it sets a significantly stronger benchmark with a
performance of 80.64% F-score. A total of 7 teams achieved performance
higher than DNorm."

This evaluation also considers chemical named entity recognition.

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
from ontogpt.templates.ctd_ner import (
    ChemicalToDiseaseDocument,
    Chemical,
    Disease,
    Publication,
    TextWithEntity,
)

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"
TEST_SET_BIOC = DATABASE_DIR / "CDR_TestSet.BioC.xml.gz"
TRAIN_SET_BIOC = DATABASE_DIR / "CDR_TrainSet.BioC.xml.gz"

# These are the entity types involved in this dataset.
TARGET_TYPES = ["Chemical", "Disease"]

logger = logging.getLogger(__name__)


class PredictionNER(BaseModel):
    """A prediction for a named entity recognition task."""

    test_object: Optional[TextWithEntity] = None
    """Source of truth to evaluate against."""

    true_positives_ce: Optional[List[Tuple]] = None
    num_true_positives_ce: Optional[int] = None
    false_positives_ce: Optional[List[Tuple]] = None
    num_false_positives_ce: Optional[int] = None
    false_negatives_ce: Optional[List[Tuple]] = None
    num_false_negatives_ce: Optional[int] = None
    true_positives_de: Optional[List[Tuple]] = None
    num_true_positives_de: Optional[int] = None
    false_positives_de: Optional[List[Tuple]] = None
    num_false_positives_de: Optional[int] = None
    false_negatives_de: Optional[List[Tuple]] = None
    num_false_negatives_de: Optional[int] = None
    scores: Optional[Dict[str, SimilarityScore]] = None
    predicted_object: Optional[TextWithEntity] = None
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

        def all_objects(dm: Optional[TextWithEntity]):
            if dm is not None:
                return list(set(dm.chemicals + dm.diseases))
            else:
                return list()

        def chem_entities(dm: TextWithEntity) -> Set:
            if dm.chemicals is not None:
                return set((label(entity)) for entity in dm.chemicals)
            else:
                return set()

        def disease_entities(dm: TextWithEntity) -> Set:
            if dm.diseases is not None:
                return set((label(entity)) for entity in dm.diseases)
            else:
                return set()

        self.scores["similarity"] = SimilarityScore.from_set(
            all_objects(self.test_object),
            all_objects(self.predicted_object),
            labelers=labelers,
        )

        if self.predicted_object is not None and self.test_object is not None:
            pred_ce = chem_entities(self.predicted_object)
            test_ce = chem_entities(self.test_object)
            pred_de = disease_entities(self.predicted_object)
            test_de = disease_entities(self.test_object)

        self.true_positives_ce = list(pred_ce.intersection(test_ce))
        self.false_positives_ce = list(pred_ce.difference(test_ce))
        self.false_negatives_ce = list(test_ce.difference(pred_ce))
        self.num_false_negatives_ce = len(self.false_negatives_ce)
        self.num_false_positives_ce = len(self.false_positives_ce)
        self.num_true_positives_ce = len(self.true_positives_ce)

        self.true_positives_de = list(pred_de.intersection(test_de))
        self.false_positives_de = list(pred_de.difference(test_de))
        self.false_negatives_de = list(test_de.difference(pred_de))
        self.num_false_negatives_de = len(self.false_negatives_de)
        self.num_false_positives_de = len(self.false_positives_de)
        self.num_true_positives_de = len(self.true_positives_de)


class EvaluationObjectSetNER(BaseModel):
    """A result of performing named entity recognition."""

    precision_ce: float = 0
    recall_ce: float = 0
    f1_ce: float = 0

    precision_de: float = 0
    recall_de: float = 0
    f1_de: float = 0

    training: Optional[List[TextWithEntity]] = None
    predictions: Optional[List[PredictionNER]] = None
    test: Optional[List[TextWithEntity]] = None


@dataclass
class EvalCTDNER(SPIRESEvaluationEngine):
    subject_prefix = "MESH"
    object_prefix = "MESH"

    def __post_init__(self):
        self.extractor = SPIRESEngine(
            template="ctd_ner.ChemicalToDiseaseDocument", model=self.model
        )
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
            chemicals_by_text = defaultdict(list)
            diseases_by_text = defaultdict(list)
            for document in collection.documents:
                these_annotations = []
                doc = {}
                for p in document.passages:
                    doc[p.infons["type"]] = p.text
                    for a in p.annotations:
                        if a.infons["type"] in TARGET_TYPES:
                            these_annotations.append(a)
                title = doc["title"]
                abstract = doc["abstract"]
                logger.debug(f"Title: {title} Abstract: {abstract}")
                for a in these_annotations:
                    i = a.infons
                    if i["type"] == "Chemical":
                        e = Chemical.model_validate(
                            {
                                "id": f"{self.subject_prefix}:{i[self.subject_prefix]}",
                            }
                        )
                        chemicals_by_text[(title, abstract)].append(e.id)
                    elif i["type"] == "Disease":
                        e = Disease.model_validate(
                            {
                                "id": f"{self.subject_prefix}:{i[self.subject_prefix]}",
                            }
                        )
                        diseases_by_text[(title, abstract)].append(e.id)

        all_entities_by_text = chemicals_by_text | diseases_by_text

        i = 0
        for (title, abstract), _entities in all_entities_by_text.items():
            i = i + 1
            pub = Publication.model_validate(
                {
                    "id": str(i),
                    "title": title,
                    "abstract": abstract,
                }
            )
            chemical_entities = chemicals_by_text[(title, abstract)]
            disease_entities = diseases_by_text[(title, abstract)]
            logger.debug(
                f"Chemicals: {len(chemical_entities)} for Title: {title} Abstract: {abstract}"
            )
            logger.debug(
                f"Diseases: {len(disease_entities)} for Title: {title} Abstract: {abstract}"
            )
            yield ChemicalToDiseaseDocument.model_validate(
                {
                    "publication": pub,
                    "chemicals": chemical_entities,
                    "diseases": disease_entities,
                }
            )

    def create_training_set(self, num=100):
        ke = self.extractor
        docs = list(self.load_test_cases())
        shuffle(docs)
        for doc in docs[0:num]:
            text = doc.text
            prompt = ke.get_completion_prompt(None, text)
            completion = ke.serialize_object()
            yield dict(prompt=prompt, completion=completion)

    def eval(self) -> EvaluationObjectSetNER:
        """Evaluate the ability to extract chemical and disease named entities."""
        labeler = get_adapter("sqlite:obo:mesh")
        if self.num_tests and isinstance(self.num_tests, int):
            num_test = self.num_tests
        else:
            num_test = 1
        ke = self.extractor
        docs = list(self.load_test_cases())
        shuffle(docs)
        eos = EvaluationObjectSetNER(
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
            pub = Publication.model_validate(
                {
                    "id": str(doc.publication.id),
                    "title": doc.publication.title,
                    "abstract": doc.publication.abstract,
                }
            )
            predicted_obj = ChemicalToDiseaseDocument.model_validate(
                {
                    "publication": pub,
                    "chemicals": [],
                    "diseases": [],
                }
            )
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
                        f"{len(extraction.extracted_object.chemicals)}\
                            chemical entities from window: {chunked_text}"
                    )
                    logger.info(
                        f"{len(extraction.extracted_object.diseases)}\
                            disease entities from window: {chunked_text}"
                    )
                if not predicted_obj and extraction.extracted_object is not None:
                    predicted_obj = extraction.extracted_object
                else:
                    if predicted_obj is not None and extraction.extracted_object is not None:
                        predicted_obj.chemicals.extend(extraction.extracted_object.chemicals)
                        predicted_obj.diseases.extend(extraction.extracted_object.diseases)
                        logger.info(
                            f"{len(predicted_obj.chemicals)} chemical entities, after concatenation"
                        )
                        logger.info(
                            f"{len(predicted_obj.diseases)} disease entities, after concatenation"
                        )
                        logger.debug(f"concatenated chemical entities: {predicted_obj.chemicals}")
                        logger.debug(f"concatenated disease entities: {predicted_obj.diseases}")
                if extraction.named_entities is not None:
                    for entity in extraction.named_entities:
                        if entity not in named_entities:
                            named_entities.append(entity)

            def included(t: str):
                if t.startswith("MESH:"):
                    return t

            predicted_obj.chemicals = [t for t in predicted_obj.chemicals if included(t)]
            predicted_obj.diseases = [t for t in predicted_obj.diseases if included(t)]

            logger.info(f"{len(predicted_obj.chemicals)} filtered chemical entities (MESH only)")
            logger.info(f"{len(predicted_obj.diseases)} filtered disease entities (MESH only)")
            pred = PredictionNER(
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

    def calc_stats(self, eos: EvaluationObjectSetNER):
        num_true_positives_ce = sum(p.num_true_positives_ce for p in eos.predictions)
        num_false_positives_ce = sum(p.num_false_positives_ce for p in eos.predictions)
        num_false_negatives_ce = sum(p.num_false_negatives_ce for p in eos.predictions)
        if num_true_positives_ce + num_false_positives_ce == 0:
            logger.warning("No true positives or false positives for chemical entities.")
            return
        eos.precision_ce = num_true_positives_ce / (num_true_positives_ce + num_false_positives_ce)
        eos.recall_ce = num_true_positives_ce / (num_true_positives_ce + num_false_negatives_ce)
        if eos.precision_ce + eos.recall_ce == 0:
            logger.warning("No precision or recall for chemical entities.")
            return
        eos.f1_ce = 2 * (eos.precision_ce * eos.recall_ce) / (eos.precision_ce + eos.recall_ce)

        num_true_positives_de = sum(p.num_true_positives_de for p in eos.predictions)
        num_false_positives_de = sum(p.num_false_positives_de for p in eos.predictions)
        num_false_negatives_de = sum(p.num_false_negatives_de for p in eos.predictions)
        if num_true_positives_de + num_false_positives_de == 0:
            logger.warning("No true positives or false positives for disease entities.")
            return
        eos.precision_de = num_true_positives_de / (num_true_positives_de + num_false_positives_de)
        eos.recall_de = num_true_positives_de / (num_true_positives_de + num_false_negatives_de)
        if eos.precision_de + eos.recall_de == 0:
            logger.warning("No precision or recall for disease entities.")
            return
        eos.f1_de = 2 * (eos.precision_de * eos.recall_de) / (eos.precision_de + eos.recall_de)
