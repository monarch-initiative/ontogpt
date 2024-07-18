"""Tests for the LLMClient."""

import unittest
import numpy as np

from ontogpt.clients import LLMClient

"""This uses whatever the default model is specified as,
generally an OpenAI API model."""


class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.client = LLMClient()
        self.embedding_client = LLMClient(model="text-embedding-ada-002")

    def test_complete(self):
        """Test completion."""
        text = self.client.complete(
            prompt="This is a test. Please respond with a single word: test.",
            show_prompt=True,
        )
        self.assertEqual("test", text.lower().replace(".", ""))

    def test_embeddings(self):
        """Test embedding retrieval."""
        results = self.embedding_client.embeddings("Egg salad")
        self.assertTrue(type(results) == list)
        self.assertEqual(len(results), 1536)

    def test_similarity(self):
        """Test similarity."""
        text1 = "I like to eat apples."
        text2 = "I like to eat egg salad."
        similarity = self.embedding_client.similarity(text1, text2)
        self.assertTrue(type(similarity) == np.float64)
        self.assertGreater(float(similarity), 0.8)

    def test_euclidean_distance(self):
        """Test euclidean distance.

        Or euclidian distance.
        One of those.
        """
        text1 = "I like to eat apples."
        text2 = "I like to eat egg salad."
        distance = self.embedding_client.euclidian_distance(text1, text2)
        self.assertTrue(type(distance) == np.float64)
        self.assertGreater(float(distance), 0.4)
