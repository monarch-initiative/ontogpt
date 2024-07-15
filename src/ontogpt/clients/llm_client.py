"""Client for running LLM completion requests through LiteLLM."""

import litellm
import logging
from dataclasses import dataclass, field
from typing import Optional

from litellm import completion, embedding
from litellm.caching import Cache
import numpy as np
from oaklib.utilities.apikey_manager import get_apikey_value
import openai  # For error handling

from ontogpt import DEFAULT_MODEL

logger = logging.getLogger(__name__)

# These are model sources which we expect to be explicitly named
# within the model or deployment name, e.g. "ollama/llama2"
# TODO: Let litellm handle this too
SERVICES = ["azure", "huggingface", "ollama", "openrouter", "replicate"]


@dataclass
class LLMClient:

    model: str = field(default_factory=lambda: DEFAULT_MODEL)
    cache_db_path: str = ""
    api_key: str = ""
    api_base: str = None
    api_version: str = None

    temperature: float = 1.0

    def __post_init__(self):
        # Get appropriate API key for the model source
        # and other details if needed
        if not self.api_key:
            self.api_key = get_apikey_value("openai")
        else:
            for service in SERVICES:
                if self.model.startswith(service):
                    self.api_key = get_apikey_value(service + "-key")
                    if service == "azure" and self.api_base is None:
                        self.api_base = get_apikey_value(service + "-base")
                    if service == "azure" and self.api_version is None:
                        self.api_version = get_apikey_value(service + "-version")

        # Set up the cache, and set the cache path if provided
        if len(self.cache_db_path) == 0:
            litellm.cache = Cache(type="disk")
        else:
            litellm.cache = Cache(type="disk", disk_cache_dir=self.cache_db_path)

    def complete(self, prompt, show_prompt: bool = False, **kwargs) -> str:

        logger.info(f"Complete: engine={self.model}, prompt[{len(prompt)}]={prompt[0:100]}...")
        if show_prompt:
            logger.info(f" SENDING PROMPT:\n{prompt}")

        response = None

        try:
            # TODO: expose user prompt to CLI
            response = completion(
                api_key=self.api_key,
                api_base=self.api_base,
                api_version=self.api_version,
                model=self.model,
                messages=[{"content": prompt, "role": "user"}],
                temperature=self.temperature,
                caching=True,
            )
        except openai.APITimeoutError as e:
            print(f"Encountered API timeout error: {e}")
        except Exception as e:
            print(f"Encountered error: {type(e)}, Error: {e}")

        if response is not None:
            payload = response.choices[0].message.content
        else:
            logger.error(f"No response or response is empty.")
            payload = ""

        return payload

    def embeddings(self, text: str):
        text = str(text)

        # TODO: set embedding model based on model source
        # Or at least set the default for OpenAI models
        if self.model is None:
            model = "text-embedding-ada-002"

        logger.info(f"Retrieving embeddings from {model} for text: {text[0:80]}...")

        response = embedding(
            api_key=self.api_key,
            model=model,
            input=[text],
            caching=True,
        )
        v = response.data[0].embedding

        return v

    def similarity(self, text1: str, text2: str, **kwargs):
        a1 = self.embeddings(text1, **kwargs)
        a2 = self.embeddings(text2, **kwargs)
        logger.debug(f"similarity: {a1[0:10]}... x {a2[0:10]}... // ({len(a1)} x {len(a2)})")
        return np.dot(a1, a2) / (np.linalg.norm(a1) * np.linalg.norm(a2))

    def euclidian_distance(self, text1: str, text2: str, **kwargs):
        a1 = self.embeddings(text1, **kwargs)
        a2 = self.embeddings(text2, **kwargs)
        return np.linalg.norm(np.array(a1) - np.array(a2))
