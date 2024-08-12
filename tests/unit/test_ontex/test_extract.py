"""Core tests for extraction."""

import csv
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
TEST_ONTOLOGY_ABOX = INPUT_DIR / "fhkb.db"


logger = logging.getLogger(extractor.__name__)
logger.setLevel(level=logging.INFO)

IS_ANCESTOR_OF = "fhkb:isAncestorOf"
HAS_ANCESTOR = "fhkb:hasAncestor"
HAS_PARENT = "fhkb:hasParent"
IS_PARENT_OF = "fhkb:isParentOf"
HAS_FATHER = "fhkb:hasFather"
HAS_MOTHER = "fhkb:hasMother"
HAS_PARENT = "fhkb:hasParent"
HAS_SIBLING = "fhkb:hasSibling"
HAS_BROTHER = "fhkb:hasBrother"
HAS_SISTER = "fhkb:hasSister"


class TestOntologyExtractor(unittest.TestCase):
    """Test ability to convert from OAK to native HALO form."""

    def setUp(self) -> None:
        """Set up."""
        self.adapter = get_adapter(str(TEST_ONTOLOGY_OAK))
        self.abox_adapter = get_adapter(str(TEST_ONTOLOGY_ABOX))
        if not isinstance(self.adapter, OboGraphInterface):
            raise ValueError("Not an OboGraphInterface")
        self.extractor = OntologyExtractor(adapter=self.adapter)
        self.abox_extractor = OntologyExtractor(adapter=self.abox_adapter)
        self.abox_extractor.query_predicates = [HAS_ANCESTOR, HAS_SIBLING]

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

    @unittest.skip("Non-deterministic")
    def test_random_taxon_constraints(self):
        """Test extract random tasks."""
        extractor = self.extractor
        task = extractor.extract_taxon_constraint_task(select_random=True, never_in=True)
        print(dump_minimal_yaml(task))

    @unittest.skip("Non-deterministic")
    def test_random(self):
        """Test extract random tasks."""
        extractor = self.extractor
        abox_extractor = self.abox_extractor
        abox_tc = abox_extractor.create_random_tasks(20, abox=True)
        tc = extractor.create_random_tasks(20, abox=False)
        tc.tasks.extend(abox_tc.tasks)
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
        # increase this every time you add a new task type
        self.assertEqual(len(task_types), 7)

    @unittest.skip("Non-deterministic")
    def test_random_obfuscated(self):
        extractor = self.extractor
        extractor.obfuscate = True
        abox_extractor = self.abox_extractor
        abox_extractor.obfuscate = True
        abox_tc = abox_extractor.create_random_tasks(20, abox=True)
        tc = extractor.create_random_tasks(20, abox=False)
        # merge
        tc.tasks.extend(abox_tc.tasks)
        for task in tc.tasks:
            if not task.answers:
                print(f"Task {task} has no answers")
                # raise ValueError(f"Task {task} has no answers")
            if not task.ontology.axioms:
                raise ValueError(f"Task {task} has no axioms")
                # raise ValueError(f"Task {task} has no axioms")
        path = OUTPUT_DIR / "obfuscated-reasoner-tasks.yaml"
        with open(path, "w") as f:
            f.write(dump_minimal_yaml(tc))
        tc = TaskCollection.load(path)
        task_types = {type(obj) for obj in tc.tasks}
        print(len(tc.tasks))
        print(task_types)
        # increase this every time you add a new task type
        self.assertEqual(len(task_types), 6)
        self.assertGreater(len(tc.obfuscated_curie_map.keys()), 20)

    def test_introspect(self):
        """Test introspection."""
        root_class = Task
        with open(OUTPUT_DIR / "task-classes.tsv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["code", "task", "description"], delimiter="\t")
            writer.writeheader()
            for subclass in root_class.__subclasses__():
                row = {
                    "code": subclass._code,
                    "task": subclass.__name__,
                    "description": subclass.__doc__.replace("\n", " ").strip(),
                }
                writer.writerow(row)
