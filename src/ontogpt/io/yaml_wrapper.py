"""YAML Wrapper."""

import io
import logging
from typing import Any, Optional, TextIO

from ruamel.yaml import YAML, RoundTripRepresenter

from ontogpt.io.utils import eliminate_empty

logger = logging.getLogger(__name__)


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
