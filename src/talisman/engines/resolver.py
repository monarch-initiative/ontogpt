"""Resolver engine."""
from typing import Optional, Type, Union

from class_resolver import ClassResolver

from talisman.engines.enrichment import EnrichmentEngine
from talisman.engines.halo_engine import HALOEngine  # type: ignore
from talisman.engines.knowledge_engine import KnowledgeEngine
from talisman.engines.spires_engine import SPIRESEngine

resolver = ClassResolver([SPIRESEngine, HALOEngine, EnrichmentEngine], base=KnowledgeEngine)


def create_engine(
    template: str, engine: Optional[Union[str, Type]] = None, **kwargs
) -> Union[KnowledgeEngine, SPIRESEngine]:
    """Create a knowledge engine."""
    if engine is None:
        engine = SPIRESEngine
    if isinstance(engine, str):
        engine = resolver.get_class(engine)(**kwargs)
    if engine is not None and not isinstance(engine, str):
        return engine(template, **kwargs)
    else:
        return SPIRESEngine  # type: ignore
