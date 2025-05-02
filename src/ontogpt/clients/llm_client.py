"""Client for running LLM completion requests through LiteLLM."""

import logging
import sys
from dataclasses import dataclass, field

import litellm
import numpy as np
import openai  # For error handling
from litellm import completion, embedding
from litellm.caching import Cache
from oaklib.utilities.apikey_manager import get_apikey_value

from ontogpt import DEFAULT_MODEL, MODELS

logger = logging.getLogger(__name__)

# Just get the part before the slash in each model name
SERVICES = {model.split("/")[0] for model in MODELS.keys() if len(model.split("/")) > 1}

# Necessary to avoid repeated debug messages
litellm.suppress_debug_info = True


@dataclass
class LLMClient:

    model: str = field(default_factory=lambda: DEFAULT_MODEL)
    cache_db_path: str = ""
    api_key: str = ""
    api_base: str = None
    api_version: str = None

    # litellm uses this param to specify client when it isn't clear from
    # the model name
    custom_llm_provider: str = None

    temperature: float = 1.0

    system_message: str = ""
    """System message to be provided to the LLM."""

    def __post_init__(self):
        # Get appropriate API key for the model source
        # and other details if needed.
        # This will look at any env vars FIRST,
        # then configs handled by oaklib.

        # Need to check on the validity of the model name first.
        # Check if the model name is a string first.
        # if not, try to make it one
        if not isinstance(self.model, str):
            if isinstance(self.model, (tuple, list)) and len(self.model) > 0:
                self.model = str(self.model[0])
                logger.warning(f"Model name was a {type(self.model).__name__}.")
                logger.warning(f"Converted to string: {self.model}")
            else:
                raise ValueError(f"Model name must be a string, got {type(self.model)}")

        if self.model.startswith("ollama"):
            self.api_key = ""  # Don't need an API key
        elif not self.api_key and not self.custom_llm_provider:
            self.api_key = get_apikey_value("openai")
        elif self.custom_llm_provider == "anthropic":
            self.api_key = get_apikey_value("anthropic-key")
        elif self.custom_llm_provider == "groq":
            self.api_key = get_apikey_value("groq-key")
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

        these_messages = [{"content": prompt, "role": "user"}]

        if self.system_message:
            these_messages.insert(0, {"content": self.system_message, "role": "system"})

        # This toggle controls whether we can continue or not.
        # Some errors may be temporary, while others, such as authentication errors,
        # require action before we may continue.
        force_stop = False

        try:
            # TODO: expose user prompt to CLI
            response = completion(
                api_key=self.api_key,
                api_base=self.api_base,
                api_version=self.api_version,
                model=self.model,
                messages=these_messages,
                temperature=self.temperature,
                caching=True,
                custom_llm_provider=self.custom_llm_provider,
            )
        except openai.APITimeoutError as e:
            logger.error(f"Encountered API timeout error: {e}")
        except litellm.exceptions.AuthenticationError as e:
            logger.error(f"Encountered authentication error: {e}")
            force_stop = True
        except litellm.exceptions.NotFoundError as e:
            logger.error(f"Encountered error due to unrecognized model or endpoint: {e}")
            force_stop = True
        except litellm.exceptions.BadRequestError as e:
            logger.error(f"Encountered error due to bad request: {e}")
            force_stop = True
        except litellm.exceptions.UnprocessableEntityError as e:
            logger.error(f"Encountered error due to unprocessable entity: {e}")
        except litellm.exceptions.PermissionDeniedError as e:
            logger.error(f"Encountered error - permission denied: {e}")
            force_stop = True
        except litellm.exceptions.RateLimitError as e:
            logger.error(f"Encountered rate limiting: {e}")
        except litellm.exceptions.ContextWindowExceededError as e:
            logger.error(f"Exceeded context window: {e}")
        except litellm.exceptions.ServiceUnavailableError as e:
            logger.error(f"Service unavailable: {e}")
            force_stop = True
        except litellm.exceptions.InternalServerError as e:
            logger.error(f"Internal server error: {e}")
            force_stop = True
        except litellm.exceptions.APIError as e:
            logger.error(f"API returned an invalid response: {e}")
        except litellm.exceptions.APIConnectionError as e:
            logger.error(f"API connection error: {e}")
        except Exception as e:
            logger.error(f"Encountered error: {type(e)}, Error: {e}")

        if force_stop:
            sys.exit("Exiting...")

        if response is not None:
            payload = response.choices[0].message.content
        else:
            logger.error("No response or response is empty.")
            payload = ""

        return payload

    def embeddings(self, text: str):
        text = str(text)

        # TODO: set embedding model based on model source
        # Or at least set the default for OpenAI models
        if self.model is None:
            model = "text-embedding-ada-002"
        else:
            model = self.model

        logger.info(f"Retrieving embeddings from {model} for text: {text[0:80]}...")

        response = embedding(
            api_key=self.api_key,
            api_base=self.api_base,
            api_version=self.api_version,
            model=model,
            input=[text],
            caching=True,
        )

        if response is not None:
            payload = response.data[0]["embedding"]
        else:
            logger.error("No response or response is empty.")
            payload = ""

        return payload

    def similarity(self, text1: str, text2: str, **kwargs):
        a1 = self.embeddings(text1, **kwargs)
        a2 = self.embeddings(text2, **kwargs)
        logger.debug(f"similarity: {a1[0:10]}... x {a2[0:10]}... // ({len(a1)} x {len(a2)})")
        return np.dot(a1, a2) / (np.linalg.norm(a1) * np.linalg.norm(a2))

    def euclidian_distance(self, text1: str, text2: str, **kwargs):
        a1 = self.embeddings(text1, **kwargs)
        a2 = self.embeddings(text2, **kwargs)
        return np.linalg.norm(np.array(a1) - np.array(a2))
