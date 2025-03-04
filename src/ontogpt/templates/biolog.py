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
     'imports': ['linkml:types'],
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

class FlexibleBooleanEnum(str, Enum):
    """
    A minimal enumeration for capturing yes/no/true/false in lowercase, plus 'not provided' if data are missing or ambiguous.

    """
    yes = "yes"
    no = "no"
    true = "true"
    false = "false"
    not_provided = "not provided"



class NamedEntity(ConfiguredBaseModel):
    """
    A generic named entity for all non-root classes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    pass


class Paper(ConfiguredBaseModel):
    """
    A single paper or study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema', 'tree_root': True})

    study_title: str = Field(default=..., description="""The paper's title.""", json_schema_extra = { "linkml_meta": {'alias': 'study_title',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "Extract the paper's title. If not found, "
                                             "return 'Not provided'."}},
         'domain_of': ['Paper'],
         'examples': [{'description': 'From Mavrodi et al. 2021',
                       'value': 'Root Exudates Alter the Expression of Diverse '
                                'Metabolic, Transport, Regulatory, and Stress Response '
                                'Genes in Rhizosphere Pseudomonas.'}]} })
    authors: List[Author] = Field(default=..., description="""Authors of the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'authors',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a list of authors (each as a '
                                             'separate entry).\n'
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
    experiments: List[Experiment] = Field(default=..., description="""Experiments (e.g., Biolog) included in the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'experiments',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a list of experiments described '
                                             'in the paper.\n'
                                             "If nothing is mentioned, use 'Not "
                                             "provided'.\n"}},
         'domain_of': ['Paper'],
         'examples': [{'value': 'Biolog Phenotype MicroArray; RNA-seq for gene '
                                'expression'}]} })


class Author(NamedEntity):
    """
    An author of the paper.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: str = Field(default=..., description="""Name of the author.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the full name of this author. If '
                                             "none, return 'Not provided'."}},
         'domain_of': ['Author'],
         'examples': [{'value': 'Olga V. Mavrodi'}]} })


class Experiment(NamedEntity):
    """
    A single experiment from the paper.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

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
                                    'value': 'Extract the environment or setting. If '
                                             "none, 'Not provided'."}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Lab-based assay under 25°C'}]} })
    host: Optional[List[Host]] = Field(default=None, description="""One or more hosts in the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'host',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Identify the host organisms or systems '
                                             'used.\n'
                                             "If not mentioned, use 'Not "
                                             "provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Brachypodium distachyon'}]} })
    host_type: Optional[str] = Field(default=None, description="""Type of host (e.g., plant, animal).""", json_schema_extra = { "linkml_meta": {'alias': 'host_type',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe the host type if applicable '
                                             "(e.g. 'plant'). If nothing specified, "
                                             "'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Plant'}]} })
    target_microbes: Optional[List[Microbe]] = Field(default=None, description="""Microbes targeted in the experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'target_microbes',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a list of target microbes '
                                             "studied. If none are mentioned, 'Not "
                                             "provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Pseudomonas fluorescens'}]} })
    biological_system: Optional[str] = Field(default=None, description="""Biological system under study.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_system',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the focal biological system '
                                             "(e.g., rhizosphere). If none, 'Not "
                                             "provided'."}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'Root exudates system'}]} })
    conditions: Optional[str] = Field(default=None, description="""Experimental conditions (temperature, pH, etc.).""", json_schema_extra = { "linkml_meta": {'alias': 'conditions',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Identify relevant experimental '
                                             'conditions (e.g., 25°C, pH 7).\n'
                                             "If not stated, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'pH 7, 25°C'}]} })
    experimental_factors: Optional[List[ExperimentalFactor]] = Field(default=None, description="""Factors tested or measured.""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_factors',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'List experimental factors or '
                                             'treatments.\n'
                                             "If no info, 'Not provided'.\n"}},
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
                                    'value': 'Extract the name(s) of any Biolog plates '
                                             '(e.g., PM01, PM02A).\n'
                                             "If not mentioned, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'PM01'}, {'value': 'PM02A'}]} })
    replicates: Optional[str] = Field(default=None, description="""Number of replicates.""", json_schema_extra = { "linkml_meta": {'alias': 'replicates',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the number of replicates.\n'
                                             "If not mentioned, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '3'}]} })
    protocol_steps: Optional[List[str]] = Field(default=None, description="""Key steps in the experimental protocol.""", json_schema_extra = { "linkml_meta": {'alias': 'protocol_steps',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'List the full protocol steps or key '
                                             'experimental procedures, including\n'
                                             'inoculation details, incubation '
                                             'times/temperatures, data recording '
                                             'intervals, etc.\n'
                                             "If not provided, 'Not provided'.\n"}},
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
                                             'plate reader (e.g. formazan, OD).\n'
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
                                             'instrument/equipment used (e.g., OmniLog '
                                             'system).\n'
                                             "If none, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'OmniLog Phenotype MicroArray System (Biolog)'}]} })
    analysis_software: Optional[List[str]] = Field(default=None, description="""Software used to analyze or interpret data.""", json_schema_extra = { "linkml_meta": {'alias': 'analysis_software',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract any software or platform used '
                                             'for data analysis.\n'
                                             "If not mentioned, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': 'OmniLog Parametric Analysis software v1.20.02 '
                                '(Biolog)'}]} })
    incubation_temperature: Optional[str] = Field(default=None, description="""Temperature used for incubating the plates or cultures.""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the incubation temperature if '
                                             'provided (e.g. 25°C).\n'
                                             "If not mentioned, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '25°C'}]} })
    incubation_duration: Optional[str] = Field(default=None, description="""Total duration of incubation (e.g., 48 h).""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract how long the incubation lasted '
                                             '(e.g. 48 hours).\n'
                                             "If not stated, 'Not provided'.\n"}},
         'domain_of': ['Experiment'],
         'examples': [{'value': '48 h'}]} })


class Host(NamedEntity):
    """
    A host organism or system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    placeholder_attribute: Optional[str] = Field(default=None, description="""Placeholder attribute for Host.""", json_schema_extra = { "linkml_meta": {'alias': 'placeholder_attribute',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract details about this host '
                                             '(placeholder).\n'
                                             "If not found, 'Not provided'.\n"}},
         'domain_of': ['Host', 'Microbe', 'ExperimentalFactor'],
         'examples': [{'value': 'Host name: B. distachyon'}]} })


class Microbe(NamedEntity):
    """
    Information about a microbial species or strain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    placeholder_attribute: Optional[str] = Field(default=None, description="""Placeholder attribute for Microbe.""", json_schema_extra = { "linkml_meta": {'alias': 'placeholder_attribute',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract details about this microbe.\n'
                                             "If none, 'Not provided'.\n"}},
         'domain_of': ['Host', 'Microbe', 'ExperimentalFactor'],
         'examples': [{'value': 'Pseudomonas fluorescens'}]} })


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
         'domain_of': ['Host', 'Microbe', 'ExperimentalFactor'],
         'examples': [{'value': 'Root exudates concentration'}]} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
Paper.model_rebuild()
Author.model_rebuild()
Experiment.model_rebuild()
Host.model_rebuild()
Microbe.model_rebuild()
ExperimentalFactor.model_rebuild()

