"""ontogpt package."""
from importlib import metadata
from pathlib import Path

from yaml import safe_load

# Load the model list and define the default model
rel_path = Path(__file__).resolve()
models_path = rel_path.parent / "models.yaml"

with open(models_path, 'r') as models_file:
    MODELS = (safe_load(models_file))["models"]
for model in MODELS:
    if "is_default" in model:
        DEFAULT_MODEL = model["alternative_names"][0]
        break

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover
