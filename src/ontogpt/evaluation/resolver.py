"""Evaluation Resolver."""

from typing import Optional, Type, Union

from class_resolver import ClassResolver

from ontogpt.evaluation.ctd.eval_ctd import EvalCTD
from ontogpt.evaluation.ctd.eval_ctd_ner import EvalCTDNER
from ontogpt.evaluation.maxo.eval_maxo import EvalMAXO
from ontogpt.evaluation.evaluation_engine import SPIRESEvaluationEngine

resolver = ClassResolver([EvalCTD, EvalCTDNER, EvalMAXO], base=SPIRESEvaluationEngine)


def create_evaluator(
    name: Optional[Union[str, Type]] = None,
    num_tests: Optional[Union[int, Type]] = None,
    chunking: Optional[Union[bool, Type]] = None,
    model: Optional[Union[str, Type]] = None,
    **kwargs,
) -> SPIRESEvaluationEngine:
    """Create a knowledge engine."""
    if name is None:
        name = EvalCTD
    if isinstance(name, str):
        return resolver.lookup(name)(num_tests=num_tests, chunking=chunking, model=model, **kwargs)
    return name(num_tests=num_tests, chunking=chunking, model=model, **kwargs)
