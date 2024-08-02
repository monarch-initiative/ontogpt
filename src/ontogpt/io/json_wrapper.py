"""JSON Wrapper."""

import io
import logging
import json
from typing import Any, Optional, TextIO

import pydantic

logger = logging.getLogger(__name__)


def eliminate_empty(obj: Any, preserve=False) -> Any:
    """Eliminate empty lists and dicts from an object."""
    if isinstance(obj, list):
        return [eliminate_empty(x, preserve) for x in obj if x or preserve]
    elif isinstance(obj, dict):
        return {k: eliminate_empty(v, preserve) for k, v in obj.items() if v or preserve}
    elif isinstance(obj, pydantic.BaseModel):
        return eliminate_empty(obj.model_dump(), preserve)
    elif isinstance(obj, tuple):
        return [eliminate_empty(x, preserve) for x in obj]
    elif isinstance(obj, str):
        return str(obj)
    else:
        return obj


def dump_minimal_json(obj: Any, minimize=True, file: Optional[TextIO] = None) -> str:
    """Dump a JSON string, but eliminate Nones and empty lists and dicts."""
    if not file:
        file = io.StringIO()
        json.dump(eliminate_empty(obj, not minimize), file, indent=2)
        return file.getvalue()
    else:
        json.dump(eliminate_empty(obj, not minimize), file, indent=2)
        return ""
