"""Soup client."""
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

PMID = str


@dataclass
class SoupClient:
    """A client for the Beautiful Soup API."""

    def text(self, url: str) -> str:
        """Get the text of a paper from its PMID.

        :param id:
        :param autoformat: if True include title and abstract concatenated
        :return:
        """
        result = requests.get(url)
        if result.status_code != 200:
            raise Exception(f"Error fetching {url}: {result.status_code}")
        soup = BeautifulSoup(result.text)
        return soup.text
