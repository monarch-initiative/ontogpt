"""Settings specific for using OpenAI models on the Azure platform."""

import logging
import os
from pathlib import Path
from typing import Any, Dict

import dpath
import toml

BASE_DIR = Path(__file__).parent.parent.absolute()

logger = logging.getLogger(__name__)

def read_toml(path: Path) -> Dict[str, Any]:
    with path.open() as cf:
        return toml.load(cf)


def merge_settings(overrides: Dict[str, Any], defaults: Dict[str, Any]) -> None:
    """Merge settings recursively to allow partial overrides without overwriting entire sections."""
    for key, value in overrides.items():
        if isinstance(value, dict):
            node = defaults.setdefault(key, {})
            merge_settings(value, node)
        else:
            defaults[key] = value


def parse_settings(
    base_dir: Path,
) -> Dict[str, Any]:
    """Parse configuration toml files from a directory with overrides.

    Args:
    base_dir: Base directory
    Returns: Dictionary of parsed configuration values.
    """
    try:
        settings_path = Path(os.getenv("SETTINGS_PATH", None))
        settings_name = os.getenv("SETTINGS_NAME", "local")
    except TypeError as e:
        logger.warning(f"Missing required settings for Azure OpenAI: {e}")
        settings_path = None
        settings_name = "local"

    etc_dir = base_dir / "etc"
    default_settings = etc_dir / f"{settings_name}.toml"
    settings_override = etc_dir / f"{settings_name}_custom.toml"

    if settings_path:
        settings = read_toml(settings_path)
    else:
        settings_path = default_settings

    settings = read_toml(settings_path) if settings_path.is_file() else {}

    return settings

settings_val = parse_settings(BASE_DIR)
try:
    AZURE_MODEL = dpath.get(settings_val, ["openai", "azure_deployment_name"])
    AZURE_API_VERSION = dpath.get(settings_val, ["openai", "azure_api_version"])
    AZURE_ENDPOINT = dpath.get(settings_val, ["openai", "azure_api_base"])
except KeyError as e:
    AZURE_MODEL = ""
    AZURE_API_VERSION = ""
    AZURE_ENDPOINT = ""
    logger.warning(f"Missing required settings for Azure OpenAI: {e}")