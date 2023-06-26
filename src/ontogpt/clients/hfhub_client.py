"""HuggingFace Hub Client."""
import logging
import os

from dataclasses import dataclass
from oaklib.utilities.apikey_manager import get_apikey_value
from langchain import HuggingFaceHub

# Note: See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
# for all relevant models

@dataclass
class HFHubClient:
    """A client for the HuggingFace Hub API."""

    try:
        api_key = get_apikey_value("hfhub-key")
    except ValueError:
        logging.error("HuggingFace Hub API key not found. See README.")

    def get_model(self, modelname: str) -> HuggingFaceHub:
        """Retreive a model from the Hub, given its repository name.

        Returns a model object of type
        langchain.llms.huggingface_hub.HuggingFaceHub
        """

        model = HuggingFaceHub(repo_id=modelname,
                               model_kwargs={"temperature": 0, "max_length": 64},
                               huggingfacehub_api_token=self.api_key)

        return model

