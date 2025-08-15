"""Tests for the LLMClient."""

import unittest
import numpy as np
import unittest.mock as mock
import tempfile
import pytest

import litellm
from ontogpt.clients import LLMClient


class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.client = LLMClient()
        self.embedding_client = LLMClient(model="text-embedding-ada-002")
        # Save original global cache to restore later
        self._original_cache = getattr(litellm, "cache", None)

    def tearDown(self) -> None:
        # Restore global state
        litellm.cache = self._original_cache

    @unittest.skip("Need to set API key first")
    def test_complete(self):
        """Test completion."""
        text = self.client.complete(
            prompt="This is a test. Please respond with a single word: test.",
            show_prompt=True,
        )
        self.assertEqual("test", text.lower().replace(".", ""))

    @unittest.skip("Need to set API key first")
    def test_embeddings(self):
        """Test embedding retrieval."""
        results = self.embedding_client.embeddings("Egg salad")
        self.assertTrue(type(results) == list)
        self.assertEqual(len(results), 1536)

    @unittest.skip("Need to set API key first")
    def test_similarity(self):
        """Test similarity."""
        text1 = "I like to eat apples."
        text2 = "I like to eat egg salad."
        similarity = self.embedding_client.similarity(text1, text2)
        self.assertTrue(type(similarity) == np.float64)
        self.assertGreater(float(similarity), 0.8)

    @unittest.skip("Need to set API key first")
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

    def test_llmclient_sets_default_cache_dir(self):
        import ontogpt.clients.llm_client as llm_mod

        class FakeCache:
            def __init__(self, disk_cache_dir=None, *args, **kwargs):
                self.disk_cache_dir = disk_cache_dir

        # Patch the Cache used inside LLMClient.__post_init__
        with mock.patch.object(llm_mod, "Cache", FakeCache, create=True):
            llm_mod.LLMClient(model="ollama/llama3", cache_db_path="")
            self.assertIsInstance(litellm.cache, FakeCache)
            # Use getattr to access the attribute safely
            self.assertEqual(getattr(litellm.cache, "disk_cache_dir", None), "./.litellm_cache")

    def test_llmclient_sets_custom_cache_dir(self):
        import ontogpt.clients.llm_client as llm_mod

        class FakeCache:
            def __init__(self, disk_cache_dir=None, *args, **kwargs):
                self.disk_cache_dir = disk_cache_dir

        with tempfile.TemporaryDirectory() as tmpdir:
            # Patch the Cache used inside LLMClient.__post_init__
            with mock.patch.object(llm_mod, "Cache", FakeCache, create=True):
                llm_mod.LLMClient(model="ollama/llama3", cache_db_path=tmpdir)
                self.assertIsInstance(litellm.cache, FakeCache)
                # Use getattr to access the attribute safely
                self.assertEqual(getattr(litellm.cache, "disk_cache_dir", None), tmpdir)


@pytest.fixture
def fake_cache():
    class FakeCache:
        def __init__(self, disk_cache_dir=None, *args, **kwargs):
            self.disk_cache_dir = disk_cache_dir
    return FakeCache


@pytest.fixture
def original_litellm_cache():
    original_cache = getattr(litellm, "cache", None)
    yield original_cache
    litellm.cache = original_cache


@pytest.mark.parametrize("cache_path", [
    "",  # Default path
    "custom/path/to/cache"  # Custom path
])
def test_llmclient_cache_paths_pytest_style(monkeypatch, tmp_path, fake_cache,
                                            original_litellm_cache, cache_path):
    """Test that LLMClient sets cache paths correctly using pytest fixtures."""
    import ontogpt.clients.llm_client as llm_mod

    monkeypatch.setattr(llm_mod, "Cache", fake_cache, raising=True)

    if cache_path:
        # If a specific path is provided
        custom_dir = tmp_path / cache_path
        custom_dir.mkdir(parents=True, exist_ok=True)
        cache_path_arg = str(custom_dir)
        expected_path = str(custom_dir)
    else:
        # Default path case
        cache_path_arg = ""
        expected_path = "./.litellm_cache"

    # Instantiate with the specified cache path
    llm_mod.LLMClient(model="ollama/llama3", cache_db_path=cache_path_arg)

    assert isinstance(litellm.cache, fake_cache)
    # Use getattr to access the attribute safely
    assert getattr(litellm.cache, "disk_cache_dir", None) == expected_path
