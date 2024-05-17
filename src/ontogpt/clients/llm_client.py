"""Client for running LLM completion requests through LiteLLM."""

import logging
from dataclasses import dataclass, field
from typing import Optional

from litellm import completion
from oaklib.utilities.apikey_manager import get_apikey_value
import openai # For error handling

logger = logging.getLogger(__name__)


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
                messages=[{"content": self.prompt, "role": "user"}],
                temperature=self.temperature,
            )
        except openai.APITimeoutError as e:
            print(f"Encountered API timeout error: {e}")
        except Exception as e:
            print(f"Encountered error: {type(e)}, Error: {e}")

        payload = response.choices[0].message.content

        return payload
