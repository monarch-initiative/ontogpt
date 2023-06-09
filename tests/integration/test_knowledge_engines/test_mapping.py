"""Core tests."""
import logging
import unittest

from oaklib import get_adapter
from sssom.parsers import parse_sssom_table, to_mapping_set_document
from sssom_schema import Mapping

from ontogpt.clients import openai_client
from ontogpt.engines import mapping_engine
from ontogpt.engines.mapping_engine import CategorizedMapping, MappingEngine, MappingTaskCollection
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import INPUT_DIR

TEST_ONTOLOGY_OAK = INPUT_DIR / "go-nucleus.db"

HEART = "UBERON:0000948"
NECK_OF_ORGAN = "UBERON:0001560"
MA_NECK_ORGAN = "MA:0000589"
MA_HEART = "MA:0000072"

ENVO_MOUTH = "ENVO:00000479"  # river mouth
WIKIDATA_MOUTH = "wikidata:Q9635"  # anatomical mouth
UBERON_MOUTH = "UBERON:0000165"  # anatomical mouth
UBERON_ORAL_OPENING = "UBERON:0000166"

logger = logging.getLogger(mapping_engine.__name__)
client_logger = logging.getLogger(openai_client.__name__)

client_logger.setLevel(logging.DEBUG)


def _show(mapping_eval: CategorizedMapping):
    print(f"{mapping_eval.subject} -> {mapping_eval.object}")
    print(mapping_eval.completion)
    print(dump_minimal_yaml(mapping_eval.dict()))


class TestMapping(unittest.TestCase):
    """Test ability to convert from OAK to native HALO form."""

    def setUp(self) -> None:
        """Set up OAK adapter, extractor, and reasoner."""
        subject_adapter = get_adapter("sqlite:obo:uberon")
        object_adapter = get_adapter("sqlite:obo:zfa")
        self.mapper = MappingEngine(subject_adapter=subject_adapter, object_adapter=object_adapter)

    def test_generate(self):
        mapper = self.mapper
        subjects = [HEART]
        tc = MappingTaskCollection(name="test", subjects=subjects, object_sources=["ZFA"])
        tasks = list(mapper.generate_tasks(tc))
        for task in tasks:
            print(dump_minimal_yaml(task.dict()))
        tc.tasks = tasks
        results = list(mapper.run_tasks(tc))
        for result in results:
            print(dump_minimal_yaml(result.dict()))

    def test_from_sssom(self):
        mapper = self.mapper

        def _exclude_trivial(m: Mapping) -> bool:
            return m.subject_label.lower() == m.object_label.lower()

        tc = mapper.from_sssom(
            INPUT_DIR / "mondo-exact-ncit.sssom.tsv", exclude_functions=[_exclude_trivial]
        )
        # print(dump_minimal_yaml(tc.dict()))
        results = list(mapper.run_tasks(tc))
        for result in results:
            print(dump_minimal_yaml(result.dict()))

    def test_from_sssom2(self):
        mapper = MappingEngine(
            subject_adapter=get_adapter("sqlite:obo:mondo"),
            object_adapter=get_adapter("sqlite:obo:ncit"),
        )

        msdf = parse_sssom_table(INPUT_DIR / "mondo-exact-ncit.sssom.tsv")
        msd = to_mapping_set_document(msdf)

        def _exclude_trivial(m: Mapping) -> bool:
            return m.subject_label.lower() == m.object_label.lower()

        for m in msd.mapping_set.mappings:
            if _exclude_trivial(m):
                continue
            m2 = mapper.categorize_sssom_mapping(m)
            print(m2)

    def test_mapping_eval(self):
        """Test evaluation of mapping on uberon."""
        mapper = self.mapper
        subjects = [HEART]
        for meval in mapper.categorize_mappings(subjects, object_sources=["ZFA"]):
            _show(meval)

    def test_different_from(self):
        mapper = MappingEngine(
            subject_adapter=get_adapter("sqlite:obo:uberon"),
            object_adapter=get_adapter("sqlite:obo:ma"),
        )
        subjects = [NECK_OF_ORGAN]
        objects = [MA_NECK_ORGAN]
        for subject in subjects:
            for object in objects:
                meval = mapper.categorize_mapping(subject, object)
                _show(meval)

    def test_very_different_from(self):
        mapper = MappingEngine(
            subject_adapter=get_adapter("sqlite:obo:uberon"),
            object_adapter=get_adapter("sqlite:obo:ma"),
        )
        subjects = [HEART]
        objects = [MA_NECK_ORGAN]
        for subject in subjects:
            for object in objects:
                meval = mapper.categorize_mapping(subject, object)
                _show(meval)

    def test_very_different_from2(self):
        mapper = MappingEngine(
            subject_adapter=get_adapter("sqlite:obo:uberon"),
            object_adapter=get_adapter("sqlite:obo:envo"),
        )
        subjects = [UBERON_MOUTH, UBERON_ORAL_OPENING]
        objects = [ENVO_MOUTH]
        for subject in subjects:
            for object in objects:
                meval = mapper.categorize_mapping(subject, object)
                _show(meval)

    def test_species_identical(self):
        mapper = MappingEngine(
            subject_adapter=get_adapter("sqlite:obo:uberon"),
            object_adapter=get_adapter("sqlite:obo:ma"),
        )
        subjects = [HEART]
        objects = [MA_HEART]
        for subject in subjects:
            for object in objects:
                meval = mapper.categorize_mapping(subject, object)
                _show(meval)

    @unittest.skip("Requires new OAK release")
    def test_wikidata(self):
        mapper = MappingEngine(
            subject_adapter=get_adapter("sqlite:obo:envo"), object_adapter=get_adapter("wikidata:")
        )
        subjects = [ENVO_MOUTH]
        objects = [WIKIDATA_MOUTH]
        for subject in subjects:
            for object in objects:
                meval = mapper.categorize_mapping(subject, object)
                _show(meval)
