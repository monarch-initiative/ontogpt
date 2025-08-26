"""
Evaluation on the CRAFT corpus.

This is an NER evaluation, or specifically
concept recognition.

It uses a specific template (craft_concepts).

The corpus is from:
https://github.com/UCDenver-ccp/CRAFT

This evaluation uses the v5.0.2 release.

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

Note: documents in this test corpus are full-texts
and may not fit into the context window of all
models. Please consider models with context window
of 12K tokens or greater.

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
from ontogpt.templates.craft_concept import (
    Document,
    NamedEntity,
    Publication,
    TextWithEntity,
)

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database" / "all"

MONDO_PURL_PREFIX = "http://purl.obolibrary.org/obo/MONDO_"

# These are the entity types involved in this dataset,
# along with their corresponding prefixes.
# GO terms need to be checked during sorting
# so they go to the correct subset.
TARGET_TYPES = {
    "AnatomicalElement": "UBERON",
    "BiologicalProcess": "GO",
    "CellType": "CL",
    "CellularComponent": "GO",
    "Chemical": "CHEBI",
    "Disease": "MONDO",
    "MolecularFunction": "GO",
    "MolecularProcess": "MOP",
    "Protein": "PR",
    "SequenceFeature": "SO",
    "Taxon": "NCBITaxon",
}

TARGET_ATTR_TYPES = [
    "publication",
    "anatomicalelements",
    "biologicalprocesses",
    "celltypes",
    "cellularcomponents",
    "chemicals",
    "diseases",
    "molecularfunctions",
    "molecularprocesses",
    "proteins",
    "sequencefeatures",
    "taxa",
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
    # results is a dict of dict of lists of tuples
    results: Dict[str, Dict[str, List[Tuple[str, str]]]] = {}
    for target in TARGET_ATTR_TYPES:
         results[target] = {}
         for result_type in RESULT_TYPES:
             results[target[result_type]] = []

    scores: Optional[Dict[str, SimilarityScore]] = None
    predicted_object: Optional[TextWithEntity] = None
    named_entities: Optional[List[Any]] = None

    def calculate_scores(self):
        self.scores = {}

        def all_objects(dm: Optional[TextWithEntity]):
            if dm is not None:
                return list(set(dm.chemicals + dm.diseases))
            else:
                return list()

        def chem_entities(dm: TextWithEntity) -> Set:
            if dm.chemicals is not None:
                return set(((entity)) for entity in dm.chemicals)
            else:
                return set()

        def disease_entities(dm: TextWithEntity) -> Set:
            if dm.diseases is not None:
                return set(((entity)) for entity in dm.diseases)
            else:
                return set()

        self.scores["similarity"] = SimilarityScore.from_set(
            all_objects(self.test_object),
            all_objects(self.predicted_object),
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

    precisions: List[float] = [0]
    recalls: List[float] = [0]
    f1s: List[float] = [0]

    training: Optional[List[TextWithEntity]] = None
    predictions: Optional[List[PredictionNER]] = None
    test: Optional[List[TextWithEntity]] = None


@dataclass
class EvalCRAFTConcepts(SPIRESEvaluationEngine):
    # TODO: nope, not these
    subject_prefix = "MESH"
    object_prefix = "MESH"

    def __post_init__(self):
        self.extractor = SPIRESEngine(template="craft_concept.Document", model=self.model)

    def load_test_cases(self) -> Iterable[Document]:
        return self.load_cases(DATABASE_DIR)

    # Load cases from txt and ann files
    def load_cases(self, path: Path) -> Iterable[Document]:
        logger.info(f"Loading {path}")

        entities_by_text = defaultdict(list)

        # Load documents
        # Remove extra empty lines from input text
        # Parse annotations to identifier only
        # MONDO ids are full PURLs for some reason, so fix those too
        for docfilepath in path.glob("*.txt"):
            logger.info(f"Loading text doc {docfilepath}")
            with open(docfilepath, "r") as docfile:
                title = docfile.readline().rstrip()
                doctext = docfile.read().replace("\n\n", "\n")
            logger.debug(
                f"Title: {title}\nDocument Text (truncated): {doctext[0:100]}...({len(doctext[100:])} chars)"
            )
            annfilepath = docfilepath.with_suffix(".ann")
            logger.info(f"Loading corresponding annotation file {annfilepath}")
            with open(annfilepath, "r") as annfile:
                annotations = annfile.readlines()

            # Get annotations and validate as CURIEs
            these_annotations = []
            for annotation in annotations:
                uri = (annotation.split())[1]
                if uri.startswith(MONDO_PURL_PREFIX):
                    uri = uri.replace(MONDO_PURL_PREFIX, "MONDO:")
                if uri not in these_annotations:
                    these_annotations.append(uri)
                e = NamedEntity.model_validate(
                    {
                        "id": uri,
                    }
                )
                entities_by_text[(title, doctext)].append(e.id)

        i = 0
        go_map = {}
        goad = get_adapter("sqlite:obo:go")
        for (title, doctext), _entities in entities_by_text.items():
            i = i + 1
            logging.debug(f"Loading document {i}")
            pub = Publication.model_validate(
                {
                    "id": str(i),
                    "title": title,
                    "abstract": doctext,  # Yes, it's the full text, but this is the slot name
                }
            )
            all_entities = entities_by_text[(title, doctext)]

            # Do entity sorting
            # Results should be unique - no duplicates
            # Check on GO terms too
            logger.info(f"Sorting {len(all_entities)} redundant entities for Title: {title}")
            entities_by_type = {key: [] for key in TARGET_TYPES.keys()}
            for entity in all_entities:
                prefix = (entity.split(":"))[0]
                # Check if this is a GO CURIE first and find substype
                # We store these subtypes too
                if prefix == "GO":
                    if entity in go_map:
                        go_type = go_map[entity]
                    else:
                        try:
                            go_meta = goad.entity_metadata_map(entity)
                            go_type = go_meta["oio:hasOBONamespace"][0]
                        except KeyError:
                            go_dep = go_meta["owl:deprecated"][0]
                            if go_dep:
                                logger.warning(f"{entity} is deprecated. Ignoring...")
                            else:
                                logger.warning(f"{entity} has something wrong with it. Ignoring...")
                        go_map[entity] = go_type
                    if go_type == "biological_process":
                        entities_by_type["BiologicalProcess"].append(entity)
                    elif go_type == "molecular_function":
                        entities_by_type["MolecularFunction"].append(entity)
                    elif go_type == "cellular_component":
                        entities_by_type["CellularComponent"].append(entity)
                    continue
                else:
                    for entity_type in TARGET_TYPES:
                        if prefix == TARGET_TYPES[entity_type]:
                            if entity not in entities_by_type[entity_type]:
                                entities_by_type[entity_type].append(entity)
                            break
            for entity_type in entities_by_type:
                logger.debug(f"{entity_type}: {len(entities_by_type[entity_type])}")
            yield Document.model_validate(
                {
                    "publication": pub,
                    "anatomicalelements": entities_by_type["AnatomicalElement"],
                    "biologicalprocesses": entities_by_type["BiologicalProcess"],
                    "celltypes": entities_by_type["CellType"],
                    "cellularcomponents": entities_by_type["CellularComponent"],
                    "chemicals": entities_by_type["Chemical"],
                    "diseases": entities_by_type["Disease"],
                    "molecularfunctions": entities_by_type["MolecularFunction"],
                    "molecularprocesses": entities_by_type["MolecularProcess"],
                    "proteins": entities_by_type["Protein"],
                    "sequencefeatures": entities_by_type["SequenceFeature"],
                    "taxa": entities_by_type["Taxon"],
                }
            )

    def eval(self) -> EvaluationObjectSetNER:
        """Evaluate the ability to extract and ground entities in CRAFT corpus."""

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
            logger.info(doc.publication.title)
            text = f"{doc.publication.title}\n{doc.publication.abstract}"
            pub = Publication.model_validate(
                {
                    "id": str(doc.publication.id),
                    "title": doc.publication.title,
                    "abstract": doc.publication.abstract,
                }
            )
            predicted_obj = Document.model_validate(
                {
                    "publication": pub,
                    "anatomicalelements": [],
                    "biologicalprocesses": [],
                    "celltypes": [],
                    "cellularcomponents": [],
                    "chemicals": [],
                    "diseases": [],
                    "molecularfunctions": [],
                    "molecularprocesses": [],
                    "proteins": [],
                    "sequencefeatures": [],
                    "taxa": [],
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
                    logger.info("Found entities in active window.")
                if not predicted_obj and extraction.extracted_object is not None:
                    predicted_obj = extraction.extracted_object
                else:
                    if predicted_obj is not None and extraction.extracted_object is not None:
                        for entity_type in TARGET_ATTR_TYPES:
                            pred_entity_list_attr = getattr(predicted_obj, entity_type)
                            extraction_list_attr = getattr(extraction.extracted_object, entity_type)
                            new_entity_list = pred_entity_list_attr.extend(extraction_list_attr)
                            setattr(predicted_obj, entity_type, new_entity_list)
                            logger.info(
                                f"{len(new_entity_list)} {entity_type} entities, after concatenation"
                            )
                if extraction.named_entities is not None:
                    for entity in extraction.named_entities:
                        if entity not in named_entities:
                            named_entities.append(entity)

            predicted_obj.anatomicalelements = [
                t for t in predicted_obj.anatomicalelements if t.startswith("UBERON")
            ]
            predicted_obj.biologicalprocesses = [
                t for t in predicted_obj.anatomicalelements if t.startswith("GO")
            ]
            predicted_obj.celltypes = [
                t for t in predicted_obj.anatomicalelements if t.startswith("CL")
            ]
            predicted_obj.cellularcomponents = [
                t for t in predicted_obj.anatomicalelements if t.startswith("GO")
            ]
            predicted_obj.chemicals = [
                t for t in predicted_obj.anatomicalelements if t.startswith("CHEBI")
            ]
            predicted_obj.diseases = [
                t for t in predicted_obj.anatomicalelements if t.startswith("MONDO")
            ]
            predicted_obj.molecularfunctions = [
                t for t in predicted_obj.anatomicalelements if t.startswith("GO")
            ]
            predicted_obj.molecularprocesses = [
                t for t in predicted_obj.anatomicalelements if t.startswith("MOP")
            ]
            predicted_obj.proteins = [
                t for t in predicted_obj.anatomicalelements if t.startswith("PR")
            ]
            predicted_obj.sequencefeatures = [
                t for t in predicted_obj.anatomicalelements if t.startswith("SO")
            ]
            predicted_obj.taxa = [
                t for t in predicted_obj.anatomicalelements if t.startswith("NCBITaxon")
            ]

            pred = PredictionNER(
                predicted_object=predicted_obj, test_object=doc, named_entities=named_entities
            )
            named_entities.clear()
            logger.info("PRED")
            logger.info(yaml.dump(data=pred.model_dump()))
            logger.info("Calc scores")
            pred.calculate_scores()
            logger.info(yaml.dump(data=pred.model_dump()))
            eos.predictions.append(pred)
        self.calc_stats(eos)
        return eos

    def calc_stats(self, eos: EvaluationObjectSetNER):
        #for attr_type in TARGET_ATTR_TYPES:
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
