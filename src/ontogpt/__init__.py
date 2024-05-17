"""ontogpt package."""

from importlib import metadata
from pathlib import Path

# Define the default model
rel_path = Path(__file__).resolve()

DEFAULT_MODEL = "gpt-4-turbo"

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover
