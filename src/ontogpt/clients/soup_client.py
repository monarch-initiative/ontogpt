"""BeautifulSoup client."""

from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class SoupClient:
    """A client for the Beautiful Soup API."""

    def text(self, url: str) -> str:
        """Get the text of a web site from its HTML.

        :param url: string containing the URL to extract text from
        :return:
        """
        result = requests.get(url)
        if result.status_code != 200:
            raise Exception(f"Error fetching {url}: {result.status_code}")
        soup = BeautifulSoup(result.text)
        return soup.text
