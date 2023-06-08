"""oak-ai package."""
from importlib import metadata

from yaml import safe_load

# Load the model list
models_path = "models.yaml"
with open(models_path, 'r') as models_file:
    MODELS = (safe_load(models_file))["models"]

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover
