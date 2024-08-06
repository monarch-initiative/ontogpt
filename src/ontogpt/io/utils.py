"""IO Utilities."""

from typing import Any

import pydantic


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
