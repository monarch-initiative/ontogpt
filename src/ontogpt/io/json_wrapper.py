"""JSON Wrapper."""

import io
import logging
import json
from typing import Any, Optional, TextIO

from ontogpt.io.utils import eliminate_empty


logger = logging.getLogger(__name__)


def dump_minimal_json(obj: Any, minimize=True, file: Optional[TextIO] = None) -> str:
    """Dump a JSON string, but eliminate Nones and empty lists and dicts."""
    if not file:
        file = io.StringIO()
        json.dump(eliminate_empty(obj, not minimize), file, indent=2)
        return file.getvalue()
    else:
        json.dump(eliminate_empty(obj, not minimize), file, indent=2)
        return ""
