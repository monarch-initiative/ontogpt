"""HPOA evaluation."""
import csv
import logging
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from random import shuffle
from typing import Dict, Iterable, Iterator, List, Tuple

from oaklib import BasicOntologyInterface, get_implementation_from_shorthand
from oaklib.datamodels.search import SearchConfiguration
from oaklib.datamodels.search_datamodel import SearchProperty
from oaklib.interfaces import SearchInterface
from pydantic import BaseModel

from ontogpt.clients.pubmed_client import PubmedClient
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.evaluation_engine import SimilarityScore, SPIRESEvaluationEngine
from ontogpt.templates.mendelian_disease import MendelianDisease

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"
TEST_CASES_DIR = THIS_DIR / "test_cases"
EXEMPLARS_DIR = THIS_DIR / "exemplars"
EXEMPLAR_CASES = EXEMPLARS_DIR / "drugmechdb-exemplars.yaml"


DISEASE_ID = str
TERM = str
ASPECT = str
PUBLICATION = str


class PredictionHPOA(BaseModel):
    predicted_object: MendelianDisease = None
    test_object: MendelianDisease = None
    scores: Dict[str, SimilarityScore] = None

    def calculate_scores(self):
        self.scores = {}
        for k in ["synonyms", "subclass_of", "symptoms", "disease_onsets", "genes"]:
            self.scores[k] = SimilarityScore.from_set(
                getattr(self.test_object, k, []),
                getattr(self.predicted_object, k, []),
            )
        for k in ["description", "name", "inheritance"]:
            if getattr(self.test_object, k):
                self.scores[k] = SimilarityScore.from_set(
                    getattr(self.test_object, k, "").split(),
                    getattr(self.predicted_object, k, "").split(),
                )


class EvaluationObjectSetHPOA(BaseModel):
    """A result of predicting paths."""

    test: List[MendelianDisease] = None
    training: List[MendelianDisease] = None
    predictions: List = None


class HPOAnnotation(BaseModel):
    subject: DISEASE_ID = None
    term: TERM = None
    aspect: ASPECT = None
    publication: PUBLICATION = None


