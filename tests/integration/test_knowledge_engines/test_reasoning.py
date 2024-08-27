"""Core tests for reasoning with knowledge engines."""

import logging
import unittest
from typing import Iterator, List

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.engines.reasoner_engine import ReasonerEngine, ReasonerResult, ReasonerResultSet
from ontogpt.io.csv_wrapper import write_obj_as_csv
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.ontex import extractor
from ontogpt.ontex.extractor import OntologyExtractor, Task
from tests import (
    BIOLOGICAL_PROCESS,
    CELLULAR_ANATOMICAL_ENTITY,
    CELLULAR_ORGANISMS,
    ENVELOPE,
    FUNGI,
    IMBO,
    INPUT_DIR,
    MAMMALIA,
    MEMBRANE,
    NUCLEAR_ENVELOPE,
    NUCLEAR_MEMBRANE,
    NUCLEUS,
    ORGANELLE,
    OUTPUT_DIR,
    PLASMA_MEMBRANE,
    VACUOLE,
)

TEST_ONTOLOGY_OAK = INPUT_DIR / "go-nucleus.db"


logger = logging.getLogger(extractor.__name__)
logger.setLevel(level=logging.INFO)


class TestReasoning(unittest.TestCase):
    """Test ability to convert from OAK to native HALO form."""

    def setUp(self) -> None:
        """Set up OAK adapter, extractor, and reasoner."""
        self.adapter = get_adapter(str(TEST_ONTOLOGY_OAK))
        if not isinstance(self.adapter, OboGraphInterface):
            raise ValueError("Not an OboGraphInterface")
        self.extractor = OntologyExtractor(adapter=self.adapter)
        self.reasoner = ReasonerEngine()
        # self.reasoner.client.model = "gpt-4"

    def save(self, results: List[ReasonerResult], name: str):
        rset = ReasonerResultSet(name=name, results=results)
        model = self.reasoner.client.model
        with open(OUTPUT_DIR / f"reasoner-{name}-{model}.yaml", "w") as f:
            f.write(dump_minimal_yaml(rset))
        path = str(OUTPUT_DIR / f"reasoner-{name}-{model}.tsv")
        write_obj_as_csv(results, path)

    def tasks(self) -> Iterator[Task]:
        extractor = self.extractor
        # yield extractor.extract_indirect_superclasses_task(
        #     name="random",
        #     select_random=True,
        # )
        yield extractor.extract_transitive_superclasses_task(
            name="transitive-ancestor-nucleus",
            subclass=NUCLEUS,
            siblings=[VACUOLE],
            roots=[ORGANELLE],
        )
        yield extractor.extract_indirect_superclasses_task(
            name="indirect-ancestor-nucleus",
            subclass=NUCLEUS,
            siblings=[VACUOLE],
            roots=[ORGANELLE],
        )
        yield extractor.extract_transitive_superclasses_task(
            name="transitive-ancestor-nuclear-membrane",
            subclass=IMBO,
            siblings=[NUCLEUS],
            roots=[ORGANELLE, BIOLOGICAL_PROCESS],
        )
        yield extractor.extract_indirect_superclasses_task(
            name="indirect-ancestor-nuclear-membrane",
            subclass=IMBO,
            siblings=[NUCLEUS],
            roots=[ORGANELLE, BIOLOGICAL_PROCESS],
        )
        yield extractor.extract_indirect_superclasses_task(
            name="ancestor-nuclear-envelope",
            subclass=NUCLEAR_MEMBRANE,
            siblings=[NUCLEAR_ENVELOPE],
            roots=[CELLULAR_ANATOMICAL_ENTITY],
        )
        yield extractor.extract_indirect_superclasses_task(
            name="ancestor-human",
            subclass=IMBO,
            siblings=[NUCLEUS],
            roots=[ORGANELLE, BIOLOGICAL_PROCESS],
        )
        yield extractor.extract_most_recent_common_subsumers_task(
            name="mrca-nucleus-vacuole",
            subclass1=NUCLEUS,
            subclass2=VACUOLE,
            siblings=[NUCLEAR_MEMBRANE],
            roots=[],
        )
        yield extractor.extract_subclass_of_expression_task(
            name="subclass-of-part-of-nuclear-envelope",
            superclass=NUCLEUS,
            predicate=PART_OF,
            siblings=[VACUOLE],
        )
        yield extractor.extract_incoherent_ontology_task(
            name="incoherent-nucleus",
            incoherents=[NUCLEUS],
            siblings=[VACUOLE],
            disjoints=[(ORGANELLE, ENVELOPE)],
            spiked_relationships=[(NUCLEUS, IS_A, NUCLEAR_MEMBRANE)],
            roots=[CELLULAR_ANATOMICAL_ENTITY],
        )
        yield extractor.extract_incoherent_ontology_task(
            name="incoherent-plasma-membrane",
            incoherents=[PLASMA_MEMBRANE],
            siblings=[NUCLEUS],
            disjoints=[(ORGANELLE, MEMBRANE)],
            spiked_relationships=[(PLASMA_MEMBRANE, IS_A, ORGANELLE)],
            roots=[CELLULAR_ANATOMICAL_ENTITY],
        )
        yield extractor.extract_incoherent_ontology_task(
            name="incoherent-ok-organism",
            incoherents=[],
            siblings=[],
            disjoints=[(MAMMALIA, FUNGI)],
            spiked_relationships=[],
            roots=[CELLULAR_ORGANISMS],
        )

    def test_reason(self):
        """Test basic reasoning, no explanations."""
        reasoner = self.reasoner
        results = []
        for task in self.tasks():
            result = reasoner.reason(task)
            print(yaml.dump(result.model_dump(), sort_keys=False))
            print(result.prompt)
            results.append(result)
            ReasonerResultSet(results=[result])
        for result in results:
            print(
                f"Result: {result.jaccard_score} {result.false_positives} {result.false_negatives}"
            )
        self.save(results, "basic")

    def test_reason_with_explanations(self):
        """Test reasoning with explanations included."""
        reasoner = self.reasoner
        results = []
        for task in self.tasks():
            task.include_explanations = True
            result = reasoner.reason(task)
            print(result.prompt)
            print(yaml.dump(result.model_dump(), sort_keys=False))
            results.append(result)
        for result in results:
            print(
                f"Result: {result.jaccard_score} {result.false_positives} {result.false_negatives}"
            )
        self.save(results, "explanation")

    def test_reason_with_chain_of_thought(self):
        """Test reasoning with explicit chain-of-thought trigger."""
        reasoner = self.reasoner
        results = []
        for task in self.tasks():
            task.chain_of_thought = True
            result = reasoner.reason(task)
            print(result.prompt)
            print(yaml.dump(result.model_dump(), sort_keys=False))
            results.append(result)
        for result in results:
            print(
                f"Result: {result.jaccard_score} {result.false_positives} {result.false_negatives}"
            )
        self.save(results, "chain-of-thought")
