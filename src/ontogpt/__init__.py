"""ontogpt package."""

from importlib import metadata
from pathlib import Path

from litellm import get_model_cost_map

rel_path = Path(__file__).resolve()

# Define the default model
DEFAULT_MODEL = "gpt-4o"

# Define the default temperature
# This assumes the OpenAI default, which is between 0 and 2
DEFAULT_TEMPERATURE = 1.0

# Define the default embedding model
DEFAULT_EMBEDDING_MODEL = "text-embedding-ada-002"

# These input formats are used in the CLI
VALID_INPUT_FORMATS = [".csv", ".tsv", ".txt", ".od", ".odf", ".ods", ".pdf", ".xls", ".xlsx"]
VALID_TABULAR_FORMATS = [".csv", ".tsv"]
VALID_SPREADSHEET_FORMATS = [".od", ".odf", ".ods", ".xls", ".xlsb", ".xlsm", ".xlsx"]

# Build list of available models
# This is provided by the litellm package
MODELS = get_model_cost_map("")

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover
