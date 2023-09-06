"""Evaluate GO."""
from dataclasses import dataclass
from pathlib import Path
from random import shuffle
from typing import Dict, List

import yaml
from oaklib import get_implementation_from_shorthand
from oaklib.datamodels.obograph import LogicalDefinitionAxiom
from oaklib.datamodels.vocabulary import IS_A
from oaklib.interfaces.obograph_interface import OboGraphInterface
from pydantic import BaseModel

from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.evaluation_engine import SimilarityScore, SPIRESEvaluationEngine
from ontogpt.templates.metabolic_process import MetabolicProcess

TEST_CASES_DIR = Path(__file__).parent / "test_cases"

METABOLIC_PROCESS = "GO:0008152"
BIOSYNTHESIS = "GO:0009058"
HAS_PRIMARY_OUTPUT = "RO:0004008"


class PredictionGO(BaseModel):
    predicted_object: MetabolicProcess = None
    test_object: MetabolicProcess = None
    scores: Dict[str, SimilarityScore] = None

    def calculate_scores(self):
        self.scores = {}
        for k in ["synonyms", "subclass_of", "inputs", "outputs"]:
            self.scores[k] = SimilarityScore.from_set(
                getattr(self.test_object, k, []),
                getattr(self.predicted_object, k, []),
            )
        for k in ["description"]:
            self.scores[k] = SimilarityScore.from_set(
                getattr(self.test_object, k, "").split(),
                getattr(self.predicted_object, k, "").split(),
            )


class EvaluationObjectSetGO(BaseModel):
    """A result of extracting knowledge on text."""

    test: List[MetabolicProcess] = None
    training: List[MetabolicProcess] = None
    predictions: List[PredictionGO] = None


@dataclass
class EvalGO(SPIRESEvaluationEngine):
    ontology: OboGraphInterface = None
    genus: str = BIOSYNTHESIS
    differentia_relation: str = HAS_PRIMARY_OUTPUT

    def __post_init__(self):
        ontology = get_implementation_from_shorthand("sqlite:obo:go")
        if not isinstance(ontology, OboGraphInterface):
            raise TypeError
        self.ontology = ontology
        self.extractor = SPIRESEngine("metabolic_process.MetabolicProcess")
        self.extractor.labelers = [ontology]

    def make_term_from_ldef(self, ldef: LogicalDefinitionAxiom) -> MetabolicProcess:
        """Make a term from a logical definition."""
        ontology = self.ontology
        term = ldef.definedClassId
        parents = [rel[2] for rel in ontology.relationships([term], [IS_A])]
        mp = MetabolicProcess(
            id=term,
            label=ontology.label(term),
            description=ontology.definition(term),
            synonyms=list(ontology.entity_aliases(term)),
            subclass_of=parents,
        )
        r = ldef.restrictions[0]
        if r.propertyId != HAS_PRIMARY_OUTPUT:
            raise NotImplementedError
        mp.outputs = [r.fillerId]
        return mp

    def valid_test_ids(self) -> List[str]:
        with open(TEST_CASES_DIR / "go-ids-2022.txt") as f:
            return [x.strip() for x in f.readlines()]

    def ldef_matches(self, ldef: LogicalDefinitionAxiom) -> bool:
        """Check if a logical definition matches the genus and differentia."""
        if self.genus not in ldef.genusIds:
            return False
        if len(ldef.restrictions) != 1:
            return False
        if self.differentia_relation != ldef.restrictions[0].propertyId:
            return False
        return True

    def create_test_and_training(
        self, num_test: int = 10, num_training: int = 10
    ) -> EvaluationObjectSetGO:
        """
        Create a test and training set of GO terms.

        This takes around 1m to run.
        """
        ontology = self.ontology
        entities = set(ontology.descendants([self.genus], [IS_A]))
        print(
            f"Found {len(entities)} entities that are descendants of\
                genus {self.genus}; {list(entities)[0:5]}"
        )
        assert "GO:0140872" in entities
        all_test_ids = set(self.valid_test_ids())
        assert "GO:0140872" in all_test_ids
        print(f"Found {len(all_test_ids)} test id candidates; {list(entities)[0:5]}")
        candidate_test_ids = entities.intersection(all_test_ids)
        print(f"Found {len(candidate_test_ids)} candidate test ids")
        assert "GO:0140872" in candidate_test_ids
        candidate_train_ids = entities.difference(all_test_ids)
        print(f"Found {len(candidate_train_ids)} candidate train ids")
        entities = list(candidate_test_ids) + list(candidate_train_ids)
        print(f"Found {len(entities)} entities from {type(ontology)}")
        ldefs = list(ontology.logical_definitions(entities))
        shuffle(ldefs)
        # ldefs = list(ontology.logical_definitions())
        print(f"Found {len(ldefs)} logical definitions")
        ldefs = [ldef for ldef in ldefs if self.ldef_matches(ldef)]
        print(f"Found {len(ldefs)} matching logical definitions")
        ldefs_test = [ldef for ldef in ldefs if ldef.definedClassId in candidate_test_ids]
        print(f"Found {len(ldefs_test)} matching logical definitions for test set")
        ldefs_train = [ldef for ldef in ldefs if ldef.definedClassId not in candidate_test_ids]
        print(f"Found {len(ldefs_train)} matching logical definitions for training set")
        shuffle(ldefs_test)
        shuffle(ldefs_train)
        test = [self.make_term_from_ldef(ldef) for ldef in ldefs_test[:num_test]]
        training = [self.make_term_from_ldef(ldef) for ldef in ldefs_train[:num_training]]

        eos = EvaluationObjectSetGO(test=test, training=training)
        return eos

    def eval(self) -> EvaluationObjectSetGO:
        ke = self.extractor
        eos = self.create_test_and_training()
        eos.predictions = []
        print(yaml.dump(eos.dict()))
        for test_obj in eos.test[0:10]:
            print(yaml.dump(test_obj.dict()))
            predicted_obj = ke.generalize({"label": test_obj.label}, eos.training[0:4])
            pred = PredictionGO(predicted_object=predicted_obj, test_object=test_obj)
            pred.calculate_scores()
            eos.predictions.append(pred)
        return eos