@dataclass
class EvalHPOA(SPIRESEvaluationEngine):
    mondo: BasicOntologyInterface = None

    def __post_init__(self):
        self.extractor = SPIRESEngine("mendelian_disease.MendelianDisease")
        self.mondo = get_implementation_from_shorthand("sqlite:obo:mondo")

    def load_test_cases(self) -> List[MendelianDisease]:
        return []

    def disease_text(self, id: str):
        id = id.replace("OMIM:", "omim-")
        with open(TEST_CASES_DIR / f"{id}.txt") as f:
            return f.read()

    def parse_hpoa(self) -> Iterator[HPOAnnotation]:
        with open(TEST_CASES_DIR / "test.hpoa.tsv") as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                yield HPOAnnotation(
                    subject=row[0],
                    term=row[3],
                    publication=row[4],
                    aspect=row[10],
                )

    def annotations_to_diseases(
        self, anns: Iterable[HPOAnnotation] = None
    ) -> List[MendelianDisease]:
        if anns is None:
            anns = self.parse_hpoa()
        diseases: Dict[str, MendelianDisease] = {}
        for ann in anns:
            subject = ann.subject
            term = ann.term
            pub = ann.publication
            aspect = ann.aspect
            if subject not in diseases:
                diseases[subject] = MendelianDisease(id=subject)
            disease = diseases[subject]
            # print(f"Adding {term} to {subject} in {aspect}")
            if aspect == "P":
                disease.symptoms.append(term)
            elif aspect == "C":
                disease.disease_onsets.append(term)
            elif aspect == "I":
                disease.inheritance = term
            if pub and pub not in disease.publications:
                disease.publications.append(pub)
        return list(diseases.values())

    def diseases(self, anns: Iterable[HPOAnnotation] = None) -> List[MendelianDisease]:
        diseases = self.annotations_to_diseases(anns)
        for disease in diseases:
            self.enhance(disease)
        return diseases

    def diseases_by_publication(self) -> Dict[Tuple[DISEASE_ID, PUBLICATION], MendelianDisease]:
        anns = list(self.parse_hpoa())
        tuple2ann = defaultdict(list)
        for ann in anns:
            if ann.publication and ann.publication.startswith("PMID:"):
                tuple2ann[(ann.subject, ann.publication)].append(ann)
        tuple2disease = {}
        for k, anns in tuple2ann.items():
            diseases = self.annotations_to_diseases(anns)
            if len(diseases) != 1:
                raise AssertionError(f"Expected 1 disease, got {len(diseases)} for {k}")
            disease = diseases[0]
            self.enhance(disease)
            tuple2disease[k] = disease
        return tuple2disease

    def enhance(self, obj: MendelianDisease):
        mondo = self.mondo
        config = SearchConfiguration(properties=[SearchProperty.MAPPED_IDENTIFIER])
        if not isinstance(mondo, SearchInterface):
            raise ValueError("Mondo is not a SearchInterface")
        entities = list(mondo.basic_search(obj.id, config))
        if len(entities) == 0:
            logging.warning(f"No matches for {obj.id} => {entities}")
            return
        if len(entities) > 1:
            logging.warning(f"multiple matches for {obj.id} => {entities}")
        entity = entities[0]
        obj.name = mondo.label(entity)
        obj.label = obj.name
        obj.description = mondo.definition(entity)
        obj.subclass_of = list(mondo.hierararchical_parents(entity))
        obj.synonyms = list(mondo.entity_aliases(entity))
        for _s, _p, gene in mondo.relationships([entity], ["RO:0004003"]):
            gene = (
                gene.replace("http://identifiers.org/hgnc/", "HGNC:")
                .replace("<", "")
                .replace(">", "")
            )
            obj.genes.append(gene)
        return obj

    def eval(self, task: str = None, **kwargs) -> EvaluationObjectSetHPOA:
        if not task or task == "pubs":
            return self.eval_against_pubs(**kwargs)
        elif task == "omim":
            return self.eval_against_omim(**kwargs)
        elif task == "all":
            return self.eval_against_omim_plus_pubs(**kwargs)
        else:
            raise ValueError(f"Unknown task {task}")

    def eval_against_pubs(self, num_tests=3) -> EvaluationObjectSetHPOA:
        ke = self.extractor
        pmc = PubmedClient()
        eos = EvaluationObjectSetHPOA()
        eos.test = list(self.diseases_by_publication().values())
        eos.training = []
        eos.predictions = []
        shuffle(eos.test)
        for test_case in eos.test[0:num_tests]:
            # text = self.disease_text(test_case.id)
            if len(test_case.publications) != 1:
                raise ValueError(f"Expected 1 publication, got {len(test_case.publications)}")
            pub = test_case.publications[0]
            text = pmc.text(pub)
            results = ke.extract_from_text(text)
            predicted_obj = results.extracted_object
            pred = PredictionHPOA(predicted_object=predicted_obj, test_object=test_case)
            pred.calculate_scores()
            eos.predictions.append(pred)
        return eos

    def eval_against_omim(self, **kwargs) -> EvaluationObjectSetHPOA:
        return self.eval_against_omim_or_pubs(use_publications=False)

    def eval_against_omim_plus_pubs(self, **kwargs) -> EvaluationObjectSetHPOA:
        return self.eval_against_omim_or_pubs(use_publications=True)

    def eval_against_omim_or_pubs(
        self, num_tests=3, use_publications=False
    ) -> EvaluationObjectSetHPOA:
        ke = self.extractor
        eos = EvaluationObjectSetHPOA()
        eos.test = self.diseases()
        eos.training = []
        eos.predictions = []
        shuffle(eos.test)
        for test_case in eos.test[0:num_tests]:
            text = self.disease_text(test_case.id)
            stub = {"name": test_case.name}
            results = ke.extract_from_text(text, object=stub)
            if use_publications:
                pmc = PubmedClient()
                pub_resultset = []
                for pmid in test_case.publications:
                    if pmid.startswith("PMID:"):
                        pub_text = pmc.text(pmid)
                        pub_resultset.append(ke.extract_from_text(pub_text, object=stub))
                results = ke.merge_resultsets([results] + pub_resultset, ["name"])
            predicted_obj = results.extracted_object
            pred = PredictionHPOA(predicted_object=predicted_obj, test_object=test_case)
            pred.calculate_scores()
            eos.predictions.append(pred)
        return eos
