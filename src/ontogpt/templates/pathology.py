from __future__ import annotations 
from datetime import (
    datetime,
    date,
    time
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
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
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


linkml_meta = LinkMLMeta({'default_prefix': 'pathology',
     'default_range': 'string',
     'description': 'A template for extracting and grounding pathology '
                    'descriptions from text.',
     'id': 'http://w3id.org/ontogpt/pathology',
     'imports': ['linkml:types', 'core'],
     'keywords': ['pathology', 'phenotype'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'pathology',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'pathology': {'prefix_prefix': 'pathology',
                                'prefix_reference': 'http://w3id.org/ontogpt/pathology'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}},
     'source_file': 'src/ontogpt/templates/pathology.yaml',
     'title': 'Pathology Grounding Template'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class SeverityLevel(str, Enum):
    """
    The severity of a pathology.
    """
    # A pathology that is mild in severity.
    mild = "mild"
    # A pathology that is moderate in severity.
    moderate = "moderate"
    # A pathology that is severe in severity.
    severe = "severe"
    # The severity of the pathology is not specified.
    Not_Specified = "Not Specified"


class PathologyClassification(str, Enum):
    """
    The final classification of the overall pathology.
    """
    # The final classification of the overall pathology is unclear.
    Unclear = "Unclear"
    # The final classification of the overall pathology is benign.
    Benign = "Benign"
    # The final classification of the overall pathology is malignant.
    Malignant = "Malignant"
    # The final classification of the overall pathology is inflammation.
    Inflammation = "Inflammation"



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
    named_entities: Optional[List[Any]] = Field(None, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'named_entities', 'domain_of': ['ExtractionResult']} })


class NamedEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
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

    publication: Optional[Publication] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    triples: Optional[List[Triple]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'triples', 'domain_of': ['TextWithTriples']} })


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    entities: Optional[List[str]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'entities', 'domain_of': ['TextWithEntity']} })


class RelationshipType(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core',
         'id_prefixes': ['RO', 'biolink']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
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


class PathologyReport(ConfiguredBaseModel):
    """
    A semicolon-delimited list of statements, each describing a pathology, including any diagnoses, one or more specific qualities being measured and the anatomical location or tissue the pathology is measured in. Each statement should describe a single condition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/pathology', 'tree_root': True})

    pathology_statements: Optional[List[PathologyStatement]] = Field(None, description="""A semicolon-delimited list of pathology statements, each describing a pathology, including any diagnoses, one or more specific qualities being measured and the anatomical location or tissue the pathology is measured in. If any of the pathology statements are negative, the negation should be included in each statment, e.g., \"no granulomas or viropathic changes\" should become \"no granulomas\" and \"no viropathic changes\".""", json_schema_extra = { "linkml_meta": {'alias': 'pathology_statements', 'domain_of': ['PathologyReport']} })
    is_benign: Optional[str] = Field(None, description="""Whether the overall pathology appears to be benign and not malignant. Other pathologies may be present, but if tissue is described as benign and/or if a carcinoma is explicitly excluded, this value should be true. A statement of \"no significant pathologic abnormality\" or the short form \"nspa\" would also have a value of true. It it otherwise false.""", json_schema_extra = { "linkml_meta": {'alias': 'is_benign',
         'annotations': {'prompt.example': {'tag': 'prompt.example',
                                            'value': 'true, false'}},
         'domain_of': ['PathologyReport']} })
    risks: Optional[List[str]] = Field(None, description="""A semicolon-delimited list of risks for development of more severe pathologies. If not specified, this value must be \"Not Specified\". Examples: gastric intestinal metaplasia, ulceration, lymphangiectasia""", json_schema_extra = { "linkml_meta": {'alias': 'risks', 'domain_of': ['PathologyReport']} })
    overall_classification: Optional[PathologyClassification] = Field(None, description="""The final classification of the overall pathology. This must be one of the following: \"Unclear\", \"Benign\", \"Malignant\", or \"Inflammation\".""", json_schema_extra = { "linkml_meta": {'alias': 'overall_classification', 'domain_of': ['PathologyReport']} })


