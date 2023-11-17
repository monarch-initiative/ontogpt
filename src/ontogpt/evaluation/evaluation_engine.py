"""
Evaluation Engines.

An evaluation engine incorporates different components to evaluate KE:

 1. ETL-ing the data from the source and mapping to a target schema
 2. Selecting test and training cases from a source database
 3. Executing the KE
 4. Calculating scores comparing test with training

"""

from dataclasses import dataclass
from typing import List, Optional, Set, Type, Union 

from oaklib import BasicOntologyInterface
from pydantic import BaseModel

from ontogpt.engines.spires_engine import SPIRESEngine


def jaccard_index(a: Set, b: Set):
    """Compute the Jaccard index between two sets."""
    if not a and not b:
        return None
    return len(a & b) / len(a | b)


class SimilarityScore(BaseModel):
    """
    Scores for an individual prediction.

    The scores are computed as the Jaccard index between the predicted and true sets.
    """

    jaccard: Optional[float]
    false_positives: Optional[List[Optional[str]]]
    false_negatives: Optional[List[Optional[str]]]
    common: Optional[List[str]]

    @staticmethod
    def from_set(
        test_list: List,
        prediction_list: List,
        labelers: Optional[List[BasicOntologyInterface]] = None,
    ):
        if labelers:

            def label(x):
                for labeler in labelers:
                    if type(labeler) == list:
                        lbl = labeler[0].label(x)
                    else:
                        lbl = labeler.label(x)
                    if lbl:
                        return f"{x} {lbl}"
                return x

            test_list = [label(x) for x in test_list]
            prediction_list = [label(x) for x in prediction_list]
        test_set = set(test_list)
        prediction_set = set(prediction_list)
        return SimilarityScore(
            jaccard=jaccard_index(test_set, prediction_set),
            false_positives=list(prediction_set - test_set),
            false_negatives=list(test_set - prediction_set),
            common=list(test_set & prediction_set),
        )


@dataclass
class EvaluationEngine:
    pass


@dataclass
class SPIRESEvaluationEngine(EvaluationEngine):
    """Base class for all evaluation engines in SPIRES.

    TODO: currently there is a lot of repetition between the different evaluation engines.
    This should be refactored so we have common base classes for different tasks

    - NamedEntity Recognition
    - Simple Relation Extraction, i.e. pairs of subject-object (e.g CTD task)
    - Triple Extraction, i.e. triples of subject-predicate-object
    - Complex Relation Extraction, i.e. triples of subject-predicate-object with\
        additional information, e.g. qualifiers
    - Structured Knowledge Extraction, i.e. arbitrary nested objects including\
        both literals and edges
    """

    extractor: SPIRESEngine = None
    """Knowledge extractor to use"""

    num_tests: Optional[Union[int, Type]] = 10
    """Number of test cases to use for evaluation"""

    num_training: Optional[Union[int, Type]] = 5
    """Number of training/exemplar cases to use for evaluation in generalization task.
    Note this number will be low as we use few-shot learning."""

    chunking: Optional[Union[bool, Type]] = False
    """Whether to pre-process input texts by chunking. If True, each chunk gets its own
    prompt. Otherwise, pass the full text with each prompt."""

    model: Optional[Union[str, Type]] = None
    """Name of the model to use in evaluation."""
