import os
from pathlib import Path
from typing import Any, Dict

import dpath
import toml

BASE_DIR = Path(__file__).parent.parent.absolute()


def read_toml(path: Path) -> Dict[str, Any]:
    with path.open() as cf:
        return toml.load(cf)


def merge_settings(overrides: Dict[str, Any], defaults: Dict[str, Any]) -> None:
    """Merges settings recursively to allow partial
    overrides without overwriting entire sections."""
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
    Returns: Dictionary of parsed configuration values
    """

    settings_path = os.getenv("SETTINGS_PATH", None)
    settings_name = os.getenv("SETTINGS_NAME", "local")

    etc_dir = base_dir / "etc"
    default_settings = etc_dir / f"{settings_name}.toml"
    settings_override = etc_dir / f"{settings_name}_custom.toml"

    if settings_path:
        settings_path = Path(settings_path)

    if settings_path.is_file():
        settings = read_toml(settings_path)
    else:
        settings_path = default_settings

    settings = read_toml(settings_path) if settings_path.is_file() else {}

    return settings

settings_val = parse_settings(BASE_DIR)

AZURE_MODEL = dpath.get(settings_val, ["openai", "azure_deployment_name"])
AZURE_API_VERSION = dpath.get(settings_val, ["openai", "azure_api_version"])
AZURE_ENDPOINT = dpath.get(settings_val, ["openai", "azure_api_base"])
