from typing import Any

import pydantic
import yaml


def eliminate_empty(obj: Any, preserve=False) -> Any:
    """
    Eliminate empty lists and dicts from an object
    """
    if isinstance(obj, list):
        return [eliminate_empty(x, preserve) for x in obj if x or preserve]
    elif isinstance(obj, dict):
        return {k: eliminate_empty(v, preserve) for k, v in obj.items() if v or preserve}
    elif isinstance(obj, pydantic.BaseModel):
        return eliminate_empty(obj.dict(), preserve)
    else:
        return obj


def dump_minimal_yaml(obj: Any, minimize=True) -> str:
    """
    Dump a YAML string, but eliminating Nones and empty lists and dicts
    """
    return yaml.dump(eliminate_empty(obj, not minimize), sort_keys=False)
