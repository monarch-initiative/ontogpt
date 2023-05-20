"""Core tests."""
import logging
import unittest
from typing import Iterator

import yaml
from oaklib import get_adapter, get_implementation_from_shorthand
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.engines.reasoner_engine import ReasonerEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.ontex import extractor
from ontogpt.ontex.extractor import OntologyExtractor, Task
from tests import (
    BIOLOGICAL_PROCESS,
    IMBO,
    INPUT_DIR,
    NUCLEAR_MEMBRANE,
    NUCLEUS,
    ORGANELLE,
    OUTPUT_DIR,
    VACUOLE, ENVELOPE, CELLULAR_ANATOMICAL_ENTITY, MEMBRANE, PLASMA_MEMBRANE,
)

TEST_ONTOLOGY_OAK = INPUT_DIR / "go-nucleus.db"


logger = logging.getLogger(extractor.__name__)
logger.setLevel(level=logging.INFO)


class TestReasoning(unittest.TestCase):
    """Test ability to convert from OAK to native HALO form."""

    def setUp(self) -> None:
        """Set up."""
        self.adapter = get_adapter(str(TEST_ONTOLOGY_OAK))
        if not isinstance(self.adapter, OboGraphInterface):
            raise ValueError("Not an OboGraphInterface")
        self.extractor = OntologyExtractor(adapter=self.adapter)
        self.reasoner = ReasonerEngine()
        # self.reasoner.client.model = "gpt-4"

    def tasks(self) -> Iterator[Task]:
        extractor = self.extractor
        yield extractor.extract_indirect_superclasses_task(
            subclass=NUCLEUS, siblings=[VACUOLE], roots=[ORGANELLE]
        )
        yield extractor.extract_indirect_superclasses_task(
            subclass=IMBO, siblings=[NUCLEUS], roots=[ORGANELLE, BIOLOGICAL_PROCESS]
        )
        yield extractor.extract_incoherent_ontology_task(
            incoherents=[NUCLEUS], siblings=[VACUOLE], disjoints=[(ORGANELLE, ENVELOPE)],
            spiked_relationships=[(NUCLEUS, IS_A, NUCLEAR_MEMBRANE)],
            roots=[CELLULAR_ANATOMICAL_ENTITY]
        )
        yield extractor.extract_incoherent_ontology_task(
            incoherents=[PLASMA_MEMBRANE], siblings=[NUCLEUS], disjoints=[(ORGANELLE, MEMBRANE)],
            spiked_relationships=[(PLASMA_MEMBRANE, IS_A, MEMBRANE)],
            roots=[CELLULAR_ANATOMICAL_ENTITY]
        )

    def test_reason(self):
        """Test extract seed ontology."""
        reasoner = self.reasoner
        results = []
        for task in self.tasks():
            result = reasoner.reason(task)
            print(yaml.dump(result.dict(), sort_keys=False))
            print(result.prompt)
            results.append(result)
        for result in results:
            print(f"Result: {result.jaccard_score} {result.false_positives} {result.false_negatives}")

    def test_reason_with_explanations(self):
        """Test extract seed ontology."""
        reasoner = self.reasoner
        results = []
        for task in self.tasks():
            task.include_explanations = True
            result = reasoner.reason(task)
            print(result.prompt)
            result.prompt = None
            result.completion = None
            print(yaml.dump(result.dict(), sort_keys=False))
            results.append(result)
        for result in results:
            print(f"Result: {result.jaccard_score} {result.false_positives} {result.false_negatives}")
