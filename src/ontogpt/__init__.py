"""ontogpt package."""

from importlib import metadata
from pathlib import Path

rel_path = Path(__file__).resolve()

# Define the default model.
# Override with the -m/--model option; see `ontogpt list-models`.
DEFAULT_MODEL = "gpt-5.5"

# Define the default temperature
# This assumes the OpenAI default, which is between 0 and 2.
# Reasoning models accept only the default value; other values are dropped.
DEFAULT_TEMPERATURE = 1.0

# Define the default embedding model
DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"

# These input formats are used in the CLI
VALID_INPUT_FORMATS = [".csv", ".tsv", ".txt", ".od", ".odf", ".ods", ".pdf", ".xls", ".xlsx"]
VALID_TABULAR_FORMATS = [".csv", ".tsv"]
VALID_SPREADSHEET_FORMATS = [".od", ".odf", ".ods", ".xls", ".xlsb", ".xlsm", ".xlsx"]

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover
