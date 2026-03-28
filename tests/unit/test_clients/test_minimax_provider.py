"""Tests for MiniMax provider support in LLMClient."""

import os
import unittest
import unittest.mock as mock
from types import SimpleNamespace

import litellm
import pytest

import ontogpt.clients.llm_client as llm_mod
from ontogpt.clients.llm_client import MINIMAX_API_BASE


class FakeCache:
    def __init__(self, disk_cache_dir=None, *args, **kwargs):
        self.disk_cache_dir = disk_cache_dir


@pytest.fixture(autouse=True)
def _restore_litellm_cache():
    original_cache = getattr(litellm, "cache", None)
    yield
    litellm.cache = original_cache


@pytest.fixture
def mock_apikey():
    """Mock get_apikey_value to avoid file system reads."""
    with mock.patch.object(llm_mod, "get_apikey_value", return_value="test-key") as m:
        yield m


@pytest.fixture
def patch_cache():
    """Patch Cache to avoid disk I/O."""
    with mock.patch.object(llm_mod, "Cache", FakeCache):
        yield


class TestMiniMaxProviderInit:
    """Test MiniMax provider detection and configuration in LLMClient."""

    def test_minimax_prefix_sets_api_base(self, mock_apikey, patch_cache, monkeypatch):
        """minimax/ prefix should auto-configure api_base."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7")
        assert client.api_base == MINIMAX_API_BASE

    def test_minimax_prefix_strips_prefix(self, mock_apikey, patch_cache, monkeypatch):
        """minimax/ prefix should be stripped from model name."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7")
        assert client.model == "MiniMax-M2.7"

    def test_minimax_prefix_sets_openai_provider(self, mock_apikey, patch_cache, monkeypatch):
        """minimax/ prefix should set custom_llm_provider to openai."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7")
        assert client.custom_llm_provider == "openai"

    def test_minimax_provider_option_sets_api_base(self, mock_apikey, patch_cache, monkeypatch):
        """--model-provider minimax should auto-configure api_base."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(
            model="MiniMax-M2.7", custom_llm_provider="minimax"
        )
        assert client.api_base == MINIMAX_API_BASE

    def test_minimax_provider_option_sets_openai_provider(
        self, mock_apikey, patch_cache, monkeypatch
    ):
        """--model-provider minimax should be rewritten to openai for litellm."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(
            model="MiniMax-M2.7", custom_llm_provider="minimax"
        )
        assert client.custom_llm_provider == "openai"

    def test_minimax_api_key_from_env(self, mock_apikey, patch_cache, monkeypatch):
        """MINIMAX_API_KEY env var should be used."""
        monkeypatch.setenv("MINIMAX_API_KEY", "env-minimax-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7")
        assert client.api_key == "env-minimax-key"

    def test_minimax_api_key_fallback_to_oaklib(self, patch_cache, monkeypatch):
        """Should fall back to oaklib minimax-key if MINIMAX_API_KEY is not set."""
        monkeypatch.delenv("MINIMAX_API_KEY", raising=False)
        with mock.patch.object(
            llm_mod, "get_apikey_value", return_value="oaklib-mm-key"
        ):
            client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7")
            assert client.api_key == "oaklib-mm-key"

    def test_minimax_explicit_api_key_preserved(self, mock_apikey, patch_cache, monkeypatch):
        """Explicitly provided api_key should not be overwritten."""
        monkeypatch.setenv("MINIMAX_API_KEY", "env-key")
        client = llm_mod.LLMClient(
            model="minimax/MiniMax-M2.7", api_key="explicit-key"
        )
        assert client.api_key == "explicit-key"

    def test_minimax_custom_api_base_preserved(self, mock_apikey, patch_cache, monkeypatch):
        """Explicitly provided api_base should not be overwritten."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(
            model="minimax/MiniMax-M2.7", api_base="https://custom.api.example.com/v1"
        )
        assert client.api_base == "https://custom.api.example.com/v1"

    def test_minimax_highspeed_model(self, mock_apikey, patch_cache, monkeypatch):
        """MiniMax-M2.7-highspeed should also be recognized."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7-highspeed")
        assert client.model == "MiniMax-M2.7-highspeed"
        assert client.api_base == MINIMAX_API_BASE
        assert client.custom_llm_provider == "openai"


class TestMiniMaxTemperatureClamping:
    """Test MiniMax temperature clamping (must be in (0.0, 1.0])."""

    def test_temperature_zero_clamped(self, mock_apikey, patch_cache, monkeypatch):
        """Temperature 0.0 should be clamped to 0.01."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7", temperature=0.0)
        assert client.temperature == pytest.approx(0.01)

    def test_temperature_negative_clamped(self, mock_apikey, patch_cache, monkeypatch):
        """Negative temperature should be clamped to 0.01."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7", temperature=-0.5)
        assert client.temperature == pytest.approx(0.01)

    def test_temperature_above_one_clamped(self, mock_apikey, patch_cache, monkeypatch):
        """Temperature > 1.0 should be clamped to 1.0."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7", temperature=1.5)
        assert client.temperature == pytest.approx(1.0)

    def test_temperature_valid_preserved(self, mock_apikey, patch_cache, monkeypatch):
        """Valid temperature (0.0 < t <= 1.0) should be preserved."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7", temperature=0.7)
        assert client.temperature == pytest.approx(0.7)

    def test_temperature_one_preserved(self, mock_apikey, patch_cache, monkeypatch):
        """Temperature 1.0 is valid for MiniMax."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7", temperature=1.0)
        assert client.temperature == pytest.approx(1.0)

    def test_non_minimax_temperature_not_clamped(self, mock_apikey, patch_cache):
        """Non-MiniMax models should not have temperature clamped."""
        client = llm_mod.LLMClient(model="fake/model", temperature=1.5)
        assert client.temperature == pytest.approx(1.5)


