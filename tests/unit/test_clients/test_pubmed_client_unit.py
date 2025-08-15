"""PubMed client tests."""

import unittest

from ontogpt.clients import PubmedClient


@unittest.skip("PubMed API is experiencing difficulties, i.e., 500 errors")
class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.client = PubmedClient()

    def test_lookup(self):
        """Test PMID lookup."""
        text = self.client.text("PMID:28449677")
        print(text)

    def test_search(self):
        """Test PMID search."""
        print("Testing...")
        results = list(self.client.search("Long covid", ["review", "treatment", "therapies"]))
        print(results)
