"""Markdown exporter."""

from dataclasses import dataclass
from io import BytesIO, StringIO, TextIOWrapper
from pathlib import Path
from typing import Optional, TextIO, Union

import pydantic
import yaml
from linkml_runtime import SchemaView

from ontogpt.io.exporter import Exporter, is_curie
from ontogpt.templates.core import ExtractionResult


@dataclass
class MarkdownExporter(Exporter):
    def export(
        self,
        extraction_output: ExtractionResult,
        output: Union[str, Path, TextIO, BytesIO],
        schemaview: Optional[SchemaView] = None,
    ):  # type: ignore
        if isinstance(output, Path):
            output = open(str(output), "w", encoding="utf-8")
        if isinstance(output, str):
            output = StringIO(output)
        if isinstance(output, BytesIO):
            output = TextIOWrapper(output, encoding="utf-8")
        output.write(f"# {extraction_output.input_id}\n\n")
        output.write("## Input\n\n")
        for block in extraction_output.input_text.split("\n"):
            output.write(f"_{block.replace('_', '')}_\n\n")
        output.write("## Results\n\n")
        obj = extraction_output.extracted_object
        self.export_object(obj, extraction_output, output, -1)
        output.write("\n\nYAML:\n\n")
        self.details(yaml.dump(extraction_output.dict()), output, code="yaml")
        output.write("\n\nPrompt:\n\n")
        self.details(extraction_output.prompt, output)
        output.write("\n\nCompletion:\n\n")
        self.details(extraction_output.raw_completion_output, output)

    def export_object(
        self,
        obj: pydantic.BaseModel,
        extraction_output: ExtractionResult,
        output: TextIO,
        indent: int,
    ):
        for field in obj.model_fields.values():
            if indent < 0:
                output.write(f"\n\n### {field.name}\n\n")
            else:
                output.write(f"\n{'  ' * indent}- {field.name}:")
            value = getattr(obj, field.name)
            if isinstance(value, pydantic.BaseModel):
                self.export_object(value, extraction_output, output, indent + 1)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, pydantic.BaseModel):
                        self.export_object(
                            item,
                            extraction_output=extraction_output,
                            output=output,
                            indent=indent + 1,
                        )
                    else:
                        self.export_atom(item, extraction_output, output, indent + 1)
            else:
                self.export_atom(value, extraction_output, output, indent + 1)
        output.write("\n")

    def export_atom(self, value, extraction_output: ExtractionResult, output: TextIO, indent: int):
        matches = [
            ne for ne in extraction_output.named_entities if ne.id == value and is_curie(ne.id)
        ]
        output.write(f"\n{'  ' * indent}- ")
        if matches:
            match = matches[0]
            output.write(f"{match.label} {self.link(match.id)}")
        else:
            output.write(f"{value}")
        output.write("\n")

    def details(self, text: str, output: TextIO, code: str = ""):
        output.write("<details>\n")
        output.write(f"```{code}\n")
        output.write(text)
        output.write("\n```\n")
        output.write("\n</details>\n")

    def link(self, curie: str) -> str:
        return f"[{curie}](https://bioregistry.io/{curie})"
