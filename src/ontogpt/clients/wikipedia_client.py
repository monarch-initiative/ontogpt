"""Wikipedia Client."""

from dataclasses import dataclass

import requests
import wikipediaapi


@dataclass
class WikipediaClient:
    """A client for extracting text from Wikipedia articles."""

    language: str = "en"

    def text(self, title: str) -> str:
        """Get the text of an article."""
        wiki = wikipediaapi.Wikipedia("ontogpt", self.language)
        page = wiki.page(title)

        if page.exists():
            return page.text
        else:
            raise ValueError(f"Page {title} does not exist.")

    def search_wikipedia_articles(self, topic, results=10):
        base_url = f"https://{self.language}.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "format": "json",
            "srsearch": topic,
            "srprop": "size|wordcount",
            "srlimit": results,
            "srinfo": "totalhits",
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        if data and "query" in data and "search" in data["query"]:
            return data["query"]["search"]
        else:
            return []
