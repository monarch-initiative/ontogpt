from typing import Optional, Type, Union

from class_resolver import ClassResolver

from ontogpt.engines.halo_engine import HALOEngine
from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.engines.spires_engine import SPIRESEngine

resolver = ClassResolver([SPIRESEngine, HALOEngine], base=KnowledgeEngine)


def create_engine(
    template: str, model: Optional[Union[str, Type]] = None, **kwargs
) -> KnowledgeEngine:
    """Create a knowledge engine."""
    if model is None:
        model = SPIRESEngine
    if isinstance(model, str):
        model = resolver.get_class(model)(**kwargs)
    return model(template, **kwargs)