class TestMiniMaxCompletion:
    """Test MiniMax completion calls pass correct parameters to litellm."""

    def test_complete_passes_openai_provider(self, mock_apikey, patch_cache, monkeypatch):
        """Completion call should use openai as custom_llm_provider."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="test response"))]
        )
        mock_completion = mock.MagicMock(return_value=response)
        monkeypatch.setattr(llm_mod, "completion", mock_completion)

        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7")
        result = client.complete("Hello")

        call_kwargs = mock_completion.call_args.kwargs
        assert call_kwargs["custom_llm_provider"] == "openai"
        assert call_kwargs["api_base"] == MINIMAX_API_BASE
        assert call_kwargs["model"] == "MiniMax-M2.7"
        assert call_kwargs["api_key"] == "mm-test-key"
        assert result == "test response"

    def test_complete_with_provider_option(self, mock_apikey, patch_cache, monkeypatch):
        """Completion via --model-provider minimax should also work."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))]
        )
        mock_completion = mock.MagicMock(return_value=response)
        monkeypatch.setattr(llm_mod, "completion", mock_completion)

        client = llm_mod.LLMClient(
            model="MiniMax-M2.7", custom_llm_provider="minimax"
        )
        client.complete("test prompt")

        call_kwargs = mock_completion.call_args.kwargs
        assert call_kwargs["custom_llm_provider"] == "openai"
        assert call_kwargs["api_base"] == MINIMAX_API_BASE

    def test_complete_temperature_clamped_in_request(
        self, mock_apikey, patch_cache, monkeypatch
    ):
        """Temperature in the completion request should reflect clamping."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))]
        )
        mock_completion = mock.MagicMock(return_value=response)
        monkeypatch.setattr(llm_mod, "completion", mock_completion)

        client = llm_mod.LLMClient(model="minimax/MiniMax-M2.7", temperature=0.0)
        client.complete("test")

        call_kwargs = mock_completion.call_args.kwargs
        assert call_kwargs["temperature"] == pytest.approx(0.01)

    def test_complete_with_system_message(self, mock_apikey, patch_cache, monkeypatch):
        """System message should be included in MiniMax requests."""
        monkeypatch.setenv("MINIMAX_API_KEY", "mm-test-key")
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))]
        )
        mock_completion = mock.MagicMock(return_value=response)
        monkeypatch.setattr(llm_mod, "completion", mock_completion)

        client = llm_mod.LLMClient(
            model="minimax/MiniMax-M2.7", system_message="You are a biomedical expert."
        )
        client.complete("Extract entities from this text.")

        call_kwargs = mock_completion.call_args.kwargs
        messages = call_kwargs["messages"]
        assert len(messages) == 2
        assert messages[0]["role"] == "system"
        assert messages[0]["content"] == "You are a biomedical expert."


class TestMiniMaxModelsRegistry:
    """Test that MiniMax models appear in the model registry."""

    def test_minimax_m27_in_models(self):
        """MiniMax-M2.7 should be in the MODELS dict."""
        from ontogpt import MODELS

        assert "minimax/MiniMax-M2.7" in MODELS

    def test_minimax_m27_highspeed_in_models(self):
        """MiniMax-M2.7-highspeed should be in the MODELS dict."""
        from ontogpt import MODELS

        assert "minimax/MiniMax-M2.7-highspeed" in MODELS

    def test_minimax_models_are_chat(self):
        """MiniMax models should be listed as chat mode."""
        from ontogpt import MODELS

        assert MODELS["minimax/MiniMax-M2.7"]["mode"] == "chat"
        assert MODELS["minimax/MiniMax-M2.7-highspeed"]["mode"] == "chat"

    def test_minimax_models_have_correct_context(self):
        """MiniMax models should have 204K context."""
        from ontogpt import MODELS

        assert MODELS["minimax/MiniMax-M2.7"]["max_tokens"] == 204800
        assert MODELS["minimax/MiniMax-M2.7-highspeed"]["max_tokens"] == 204800

    def test_minimax_in_services(self):
        """minimax should appear in the SERVICES set."""
        from ontogpt.clients.llm_client import SERVICES

        assert "minimax" in SERVICES
