"""HTML Exporter."""
import html
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TextIO, Union

import pydantic
import yaml

from ontogpt.io.exporter import Exporter, is_curie
from ontogpt.templates.core import ExtractionResult


@dataclass
class HTMLExporter(Exporter):
    """
    An exporter that will generate HTML for extraction results.

    TODO: rewrite to use bootstrap
    """

    output: TextIO = None

    def export(self, extraction_output: ExtractionResult, output: Union[str, Path, TextIO]):
        if isinstance(output, Path):
            output = str(output)
        if isinstance(output, str):
            output = open(str(output), "w", encoding="utf-8")
        self.output = output
        self.export_metadata(extraction_output)
        self.export_results(extraction_output.extracted_object, extraction_output)
        self.h2("YAML Object")
        self.details(yaml.dump(extraction_output.dict()), output, code="yaml")
        self.h2("Prompt")
        self.details(extraction_output.prompt, output)
        self.h2("Completion")
        self.details(extraction_output.raw_completion_output, output)

    def export_metadata(self, extraction_output: ExtractionResult):
        output = self.output
        self.h1(f"Results: {extraction_output.input_id}\n\n")
        self.h2("Input")
        self.i(extraction_output.input_text)

    def export_results(self, obj: Any, extraction_output: ExtractionResult):
        self.h2("Results")
        self.export_object(obj, extraction_output, -1)

    def export_object(
        self, obj: pydantic.BaseModel, extraction_output: ExtractionResult, indent: int
    ):
        self.open_div()
        if indent >= 0:
            self.open_ul()
        for field in obj.__fields__.values():
            if indent < 0:
                self.h3(field.name)
            else:
                self.li(f"<i>{field.name}</i>: ")
            value = getattr(obj, field.name)
            if isinstance(value, pydantic.BaseModel):
                self.export_object(value, extraction_output, indent + 1)
            elif isinstance(value, list):
                self.open_ul()
                n = 1
                for item in value:
                    self.li(f"<b>item: {n}</b>: ")
                    n += 1
                    if isinstance(item, pydantic.BaseModel):
                        self.export_object(
                            item, extraction_output=extraction_output, indent=indent + 1
                        )
                    else:
                        self.export_atom(item, extraction_output, indent + 1)
                self.close_ul()
            else:
                self.export_atom(value, extraction_output, indent + 1)
        if indent >= 0:
            self.open_ul()
        self.close_div()

    def export_atom(self, value, extraction_output: ExtractionResult, indent: int):
        output = self.output
        matches = [
            ne for ne in extraction_output.named_entities if ne.id == value and is_curie(ne.id)
        ]
        if matches:
            match = matches[0]
            output.write(f"{match.label} {self.link(match.id)}")
        else:
            output.write(str(value))
        output.write("\n")

    def details(self, text: str, output: TextIO, code: str = ""):
        output.write("<details>\n")
        output.write("<pre>\n")
        self.w(text)
        output.write("\n</pre>\n")
        output.write("\n</details>\n")

    def link(self, curie: str) -> str:
        return f'<a href="https://bioregistry.io/{curie}">{curie}</a>'

    def open_ul(self):
        self.output.write("<ul>\n")

    def close_ul(self):
        self.output.write("</ul>\n")

    def open_div(self):
        self.output.write("<div>\n")

    def close_div(self):
        self.output.write("</div>\n")

    def li(self, text: str = None):
        self.tag("li", text)

    def h1(self, text: str):
        self.tag("h1", text)

    def h2(self, text: str):
        self.tag("h1", text)

    def h3(self, text: str):
        self.tag("h3", text)

    def i(self, text: str):
        self.tag("i", html.escape(text))

    def tag(self, tag: str, text: str):
        self.output.write(f"<{tag}>{text}</{tag}>\n")

    def w(self, text: str):
        self.output.write(html.escape(text))
