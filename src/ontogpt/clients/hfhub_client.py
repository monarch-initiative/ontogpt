"""HuggingFace Hub Client."""
import logging
from dataclasses import dataclass
from typing import List, Union
from urllib import parse

import requests
from oaklib.utilities.apikey_manager import get_apikey_value


@dataclass
class HFHubClient:
    """A client for the HuggingFace Hub API."""

    try:
        ncbi_key = get_apikey_value("hfhub-key")
    except ValueError:
        ncbi_key = None
        logging.error("HuggingFace Hub API key not found. See README.")
