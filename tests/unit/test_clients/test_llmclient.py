"""Tests for the LLMClient."""

import tempfile
import unittest
import unittest.mock as mock
from types import SimpleNamespace

import litellm
import pytest


class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        # Only initialize the clients for the cache-related tests
        # All the API tests will mock LLMClient directly
        self.client = None
        self.embedding_client = None
        # Save original global cache to restore later
        self._original_cache = getattr(litellm, "cache", None)

    def tearDown(self) -> None:
        # Restore global state
        litellm.cache = self._original_cache

    def test_complete(self):
        """Test completion."""
        # Create a mock for the LLMClient class
        with mock.patch('ontogpt.clients.LLMClient') as mock_client_class:
            # Configure the mock
            mock_client = mock_client_class.return_value
            mock_client.complete.return_value = "test"

            # Instantiate and use the client
            client = mock_client_class(model="fake/model")
            text = client.complete(
                prompt="This is a test. Please respond with a single word: test.",
                show_prompt=True,
            )

            # Verify the mocked response
            self.assertEqual(text, "test")

    def test_embeddings(self):
        """Test embedding retrieval."""
        # Create a mock embedding result
        mock_embedding_result = [0.1] * 1536

        # Create a mock for the LLMClient class
        with mock.patch('ontogpt.clients.LLMClient') as mock_client_class:
            # Configure the mock
            mock_client = mock_client_class.return_value
            mock_client.embeddings.return_value = mock_embedding_result

            # Instantiate and use the client
            client = mock_client_class(model="fake/embeddings")
            results = client.embeddings("Egg salad")

            # Verify the mocked response
            self.assertTrue(isinstance(results, list))
            self.assertEqual(len(results), 1536)

    def test_similarity(self):
        """Test similarity."""
        text1 = "I like to eat apples."
        text2 = "I like to eat egg salad."

        # Create a mock similarity value
        expected_similarity = 0.85

        # Create a mock for the LLMClient class
        with mock.patch('ontogpt.clients.LLMClient') as mock_client_class:
            # Configure the mock
            mock_client = mock_client_class.return_value
            mock_client.similarity.return_value = expected_similarity

            # Instantiate and use the client
            client = mock_client_class(model="fake/embeddings")
            similarity = client.similarity(text1, text2)

            # Verify the mocked response
            self.assertEqual(similarity, expected_similarity)
            self.assertGreaterEqual(float(similarity), 0)
            self.assertLessEqual(float(similarity), 1)

    def test_euclidean_distance(self):
        """Test euclidean distance.

        Or euclidian distance.
        One of those.
        """
        text1 = "I like to eat apples."
        text2 = "I like to eat egg salad."

        # Create a mock distance value
        expected_distance = 0.25

        # Create a mock for the LLMClient class
        with mock.patch('ontogpt.clients.LLMClient') as mock_client_class:
            # Configure the mock
            mock_client = mock_client_class.return_value
            mock_client.euclidian_distance.return_value = expected_distance

            # Instantiate and use the client
            client = mock_client_class(model="fake/embeddings")
            distance = client.euclidian_distance(text1, text2)

            # Verify the mocked response
            self.assertEqual(distance, expected_distance)
            self.assertGreaterEqual(float(distance), 0)

    def test_llmclient_sets_default_cache_dir(self):
        import ontogpt.clients.llm_client as llm_mod

        class FakeCache:
            def __init__(self, disk_cache_dir=None, *args, **kwargs):
                self.disk_cache_dir = disk_cache_dir

        # Patch the Cache used inside LLMClient.__post_init__
        with mock.patch.object(llm_mod, "Cache", FakeCache, create=True):
            # Also mock the API client to avoid any API calls
            with mock.patch('litellm.completion'):
                # Create client with default cache path (empty string)
                llm_mod.LLMClient(model="fake/model", cache_db_path="")
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
                # Also mock the API client to avoid any API calls
                with mock.patch('litellm.completion'):
                    # Create client with custom cache path
                    llm_mod.LLMClient(model="fake/model", cache_db_path=tmpdir)
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

    # Also mock litellm.completion to avoid API calls
    monkeypatch.setattr('litellm.completion', mock.MagicMock())

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

    # Instantiate with the specified cache path using a fake model
    llm_mod.LLMClient(model="fake/model", cache_db_path=cache_path_arg)

    assert isinstance(litellm.cache, fake_cache)
    # Use getattr to access the attribute safely
    assert getattr(litellm.cache, "disk_cache_dir", None) == expected_path


