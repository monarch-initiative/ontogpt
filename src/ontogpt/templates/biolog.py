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


linkml_meta = LinkMLMeta({'default_prefix': 'paperex',
     'default_range': 'string',
     'description': 'Schema for extracting structured data from papers, including '
                    'Biolog Phenotype MicroArray experiments.',
     'id': 'https://example.org/PaperExtractionSchema',
     'imports': ['linkml:types', 'core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'PaperExtractionSchema',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'paperex': {'prefix_prefix': 'paperex',
                              'prefix_reference': 'https://example.org/PaperExtractionSchema/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}},
     'source_file': 'src/ontogpt/templates/biolog.yaml',
     'title': 'Paper Extraction Schema'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class FlexibleBooleanEnum(str, Enum):
    """
    A minimal enumeration for capturing yes/no/true/false in lowercase, plus 'not provided' if data are missing or ambiguous.

    """
    yes = "yes"
    no = "no"
    true = "true"
    false = "false"
    not_provided = "not provided"



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
    named_entities: Optional[List[Any]] = Field(default=None, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'named_entities', 'domain_of': ['ExtractionResult']} })


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
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
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
    triples: Optional[List[Triple]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'triples', 'domain_of': ['TextWithTriples']} })


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    entities: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'entities', 'domain_of': ['TextWithEntity']} })


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
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
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


