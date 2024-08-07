from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        RootModel,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


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


linkml_meta = LinkMLMeta({'default_prefix': 'miro',
     'default_range': 'string',
     'description': 'A template for extracting the minimal information for '
                    'reporting an ontology, as per the MIRO guidelines. See '
                    'doi:10.1186/s13326-017-0172-7 The target for this template '
                    'should be a report or publication describing a single '
                    'ontology.',
     'id': 'http://w3id.org/ontogpt/miro',
     'imports': ['linkml:types', 'core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'miro',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'onto_usage': {'prefix_prefix': 'onto_usage',
                                 'prefix_reference': 'http://w3id.org/ontogpt/onto_usage'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}},
     'source_file': 'src/ontogpt/templates/miro.yaml',
     'title': 'MIRO Extraction Template'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"



class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    input_id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'input_id', 'domain_of': ['ExtractionResult']} })
    input_title: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'input_title', 'domain_of': ['ExtractionResult']} })
    input_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'input_text', 'domain_of': ['ExtractionResult']} })
    raw_completion_output: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'raw_completion_output', 'domain_of': ['ExtractionResult']} })
    prompt: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'prompt', 'domain_of': ['ExtractionResult']} })
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'extracted_object', 'domain_of': ['ExtractionResult']} })
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'named_entities', 'domain_of': ['ExtractionResult']} })


class NamedEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class CompoundExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    pass


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    subject: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['Triple']} })
    predicate: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['Triple']} })
    object: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'object', 'domain_of': ['Triple']} })
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""", json_schema_extra = { "linkml_meta": {'alias': 'qualifier', 'domain_of': ['Triple']} })
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""", json_schema_extra = { "linkml_meta": {'alias': 'subject_qualifier', 'domain_of': ['Triple']} })
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""", json_schema_extra = { "linkml_meta": {'alias': 'object_qualifier', 'domain_of': ['Triple']} })


class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'publication', 'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    triples: Optional[List[Triple]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'triples', 'domain_of': ['TextWithTriples']} })


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'publication', 'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    entities: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'entities', 'domain_of': ['TextWithEntity']} })


class RelationshipType(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core',
         'id_prefixes': ['RO', 'biolink']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class Publication(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    id: Optional[str] = Field(None, description="""The publication identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })
    title: Optional[str] = Field(None, description="""The title of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Publication']} })
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'abstract', 'domain_of': ['Publication']} })
    combined_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'combined_text', 'domain_of': ['Publication']} })
    full_text: Optional[str] = Field(None, description="""The full text of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'full_text', 'domain_of': ['Publication']} })


class AnnotatorResult(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    subject_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'subject_text', 'domain_of': ['AnnotatorResult']} })
    object_id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'object_id', 'domain_of': ['AnnotatorResult']} })
    object_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'object_text', 'domain_of': ['AnnotatorResult']} })


class Ontology(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/miro', 'tree_root': True})

    name: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Ontology', 'Owner', 'CitedOntology']} })
    owners: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'owners', 'domain_of': ['Ontology']} })
    license: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Ontology']} })
    url: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Ontology']} })
    repository: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'repository', 'domain_of': ['Ontology']} })
    methodological_framework: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'methodological_framework', 'domain_of': ['Ontology']} })
    need: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'need', 'domain_of': ['Ontology']} })
    competition: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'competition', 'domain_of': ['Ontology']} })
    target_audience: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'target_audience', 'domain_of': ['Ontology']} })
    scope_and_coverage: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'scope_and_coverage', 'domain_of': ['Ontology']} })
    development_community: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'development_community', 'domain_of': ['Ontology']} })
    communication: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'communication', 'domain_of': ['Ontology']} })
    knowledge_acquisition_method: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'knowledge_acquisition_method', 'domain_of': ['Ontology']} })
    source_knowledge_location: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'source_knowledge_location', 'domain_of': ['Ontology']} })
    content_selection: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'content_selection', 'domain_of': ['Ontology']} })
    knowledge_representation_language: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'knowledge_representation_language', 'domain_of': ['Ontology']} })
    development_environment: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'development_environment', 'domain_of': ['Ontology']} })
    ontology_metrics: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'ontology_metrics', 'domain_of': ['Ontology']} })
    incorporation_of_ontologies: Optional[List[str]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'incorporation_of_ontologies', 'domain_of': ['Ontology']} })
    entity_naming_convention: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'entity_naming_convention', 'domain_of': ['Ontology']} })
    identifier_generation_policy: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'identifier_generation_policy', 'domain_of': ['Ontology']} })
    entity_metadata_policy: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'entity_metadata_policy', 'domain_of': ['Ontology']} })
    upper_ontology: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'upper_ontology', 'domain_of': ['Ontology']} })
    ontology_relationships: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'ontology_relationships', 'domain_of': ['Ontology']} })
    axiom_patterns: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'axiom_patterns', 'domain_of': ['Ontology']} })
    dereferencable_iri: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'dereferencable_iri', 'domain_of': ['Ontology']} })
    sustainability_plan: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sustainability_plan', 'domain_of': ['Ontology']} })
    deprecation_strategy: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'deprecation_strategy', 'domain_of': ['Ontology']} })
    versioning_policy: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'versioning_policy', 'domain_of': ['Ontology']} })
    testing: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'testing', 'domain_of': ['Ontology']} })
    evaluation: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'evaluation', 'domain_of': ['Ontology']} })
    examples_of_use: Optional[List[UseExample]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'examples_of_use', 'domain_of': ['Ontology']} })
    institutional_endorsement: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'institutional_endorsement', 'domain_of': ['Ontology']} })
    evidence_of_use: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'evidence_of_use', 'domain_of': ['Ontology']} })
    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class Owner(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'owl': {'tag': 'owl', 'value': 'IntersectionOf'}},
         'from_schema': 'http://w3id.org/ontogpt/miro'})

    name: Optional[str] = Field(None, description="""The name of a person, group of people, organization, or consortium that manages development of the ontology.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Ontology', 'Owner', 'CitedOntology']} })
    affiliation: Optional[str] = Field(None, description="""The name of the organization with which the owner is affiliated.""", json_schema_extra = { "linkml_meta": {'alias': 'affiliation', 'domain_of': ['Owner']} })
    contact: Optional[str] = Field(None, description="""The contact details of the owner. This is typically an email address.""", json_schema_extra = { "linkml_meta": {'alias': 'contact', 'domain_of': ['Owner']} })
    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class CitedOntology(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/miro'})

    name: Optional[str] = Field(None, description="""The name of the ontology being cited.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Ontology', 'Owner', 'CitedOntology']} })
    version: Optional[str] = Field(None, description="""The version of the ontology being cited.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['CitedOntology']} })
    citation: Optional[str] = Field(None, description="""The citation for the ontology being cited.""", json_schema_extra = { "linkml_meta": {'alias': 'citation', 'domain_of': ['CitedOntology']} })
    integration: Optional[str] = Field(None, description="""A description of how the ontology being cited is integrated into the ontology being reported.""", json_schema_extra = { "linkml_meta": {'alias': 'integration', 'domain_of': ['CitedOntology']} })
    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class UseExample(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/miro'})

    example_description: Optional[str] = Field(None, description="""A description of the ontology in use in its application setting or use case.""", json_schema_extra = { "linkml_meta": {'alias': 'example_description', 'domain_of': ['UseExample']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()
Ontology.model_rebuild()
Owner.model_rebuild()
CitedOntology.model_rebuild()
UseExample.model_rebuild()

