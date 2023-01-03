from typing import Optional, Type, Union

from class_resolver import ClassResolver

from ontogpt.evaluation.ctd.eval_ctd import EvalCTD
from ontogpt.evaluation.evaluation_engine import EvaluationEngine

resolver = ClassResolver([EvalCTD], base=EvaluationEngine)


def create_evaluator(name: Optional[Union[str, Type]] = None, **kwargs) -> EvaluationEngine:
    """Create a knowledge engine."""
    if name is None:
        name = EvalCTD
    if isinstance(name, str):
        return resolver.lookup(name)(**kwargs)
    return name(**kwargs)
