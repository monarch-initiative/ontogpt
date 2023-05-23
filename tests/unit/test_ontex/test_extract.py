"""Core tests."""
import logging
import unittest
from typing import Iterator, List, Tuple

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.ontex import extractor
from ontogpt.ontex.extractor import OntologyExtractor, Task
from tests import (
    CELLULAR_ANATOMICAL_ENTITY,
    ENVELOPE,
    INPUT_DIR,
    INTRACELLULAR_ORGANELLE,
    MEMBRANE_BOUNDED_ORGANELLE,
    NUCLEAR_ENVELOPE,
    NUCLEAR_MEMBRANE,
    NUCLEUS,
    ORGANELLE,
    VACUOLE, IMBO,
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
        yield extractor.extract_indirect_superclasses_task(select_random=True), None
        yield extractor.extract_indirect_superclasses_task(
            subclass=NUCLEUS, siblings=[VACUOLE], roots=[ORGANELLE]
        ), [ORGANELLE, INTRACELLULAR_ORGANELLE, MEMBRANE_BOUNDED_ORGANELLE]
        yield extractor.extract_most_recent_common_subsumers_task(
            subclass1=NUCLEUS, subclass2=VACUOLE, siblings=[NUCLEAR_MEMBRANE], roots=[]
        ), [IMBO]
        yield extractor.extract_incoherent_ontology_task(
            incoherents=[NUCLEUS],
            siblings=[VACUOLE],
            disjoints=[(ORGANELLE, ENVELOPE)],
            spiked_relationships=[(NUCLEUS, IS_A, NUCLEAR_MEMBRANE)],
            roots=[CELLULAR_ANATOMICAL_ENTITY],
        ), [NUCLEUS]
        yield extractor.extract_subclass_of_expression_task(
            superclass=NUCLEUS,
            predicate=PART_OF,
            siblings=[VACUOLE],
        ), [NUCLEAR_MEMBRANE, NUCLEAR_ENVELOPE]

    def test_extract(self):
        """Test extract seed ontology."""
        extractor = self.extractor
        for task, expected in self.cases():
            print(yaml.dump(task.dict(), sort_keys=False))
            answer_texts = [a.text for a in task.answers]
            if expected is not None:
                self.assertCountEqual(answer_texts, [extractor._name(x) for x in expected])
