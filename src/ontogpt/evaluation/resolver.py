"""Evaluation Resolver."""
from typing import Optional, Type, Union

from class_resolver import ClassResolver

from ontogpt.evaluation.ctd.eval_ctd import EvalCTD
from ontogpt.evaluation.evaluation_engine import SPIRESEvaluationEngine

resolver = ClassResolver([EvalCTD], base=SPIRESEvaluationEngine)


def create_evaluator(name: Optional[Union[str, Type]] = None, **kwargs) -> SPIRESEvaluationEngine:
    """Create a knowledge engine."""
    if name is None:
        name = EvalCTD
    if isinstance(name, str):
        return resolver.lookup(name)(**kwargs)
    return name(**kwargs)
