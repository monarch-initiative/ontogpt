"""Core tests."""
import unittest

import yaml

from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.drugmechdb.datamodel.drugmechdb import Graph, Mechanism
from ontogpt.evaluation.drugmechdb.eval_drugmechdb import EvalDrugMechDB, _fix_source_mechanism
from tests import OUTPUT_DIR

NORMALIZED_OUT = OUTPUT_DIR / "drugmechdb-normalized.yaml"
PREDICTIONS_OUT = OUTPUT_DIR / "eval-drugmechdb-predictions.yaml"
EXTRACTION_OUT = OUTPUT_DIR / "eval-drugmechdb-extraction.yaml"
TRAINING_OUT = OUTPUT_DIR / "training-drugmechdb.yaml"

EXAMPLE_SOURCE = """
-   directed: true
    graph:
        _id: DB00316_MESH_D018771_1
        disease: Arthralgia
        disease_mesh: MESH:D018771
        drug: Acetaminophen
        drug_mesh: MESH:D000082
        drugbank: DB:DB00316
    links:
    -   key: decreases activity of
        source: MESH:D000082
        target: UniProt:P23219
    -   key: decreases activity of
        source: MESH:D000082
        target: UniProt:P35354
    -   key: decreases activity of
        source: MESH:D000082
        target: UniProt:Q15185
    -   key: positively regulates
        source: UniProt:P23219
        target: GO:0001516
    -   key: positively regulates
        source: UniProt:P35354
        target: GO:0001516
    -   key: positively regulates
        source: UniProt:Q15185
        target: GO:0001516
    -   key: increases abundance of
        source: GO:0001516
        target: MESH:D011453
    -   key: positively correlated with
        source: MESH:D011453
        target: MESH:D018771
    multigraph: true
    nodes:
    -   id: MESH:D000082
        label: Drug
        name: Acetaminophen
    -   id: UniProt:P23219
        label: Protein
        name: Prostaglandin G/H synthase 1
    -   id: UniProt:P35354
        label: Protein
        name: Prostaglandin G/H synthase 2
    -   id: UniProt:Q15185
        label: Protein
        name: Prostaglandin E synthase 3
    -   id: GO:0001516
        label: BiologicalProcess
        name: prostaglandin biosynthetic process
    -   id: MESH:D011453
        label: ChemicalSubstance
        name: Prostaglandins
    -   id: MESH:D018771
        label: Disease
        name: Arthralgia
    reference:
    - https://go.drugbank.com/drugs/DB00316#mechanism-of-action
    - https://www.uniprot.org/uniprot/P23219#function
    - https://www.uniprot.org/uniprot/P35354#function
    - https://www.uniprot.org/uniprot/Q15185#function
    - https://en.wikipedia.org/wiki/Arthralgia
"""


class TestDrugMechDB(unittest.TestCase):
    """Test GO evaluation."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.engine = EvalDrugMechDB()

    def test_data_model(self):
        g = Graph(id="x")
        m = Mechanism(
            directed=True,
            graph={
                "id": "DB11888_MESH_D007251_1",
            },
        )

    def test_load_exemplars(self):
        mechanisms = self.engine.load_exemplars()
        objs = [m.dict() for m in mechanisms]
        print(yaml.dump(objs[0:5]))
        self.assertGreater(len(mechanisms), 0)

    def test_transform(self):
        objs = yaml.safe_load(EXAMPLE_SOURCE)
        obj = _fix_source_mechanism(objs[0])
        src_mechanism = Mechanism(**obj)
        r = self.engine.transform_mechanism(src_mechanism)
        print(yaml.dump(r.model_dump()))

    def test_load_and_transform_source_database(self):
        """
        Tests the ability to translate the source DrugMechDB yaml into Llama model.

        This is currently slow: this test may be skipped.

        If the source YAML changes, then re-run this and copy the file from
        the output directory (drugmechdb-normalized.yaml) to

        :return:
        """
        mechanisms = self.engine.load_and_transform_source_database()
        print(f"Loaded {len(mechanisms)} mechanisms")
        objs = [m.dict() for m in mechanisms]
        with open(NORMALIZED_OUT, "w") as f:
            yaml.dump(objs, f)
        print(yaml.dump(objs[0:5]))
        self.assertGreater(len(mechanisms), 0)

    def test_load_target_database(self):
        mechanisms = self.engine.load_target_database()
        print(f"Loaded {len(mechanisms)} mechanisms")
        objs = [m.dict() for m in mechanisms[0:5]]
        print(yaml.dump(objs))
        self.assertGreater(len(mechanisms), 0)

    def test_drug_to_mechanism_text(self):
        self.assertTrue(
            self.engine.drug_to_mechanism_text["drugbank:DB00005"].startswith(
                "There are two distinct receptors"
            )
        )

    def test_training_set(self):
        evaluator = self.engine
        ke = evaluator.extractor
        training_set = list(evaluator.create_training_set(100))
        t = dict(base_model="gpt-4o", template=ke.template, examples=training_set)
        with open(TRAINING_OUT, "w") as f:
            yaml.dump(t, f)
        # print(yaml.dump(training_set))

    def test_eval_extraction(self):
        evaluator = self.engine
        evaluator.num_tests = 100
        eos = evaluator.eval()
        with open(EXTRACTION_OUT, "w") as f:
            yaml.dump(eos.dict(), f)

    @unittest.skip("Skip this test because it takes a long time and is more expensive")
    def test_eval_fine_tuned_extraction(self):
        evaluator = EvalDrugMechDB()
        ft = "davinci:ft-lawrence-berkeley-national-laboratory:drugmechdb-001-2022-12-22-02-25-40"
        evaluator.extractor = SPIRESEngine("drug.DrugMechanism", engine=ft)
        evaluator.num_tests = 40
        eos = evaluator.eval()
        with open(EXTRACTION_OUT, "w") as f:
            yaml.dump(eos.dict(), f)

    def test_eval_generalize(self):
        evaluator = self.engine
        evaluator.num_tests = 3
        evaluator.num_training = 3
        mechanisms = self.engine.load_exemplars()
        evaluator.data = mechanisms
        eos = evaluator.eval_path_prediction()
        with open(PREDICTIONS_OUT, "w") as f:
            yaml.dump(eos.dict(), f)
