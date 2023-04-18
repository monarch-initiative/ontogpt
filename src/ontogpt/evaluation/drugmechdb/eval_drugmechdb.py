"""
DrugMechDB evaluation.

Source Data Model: a direct transliteration of the DrugMechDB schema
Target Data Model: the semllama native representation of drugs and mechanism
"""
import gzip
import logging
from dataclasses import dataclass
from pathlib import Path
from random import shuffle
from typing import Any, Dict, List, Optional, TextIO, Union

import yaml
from oaklib import get_implementation_from_shorthand
from pydantic import BaseModel

import ontogpt.evaluation.drugmechdb.datamodel.drugmechdb as source_datamodel
import ontogpt.templates.drug as target_datamodel
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.evaluation_engine import SimilarityScore, SPIRESEvaluationEngine

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"
MOA_TEXTS = DATABASE_DIR / "drugbank-to-mechanism-text.tsv"
TEST_CASES_DIR = THIS_DIR / "test_cases"
EXEMPLARS_DIR = THIS_DIR / "exemplars"
EXEMPLAR_CASES = EXEMPLARS_DIR / "drugmechdb-exemplars.yaml"


def _fix_source_mechanism(mechanism_dict: dict) -> dict:
    """Fix the id field in Graph objects.

    drugmechdb uses `_id` in the json but this is not
    compatible with pydantic, so we translate to `id`

    https://github.com/linkml/linkml/issues/1179
    """
    g = mechanism_dict["graph"]
    g["id"] = g["_id"]
    del g["_id"]
    # normalize alt_ids
    bad_fields = ["all_id", "alt_name", "alt-name", "comemt", "comemnt"]
    for n in mechanism_dict["nodes"]:
        if "alt_ids" in n and isinstance(n["alt_ids"], str):
            n["alt_ids"] = [n["alt_ids"]]
        for f in bad_fields:
            if f in n:
                del n[f]
                # don't bother trying to repair for now - too messy
    for f in bad_fields:
        if f in mechanism_dict:
            del mechanism_dict[f]
    # print(mechanism_dict)
    return mechanism_dict


def _fix_id(id: Optional[str]) -> str:
    return id.replace("UniProt:", "PR:").replace("DB:", "drugbank:") if id else None


class PredictionDrugMechDB(BaseModel):
    predicted_object: target_datamodel.DrugMechanism = None
    test_object: target_datamodel.DrugMechanism = None
    scores: Dict[str, SimilarityScore] = None
    named_entities: List[Any] = None

    def calculate_scores(self):
        self.scores = {}

        def all_objects(dm: target_datamodel.DrugMechanism):
            return list(
                set(link.subject for link in dm.mechanism_links)
                | set(link.object for link in dm.mechanism_links)
            )

        self.scores["similarity"] = SimilarityScore.from_set(
            all_objects(self.test_object),
            all_objects(self.predicted_object),
        )


class EvaluationObjectSetDrugMechDB(BaseModel):
    """A result of predicting paths."""

    test: List[target_datamodel.DrugMechanism] = None
    training: List[target_datamodel.DrugMechanism] = None
    predictions: List[PredictionDrugMechDB] = None


