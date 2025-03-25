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


linkml_meta = LinkMLMeta({'default_prefix': 'microex',
     'default_range': 'string',
     'description': 'A more sophisticated schema for extracting structured data '
                    'about microbial liquid culturing media and growth conditions '
                    'from research articles.\n',
     'id': 'https://example.org/MicrobialCulturingExtraction',
     'imports': ['linkml:types', 'core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'MicrobialCulturingExtraction',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'microex': {'prefix_prefix': 'microex',
                              'prefix_reference': 'https://example.org/MicrobialCulturingExtraction/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}},
     'source_file': 'src/ontogpt/templates/growth_experiment.yaml',
     'title': 'Microbial Culturing Extraction Schema'} )

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
         'domain_of': ['NamedEntity', 'Medium'],
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
         'domain_of': ['NamedEntity', 'Medium'],
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


class MicrobialCulturing(ConfiguredBaseModel):
    """
    Container for microbial culturing information extracted from text.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/MicrobialCulturingExtraction',
         'tree_root': True})

    media: Optional[List[Medium]] = Field(default=None, description="""One or more culture media used in the study.""", json_schema_extra = { "linkml_meta": {'alias': 'media',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Summarize each distinct culture medium '
                                             'described in the text. Separate multiple '
                                             'summaries with semicolons. For each, '
                                             'include the main name or code, '
                                             'ingredients, any modifications, and '
                                             'preparation steps. Do not include '
                                             'newlines or numbering.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Blood agar (BA), made from 0.5% '
                                                      'Peptone, 0.3% beef '
                                                      'extract/yeast extract, 1.5% '
                                                      'agar, 0.5% NaCl, and distilled '
                                                      'water; M9 minimal medium'}},
         'domain_of': ['MicrobialCulturing']} })
    growth_experiments: Optional[List[GrowthExperiment]] = Field(default=None, description="""One or more growth experiments or conditions described in the study.""", json_schema_extra = { "linkml_meta": {'alias': 'growth_experiments',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Summarize each distinct growth '
                                             'experiment or set of conditions. '
                                             'Separate all summaries in a '
                                             'semicolon-delimited list with no '
                                             'numbering and no newlines. For each, '
                                             'include temperature, salinity, pH, '
                                             'oxygen status, sparging equipment, '
                                             'inoculation method, mixing method, '
                                             'culturing duration, light method (if '
                                             'relevant), and any other methods or '
                                             'conditions.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Aerobic growth at 30°C; '
                                                      'Anaerobic growth in sealed '
                                                      'flasks at 37°C'}},
         'domain_of': ['MicrobialCulturing']} })


class Medium(ConfiguredBaseModel):
    """
    Details about a liquid culturing medium.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/MicrobialCulturingExtraction'})

    identifier: Optional[str] = Field(default=None, description="""A name or code used to identify the medium (e.g., LB, M9, etc.).""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the main name or code for this '
                                             'medium.'}},
         'domain_of': ['Medium', 'GrowthExperiment'],
         'examples': [{'value': 'LB'}]} })
    label: Optional[str] = Field(default=None, description="""A human-readable label or short name for the medium.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide the full or commonly used label '
                                             'for the medium.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Lysogeny Broth'}},
         'domain_of': ['NamedEntity', 'Medium'],
         'examples': [{'value': 'Lysogeny Broth'}]} })
    ingredients: Optional[List[str]] = Field(default=None, description="""Ingredients of the medium, including chemical compounds and concentrations.""", json_schema_extra = { "linkml_meta": {'alias': 'ingredients',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide all ingredients used in the '
                                             'medium, including concentrations where '
                                             'specified. If multiple ingredients, '
                                             'separate them with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Tryptone 10 g/L; Yeast Extract '
                                                      '5 g/L; NaCl 10 g/L'}},
         'domain_of': ['Medium'],
         'examples': [{'value': 'Tryptone 10 g/L, Yeast Extract 5 g/L, NaCl 10 g/L'}]} })
    modifications: Optional[List[str]] = Field(default=None, description="""Any modifications or special additives to the standard medium recipe.""", json_schema_extra = { "linkml_meta": {'alias': 'modifications',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe any deviations from the '
                                             'standard recipe. If multiple '
                                             'modifications, separate them with '
                                             'semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Extra glucose; Reduced NaCl'}},
         'domain_of': ['Medium'],
         'examples': [{'value': 'Adjusted NaCl to 5 g/L; Added 2 g/L glucose'}]} })
    preparation_steps: Optional[List[str]] = Field(default=None, description="""Description of how the medium is prepared.""", json_schema_extra = { "linkml_meta": {'alias': 'preparation_steps',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Outline the preparation steps for the '
                                             'medium, including sterilization, pH '
                                             'adjustment, or other relevant details. '
                                             'If multiple steps, separate them with '
                                             'semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Autoclave at 121°C for 15 '
                                                      'minutes; Adjust pH to 7.0'}},
         'domain_of': ['Medium'],
         'examples': [{'value': 'Sterilized by autoclaving at 121°C for 15 minutes; pH '
                                'adjusted to 7.0'}]} })


