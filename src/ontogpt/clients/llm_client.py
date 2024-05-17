"""Client for running LLM completion requests through LiteLLM."""

import ast
import logging
from dataclasses import dataclass, field
import sqlite3
from typing import Optional

from litellm import completion, embedding
import numpy as np
from oaklib.utilities.apikey_manager import get_apikey_value
import openai  # For error handling

logger = logging.getLogger(__name__)

# TODO: re-add prompt and response caching through litellm
# see https://docs.litellm.ai/docs/caching/all_caches
# It looks like it's supported for embeddings, too,
# even though it's not as well documented


@dataclass
class LLMClient:

    model: str = field(default_factory=lambda: "gpt-3.5-turbo")
    cache_db_path: str = ""
    api_key: str = ""
    # TODO: consider deprecating this in favor
    # of a more general chained mode
    interactive: Optional[bool] = None
    # TODO: deprecate in favor of how litellm handles azure endpoints
    # see https://docs.litellm.ai/docs/providers/azure
    use_azure: Optional[bool] = None

    # TODO: expose to CLI
    temperature: float = 1.0

    def __post_init__(self):

        # TODO: get appropriate API key for the model source
        if not self.api_key:
            self.api_key = get_apikey_value("openai")

    def complete(self, prompt, show_prompt: bool = False, **kwargs) -> str:

        logger.info(f"Complete: engine={self.model}, prompt[{len(prompt)}]={prompt[0:100]}...")
        if show_prompt:
            logger.info(f" SENDING PROMPT:\n{prompt}")

        response = None

        try:
            if self.interactive:
                raise NotImplementedError("Interactive mode not yet supported")
            # TODO: expose user prompt to CLI
            response = completion(
                api_key=self.api_key,
                model=self.model,
                messages=[{"content": prompt, "role": "user"}],
                temperature=self.temperature,
            )
        except openai.APITimeoutError as e:
            print(f"Encountered API timeout error: {e}")
        except Exception as e:
            print(f"Encountered error: {type(e)}, Error: {e}")

        payload = response.choices[0].message.content

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
