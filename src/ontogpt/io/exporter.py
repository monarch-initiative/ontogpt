"""Exporter."""
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO, Union

from ontogpt.templates.core import ExtractionResult


def is_curie(s: str) -> bool:
    return ":" in s and " " not in s


@dataclass
class Exporter:
    def export(self, extraction_output: ExtractionResult, output: Union[str, Path, TextIO]):
        raise NotImplementedError
