from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://example.org/PaperExtractionSchema/',
     'description': 'A simplified schema describing the fields to extract from a '
                    'paper that includes study metadata and a minimal notion of '
                    'experiments.\n',
     'id': 'https://example.org/PaperExtractionSchema',
     'imports': ['linkml:types'],
     'name': 'PaperExtractionSchema',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/ontogpt/templates/biolog_simple.yaml',
     'title': 'Paper Extraction Schema',
     'types': {'boolean': {'base': 'bool',
                           'from_schema': 'https://example.org/PaperExtractionSchema',
                           'name': 'boolean'},
               'string': {'base': 'str',
                          'from_schema': 'https://example.org/PaperExtractionSchema',
                          'name': 'string'}}} )


class Paper(ConfiguredBaseModel):
    """
    Top-level class representing a single paper/study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema', 'tree_root': True})

    study_title: str = Field(default=..., description="""Title of the study.""", json_schema_extra = { "linkml_meta": {'alias': 'study_title', 'domain_of': ['Paper']} })
    authors: List[Author] = Field(default=..., description="""List of authors of the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'authors', 'domain_of': ['Paper']} })
    doi: Optional[str] = Field(default=None, description="""DOI of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'doi', 'domain_of': ['Paper']} })
    date: Optional[str] = Field(default=None, description="""Date of the publication or the study.""", json_schema_extra = { "linkml_meta": {'alias': 'date', 'domain_of': ['Paper']} })
    experiments: Optional[List[Experiment]] = Field(default=None, description="""List of experiments mentioned in the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'experiments', 'domain_of': ['Paper']} })


class Author(ConfiguredBaseModel):
    """
    Represents an author of the paper.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: str = Field(default=..., description="""Name of the author.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Author']} })


class Experiment(ConfiguredBaseModel):
    """
    A minimal experiment class (could be Biolog or otherwise).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    experiment_title: Optional[str] = Field(default=None, description="""Title or short description of the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_title', 'domain_of': ['Experiment']} })
    is_biolog_experiment: Optional[bool] = Field(default=None, description="""Flag indicating if this experiment is a Biolog experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'is_biolog_experiment', 'domain_of': ['Experiment']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Paper.model_rebuild()
Author.model_rebuild()
Experiment.model_rebuild()

