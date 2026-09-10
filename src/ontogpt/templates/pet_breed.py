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
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





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


linkml_meta = LinkMLMeta({'default_prefix': 'pet_breed',
     'default_range': 'string',
     'description': 'Extracts a structured description of a single cat or dog '
                    'breed from an encyclopedia-style text such as a Wikipedia '
                    'article. The breed grounds to VBO (Vertebrate Breed '
                    'Ontology). Each characteristic is decomposed into a '
                    'whole-phenotype term (UPHENO), the body part involved '
                    '(UBERON), and the quality observed (PATO).',
     'id': 'http://w3id.org/ontogpt/pet_breed',
     'imports': ['linkml:types', 'core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'pet_breed',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UPHENO': {'prefix_prefix': 'UPHENO',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UPHENO_'},
                  'VBO': {'prefix_prefix': 'VBO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/VBO_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'pet_breed': {'prefix_prefix': 'pet_breed',
                                'prefix_reference': 'http://w3id.org/ontogpt/pet_breed/'}},
     'source_file': 'src/ontogpt/templates/pet_breed.yaml',
     'title': 'Cat and Dog Breed Description Template'} )

class TermValidationStatus(str, Enum):
    """
    Outcome categories for ontology term validation.
    """
    VALID = "VALID"
    """
    The identifier resolves and the extracted label is its label or a synonym
    """
    LABEL_DIFFERS = "LABEL_DIFFERS"
    """
    The identifier resolves but the extracted label is neither its label nor a synonym
    """
    REPLACED = "REPLACED"
    """
    The identifier was invalid or obsolete and a valid substitute was found
    """
    UNRESOLVED = "UNRESOLVED"
    """
    The identifier was invalid and no substitute was found; the value was rewritten with the auto prefix
    """
    SKIPPED = "SKIPPED"
    """
    The identifier could not be checked because no ontology adapter was available for its prefix
    """


class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class SpeciesEnum(str, Enum):
    cat = "cat"
    dog = "dog"


class CatOrDogBreedIdentifier(str):
    """
    Any breed below the VBO cat breed or dog breed nodes.
    """
    pass



class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    input_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    input_title: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    input_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    raw_completion_output: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    prompt: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    extracted_object: Optional[Any] = Field(default=None, description="""The complex objects extracted from the text""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    named_entities: Optional[list[Any]] = Field(default=None, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })
    validation: Optional[TermValidationReport] = Field(default=None, description="""Results of validating the grounded terms in the extracted object against their source ontologies, including any replacements made. Absent when validation was not run.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtractionResult']} })


class TermValidationReport(ConfiguredBaseModel):
    """
    Summary of ontology term validation performed on an extraction result. Each grounded identifier in the extracted object is checked for existence and obsolescence in its ontology and for agreement between the extracted label and the ontology's label or synonyms. Invalid identifiers are replaced when a valid substitute can be found.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    validator: Optional[str] = Field(default=None, description="""Name and version of the validation library used""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    total_terms: Optional[int] = Field(default=None, description="""Number of grounded identifiers examined""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    valid_terms: Optional[int] = Field(default=None, description="""Identifiers that resolved with a matching label or synonym""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    replaced_terms: Optional[int] = Field(default=None, description="""Identifiers replaced with a valid substitute""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    unresolved_terms: Optional[int] = Field(default=None, description="""Invalid identifiers for which no substitute was found; these are rewritten with the auto prefix so that no invalid identifier remains""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    label_mismatches: Optional[int] = Field(default=None, description="""Identifiers that resolved but whose extracted label is neither the ontology label nor a known synonym; kept as they are""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    skipped_terms: Optional[int] = Field(default=None, description="""Identifiers that could not be checked because no ontology adapter was available""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })
    results: Optional[list[TermValidationResult]] = Field(default=None, description="""One entry per examined identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationReport']} })


class TermValidationResult(ConfiguredBaseModel):
    """
    Outcome of validating one grounded identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    original_id: Optional[str] = Field(default=None, description="""The identifier as produced by grounding""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    label: Optional[str] = Field(default=None, description="""The label extracted from the text for this identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult', 'NamedEntity']} })
    entity_class: Optional[str] = Field(default=None, description="""The template class the identifier was grounded for""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    status: Optional[TermValidationStatus] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    ontology_label: Optional[str] = Field(default=None, description="""The label of the original identifier in its ontology, when it resolved""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    replacement_id: Optional[str] = Field(default=None, description="""The identifier substituted into the output, if any""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    replacement_label: Optional[str] = Field(default=None, description="""The ontology label of the replacement identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    message: Optional[str] = Field(default=None, description="""Human-readable explanation of the outcome""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })
    attempts: Optional[list[str]] = Field(default=None, description="""Candidate identifiers considered while searching for a replacement""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermValidationResult']} })


class NamedEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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

    subject: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Triple']} })
    predicate: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Triple']} })
    object: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Triple']} })
    qualifier: Optional[str] = Field(default=None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Triple']} })
    subject_qualifier: Optional[str] = Field(default=None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Triple']} })
    object_qualifier: Optional[str] = Field(default=None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Triple']} })


class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    triples: Optional[list[Triple]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TextWithTriples']} })


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    entities: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TextWithEntity']} })


class RelationshipType(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core',
         'id_prefixes': ['RO', 'biolink']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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

    id: Optional[str] = Field(default=None, description="""The publication identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Publication']} })
    title: Optional[str] = Field(default=None, description="""The title of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    abstract: Optional[str] = Field(default=None, description="""The abstract of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    combined_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })
    full_text: Optional[str] = Field(default=None, description="""The full text of the publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication']} })


class AnnotatorResult(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    subject_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotatorResult']} })
    object_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotatorResult']} })
    object_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotatorResult']} })


class BreedDescription(ConfiguredBaseModel):
    """
    A structured description of one cat or dog breed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/pet_breed', 'tree_root': True})

    breed: Optional[str] = Field(default=None, description="""the name of the single cat or dog breed that the text is about, as written in the text, followed by the species in parentheses, e.g. \"Abyssinian (Cat)\" or \"Border Collie (Dog)\"""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Abyssinian (Cat), Siamese '
                                                      '(Cat), Border Collie (Dog)'}},
         'domain_of': ['BreedDescription']} })
    species: Optional[SpeciesEnum] = Field(default=None, description="""whether the breed is a breed of cat or of dog""", json_schema_extra = { "linkml_meta": {'domain_of': ['BreedDescription']} })
    year_established: Optional[str] = Field(default=None, description="""the year the breed was first established, recognized, or registered as a breed, as a four-digit year. If the text gives several years, use the earliest year of formal recognition by a breed registry. If no year is given, write \"not stated\".""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '1868, 1979, not stated'}},
         'domain_of': ['BreedDescription']} })
    place_of_origin: Optional[str] = Field(default=None, description="""the country or region where the breed is said to have originated, as written in the text""", json_schema_extra = { "linkml_meta": {'domain_of': ['BreedDescription']} })
    characteristics: Optional[list[BreedCharacteristic]] = Field(default=None, description="""semicolon-separated list of the distinctive physical characteristics of the breed described in the text. Each item is exactly one body part with exactly one quality, as a short phrase, e.g. \"ticked coat\", \"large ears\", \"almond-shaped eyes\", \"long body\". If the text gives a body part two qualities, such as \"large erect ears\" or \"long lean body\", write two items: \"large ears; erect ears\". Do not include behaviour or temperament here.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'ticked coat; large ears; erect '
                                                      'ears; almond-shaped eyes; long '
                                                      'body'}},
         'domain_of': ['BreedDescription']} })
    coat_colors: Optional[list[str]] = Field(default=None, description="""semicolon-separated list of the coat colours accepted for the breed, each as a single colour word or short phrase as written in the text""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'ruddy; sorrel; blue; fawn'}},
         'domain_of': ['BreedDescription']} })
    temperament: Optional[list[str]] = Field(default=None, description="""semicolon-separated list of short phrases describing the behaviour and temperament of the breed, as written in the text""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'highly social; active; playful; '
                                                      'not a lap cat'}},
         'domain_of': ['BreedDescription']} })


class BreedCharacteristic(CompoundExpression):
    """
    One physical characteristic of a breed, decomposed into the phenotype as a whole, the body part it affects, and the quality of that part.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/pet_breed'})

    phenotype: Optional[str] = Field(default=None, description="""the characteristic restated as a formal phenotype phrase of the form \"<increased or decreased> <attribute> of the <body part>\" or \"<shape> <body part>\", naming exactly one attribute, e.g. for \"large ears\" write \"increased size of the external ear\"; for \"long body\" write \"increased length of the trunk\"; for \"short coat\" write \"decreased length of the hair\"; for \"almond-shaped eyes\" write \"almond-shaped eye\"""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'increased size of the external '
                                                      'ear, increased length of the '
                                                      'trunk, almond-shaped eye'}},
         'domain_of': ['BreedCharacteristic']} })
    anatomical_part: Optional[str] = Field(default=None, description="""the body part or structure the characteristic refers to, as a single anatomical noun, e.g. \"ear\", \"coat hair\", \"eye\", \"trunk\"""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'ear, coat hair, eye, trunk, '
                                                      'limb'}},
         'domain_of': ['BreedCharacteristic']} })
    quality: Optional[str] = Field(default=None, description="""the quality of the body part, as exactly one adjective, e.g. \"large\", \"erect\", \"long\", \"tapered\", \"oval\", \"dense\", \"short\". Never give two adjectives. Prefer a plain adjective of size, length, shape, or density over a specialised term, e.g. \"banded\" rather than \"ticked\", \"slender\" rather than \"lithe\"""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'large, erect, long, tapered, '
                                                      'oval, dense, short'}},
         'domain_of': ['BreedCharacteristic']} })


