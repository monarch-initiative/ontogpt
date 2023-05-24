"""Core tests."""
import logging
import unittest
from typing import Iterator, List, Tuple

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.ontex import extractor
from ontogpt.ontex.extractor import OntologyExtractor, Task, TaskCollection
from tests import (
    CELLULAR_ANATOMICAL_ENTITY,
    ENVELOPE,
    FUNGI,
    IMBO,
    INPUT_DIR,
    INTRACELLULAR_ORGANELLE,
    MEMBRANE_BOUNDED_ORGANELLE,
    NUCLEAR_ENVELOPE,
    NUCLEAR_MEMBRANE,
    NUCLEUS,
    ORGANELLE,
    OUTPUT_DIR,
    VACUOLE,
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
        # yield extractor.extract_indirect_superclasses_task(select_random=True), None
        yield extractor.extract_transitive_superclasses_task(
            subclass=NUCLEUS, siblings=[VACUOLE], roots=[ORGANELLE]
        ), [ORGANELLE, IMBO, INTRACELLULAR_ORGANELLE, MEMBRANE_BOUNDED_ORGANELLE]
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
        yield extractor.extract_subclass_of_expression_task(
            superclass=IMBO,
            predicate=PART_OF,
            siblings=[FUNGI],
        ), [NUCLEAR_MEMBRANE, NUCLEAR_ENVELOPE]

    def test_extract(self):
        """Test extract tasks."""
        extractor = self.extractor
        for task, expected in self.cases():
            if not task.ontology.axioms:
                raise ValueError(f"Task {task} has no axioms")
            print(yaml.dump(task.dict(), sort_keys=False))
            answer_texts = [a.text for a in task.answers]
            if expected is not None:
                self.assertCountEqual(answer_texts, [extractor._name(x) for x in expected])

    def test_random(self):
        """Test extract random tasks."""
        extractor = self.extractor
        tc = extractor.create_random_tasks(20)
        for task in tc.tasks:
            if not task.answers:
                print(f"Task {task} has no answers")
                # raise ValueError(f"Task {task} has no answers")
            if not task.ontology.axioms:
                raise ValueError(f"Task {task} has no axioms")
                # raise ValueError(f"Task {task} has no axioms")
        path = OUTPUT_DIR / "random-reasoner-tasks.yaml"
        with open(path, "w") as f:
            f.write(dump_minimal_yaml(tc))
        tc = TaskCollection.load(path)
        task_types = {type(obj) for obj in tc.tasks}
        print(len(tc.tasks))
        print(task_types)
        self.assertEqual(len(task_types), 5)
