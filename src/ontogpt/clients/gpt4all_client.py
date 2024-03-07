"""GPT4All Client."""
import logging
from dataclasses import dataclass, field
from typing import Optional

import llm

logger = logging.getLogger(__name__)

# GPT4ALL support is optional, so 
# if it's not installed, we'll just skip it
# Normally the __init__ gets this
# So this bit is here in case we try a direct import
try:
    from llm_gpt4all import Gpt4AllModel
except ModuleNotFoundError:
    logger.warning("llm_gpt4all module not found. GPT4All support will be disabled.")

@dataclass
class GPT4AllClient:
    """A client for interfacing with local GPT4All models.

    This interfaces with the llm-gpt4all module.
    """

    model: str = field(default_factory=lambda: "orca-mini-3b-gguf2-q4_0")
    cache_db_path: str = ""
    api_key: str = ""

    # TODO: Explicitly deprecate interactive mode for local models
    interactive: Optional[bool] = None

    local_model: Gpt4AllModel = None

    def __post_init__(self):
        logging.info(f"Preparing {self.model} for local use...")
        if self.model not in llm.get_model_aliases():
            raise ValueError(f"Model {self.model} not found in llm.get_model_aliases()")
        print(llm.get_model_aliases())
        self.local_model = llm.get_model(self.model)

    # Use this command in subsequent calls
    def chain_gpt4all_model(model, prompt_text):
        """Interact with a GPT4All model."""
        raw_output = model.prompt(prompt_text)

        return raw_output.text()

    # TODO: Dynamically update max_tokens
    # For now, this argument is ignored
    def complete(self, prompt, max_tokens=3000, show_prompt: bool = False, **kwargs) -> str:
        engine = self.model
        logger.info(f"Complete: engine={engine}, prompt[{len(prompt)}]={prompt[0:100]}...")
        if show_prompt:
            logger.info(f" SENDING PROMPT:\n{prompt}")

        response = None
        logger.debug("Prompting model for completion...")
        try:
            response = self.local_model.prompt(prompt)
        except Exception as e:
            logger.error(f"Encountered error: {e}")

        payload = response.text()

        return payload

    def db_connection(self):
        raise NotImplementedError("GPT4All local models do not currently support caching.")

    def cached_completions(self):
        raise NotImplementedError("GPT4All local models do not currently support caching.")

    def embeddings(self):
        raise NotImplementedError("GPT4All local models do not currently support embeddings.")

    def similarity(self):
        raise NotImplementedError("GPT4All local models do not currently support similarity.")

    def euclidian_distance(self):
        raise NotImplementedError(
            "GPT4All local models do not currently support distance measurement."
        )
