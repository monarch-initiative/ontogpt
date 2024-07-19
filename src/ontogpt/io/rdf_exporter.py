"""RDF convertor."""

import logging
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import TextIO, Union

from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import rdflib_dumper

from ontogpt.io.exporter import Exporter
from ontogpt.templates.core import ExtractionResult

# TODO: get URI prefixes from bioregistry


@dataclass
class RDFExporter(Exporter):
    def export(
        self,
        extraction_output: ExtractionResult,
        output: Union[str, Path, TextIO, BytesIO],
        schemaview: SchemaView,
        id_value=None,
    ):
        if isinstance(output, Path):
            output = str(output)
        if isinstance(output, str):
            output = open(str(output), "w", encoding="utf-8")
        element = extraction_output.extracted_object
        cls_name = type(element).__name__
        element_dict_obj = element.dict()
        dc_mod = self._dataclass_model(schemaview)
        dc_cls = dc_mod.__dict__[cls_name]
        dc_obj = dc_cls(**element_dict_obj)
        pm = {"_base": "http://example.org/NOPREFIX/"}
        if "AUTO" not in schemaview.schema.prefixes:
            pm["AUTO"] = "http://example.org/AUTO/"
        try:
            dmp = rdflib_dumper.dumps(dc_obj, schemaview=schemaview, prefix_map=pm)
            output.write(dmp)
        except Exception as e:
            # Don't really like catching base Exception here,
            # but that's what rdflib raises.
            # Otherwise, catch ValueError
            logging.error(e)

    def _dataclass_model(self, schemaview: SchemaView):
        schemaview.merge_imports()
        return PythonGenerator(schemaview.schema).compile_module()
