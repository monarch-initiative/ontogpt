"""PubMed client tests."""
import unittest

from ontogpt.clients import PubmedClient


class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.client = PubmedClient()

    def test_lookup(self):
        """Test PMID lookup."""
        text = self.client.text("PMID:28449677")
        print(text)

    def test_multiple_lookup(self):
        """Test lookup of multiple PMIDs."""
        text = self.client.text(["25662031", "28449677"])
        print(text)

    def test_malformed_lookup(self):
        """Text lookup of invalid PMID."""
        text = self.client.text("jelly")
        self.assertFalse(text)

    def test_search(self):
        """Test PMID search."""
        print("Testing...")
        results = list(self.client.search("Long covid", ["review", "treatment", "therapies"]))
        print(results)