class GrowthExperiment(ConfiguredBaseModel):
    """
    Growth conditions and experimental methods for culturing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/MicrobialCulturingExtraction'})

    identifier: Optional[str] = Field(default=None, description="""A unique identifier for the growth experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide a unique identifier for this '
                                             'growth experiment. This may be a summary '
                                             'of the experiment in a few words.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Aerobic growth of '
                                                      'Staphylococcus aureus'}},
         'domain_of': ['Medium', 'GrowthExperiment']} })
    temperature: Optional[List[str]] = Field(default=None, description="""Temperature(s) at which the culture is grown (e.g., in Celsius).""", json_schema_extra = { "linkml_meta": {'alias': 'temperature',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Specify the growth temperature(s). If '
                                             'multiple, separate with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '30°C; 37°C'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': '30°C'}]} })
    salinity: Optional[List[str]] = Field(default=None, description="""Salinity or salt concentration conditions (e.g., % NaCl).""", json_schema_extra = { "linkml_meta": {'alias': 'salinity',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide salinity or salt concentration '
                                             'if given. If multiple or a range, '
                                             'separate with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '3% NaCl; 2 M NaCl'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': '3% NaCl'}]} })
    pH: Optional[List[str]] = Field(default=None, description="""pH level at which the culture is maintained.""", json_schema_extra = { "linkml_meta": {'alias': 'pH',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide the pH level for the culture '
                                             '(e.g., pH 7.0). If multiple or a range, '
                                             'separate with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'pH 7.2'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'pH 7.0'}]} })
    oxygen_status: Optional[List[str]] = Field(default=None, description="""Oxygen conditions (e.g., aerobic, anaerobic, microaerophilic).""", json_schema_extra = { "linkml_meta": {'alias': 'oxygen_status',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Indicate whether the culture is aerobic, '
                                             'anaerobic, microaerophilic, or specify '
                                             'an oxygen concentration or partial '
                                             'pressure. If multiple, separate with '
                                             'semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Aerobic; Microaerophilic; ~5% '
                                                      'O2'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'Aerobic'}, {'value': 'Anaerobic'}]} })
    sparging_equipment: Optional[List[str]] = Field(default=None, description="""Equipment or method used for sparging or aeration (if any).""", json_schema_extra = { "linkml_meta": {'alias': 'sparging_equipment',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide details on aeration equipment or '
                                             'methods. Include flow rate, filter size, '
                                             'or other relevant information. If '
                                             'multiple, separate with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Air sparger at 1 L/min'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'Air sparger with 0.2 μm filter at 1 L/min'}]} })
    inoculation_method: Optional[List[str]] = Field(default=None, description="""Method(s) used to inoculate the culture (e.g., inoculum source or process).""", json_schema_extra = { "linkml_meta": {'alias': 'inoculation_method',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe how the culture was inoculated, '
                                             'including inoculum origin and technique. '
                                             'If multiple methods, separate with '
                                             'semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Single colony from LB agar '
                                                      'plate; 1% v/v seed culture'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'Inoculated with a single colony from a streak plate'}]} })
    mixing_method: Optional[List[str]] = Field(default=None, description="""Method of agitation or mixing (e.g., stirring speed, shaker, etc.).""", json_schema_extra = { "linkml_meta": {'alias': 'mixing_method',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide details on how the culture was '
                                             'mixed, if at all. If multiple methods, '
                                             'separate with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '200 rpm on orbital shaker'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'Shaken at 200 rpm on an orbital shaker'}]} })
    culturing_duration: Optional[List[str]] = Field(default=None, description="""Duration of the culture growth or experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'culturing_duration',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'State how long the culture was grown or '
                                             'observed. Include time units (e.g., 24 '
                                             'h, 48 h). If multiple durations, '
                                             'separate with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '24 h; 48 h'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': '24 hours'}, {'value': '48 h'}]} })
    light_method: Optional[List[str]] = Field(default=None, description="""Type or intensity of light provided (if relevant) for phototrophic organisms.""", json_schema_extra = { "linkml_meta": {'alias': 'light_method',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide the type of lighting (e.g., '
                                             'wavelength, intensity) or indicate dark '
                                             'conditions if relevant. If multiple '
                                             'light conditions, separate with '
                                             'semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Continuous white light at 50 '
                                                      'μmol photons m⁻² s⁻¹'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'Continuous light at 50 μmol photons m⁻² s⁻¹'}]} })
    other_methods: Optional[List[str]] = Field(default=None, description="""Any other relevant growth or handling methods not captured above.""", json_schema_extra = { "linkml_meta": {'alias': 'other_methods',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe any additional methods or '
                                             'conditions (e.g., special additives, '
                                             'pressure). If multiple methods, separate '
                                             'with semicolons.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '10% CO2 atmosphere; High '
                                                      'pressure environment'}},
         'domain_of': ['GrowthExperiment'],
         'examples': [{'value': 'Maintained under 1 atm CO2; Pressure of 10 MPa'}]} })


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
MicrobialCulturing.model_rebuild()
Medium.model_rebuild()
GrowthExperiment.model_rebuild()