class Paper(ConfiguredBaseModel):
    """
    A single paper or study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema', 'tree_root': True})

    study_title: str = Field(default=..., description="""The paper's title.""", json_schema_extra = { "linkml_meta": {'alias': 'study_title',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "Extract the paper's title. If not found, "
                                             "return only 'Not provided'."},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Root Exudates Alter the '
                                                      'Expression of Diverse '
                                                      'Metabolic, Transport, '
                                                      'Regulatory, and Stress Response '
                                                      'Genes in Rhizosphere '
                                                      'Pseudomonas.'}},
         'domain_of': ['Paper'],
         'examples': [{'description': 'From Mavrodi et al. 2021',
                       'value': 'Root Exudates Alter the Expression of Diverse '
                                'Metabolic, Transport, Regulatory, and Stress Response '
                                'Genes in Rhizosphere Pseudomonas.'}]} })
    authors: List[str] = Field(default=..., description="""Authors of the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'authors',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a list of authors, semicolon '
                                             'delimited.\n'
                                             'If multiple authors appear in one '
                                             'string, please split them carefully.\n'
                                             "If not found, use 'Not provided'.\n"}},
         'domain_of': ['Paper'],
         'examples': [{'value': 'Olga V. Mavrodi'}, {'value': 'Janiece R. McWilliams'}]} })
    doi: Optional[str] = Field(default=None, description="""DOI of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "Extract the DOI. If not found, use 'Not "
                                             "provided'."}},
         'domain_of': ['Paper'],
         'examples': [{'value': '10.3389/fmicb.2021.651282'}]} })
    date: Optional[str] = Field(default=None, description="""Publication date.""", json_schema_extra = { "linkml_meta": {'alias': 'date',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the publication date. If not '
                                             "found, use 'Not provided'."}},
         'domain_of': ['Paper'],
         'examples': [{'value': '14 April 2021'}]} })
    traits: Optional[List[str]] = Field(default=None, description="""Organismal traits measured or observed.""", json_schema_extra = { "linkml_meta": {'alias': 'traits',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a semicolon-delimited list of '
                                             'traits\n'
                                             'focused on in the study.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Growth rate; Lactose '
                                                      'production; motility'}},
         'domain_of': ['Paper', 'Experiment']} })
    experiments: List[Experiment] = Field(default=..., description="""Experiments (e.g., Biolog) included in the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'experiments',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a list of brief descriptions of '
                                             'experiments\n'
                                             'described in the paper. This list must '
                                             'be semicolon-delimited.\n'
                                             'For each description, include all of the '
                                             'following details if\n'
                                             'provided: experiment motivation (why it '
                                             'was performed),\n'
                                             'experiment design (how it was performed, '
                                             'including methods,\n'
                                             'tools, organisms, and chemicals used), '
                                             'environment (the location\n'
                                             'and conditions in which the experiment '
                                             'occurred, including\n'
                                             'metrics like temperature), all organisms '
                                             'used and their\n'
                                             'high-level type (e.g., plant, animal), '
                                             'the biological system\n'
                                             'under study (e.g., rhizosphere), '
                                             'experimental conditions\n'
                                             '(temperature, pH, etc.), and '
                                             'experimental factors tested or '
                                             'measured.\n'
                                             'Also note whether the experiment is a '
                                             'Biolog experiment and if so,\n'
                                             'the type or subtype of experiment (e.g., '
                                             'Phenotype MicroArray),\n'
                                             'the Biolog plates used (e.g., PM01), the '
                                             'number of replicates, all\n'
                                             'key steps in the experimental protocol, '
                                             'the types of data collected\n'
                                             'by the plate reader (e.g., OD, '
                                             'respiration), the protocol for\n'
                                             'measuring optical density (e.g., OD600 '
                                             'measured every 2 hours), \n'
                                             'the protocol for measuring respiration '
                                             '(e.g., Colorimetric change\n'
                                             'at 590 nm for formazan detection), the '
                                             'instrument or equipment used\n'
                                             '(e.g., OmniLog Phenotype MicroArray '
                                             'System), the software used for\n'
                                             'data analysis (e.g., OmniLog Parametric '
                                             'Analysis software), the\n'
                                             'incubation temperature (e.g., 25°C), the '
                                             'total duration of incubation\n'
                                             '(e.g., 48 h), and any other relevant '
                                             'details.\n'
                                             'If nothing is mentioned regarding '
                                             "experiments, use 'Not provided'.\n"
                                             'Do not provide any details here not '
                                             'related to experiments.\n'
                                             'Do not include newlines.\n'}},
         'domain_of': ['Paper'],
         'examples': [{'value': 'Biolog Phenotype MicroArray; RNA-seq for gene '
                                'expression'}]} })


class Experiment(ConfiguredBaseModel):
    """
    A single experiment from the paper.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    label: Optional[str] = Field(default=None, description="""A single sentence description of this experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A single sentence description of this '
                                             'experiment.\n'}},
         'domain_of': ['NamedEntity', 'Experiment']} })
    experiment_motivation: Optional[str] = Field(default=None, description="""Rationale for the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_motivation',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Explain the motivation or purpose of the '
                                             'experiment.\n'
                                             "If missing, use 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Assess the metabolic impact of root exudates on '
                                'Pseudomonas strains.'}]} })
    experiment_design: Optional[str] = Field(default=None, description="""Summary of how the experiment was designed.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_design',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Summarize the overall design. If '
                                             "missing, use 'Not provided'."}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Comparative analysis of Pseudomonas gene expression '
                                'with/without root exudates.'}]} })
    environment: Optional[str] = Field(default=None, description="""Location or conditions in which the experiment occurred.""", json_schema_extra = { "linkml_meta": {'alias': 'environment',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the environment or setting.'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Lab-based assay under 25°C'}]} })
    host_organism: Optional[List[str]] = Field(default=None, description="""One or more hosts in the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'host_organism',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Identify the host organisms or systems '
                                             'used\n'
                                             'in a semicolon-delimited list.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Brachypodium distachyon; '
                                                      'Arabidopsis thaliana'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Brachypodium distachyon'}]} })
    host_type: Optional[str] = Field(default=None, description="""Type of host (e.g., plant, animal).""", json_schema_extra = { "linkml_meta": {'alias': 'host_type',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe the host type if applicable '
                                             "(e.g. 'plant')."}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Plant'}]} })
    target_organisms: Optional[List[str]] = Field(default=None, description="""Organisms, including microbes, targeted in the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'target_organisms',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a semicolon-delimited list of '
                                             'target organisms,\n'
                                             'including microbes, targeted in the '
                                             'study. \n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Pseudomonas fluorescens; '
                                                      'Bacillus subtilis; Pseudomonas '
                                                      'simiae WCS 417'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Pseudomonas fluorescens'}]} })
    target_organism_group: Optional[List[str]] = Field(default=None, description="""\"A high-level description of organisms, including microbes, targeted in the experiment.\"""", json_schema_extra = { "linkml_meta": {'alias': 'target_organism_group',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a semicolon-delimited list of '
                                             'groups of target organisms,\n'
                                             'including microbes, targeted in the '
                                             'study.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Pseudomonas strains; '
                                                      'Pseudomonas group; Roseobacter '
                                                      'clade'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Pseudomonas strains'}]} })
    biological_system: Optional[str] = Field(default=None, description="""Biological system under study.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_system',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the focal biological system '
                                             '(e.g., rhizosphere).'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Root exudates system'}]} })
    conditions: Optional[List[str]] = Field(default=None, description="""Experimental conditions (temperature, pH, etc.).""", json_schema_extra = { "linkml_meta": {'alias': 'conditions',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Identify relevant experimental '
                                             'conditions in a\n'
                                             'semicolon-delimited list (e.g., 25°C; pH '
                                             '7).\n'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'pH 7, 25°C'}]} })
    traits: Optional[List[str]] = Field(default=None, description="""Organismal traits measured or observed.""", json_schema_extra = { "linkml_meta": {'alias': 'traits',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a semicolon-delimited list of '
                                             'traits\n'
                                             'measured or observed in the '
                                             'experiment.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Growth rate; Lactose '
                                                      'production; motility'}},
         'domain_of': ['Paper', 'Experiment']} })
    experimental_factors: Optional[List[str]] = Field(default=None, description="""Factors tested or measured.""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_factors',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'List experimental factors or treatments\n'
                                             'in a semicolon-delimited list.\n'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Root exudates presence vs. absence'}]} })
    is_biolog_experiment: Optional[FlexibleBooleanEnum] = Field(default=None, description="""Whether the experiment is a Biolog experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'is_biolog_experiment',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "Indicate if it's a Biolog experiment "
                                             "('yes' or 'no').\n"
                                             "If not stated, 'not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'yes'}, {'value': 'no'}]} })
    type_of_biolog_experiment: Optional[str] = Field(default=None, description="""Type or subtype of the Biolog experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'type_of_biolog_experiment',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'If it is a Biolog experiment, specify '
                                             'the subtype (e.g., Phenotype '
                                             'MicroArray).\n'
                                             "Otherwise, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Phenotype MicroArray'}]} })
    plates: Optional[List[str]] = Field(default=None, description="""Biolog plates used (e.g., EcoPlate, GEN III, PM01, PM02A).""", json_schema_extra = { "linkml_meta": {'alias': 'plates',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the name(s) of any Biolog '
                                             'plates\n'
                                             '(e.g., PM01, PM02A) in a '
                                             'semicolon-delimited list.\n'
                                             "If not mentioned, 'Not provided'.\n"},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'PM01; PM02A'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'PM01'}, {'value': 'PM02A'}]} })
    replicates: Optional[str] = Field(default=None, description="""Number of replicates.""", json_schema_extra = { "linkml_meta": {'alias': 'replicates',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the number of replicates as a '
                                             'single number.\n'
                                             "If not mentioned, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '3'}]} })
    protocol_steps: Optional[List[str]] = Field(default=None, description="""Key steps in the experimental protocol.""", json_schema_extra = { "linkml_meta": {'alias': 'protocol_steps',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'List the full protocol steps or key '
                                             'experimental procedures,\n'
                                             'including inoculation details, '
                                             'incubation times/temperatures,\n'
                                             'data recording intervals, and data '
                                             'analysis steps.\n'
                                             'This should be a semicolon-delimited '
                                             'list.\n'
                                             'Do not include newlines.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '1) Grow cells overnight on LB '
                                                      'agar; 2) Harvest and suspend in '
                                                      'IF-0'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '1) Grow cells overnight on LB agar   2) Harvest and '
                                'suspend in IF-0   3) Adjust transmittance to 42% '
                                'using a turbidimeter   4) Mix suspension to final '
                                'transmittance of 85%   5) Inoculate PM01 and PM02A '
                                'plates   6) Incubate in OmniLog at 25°C for 48 h   7) '
                                'Record formazan formation every 15 min   8) Data '
                                'analysis with OmniLog Parametric Analysis '
                                'software\n'}]} })
    plate_reader_types_of_data_collected: Optional[List[str]] = Field(default=None, description="""Data types collected (OD, respiration, formazan formation, etc.).""", json_schema_extra = { "linkml_meta": {'alias': 'plate_reader_types_of_data_collected',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Identify data types measured by the '
                                             'plate reader\n'
                                             '(e.g. formazan, OD) in a semi-colon '
                                             'delimited list.\n'
                                             "If none, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Formazan production, recorded by OmniLog system'}]} })
    od_protocol: Optional[str] = Field(default=None, description="""Protocol for measuring optical density.""", json_schema_extra = { "linkml_meta": {'alias': 'od_protocol',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe OD measurement protocol (if '
                                             'relevant).\n'
                                             "If not described, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'OD600 measured every 2 hours'}]} })
    respiration_protocol: Optional[str] = Field(default=None, description="""Protocol for measuring respiration or related metabolic activity.""", json_schema_extra = { "linkml_meta": {'alias': 'respiration_protocol',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe the respiration or metabolic '
                                             'activity measurement protocol (e.g. '
                                             'formazan production).\n'
                                             "If none, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Colorimetric change at 590 nm for formazan '
                                'detection'}]} })
    instrument_used: Optional[List[str]] = Field(default=None, description="""Instrument or equipment used for the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_used',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the name(s) of the '
                                             'instrument/equipment used\n'
                                             '(e.g., OmniLog system) in a '
                                             'semicolon-delimited list.\n'
                                             "If none, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'OmniLog Phenotype MicroArray System (Biolog)'}]} })
    analysis_software: Optional[List[str]] = Field(default=None, description="""Software used to analyze or interpret data.""", json_schema_extra = { "linkml_meta": {'alias': 'analysis_software',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract any software or platforms used '
                                             'for data analysis\n'
                                             'in a semicolon-delimited list.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'OmniLog Parametric Analysis '
                                                      'software v1.20.02'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'OmniLog Parametric Analysis software v1.20.02 '
                                '(Biolog)'}]} })
    incubation_temperature: Optional[str] = Field(default=None, description="""Temperature used for incubating the plates or cultures.""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the incubation temperature if '
                                             'provided (e.g. 25°C).\n'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '25°C'}]} })
    incubation_duration: Optional[str] = Field(default=None, description="""Total duration of incubation (e.g., 48 h).""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract how long the incubation lasted '
                                             '(e.g. 48 hours).\n'}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '48 h'}]} })


class Host(NamedEntity):
    """
    Detail of a host organism or system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of the host organism or system.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the host organism or '
                                             'system.\n'}},
         'domain_of': ['Host', 'Microbe', 'MicrobeGroup'],
         'examples': [{'value': 'B. distachyon'}]} })
    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
        return v


class Microbe(NamedEntity):
    """
    Information about a microbial species or strain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of a microbial taxon.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the microbial species or '
                                             'strain.\n'}},
         'domain_of': ['Host', 'Microbe', 'MicrobeGroup'],
         'examples': [{'value': 'Pseudomonas fluorescens'}]} })
    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
        return v


class MicrobeGroup(NamedEntity):
    """
    Information about a microbial group or taxon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of a microbial group or taxon.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the microbial group.\n'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Pseudomonas strains'}},
         'domain_of': ['Host', 'Microbe', 'MicrobeGroup'],
         'examples': [{'value': 'Pseudomonas strains'}]} })
    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
        return v


class ExperimentalFactor(NamedEntity):
    """
    A factor manipulated or measured in an experiment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    placeholder_attribute: Optional[str] = Field(default=None, description="""Placeholder attribute for ExperimentalFactor.""", json_schema_extra = { "linkml_meta": {'alias': 'placeholder_attribute',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract details about this experimental '
                                             'factor (e.g. concentration).\n'
                                             "If absent, 'Not provided'.\n"}},
         'domain_of': ['ExperimentalFactor'],
         'examples': [{'value': 'Root exudates concentration'}]} })
    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
        return v


class Trait(NamedEntity):
    """
    An organism's physical trait measured or observed in an experiment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'bioportal:metpo'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'A physical trait of an organism measured '
                                             'or observed in the study.\n'}},
         'from_schema': 'https://example.org/PaperExtractionSchema',
         'id_prefixes': ['https']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'Experiment'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid original_spans format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid original_spans format: {v}")
        return v


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
Paper.model_rebuild()
Experiment.model_rebuild()
Host.model_rebuild()
Microbe.model_rebuild()
MicrobeGroup.model_rebuild()
ExperimentalFactor.model_rebuild()
Trait.model_rebuild()

