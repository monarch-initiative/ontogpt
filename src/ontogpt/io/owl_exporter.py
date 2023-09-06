"""OWL convertor."""
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO, Union

import pydantic
from linkml.generators.pythongen import PythonGenerator
from linkml_owl.dumpers.owl_dumper import OWLDumper
from linkml_runtime import SchemaView

from ontogpt.io.exporter import Exporter
from ontogpt.templates.core import ExtractionResult


@dataclass
class OWLExporter(Exporter):
    def export(
        self,
        extraction_output: ExtractionResult,
        output: Union[str, Path, TextIO],
        schemaview: SchemaView,
        id_value=None,
    ):
        if isinstance(output, Path):
            output = str(output)
        if isinstance(output, str):
            output = open(str(output), "w", encoding="utf-8")
        dumper = OWLDumper()
        element = extraction_output.extracted_object
        cls_name = type(element).__name__
        id_slot = schemaview.get_identifier_slot(cls_name)
        if id_slot is not None:
            id_slot_name = id_slot.name
            if id_value is not None:
                setattr(element, id_slot_name, "AUTO:_ROOT")
            else:
                id_value = getattr(element, id_slot_name, None)
                print(f"Setting {id_slot_name} [{id_value}] to AUTO:_ROOT for {cls_name}")
                if id_value is None:
                    setattr(element, id_slot_name, "AUTO:_ROOT")
        axioms = []
        for named_entity in extraction_output.named_entities:
            ne_as_dc = self._as_dataclass_object(named_entity, schemaview)
            doc = dumper.to_ontology_document(ne_as_dc, schemaview.schema)
            axioms.extend(doc.ontology.axioms)
        element_as_dataclass = self._as_dataclass_object(element, schemaview)
        doc = dumper.to_ontology_document(element_as_dataclass, schemaview.schema)
        doc.ontology.axioms.extend(axioms)
        output.write(str(doc))

    def _as_dataclass_object(self, element: pydantic.BaseModel, schemaview: SchemaView):
        cls_name = type(element).__name__
        schemaview.merge_imports()
        element_dict = element.dict()
        dataclasses_module = PythonGenerator(schemaview.schema).compile_module()
        target_class_py = dataclasses_module.__dict__[cls_name]
        element_as_dataclass = target_class_py(**element_dict)
        return element_as_dataclass