@dataclass
class EvalDrugMechDB(SPIRESEvaluationEngine):
    # ontology: OboGraphInterface = None
    data: List[target_datamodel.DrugMechanism] = None
    _drug_to_mechanism_text: Dict[str, str] = None
    default_labelers = [
        "sqlite:obo:mesh",
        "sqlite:obo:drugbank",
        "sqlite:obo:go",
        "sqlite:obo:uberon",
        "sqlite:obo:pr",
    ]

    def __post_init__(self):
        self.extractor = SPIRESEngine("drug.DrugMechanism")
        self.extractor.labelers = [
            get_implementation_from_shorthand(lab) for lab in self.default_labelers
        ]

    @property
    def drug_to_mechanism_text(self) -> Dict[str, str]:
        """Mapping between drugbank id and MOA text from drugbank record.

        :return:
        """
        if self._drug_to_mechanism_text is None:
            with open(MOA_TEXTS, "r") as f:
                self._drug_to_mechanism_text = {}
                for line in f:
                    toks = line.strip().split("\t")
                    if len(toks) != 2:
                        logging.warning(f"Bad line: {line}")
                        continue
                    drug, text = toks
                    if text != "NA":
                        self._drug_to_mechanism_text[f"drugbank:{drug}"] = text
        return self._drug_to_mechanism_text

    def load_source_mechanisms_from_path(
        self, file: Union[str, Path, TextIO]
    ) -> List[source_datamodel.Mechanism]:
        if isinstance(file, Path):
            file = str(file)
        if isinstance(file, str):
            with open(file, "r") as f:
                return self.load_source_mechanisms_from_path(f)
        mechanisms = yaml.safe_load(file)
        print(f"Loading {len(mechanisms)} mechanism objects from yaml; translating...")
        return [source_datamodel.Mechanism(**_fix_source_mechanism(m)) for m in mechanisms]

    def load_exemplars(self) -> List[target_datamodel.DrugMechanism]:
        srcs = self.load_source_mechanisms_from_path(EXEMPLAR_CASES)
        return [self.transform_mechanism(m) for m in srcs]

    def load_and_transform_source_database(self) -> List[target_datamodel.DrugMechanism]:
        """Load the entire DrugMechDB database."""
        with gzip.open(str(DATABASE_DIR / "indication_paths.yaml.gz"), "rb") as f:
            srcs = self.load_source_mechanisms_from_path(f)
            return [self.transform_mechanism(m) for m in srcs]

    def load_target_database(self) -> List[target_datamodel.DrugMechanism]:
        """Load the entire DrugMechDB database."""
        with gzip.open(str(DATABASE_DIR / "drugmechdb-normalized.yaml.gz"), "rb") as f:
            objs = yaml.safe_load(f)
            return [target_datamodel.DrugMechanism(**m) for m in objs]

    def transform_mechanism(
        self, mechanism: source_datamodel.Mechanism
    ) -> target_datamodel.DrugMechanism:
        """Translate a mechanism from DrugMechDB to the target template."""
        triples = []
        for link in mechanism.links:
            triples.append(
                target_datamodel.MechanismLink(
                    subject=_fix_id(link.source),
                    object=_fix_id(link.target),
                    predicate=link.key,
                )
            )
        # the source YAML is a little odd;
        # - the singular field "reference" is usually a *list*
        # - the field "references" is usually a single string
        refs = mechanism.reference if mechanism.reference else []
        if mechanism.references:
            refs.append(mechanism.references)
        return target_datamodel.DrugMechanism(
            disease=mechanism.graph.disease_mesh,
            drug=_fix_id(mechanism.graph.drugbank),
            mechanism_links=triples,
            references=refs,
        )

    def create_test_and_training(
        self, num_test: int = 10, num_training: int = 5, include_texts: bool = False
    ) -> EvaluationObjectSetDrugMechDB:
        """Create a test and training set from the DrugMechDB database."""
        if self.data is None:
            mechanisms = self.load_target_database()
        else:
            mechanisms = self.data
        if include_texts:
            mechanisms = [m for m in mechanisms if m.drug in self.drug_to_mechanism_text]
        shuffle(mechanisms)
        return EvaluationObjectSetDrugMechDB(
            test=mechanisms[:num_test],
            training=mechanisms[num_test : num_test + num_training],
        )

    def create_training_set(self, num=100):
        ke = self.extractor
        mechanisms = self.load_target_database()
        mechanisms = [m for m in mechanisms if m.drug in self.drug_to_mechanism_text]
        shuffle(mechanisms)
        for m in mechanisms[0:num]:
            stub = {
                "disease": m.disease,
                "drug": m.drug,
            }
            text = self.drug_to_mechanism_text[m.drug]
            prompt = ke.get_completion_prompt(None, text, object=stub)
            completion = ke.serialize_object(m)
            yield dict(prompt=prompt, completion=completion)

    def eval(self) -> EvaluationObjectSetDrugMechDB:
        """Evaluate the ability to extract a path from MOA text."""
        num_test = self.num_tests
        ke = self.extractor
        mechanisms = self.load_target_database()

        def is_candidate(m: target_datamodel.DrugMechanism):
            if m.drug not in self.drug_to_mechanism_text:
                return False
            if len(m.references) != 1:
                return False
            ref = m.references[0]
            if ref.startswith("https://go.drugbank.com/drugs/") and ref.endswith(
                "#mechanism-of-action"
            ):
                return True
            return False

        mechanisms = [m for m in mechanisms if is_candidate(m)]
        print(f"Using {len(mechanisms)} mechanisms")
        shuffle(mechanisms)
        eos = EvaluationObjectSetDrugMechDB(
            test=mechanisms[:num_test],
            training=[],
            predictions=[],
        )
        print(yaml.dump(eos.dict()))
        for test_obj in eos.test:
            text = self.drug_to_mechanism_text[test_obj.drug]
            test_obj.source_text = text
            print(yaml.dump(test_obj.dict()))
            stub = {
                "disease": test_obj.disease,
                "drug": test_obj.drug,
            }
            results = ke.extract_from_text(text, object=stub)
            predicted_obj = results.extracted_object
            pred = PredictionDrugMechDB(predicted_object=predicted_obj, test_object=test_obj)
            pred.named_entities = results.named_entities
            print(yaml.dump(pred.dict()))
            pred.calculate_scores()
            print(yaml.dump(pred.dict()))
            eos.predictions.append(pred)
        return eos

    def eval_path_prediction(self) -> EvaluationObjectSetDrugMechDB:
        """Evaluate the ability to predict a path purely from background knowledge in the LLM.

        :return:
        """
        ke = self.extractor
        eos = self.create_test_and_training(num_test=self.num_tests, num_training=self.num_training)
        eos.predictions = []
        print(yaml.dump(eos.dict()))
        for test_obj in eos.test:
            print(yaml.dump(test_obj.dict()))
            stub = {
                "disease": test_obj.disease,
                "drug": test_obj.drug,
            }
            results = ke.generalize(stub, eos.training)
            predicted_obj = results.extracted_object[0]
            pred = PredictionDrugMechDB(predicted_object=predicted_obj, test_object=test_obj)
            pred.calculate_scores()
            eos.predictions.append(pred)
        return eos
