"""Resolver engine."""

from typing import Optional, Type, Union

from class_resolver import ClassResolver

from ontogpt.engines.halo_engine import HALOEngine  # type: ignore
from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.template_loader import get_template_details

resolver = ClassResolver([SPIRESEngine, HALOEngine], base=KnowledgeEngine)


def create_engine(
    template: str, engine: Optional[Union[str, Type, KnowledgeEngine]] = None, **kwargs
) -> Union[KnowledgeEngine, SPIRESEngine]:
    """Create a knowledge engine."""
    template_details = get_template_details(template=template)
    if engine is None:
        engine = SPIRESEngine(template_details=template_details)
    if isinstance(engine, str):
        engine = resolver.get_class(engine)(**kwargs)
    if engine is not None and not isinstance(engine, str):
        return engine(template_details=template_details, **kwargs)  # type: ignore
    else:
        return SPIRESEngine  # type: ignore