class Breed(NamedEntity):
    """
    A cat or dog breed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:vbo'}},
         'from_schema': 'http://w3id.org/ontogpt/pet_breed',
         'id_prefixes': ['VBO'],
         'slot_usage': {'id': {'identifier': True,
                               'name': 'id',
                               'values_from': ['CatOrDogBreedIdentifier']}}})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication'],
         'values_from': ['CatOrDogBreedIdentifier']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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


class Phenotype(NamedEntity):
    """
    A whole-organism or body-part phenotype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:upheno'}},
         'from_schema': 'http://w3id.org/ontogpt/pet_breed',
         'id_prefixes': ['UPHENO']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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


class AnatomicalPart(NamedEntity):
    """
    An anatomical structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:uberon'}},
         'from_schema': 'http://w3id.org/ontogpt/pet_breed',
         'id_prefixes': ['UBERON']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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


class Quality(NamedEntity):
    """
    A quality or attribute.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:pato'}},
         'from_schema': 'http://w3id.org/ontogpt/pet_breed',
         'id_prefixes': ['PATO']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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


class Color(NamedEntity):
    """
    A colour, as a PATO color quality.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:pato'}},
         'from_schema': 'http://w3id.org/ontogpt/pet_breed',
         'id_prefixes': ['PATO']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['TermValidationResult', 'NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
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


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ExtractionResult.model_rebuild()
TermValidationReport.model_rebuild()
TermValidationResult.model_rebuild()
NamedEntity.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()
BreedDescription.model_rebuild()
BreedCharacteristic.model_rebuild()
Breed.model_rebuild()
Phenotype.model_rebuild()
AnatomicalPart.model_rebuild()
Quality.model_rebuild()
Color.model_rebuild()
