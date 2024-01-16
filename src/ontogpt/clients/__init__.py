"""Clients for accessing different APIs."""
import logging
from ontogpt.clients.openai_client import OpenAIClient  # noqa:F401

# from ontogpt.clients.hfhub_client import HFHubClient  # noqa:F401
from ontogpt.clients.pubmed_client import PubmedClient  # noqa:F401
from ontogpt.clients.soup_client import SoupClient  # noqa:F401

# GPT4ALL support is optional, so 
# if it's not installed, we'll just skip it
try:
    from llm_gpt4all import Gpt4AllModel # noqa:F401
    from ontogpt.clients.gpt4all_client import GPT4AllClient  # noqa:F401
except ModuleNotFoundError:
    logger = logging.getLogger(__name__)
    logger.warning("llm_gpt4all module not found. GPT4All support will be disabled.")
