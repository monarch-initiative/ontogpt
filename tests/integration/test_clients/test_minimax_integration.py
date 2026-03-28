"""Integration tests for MiniMax provider support.

These tests require a valid MINIMAX_API_KEY environment variable.
They are skipped if the key is not set.
"""

import os
import unittest

import pytest

from ontogpt.clients.llm_client import LLMClient

MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "")


@pytest.mark.skipif(not MINIMAX_API_KEY, reason="MINIMAX_API_KEY not set")
class TestMiniMaxIntegration(unittest.TestCase):
    """Integration tests for MiniMax LLM provider."""

    def test_minimax_completion_with_prefix(self):
        """Test basic completion using minimax/ model prefix."""
        client = LLMClient(model="minimax/MiniMax-M2.7", temperature=0.7)
        result = client.complete("Respond with exactly one word: hello")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result.strip()), 0)

    def test_minimax_completion_with_provider(self):
        """Test basic completion using --model-provider minimax."""
        client = LLMClient(
            model="MiniMax-M2.7",
            custom_llm_provider="minimax",
            temperature=0.5,
        )
        result = client.complete("What is 2 + 2? Answer with just the number.")
        self.assertIsInstance(result, str)
        self.assertIn("4", result)

    def test_minimax_highspeed_model(self):
        """Test completion with the highspeed variant."""
        client = LLMClient(model="minimax/MiniMax-M2.7-highspeed", temperature=0.7)
        result = client.complete("Say the word 'test'.")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result.strip()), 0)
