"""
Evaluation on the CRAFT corpus.

This is an NER evaluation, or specifically
concept recognition.

It uses a specific template (craft_concepts)

The corpus is retrieved from:
https://github.com/UCDenver-ccp/CRAFT

This evaluation use the v5.0.2 release.

Funk et al. 2014 BMC Bioinformatics
(https://doi.org/10.1186/1471-2105-15-59)
reported that the ConceptMapper dictionary
lookup tool generally performed the best
across most ontologies,
with F-scores on these:
Cell Type Ontology (CL)  0.83
Gene Ontology (GO) Cellular Component  0.77
Gene Ontology (GO) Biological Process  0.37
Gene Ontology (GO) Molecular Function* 0.48
Sequence Ontology (SO)  0.56
Protein Ontology (PR) 0.57
NCBI Taxonomy (NCBITaxon) 0.69
CHEBI  0.56
* after adding synonyms without the word "activity"

Annotations in CRAFT also include:
MONDO Disease Ontology
Molecular Process Ontology (MOP)
UBERON Ontology

"""


import gzip
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
from ontogpt.templates.craft_concept import (
    Document,
    TextWithEntity,
)

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"

# These are the entity types involved in this dataset.
TARGET_TYPES = [
    "AnatomicalElement",
    "BiologicalProcess",
    "CellType",
    "CellularComponent",
    "Chemical",
    "Disease",
    "MolecularFunction",
    "MolecularProcess",
    "Protein",
    "SequenceEntity",
    "Taxon",
]

RESULT_TYPES = [
    "true_positives",
    "num_true_positives",
    "false_positives",
    "num_false_positives",
    "false_negatives",
    "num_false_negatives",
]

logger = logging.getLogger(__name__)


