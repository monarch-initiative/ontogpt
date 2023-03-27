"""Core tests."""
import pickle
import unittest

from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import CASES_DIR, OUTPUT_DIR

CASES = [
    ("recipe", "recipe-palak-paneer"),
    ("treatment", "treatment-schiz"),
    ("recipe.Recipe", "recipe-spaghetti"),
    ("recipe.Recipe", "recipe-tortilla-soup"),
    ("recipe.Recipe", "recipe-egg-noodles"),
    ("mendelian_disease.MendelianDisease", "mendelian-disease-cmt2e-summary"),
    ("mendelian_disease.MendelianDisease", "mendelian-disease-cmt2e"),
    ("drug.DrugMechanism", "drug-DB00316-moa"),
    ("metagenome_study.Study", "environment-jgi2"),
    ("environmental_sample.Study", "environment-jgi1"),
    ("reaction.ReactionDocument", "reaction-20657015"),
    ("reaction.GeneToReaction", "reaction-21290071"),
    ("gocam.GoCamAnnotations", "gocam-27929086"),
    ("gocam.GoCamAnnotations", "gocam-33246504"),
    ("gocam.GoCamAnnotations", "gocam-betacat"),
    ("environmental_sample.Study", "environmental-sample-hyporheic"),
    ("treatment.DiseaseTreatmentSummary", "treatment-marfan"),
    ("treatment.DiseaseTreatmentSummary", "treatment-eds"),
    ("mendelian_disease.MendelianDisease", "mendelian-disease-sly"),
    ("mendelian_disease.MendelianDisease", "mendelian-disease-marfan"),
    ("environmental_sample.Study", "amphibian_skin"),
    ("environmental_sample.Study", "human_urban_green_space"),
    ("environmental_sample.Study", "human_smoking_China"),
]


class TestCases(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        ke_map = {}
        for template, _ in CASES:
            ke_map[template] = SPIRESEngine(template, recurse=True, auto_prefix="AUTO")
        self.ke_map = ke_map

    def test_cases(self):
        """Tests end to end knowledge extraction."""
        for template, input_name in CASES:
            ke = self.ke_map[template]
            input_file = CASES_DIR / f"{input_name}.txt"
            ann = ke.extract_from_file(input_file)
            # print(yaml.dump(ann.dict()))
            # for ne in ke.named_entities:
            #    print(yaml.dump(ne.dict()))
            # result_dict = {
            #    "input_file": str(input_file),
            #    "text": ke.last_text,
            #    "results": ann.dict(),
            #    "named_entities": [ne.dict() for ne in ke.named_entities],
            # }
            # print(yaml.dump(result_dict))
            output_file = str(OUTPUT_DIR / f"{input_name}.yaml")
            print(f"Writing {output_file}")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(dump_minimal_yaml(ann))
            pkl_output_file = str(OUTPUT_DIR / f"{input_name}.pickle")
            print(f"Writing {pkl_output_file}")
            with open(pkl_output_file, "wb") as f:
                f.write(pickle.dumps(ann))
