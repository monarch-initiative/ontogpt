"""Backward-compatible OpenAI client module.

This module remains importable for older code paths that still reference
``ontogpt.clients.openai_client`` even though LLM access now routes through
LiteLLM in :mod:`ontogpt.clients.llm_client`.
"""

from ontogpt.clients.llm_client import LLMClient

__all__ = ["LLMClient"]