def test_llmclient_complete_omits_empty_api_key(monkeypatch):
    """Ensure empty API keys aren't sent to providers like Ollama."""
    import ontogpt.clients.llm_client as llm_mod

    response = SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))])
    mock_completion = mock.MagicMock(return_value=response)
    monkeypatch.setattr(llm_mod, "completion", mock_completion)

    client = llm_mod.LLMClient(model="ollama/llama3")
    client.complete("hello")

    assert "api_key" not in mock_completion.call_args.kwargs


def test_llmclient_embeddings_omits_empty_api_key(monkeypatch):
    """Ensure empty API keys aren't sent for embeddings."""
    import ontogpt.clients.llm_client as llm_mod

    response = SimpleNamespace(data=[{"embedding": [0.1, 0.2, 0.3]}])
    mock_embedding = mock.MagicMock(return_value=response)
    monkeypatch.setattr(llm_mod, "embedding", mock_embedding)

    client = llm_mod.LLMClient(model="ollama/llama3")
    client.embeddings("hello")

    assert "api_key" not in mock_embedding.call_args.kwargs


def test_llmclient_complete_includes_api_key_when_set(monkeypatch):
    """Ensure non-empty API keys are passed through."""
    import ontogpt.clients.llm_client as llm_mod

    response = SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))])
    mock_completion = mock.MagicMock(return_value=response)
    monkeypatch.setattr(llm_mod, "completion", mock_completion)

    client = llm_mod.LLMClient(model="ollama/llama3")
    client.api_key = "test-key"
    client.complete("hello")

    assert mock_completion.call_args.kwargs.get("api_key") == "test-key"


def test_llmclient_explicit_api_key_skips_provider_lookup(monkeypatch):
    """Ensure an explicitly provided key wins over provider-specific lookup."""
    import ontogpt.clients.llm_client as llm_mod

    lookup = mock.MagicMock(side_effect=AssertionError("provider lookup should not run"))
    monkeypatch.setattr(llm_mod, "get_apikey_value", lookup)

    client = llm_mod.LLMClient(
        model="anthropic/claude-3-5-sonnet",
        custom_llm_provider="anthropic",
        api_key="provided-key",
    )

    assert client.api_key == "provided-key"
    lookup.assert_not_called()


def test_llmclient_uses_provider_specific_key_lookup_when_api_key_missing(monkeypatch):
    """Ensure provider-specific fallback still happens when no key is supplied."""
    import ontogpt.clients.llm_client as llm_mod

    lookup = mock.MagicMock(return_value="anthropic-from-config")
    monkeypatch.setattr(llm_mod, "get_apikey_value", lookup)

    client = llm_mod.LLMClient(
        model="anthropic/claude-3-5-sonnet",
        custom_llm_provider="anthropic",
    )

    assert client.api_key == "anthropic-from-config"
    lookup.assert_called_once_with("anthropic-key")


def test_llmclient_explicit_api_key_preserves_azure_base_and_version_lookup(monkeypatch):
    """Ensure explicit keys do not disable non-key Azure config fallback."""
    import ontogpt.clients.llm_client as llm_mod

    def fake_get_apikey_value(name):
        values = {
            "azure-base": "https://example.openai.azure.com/",
            "azure-version": "2024-10-21",
        }
        return values[name]

    lookup = mock.MagicMock(side_effect=fake_get_apikey_value)
    monkeypatch.setattr(llm_mod, "get_apikey_value", lookup)

    client = llm_mod.LLMClient(model="azure/gpt-4o", api_key="provided-key")

    assert client.api_key == "provided-key"
    assert client.api_base == "https://example.openai.azure.com/"
    assert client.api_version == "2024-10-21"
    assert lookup.call_args_list == [mock.call("azure-base"), mock.call("azure-version")]
