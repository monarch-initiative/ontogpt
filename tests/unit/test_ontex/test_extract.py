"""Core tests."""
import logging
import unittest
from typing import Iterator, List, Tuple

import yaml
from oaklib import get_adapter, get_implementation_from_shorthand
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.ontex import extractor
from ontogpt.ontex.extractor import OntologyExtractor, Task
from tests import (
    INPUT_DIR,
    INTRACELLULAR_ORGANELLE,
    MEMBRANE_BOUNDED_ORGANELLE,
    NUCLEUS,
    ORGANELLE,
    OUTPUT_DIR,
    VACUOLE, CELLULAR_ANATOMICAL_ENTITY, ENVELOPE, NUCLEAR_MEMBRANE,
)

TEST_ONTOLOGY_OAK = INPUT_DIR / "go-nucleus.db"


logger = logging.getLogger(extractor.__name__)
logger.setLevel(level=logging.INFO)


class TestOntologyExtractor(unittest.TestCase):
    """Test ability to convert from OAK to native HALO form."""

    def setUp(self) -> None:
        """Set up."""
        self.adapter = get_adapter(str(TEST_ONTOLOGY_OAK))
        if not isinstance(self.adapter, OboGraphInterface):
            raise ValueError("Not an OboGraphInterface")
        self.extractor = OntologyExtractor(adapter=self.adapter)

    def cases(self) -> Iterator[Tuple[Task, List[str]]]:
        extractor = self.extractor
        yield extractor.extract_indirect_superclasses_task(
            subclass=NUCLEUS, siblings=[VACUOLE], roots=[ORGANELLE]
        ), [ORGANELLE, INTRACELLULAR_ORGANELLE, MEMBRANE_BOUNDED_ORGANELLE]
        yield extractor.extract_incoherent_ontology_task(
            incoherents=[NUCLEUS], siblings=[VACUOLE], disjoints=[(ORGANELLE, ENVELOPE)],
            spiked_relationships=[(NUCLEUS, IS_A, NUCLEAR_MEMBRANE)],
            roots=[CELLULAR_ANATOMICAL_ENTITY]
        ), [NUCLEUS]

    def test_extract(self):
        """Test extract seed ontology."""
        extractor = self.extractor
        for task, expected in self.cases():
            print(yaml.dump(task.dict(), sort_keys=False))
            answer_texts = [a.text for a in task.answers]
            self.assertCountEqual(answer_texts, [extractor._name(x) for x in expected])
