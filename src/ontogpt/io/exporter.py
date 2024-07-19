"""Generic exporter class."""

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Optional, TextIO, Union

from linkml_runtime import SchemaView

from ontogpt.templates.core import ExtractionResult


def is_curie(s: str) -> bool:
    return ":" in s and " " not in s


@dataclass
class Exporter:
    def export(
        self,
        extraction_output: ExtractionResult,
        output: Union[str, Path, TextIO, BytesIO],
        schemaview: Optional[SchemaView],
    ):
        raise NotImplementedError