class PredictionNER(BaseModel):
    """A prediction for a named entity recognition task."""

    test_object: Optional[TextWithEntity] = None
    """Source of truth to evaluate against."""

    # results stores all the TP, FP, FN, and TP entities
    # with entity name from TARGET_TYPES as key
    results = Dict[Dict[List[Tuple]]]
    for target in TARGET_TYPES:
        results[target] = {}
        for result_type in RESULT_TYPES:
            results[target[result_type]] = []

    scores: Optional[Dict[str, SimilarityScore]] = None
    predicted_object: Optional[TextWithEntity] = None
    named_entities: Optional[List[Any]] = None

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
class EvalCRAFTConcepts(SPIRESEvaluationEngine):

    # TODO: nope, not these
    subject_prefix = "MESH"
    object_prefix = "MESH"

    def __post_init__(self):
        self.extractor = SPIRESEngine(
            template="craft_concept.Document", model=self.model
        )

    def load_test_cases(self) -> Iterable[Document]:
        return self.load_cases(DATABASE_DIR)

    def load_cases(self, path: Path) -> Iterable[Document]:
        logger.info(f"Loading {path}")

        # Retrieve corpus if not present
        # Preprocess corpus
        # Load documents
        # Validate documents

        # with gzip.open(str(path), "rb") as f:
        #     collection = biocxml.load(f)
        #     chemicals_by_text = defaultdict(list)
        #     diseases_by_text = defaultdict(list)
        #     for document in collection.documents:
        #         these_annotations = []
        #         doc = {}
        #         for p in document.passages:
        #             doc[p.infons["type"]] = p.text
        #             for a in p.annotations:
        #                 if a.infons["type"] in TARGET_TYPES:
        #                     these_annotations.append(a)
        #         title = doc["title"]
        #         abstract = doc["abstract"]
        #         logger.debug(f"Title: {title} Abstract: {abstract}")
        #         for a in these_annotations:
        #             i = a.infons
        #             if i["type"] == "Chemical":
        #                 e = Chemical.model_validate(
        #                     {
        #                         "id": f"{self.subject_prefix}:{i[self.subject_prefix]}",
        #                     }
        #                 )
        #                 chemicals_by_text[(title, abstract)].append(e.id)
        #             elif i["type"] == "Disease":
        #                 e = Disease.model_validate(
        #                     {
        #                         "id": f"{self.subject_prefix}:{i[self.subject_prefix]}",
        #                     }
        #                 )
        #                 diseases_by_text[(title, abstract)].append(e.id)

        # all_entities_by_text = chemicals_by_text | diseases_by_text

        # i = 0
        # for (title, abstract), _entities in all_entities_by_text.items():
        #     i = i + 1
        #     pub = Publication.model_validate(
        #         {
        #             "id": str(i),
        #             "title": title,
        #             "abstract": abstract,
        #         }
        #     )
        #     chemical_entities = chemicals_by_text[(title, abstract)]
        #     disease_entities = diseases_by_text[(title, abstract)]
        #     logger.debug(
        #         f"Chemicals: {len(chemical_entities)} for Title: {title} Abstract: {abstract}"
        #     )
        #     logger.debug(
        #         f"Diseases: {len(disease_entities)} for Title: {title} Abstract: {abstract}"
        #     )
        #     yield ChemicalToDiseaseDocument.model_validate(
        #         {
        #             "publication": pub,
        #             "chemicals": chemical_entities,
        #             "diseases": disease_entities,
        #         }
        #     )


    # def eval(self) -> EvaluationObjectSetNER:
    #     """Evaluate the ability to extract chemical and disease named entities."""

    #     # TODO: need other labelers
    #     labeler = get_adapter("sqlite:obo:mesh")
    #     if self.num_tests and isinstance(self.num_tests, int):
    #         num_test = self.num_tests
    #     else:
    #         num_test = 1
    #     ke = self.extractor
    #     docs = list(self.load_test_cases())
    #     shuffle(docs)
    #     eos = EvaluationObjectSetNER(
    #         test=docs[:num_test],
    #         training=[],
    #         predictions=[],
    #     )
    #     n = 1
    #     for doc in eos.test:
    #         logger.info(f"Iteration {n} of {num_test}")
    #         n += 1
    #         logger.info(doc)
    #         text = f"Title: {doc.publication.title} Abstract: {doc.publication.abstract}"
    #         pub = Publication.model_validate(
    #             {
    #                 "id": str(doc.publication.id),
    #                 "title": doc.publication.title,
    #                 "abstract": doc.publication.abstract,
    #             }
    #         )
    #         predicted_obj = Document.model_validate(
    #             {
    #                 "publication": pub,
    #                 "chemicals": [],
    #                 "diseases": [],
    #             }
    #         )
    #         named_entities: List[str] = []  # This stores the NEs for the whole document
    #         ke.named_entities = []  # This stores the NEs the extractor knows about

    #         if self.chunking:
    #             text_list = chunk_text(text)
    #         else:
    #             text_list = iter([text])

    #         for chunked_text in text_list:
    #             extraction = ke.extract_from_text(chunked_text)
    #             if extraction.extracted_object is not None:
    #                 logger.info(
    #                     f"{len(extraction.extracted_object.chemicals)}\
    #                         chemical entities from window: {chunked_text}"
    #                 )
    #                 logger.info(
    #                     f"{len(extraction.extracted_object.diseases)}\
    #                         disease entities from window: {chunked_text}"
    #                 )
    #             if not predicted_obj and extraction.extracted_object is not None:
    #                 predicted_obj = extraction.extracted_object
    #             else:
    #                 if predicted_obj is not None and extraction.extracted_object is not None:
    #                     predicted_obj.chemicals.extend(extraction.extracted_object.chemicals)
    #                     predicted_obj.diseases.extend(extraction.extracted_object.diseases)
    #                     logger.info(
    #                         f"{len(predicted_obj.chemicals)} chemical entities, after concatenation"
    #                     )
    #                     logger.info(
    #                         f"{len(predicted_obj.diseases)} disease entities, after concatenation"
    #                     )
    #                     logger.debug(f"concatenated chemical entities: {predicted_obj.chemicals}")
    #                     logger.debug(f"concatenated disease entities: {predicted_obj.diseases}")
    #             if extraction.named_entities is not None:
    #                 for entity in extraction.named_entities:
    #                     if entity not in named_entities:
    #                         named_entities.append(entity)

    #         def included(t: str):
    #             if t.startswith("MESH:"):
    #                 return t

    #         predicted_obj.chemicals = [t for t in predicted_obj.chemicals if included(t)]
    #         predicted_obj.diseases = [t for t in predicted_obj.diseases if included(t)]

    #         logger.info(f"{len(predicted_obj.chemicals)} filtered chemical entities (MESH only)")
    #         logger.info(f"{len(predicted_obj.diseases)} filtered disease entities (MESH only)")
    #         pred = PredictionNER(
    #             predicted_object=predicted_obj, test_object=doc, named_entities=named_entities
    #         )
    #         named_entities.clear()
    #         logger.info("PRED")
    #         logger.info(yaml.dump(data=pred.model_dump()))
    #         logger.info("Calc scores")
    #         pred.calculate_scores(labelers=[labeler])
    #         logger.info(yaml.dump(data=pred.model_dump()))
    #         eos.predictions.append(pred)
    #     self.calc_stats(eos)
    #     return eos

    # def calc_stats(self, eos: EvaluationObjectSetNER):
    #     num_true_positives_ce = sum(p.num_true_positives_ce for p in eos.predictions)
    #     num_false_positives_ce = sum(p.num_false_positives_ce for p in eos.predictions)
    #     num_false_negatives_ce = sum(p.num_false_negatives_ce for p in eos.predictions)
    #     if num_true_positives_ce + num_false_positives_ce == 0:
    #         logger.warning("No true positives or false positives for chemical entities.")
    #         return
    #     eos.precision_ce = num_true_positives_ce / (num_true_positives_ce + num_false_positives_ce)
    #     eos.recall_ce = num_true_positives_ce / (num_true_positives_ce + num_false_negatives_ce)
    #     if eos.precision_ce + eos.recall_ce == 0:
    #         logger.warning("No precision or recall for chemical entities.")
    #         return
    #     eos.f1_ce = 2 * (eos.precision_ce * eos.recall_ce) / (eos.precision_ce + eos.recall_ce)

    #     num_true_positives_de = sum(p.num_true_positives_de for p in eos.predictions)
    #     num_false_positives_de = sum(p.num_false_positives_de for p in eos.predictions)
    #     num_false_negatives_de = sum(p.num_false_negatives_de for p in eos.predictions)
    #     if num_true_positives_de + num_false_positives_de == 0:
    #         logger.warning("No true positives or false positives for disease entities.")
    #         return
    #     eos.precision_de = num_true_positives_de / (num_true_positives_de + num_false_positives_de)
    #     eos.recall_de = num_true_positives_de / (num_true_positives_de + num_false_negatives_de)
    #     if eos.precision_de + eos.recall_de == 0:
    #         logger.warning("No precision or recall for disease entities.")
    #         return
    #     eos.f1_de = 2 * (eos.precision_de * eos.recall_de) / (eos.precision_de + eos.recall_de)
