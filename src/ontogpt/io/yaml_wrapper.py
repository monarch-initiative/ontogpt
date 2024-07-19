"""YAML Wrapper."""

import io
import logging
from typing import Any, Optional, TextIO

import pydantic
from ruamel.yaml import YAML, RoundTripRepresenter

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


def repr_str(dumper: RoundTripRepresenter, data: str):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def dump_minimal_yaml(obj: Any, minimize=True, file: Optional[TextIO] = None) -> str:
    """Dump a YAML string, but eliminate Nones and empty lists and dicts."""
    yaml = YAML()
    yaml.representer.add_representer(str, repr_str)
    yaml.default_flow_style = False
    yaml.indent(sequence=4, offset=2)
    if not file:
        file = io.StringIO()
        yaml.dump(eliminate_empty(obj, not minimize), file)
        return file.getvalue()
    else:
        yaml.dump(eliminate_empty(obj, not minimize), file)
        return ""