class PathologyStatement(ConfiguredBaseModel):
    """
    A statement that describes a pathology, including any diagnoses, one or more specific qualities being measured and the anatomical location or tissue the pathology is measured in.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/pathology'})

    diagnosis: Optional[str] = Field(None, description="""The diagnosis or pathology being described. This may include full diagnoses or observations, for example, \"colitis\", \"inflammation\", \"dysplasia\", \"polyp\". If not specified, this value must be \"Not Specified\". If a diagnosis cannot be reached (e.g., due to lack of tissue sample), this value must be \"No Diagnosis\". Do not include qualifiers in this field, e.g., \"active colitis\" should be \"colitis\".""", json_schema_extra = { "linkml_meta": {'alias': 'diagnosis',
         'annotations': {'prompt.example': {'tag': 'prompt.example',
                                            'value': 'colitis, inflammation, '
                                                     'dysplasia'}},
         'domain_of': ['PathologyStatement']} })
    qualifiers: Optional[List[str]] = Field(None, description="""A semicolon-delimited list of descriptors other than those for severity. If not specified, this value must be \"Not Specified\".""", json_schema_extra = { "linkml_meta": {'alias': 'qualifiers',
         'annotations': {'prompt.example': {'tag': 'prompt.example',
                                            'value': 'active, chronic, focal'}},
         'domain_of': ['PathologyStatement']} })
    severity: Optional[SeverityLevel] = Field(None, description="""The severity of the pathology, for example, mild, moderate, or severe. If not specified, this value must be \"N/A\".""", json_schema_extra = { "linkml_meta": {'alias': 'severity',
         'annotations': {'prompt.example': {'tag': 'prompt.example',
                                            'value': 'mild, moderate, severe'}},
         'domain_of': ['PathologyStatement']} })
    anatomical_entities: Optional[List[str]] = Field(None, description="""Semicolon-delimited list of anatomical locations or tissues the pathology is measured in. This may need to be inferred from the text, for example, \"colitis\" means the entity should be \"colon\". A statement of \"gastric antral-type mucosa\" should be changed to include only the anatomical entity, in this case \"gastric mucosa\". If this is not specified or cannot be inferred then this value must be \"N/A\".""", json_schema_extra = { "linkml_meta": {'alias': 'anatomical_entities',
         'annotations': {'prompt.example': {'tag': 'prompt.example',
                                            'value': 'duodenum, colonic mucosa, '
                                                     'liver'}},
         'domain_of': ['PathologyStatement']} })
    negative: Optional[str] = Field(None, description="""Whether the pathology is negative or not present. This must be explicitly stated in the input, e.g., \"no granulomas\", in order to be true. It is otherwise false.""", json_schema_extra = { "linkml_meta": {'alias': 'negative',
         'annotations': {'prompt.example': {'tag': 'prompt.example',
                                            'value': 'true, false'}},
         'domain_of': ['PathologyStatement']} })


class Diagnosis(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'bioportal:SNOMEDCT, '
                                                 'bioportal:ICD10CM, sqlite:obo:ncit, '
                                                 'sqlite:obo:mesh, sqlite:obo:mondo'}},
         'from_schema': 'http://w3id.org/ontogpt/pathology',
         'id_prefixes': ['SNOMEDCT', 'ICD10CM']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class AnatomicalEntity(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:uberon'}},
         'from_schema': 'http://w3id.org/ontogpt/pathology',
         'id_prefixes': ['UBERON']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


class Qualifier(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:pato'}},
         'from_schema': 'http://w3id.org/ontogpt/pathology',
         'id_prefixes': ['PATO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })


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
PathologyReport.model_rebuild()
PathologyStatement.model_rebuild()
Diagnosis.model_rebuild()
AnatomicalEntity.model_rebuild()
Qualifier.model_rebuild()

