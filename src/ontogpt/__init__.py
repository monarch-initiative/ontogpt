"""ontogpt package."""

from importlib import metadata
from pathlib import Path

from litellm import get_model_cost_map

# Define the default model
rel_path = Path(__file__).resolve()

DEFAULT_MODEL = "gpt-4o"

# Build list of available models
MODELS = get_model_cost_map("")

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover
