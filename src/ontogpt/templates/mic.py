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
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'mic',
     'default_range': 'string',
     'description': 'A template for micronutrient information from text, including '
                    'its participation in biochemical pathways and relationships '
                    'to genes and diseases. Intended for use with the '
                    'Micronutrient Information Center, a resource curated and '
                    'managed by the Linus Pauling Institute at Oregon State '
                    'University.',
     'id': 'http://w3id.org/ontogpt/mic',
     'imports': ['linkml:types', 'core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'mic',
     'prefixes': {'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'chebi': {'prefix_prefix': 'chebi',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'foodon': {'prefix_prefix': 'foodon',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/foodon_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mic': {'prefix_prefix': 'mic',
                          'prefix_reference': 'http://w3id.org/ontogpt/mic'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}},
     'source_file': 'src/ontogpt/templates/mic.yaml',
     'title': 'Micronutrient Information Extraction Template'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class GOBiologicalProcessType(str):
    pass



class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    input_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_id', 'domain_of': ['ExtractionResult']} })
    input_title: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_title', 'domain_of': ['ExtractionResult']} })
    input_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_text', 'domain_of': ['ExtractionResult']} })
    raw_completion_output: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'raw_completion_output', 'domain_of': ['ExtractionResult']} })
    prompt: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'prompt', 'domain_of': ['ExtractionResult']} })
    extracted_object: Optional[Any] = Field(default=None, description="""The complex objects extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'extracted_object', 'domain_of': ['ExtractionResult']} })
    named_entities: Optional[list[Any]] = Field(default=None, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'named_entities', 'domain_of': ['ExtractionResult']} })


class NamedEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class CompoundExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    pass


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    subject: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['Triple']} })
    predicate: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['Triple']} })
    object: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object', 'domain_of': ['Triple']} })
    qualifier: Optional[str] = Field(default=None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""", json_schema_extra = { "linkml_meta": {'alias': 'qualifier', 'domain_of': ['Triple']} })
    subject_qualifier: Optional[str] = Field(default=None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""", json_schema_extra = { "linkml_meta": {'alias': 'subject_qualifier', 'domain_of': ['Triple']} })
    object_qualifier: Optional[str] = Field(default=None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""", json_schema_extra = { "linkml_meta": {'alias': 'object_qualifier', 'domain_of': ['Triple']} })


class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    triples: Optional[list[Triple]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'triples', 'domain_of': ['TextWithTriples']} })


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    entities: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'entities', 'domain_of': ['TextWithEntity']} })


class RelationshipType(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core',
         'id_prefixes': ['RO', 'biolink']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class Publication(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    id: Optional[str] = Field(default=None, description="""The publication identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })
    title: Optional[str] = Field(default=None, description="""The title of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Publication']} })
    abstract: Optional[str] = Field(default=None, description="""The abstract of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'abstract', 'domain_of': ['Publication']} })
    combined_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'combined_text', 'domain_of': ['Publication']} })
    full_text: Optional[str] = Field(default=None, description="""The full text of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'full_text', 'domain_of': ['Publication']} })


class AnnotatorResult(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    subject_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subject_text', 'domain_of': ['AnnotatorResult']} })
    object_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object_id', 'domain_of': ['AnnotatorResult']} })
    object_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object_text', 'domain_of': ['AnnotatorResult']} })


class Document(NamedEntity):
    """
    A document that contains information about micronutrients, including vitamins and minerals.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/mic', 'tree_root': True})

    nutrient_to_feature_relationships: Optional[list[NutrientToFeatureRelationship]] = Field(default=None, description="""A list of relationships between nutrients and biological features.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_to_feature_relationships',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'relationships between a single nutrient '
                                             '(including vitamins, minerals, and '
                                             'micronutrients) and a single feature, '
                                             'such as a disease, symptom, abnormality, '
                                             'or other health status. This may include '
                                             "diseases like Alzheimer's disease, "
                                             'systemic lupus erythematosus, rheumatoid '
                                             'arthritis, sickle cell anemia, or Barth '
                                             'syndrome. It may also include phenotypes '
                                             'such as an observable physical or '
                                             'behavioral trait or symptom (e.g., '
                                             'fever, headache, short attention span, '
                                             'petechiae, telangiectasia). Do NOT '
                                             'include relationships concerning only  '
                                             'biological processes (e.g., "Insulin '
                                             'signaling" or "lipid metabolism"), '
                                             'developmental processes such as "limb '
                                             'development", or health states such as '
                                             '"healthy teeth". Provide the full text '
                                             'from the input text describing the '
                                             'relationship without changes or '
                                             'summarization. Include all numbered '
                                             'inline references contained in the '
                                             'sentences without changes. Do not '
                                             'include newlines. If multiple sentences '
                                             'describe the same relationship, include '
                                             'all of them. If the text describes a '
                                             'one-to-many relationship, include all of '
                                             'them separately. For example, "Vitamin A '
                                             'is associated with Systemic Lupus '
                                             'Erythematosus and Rheumatoid Arthritis '
                                             '(5,6)" should be "Vitamin A is '
                                             'associated with Systemic Lupus '
                                             'Erythematosus (5,6); Vitamin A is '
                                             'associated with Rheumatoid Arthritis '
                                             '(5,6)". Use the same description of the '
                                             'relationship as in the input text. For '
                                             'example, if the input text states "Iron '
                                             'supplementation was shown to '
                                             'successfully treat anemia (5,6)", the '
                                             'output should be "Iron supplementation '
                                             'treats anemia (5,6)". Do not assign a '
                                             'relationship type. Retain the language '
                                             'used in the source text.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Evidence suggests that '
                                                      'high-dose Vitamin A treatment '
                                                      'may prevent Systemic Lupus '
                                                      'Erythematosus (5,6). Further '
                                                      'studies confirmed this finding '
                                                      '(7); Studies have shown that '
                                                      'Vitamin A is associated with '
                                                      'bone cancer (8).'}},
         'domain_of': ['Document']} })
    nutrient_to_biological_process_relationships: Optional[list[NutrientToBiologicalProcessRelationship]] = Field(default=None, description="""A list of relationships between nutrients and biological processes.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_to_biological_process_relationships',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'relationships between a single nutrient '
                                             '(including vitamins, minerals, and '
                                             'micronutrients) and a single biological '
                                             'process, with a type of relationship '
                                             'connecting them both. A biological '
                                             'process is an activity or series of '
                                             'activities that occur in a cell or '
                                             'organism, such as "nuclear axial '
                                             'expansion", "intracellular transport", '
                                             '"ribosomal subunit export from nucleus", '
                                             '"insulin signaling", or "DNA repair". '
                                             'Biological processes do NOT include '
                                             'health states such as "healthy teeth" or '
                                             'proteins such as "retinoic acid '
                                             'receptor". Provide the full text from '
                                             'the input text describing the '
                                             'relationship without changes or '
                                             'summarization. Include all numbered '
                                             'inline references contained in the '
                                             'sentences without changes. Do not '
                                             'include newlines. If multiple sentences '
                                             'describe the same relationship, include '
                                             'all of them. If the text describes a '
                                             'one-to-many relationship, include all of '
                                             'them separately. For example, "Vitamin A '
                                             'is associated with Insulin Signaling and '
                                             'DNA repair (5,6)" should be "Vitamin A '
                                             'is associated with Insulin Signaling '
                                             '(5,6); Vitamin A is associated with DNA '
                                             'repair (5,6)". Use the same description '
                                             'of the relationship as in the input '
                                             'text. For example, if the input text '
                                             'states "Vitamin A is a participant in '
                                             'Insulin Signaling (5,6)", the output '
                                             'should be "Vitamin A participates in '
                                             'Insulin Signaling (5,6)". Do not assign '
                                             'a relationship type. Retain the language '
                                             'used in the source text.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'There is a relationship between '
                                                      'Vitamin A and Insulin Signaling '
                                                      '(5). This relationship was '
                                                      'confirmed in additional studies '
                                                      '(6).'}},
         'domain_of': ['Document']} })
    nutrient_to_health_status_relationships: Optional[list[NutrientToHealthStatusRelationship]] = Field(default=None, description="""A list of relationships between nutrients and health of a specific part or system of the human body.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_to_health_status_relationships',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'relationships between a single nutrient '
                                             '(including vitamins, minerals, and '
                                             'micronutrients) and a single part or '
                                             'system of the body, with a type of '
                                             'relationship connecting them both. '
                                             'Example parts or systems include '
                                             '"teeth", "skin", "cardiovascular '
                                             'system", "digestive system", or "liver". '
                                             'Transform names of processes to their '
                                             'respective anatomy, e.g., "thyroid '
                                             'function" or "thyroid health" should be '
                                             'changed to "thyroid"; "digestion" should '
                                             'be changed to "digestive system". '
                                             'Provide the full text from the input '
                                             'text describing the relationship without '
                                             'changes or summarization. Include all '
                                             'numbered inline references contained in '
                                             'the sentences without changes. Do not '
                                             'include newlines. If multiple sentences '
                                             'describe the same relationship, include '
                                             'all of them. If the text describes a '
                                             'one-to-many relationship, include all of '
                                             'them separately. For example, "Vitamin A '
                                             'is associated with healthy teeth and '
                                             'healthy skin (5,6)" should be "Vitamin A '
                                             'is associated with healthy teeth (5,6); '
                                             'Vitamin A is associated with healthy '
                                             'skin (5,6)". Use the same description of '
                                             'the relationship as in the input text. '
                                             'For example, if the input text states '
                                             '"Vitamin A levels are necessary for '
                                             'healthy teeth (5,6)", the output should '
                                             'be "Vitamin A participates in the health '
                                             'of teeth (5,6)". Do not assign a '
                                             'relationship type. Retain the language '
                                             'used in the source text.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'There is a relationship between '
                                                      'Vitamin A and Teeth (5). This '
                                                      'relationship was confirmed in '
                                                      'additional studies (6).'}},
         'domain_of': ['Document']} })
    nutrient_to_source_relationships: Optional[list[NutrientToSourceRelationship]] = Field(default=None, description="""A list of relationships between nutrients and their sources in food or supplements.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_to_source_relationships',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'relationships between a single nutrient '
                                             '(including vitamins, minerals, and '
                                             'micronutrients) and a single food or '
                                             'supplement, with a type of relationship '
                                             'connecting them both. Example foods '
                                             'include "butter", "apple", "watermelon", '
                                             '"beef", or "breakfast cereal". Provide '
                                             'the full text from the input text '
                                             'describing the relationship without '
                                             'changes or summarization. Include all '
                                             'numbered inline references contained in '
                                             'the sentences without changes. Do not '
                                             'include newlines. If multiple sentences '
                                             'describe the same relationship, include '
                                             'all of them. If the text describes a '
                                             'one-to-many relationship, include all of '
                                             'them separately. For example, "Vitamin A '
                                             'is associated with butter and apple '
                                             '(5,6)" should be "Vitamin A is '
                                             'associated with butter (5,6); Vitamin A '
                                             'is associated with apple (5,6)". These '
                                             'relationships may require some '
                                             'processing, e.g., "Vitamin A is found in '
                                             'butter (5,6)" should be "Vitamin A is a '
                                             'nutrient of butter (5,6)".'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Butter is a source of Vitamin A '
                                                      '(12). This relationship was '
                                                      'confirmed in additional studies '
                                                      '(13).'}},
         'domain_of': ['Document']} })
    nutrient_to_nutrient_relationships: Optional[list[NutrientToNutrientRelationship]] = Field(default=None, description="""A list of relationships between nutrients and other nutrients.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_to_nutrient_relationships',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'relationships between a single nutrient '
                                             '(including vitamins, minerals, and '
                                             'micronutrients) and another single '
                                             'nutrient, with a type of relationship '
                                             'connecting them both. This does not '
                                             'include relationships between nutrients '
                                             'and proteins (e.g., a nutrient and its '
                                             'receptor protein). Provide the full text '
                                             'from the input text describing the '
                                             'relationship without changes or '
                                             'summarization. Include all numbered '
                                             'inline references contained in the '
                                             'sentences without changes. Do not '
                                             'include newlines. If multiple sentences '
                                             'describe the same relationship, include '
                                             'all of them. If the text describes a '
                                             'one-to-many relationship, include all of '
                                             'them separately. For example, "Vitamin A '
                                             'is associated with Vitamin D and Vitamin '
                                             'E (5,6)" should be "Vitamin A is '
                                             'associated with Vitamin D (5,6); Vitamin '
                                             'A is associated with Vitamin E (5,6)". '
                                             'Use the same description of the '
                                             'relationship as in the input text. For '
                                             'example, if the input text states '
                                             '"Vitamin A participates in physiological '
                                             'processes with Vitamin D (5,6)", the '
                                             'output should be "Vitamin A physically '
                                             'interacts with Vitamin D (5,6)".'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'There is a relationship between '
                                                      'Vitamin A and Vitamin D (5). '
                                                      'This relationship was confirmed '
                                                      'in additional studies (6).'}},
         'domain_of': ['Document']} })
    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class Nutrient(NamedEntity):
    """
    The name of a nutrient, including vitamins and minerals.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:chebi, sqlite:obo:foodon'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of a nutrient, including '
                                             'vitamins and minerals.'}},
         'from_schema': 'http://w3id.org/ontogpt/mic',
         'id_prefixes': ['CHEBI', 'FOODON']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class Feature(NamedEntity):
    """
    The name of a biological feature or health status, such as a disease, symptom, or abnormality.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:mondo, sqlite:obo:hp, '
                                                 'sqlite:obo:efo'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of a biological feature. This '
                                             'may include diseases, symptoms, '
                                             'abnormalities, or other health statuses, '
                                             'as well as observable properties of an '
                                             'organism, such as body weight.'}},
         'from_schema': 'http://w3id.org/ontogpt/mic',
         'id_prefixes': ['MONDO', 'HP', 'EFO']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class BiologicalProcess(NamedEntity):
    """
    The name of a biological process.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators', 'value': 'sqlite:obo:go'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of a biological process.'}},
         'from_schema': 'http://w3id.org/ontogpt/mic',
         'id_prefixes': ['GO'],
         'slot_usage': {'id': {'name': 'id',
                               'values_from': ['GOBiologicalProcessType']}}})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication'],
         'values_from': ['GOBiologicalProcessType']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class Anatomy(NamedEntity):
    """
    The name of an anatomical part or system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:uberon'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of an anatomical part or '
                                             'system.'}},
         'from_schema': 'http://w3id.org/ontogpt/mic',
         'id_prefixes': ['UBERON']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class FoodOrSupplement(NamedEntity):
    """
    The name of a food or supplement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:foodon'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of a food or supplement.'}},
         'from_schema': 'http://w3id.org/ontogpt/mic',
         'id_prefixes': ['FOODON']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class ScientificClaim(CompoundExpression):
    """
    A scientific claim made in the input text.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/mic'})

    negated: Optional[str] = Field(default=None, description="""Whether the claim is negated in the text. This value must be either \"True\" if the claim is negated or \"False\" if it is not. For example, \"Vitamin A is not associated with cancer\" would be \"True\" and \"Vitamin A is associated with cancer\" would be \"False\". Statements characterized as \"clinically insignificant\", \"not clinically significant\", or \"not statistically significant\" should also be considered negated.""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ScientificClaim']} })
    context: Optional[str] = Field(default=None, description="""The full text of this relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ScientificClaim']} })
    references: Optional[list[str]] = Field(default=None, description="""A semi-colon separated list of references included inline in the input, identified by number only. Multiple references may contain commas, e.g., \"(3, 4)\" and should be treated as two different values. If a range of references is provided, include all, e.g., \"(3-5)\" should become 3;4;5.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ScientificClaim']} })


class Relationship(NamedEntity):
    """
    The name of a type of relationship between two entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ro, sqlite:obo:biolink'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of a type of relationship '
                                             'between two entities.'}},
         'from_schema': 'http://w3id.org/ontogpt/mic',
         'id_prefixes': ['RO', 'biolink']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class NutrientToFeatureRelationship(ScientificClaim):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['a Chemical to Feature relationship'],
         'from_schema': 'http://w3id.org/ontogpt/mic'})

    nutrient: Optional[str] = Field(default=None, description="""The name of the nutrient defined in the claim, including vitamins and minerals.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    relationship: Optional[str] = Field(default=None, description="""The name of a type of relationship between the nutrient and the feature. Choose from one of the following: \"positively correlated with\", \"negatively correlated with\", \"treats\", \"studied to treat\", \"in clinical trials for\", \"in preclinical trials for\", \"beneficial in models for\", \"applied to treat\". If none of these apply, use \"associated with\".""", json_schema_extra = { "linkml_meta": {'alias': 'relationship',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToNutrientRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    feature: Optional[str] = Field(default=None, description="""The name of the biological feature defined in the claim. This may need to be processed to a single term, e.g.,  the phrase \"proteolysis (degradation) of insulin and some downstream  effectors\" is too long, but \"insulin degradation\" is acceptable.""", json_schema_extra = { "linkml_meta": {'alias': 'feature', 'domain_of': ['NutrientToFeatureRelationship']} })
    negated: Optional[str] = Field(default=None, description="""Whether the claim is negated in the text. This value must be either \"True\" if the claim is negated or \"False\" if it is not. For example, \"Vitamin A is not associated with cancer\" would be \"True\" and \"Vitamin A is associated with cancer\" would be \"False\". Statements characterized as \"clinically insignificant\", \"not clinically significant\", or \"not statistically significant\" should also be considered negated.""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ScientificClaim']} })
    context: Optional[str] = Field(default=None, description="""The full text of this relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ScientificClaim']} })
    references: Optional[list[str]] = Field(default=None, description="""A semi-colon separated list of references included inline in the input, identified by number only. Multiple references may contain commas, e.g., \"(3, 4)\" and should be treated as two different values. If a range of references is provided, include all, e.g., \"(3-5)\" should become 3;4;5.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ScientificClaim']} })


class NutrientToBiologicalProcessRelationship(ScientificClaim):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/mic'})

    nutrient: Optional[str] = Field(default=None, description="""The name of the nutrient defined in the claim, including vitamins and minerals.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    relationship: Optional[str] = Field(default=None, description="""The name of a type of relationship between the nutrient and the biological process. Choose from one of the following: \"interacts with\", \"physically interacts with\", \"increases amount or activity of\", \"decreases amount or activity of\", \"amount or activity increased by\", \"amount or activity decreased by\", \"response affected by\", \"increases response to\", \"decreases response to\", \"response increased by\". If none of these apply, use \"associated with\".""", json_schema_extra = { "linkml_meta": {'alias': 'relationship',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToNutrientRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    process: Optional[str] = Field(default=None, description="""The name of the biological process defined in the claim.""", json_schema_extra = { "linkml_meta": {'alias': 'process', 'domain_of': ['NutrientToBiologicalProcessRelationship']} })
    negated: Optional[str] = Field(default=None, description="""Whether the claim is negated in the text. This value must be either \"True\" if the claim is negated or \"False\" if it is not. For example, \"Vitamin A is not associated with cancer\" would be \"True\" and \"Vitamin A is associated with cancer\" would be \"False\". Statements characterized as \"clinically insignificant\", \"not clinically significant\", or \"not statistically significant\" should also be considered negated.""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ScientificClaim']} })
    context: Optional[str] = Field(default=None, description="""The full text of this relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ScientificClaim']} })
    references: Optional[list[str]] = Field(default=None, description="""A semi-colon separated list of references included inline in the input, identified by number only. Multiple references may contain commas, e.g., \"(3, 4)\" and should be treated as two different values. If a range of references is provided, include all, e.g., \"(3-5)\" should become 3;4;5.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ScientificClaim']} })


class NutrientToNutrientRelationship(ScientificClaim):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['a Chemical to Chemical relationship'],
         'from_schema': 'http://w3id.org/ontogpt/mic'})

    nutrient_subject: Optional[str] = Field(default=None, description="""The name of a nutrient defined in the claim, including vitamins and minerals.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_subject', 'domain_of': ['NutrientToNutrientRelationship']} })
    relationship: Optional[str] = Field(default=None, description="""The name of a type of relationship between the nutrient_subject and nutrient_object. Choose from one of the following: \"interacts with\", \"physically interacts with\", \"increases amount or activity of\", \"decreases amount or activity of\", \"amount or activity increased by\", \"amount or activity decreased by\", \"response affected by\", \"increases response to\", \"decreases response to\", \"response increased by\". If none of these apply, use \"associated with\".""", json_schema_extra = { "linkml_meta": {'alias': 'relationship',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToNutrientRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    nutrient_object: Optional[str] = Field(default=None, description="""The name of a nutrient defined in the claim, including vitamins and minerals.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient_object', 'domain_of': ['NutrientToNutrientRelationship']} })
    negated: Optional[str] = Field(default=None, description="""Whether the claim is negated in the text. This value must be either \"True\" if the claim is negated or \"False\" if it is not. For example, \"Vitamin A is not associated with cancer\" would be \"True\" and \"Vitamin A is associated with cancer\" would be \"False\". Statements characterized as \"clinically insignificant\", \"not clinically significant\", or \"not statistically significant\" should also be considered negated.""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ScientificClaim']} })
    context: Optional[str] = Field(default=None, description="""The full text of this relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ScientificClaim']} })
    references: Optional[list[str]] = Field(default=None, description="""A semi-colon separated list of references included inline in the input, identified by number only. Multiple references may contain commas, e.g., \"(3, 4)\" and should be treated as two different values. If a range of references is provided, include all, e.g., \"(3-5)\" should become 3;4;5.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ScientificClaim']} })


class NutrientToHealthStatusRelationship(ScientificClaim):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/mic'})

    nutrient: Optional[str] = Field(default=None, description="""The name of the nutrient defined in the claim, including vitamins and minerals.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    relationship: Optional[str] = Field(default=None, description="""The name of a type of relationship between the nutrient and the anatomical part or system. Choose from one of the following: \"affects\", \"participates in\". If none of these apply, use \"associated with\".""", json_schema_extra = { "linkml_meta": {'alias': 'relationship',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToNutrientRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    anatomy: Optional[str] = Field(default=None, description="""The name of the anatomical part or system defined in the claim.""", json_schema_extra = { "linkml_meta": {'alias': 'anatomy', 'domain_of': ['NutrientToHealthStatusRelationship']} })
    negated: Optional[str] = Field(default=None, description="""Whether the claim is negated in the text. This value must be either \"True\" if the claim is negated or \"False\" if it is not. For example, \"Vitamin A is not associated with cancer\" would be \"True\" and \"Vitamin A is associated with cancer\" would be \"False\". Statements characterized as \"clinically insignificant\", \"not clinically significant\", or \"not statistically significant\" should also be considered negated.""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ScientificClaim']} })
    context: Optional[str] = Field(default=None, description="""The full text of this relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ScientificClaim']} })
    references: Optional[list[str]] = Field(default=None, description="""A semi-colon separated list of references included inline in the input, identified by number only. Multiple references may contain commas, e.g., \"(3, 4)\" and should be treated as two different values. If a range of references is provided, include all, e.g., \"(3-5)\" should become 3;4;5.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ScientificClaim']} })


class NutrientToSourceRelationship(ScientificClaim):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/mic'})

    nutrient: Optional[str] = Field(default=None, description="""The name of the nutrient defined in the claim, including vitamins and minerals.""", json_schema_extra = { "linkml_meta": {'alias': 'nutrient',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    relationship: Optional[str] = Field(default=None, description="""The name of a type of relationship between the nutrient and the food or supplement. Choose from one of the following: \"nutrient of\", \"is active ingredient of\", \"food component of\". If none of these apply, use \"associated with\".""", json_schema_extra = { "linkml_meta": {'alias': 'relationship',
         'domain_of': ['NutrientToFeatureRelationship',
                       'NutrientToBiologicalProcessRelationship',
                       'NutrientToNutrientRelationship',
                       'NutrientToHealthStatusRelationship',
                       'NutrientToSourceRelationship']} })
    source: Optional[str] = Field(default=None, description="""The name of the food or supplement defined in the claim.""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['NutrientToSourceRelationship']} })
    negated: Optional[str] = Field(default=None, description="""Whether the claim is negated in the text. This value must be either \"True\" if the claim is negated or \"False\" if it is not. For example, \"Vitamin A is not associated with cancer\" would be \"True\" and \"Vitamin A is associated with cancer\" would be \"False\". Statements characterized as \"clinically insignificant\", \"not clinically significant\", or \"not statistically significant\" should also be considered negated.""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ScientificClaim']} })
    context: Optional[str] = Field(default=None, description="""The full text of this relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ScientificClaim']} })
    references: Optional[list[str]] = Field(default=None, description="""A semi-colon separated list of references included inline in the input, identified by number only. Multiple references may contain commas, e.g., \"(3, 4)\" and should be treated as two different values. If a range of references is provided, include all, e.g., \"(3-5)\" should become 3;4;5.""", json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['ScientificClaim']} })


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
Document.model_rebuild()
Nutrient.model_rebuild()
Feature.model_rebuild()
BiologicalProcess.model_rebuild()
Anatomy.model_rebuild()
FoodOrSupplement.model_rebuild()
ScientificClaim.model_rebuild()
Relationship.model_rebuild()
NutrientToFeatureRelationship.model_rebuild()
NutrientToBiologicalProcessRelationship.model_rebuild()
NutrientToNutrientRelationship.model_rebuild()
NutrientToHealthStatusRelationship.model_rebuild()
NutrientToSourceRelationship.model_rebuild()

