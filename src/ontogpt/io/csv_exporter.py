"""CSV exporter class."""

from dataclasses import dataclass
from io import BytesIO, StringIO, TextIOWrapper
from pathlib import Path
from typing import Optional, TextIO, Union

import pandas as pd

from linkml_runtime import SchemaView

from ontogpt.io.exporter import Exporter
from ontogpt.templates.core import ExtractionResult


@dataclass
class CSVExporter(Exporter):

    sep: str = ","

    def export(
        self,
        extraction_output: ExtractionResult,
        output: Union[str, Path, TextIO, BytesIO],
        schemaview: Optional[SchemaView],
    ):
        if isinstance(output, Path):
            output = open(str(output), "w", encoding="utf-8")
        if isinstance(output, str):
            output = StringIO(output)
        if isinstance(output, BytesIO):
            output = TextIOWrapper(output, encoding="utf-8")
        out_dict = extraction_output.extracted_object.model_dump()
        df = pd.DataFrame.from_dict(out_dict, orient="index")
        df.columns = ["values"]
        df = df.explode("values")
        df.to_csv(path_or_buf=output, sep=self.sep, header=True)
