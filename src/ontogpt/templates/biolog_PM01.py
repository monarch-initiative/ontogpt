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
version = "0.4.3"


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


linkml_meta = LinkMLMeta({'default_prefix': 'paperex',
     'default_range': 'string',
     'description': 'Structured extraction for Biolog Phenotype MicroArray '
                    'experiments.',
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
     'source_file': '/Users/marcin/Documents/VIMSS/ontology/LLMs/ontogpt/src/ontogpt/templates/biolog_PM01.yaml',
     'title': 'Paper Extraction Schema'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class FlexibleBooleanEnum(str, Enum):
    """
    yes/no in lowercase; 'not provided' if ambiguous.
    """
    yes = "yes"
    no = "no"
    true = "true"
    false = "false"
    not_provided = "not provided"


class PlateEnum(str, Enum):
    """
    Biolog Phenotype MicroArray plates.
    """
    PM01 = "PM01"
    PM02 = "PM02"
    PM1 = "PM1"


class PMResultEnum(str, Enum):
    """
    Result for a single well.
    """
    positive = "positive"
    negative = "negative"
    undetermined = "undetermined"
    not_provided = "not provided"


class GroupResultEnum(str, Enum):
    """
    Utilisation level for a compound cluster.
    """
    high = "high"
    variable = "variable"
    none = "none"
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
    named_entities: Optional[list[Any]] = Field(default=None, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'named_entities', 'domain_of': ['ExtractionResult']} })


class NamedEntity(ConfiguredBaseModel):
    """
    Minimal base for all named entities in this schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })


class CompoundExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    pass


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    subject: Optional[NamedEntity] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['Triple']} })
    predicate: Optional[RelationshipType] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['Triple']} })
    object: Optional[NamedEntity] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object', 'domain_of': ['Triple']} })
    qualifier: Optional[str] = Field(default=None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""", json_schema_extra = { "linkml_meta": {'alias': 'qualifier', 'domain_of': ['Triple']} })
    subject_qualifier: Optional[NamedEntity] = Field(default=None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""", json_schema_extra = { "linkml_meta": {'alias': 'subject_qualifier', 'domain_of': ['Triple']} })
    object_qualifier: Optional[NamedEntity] = Field(default=None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""", json_schema_extra = { "linkml_meta": {'alias': 'object_qualifier', 'domain_of': ['Triple']} })


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
    entities: Optional[list[NamedEntity]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'entities', 'domain_of': ['TextWithEntity']} })


class RelationshipType(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core',
         'id_prefixes': ['RO', 'biolink']})

    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })


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
    One publication that includes ≥ 1 Biolog assay.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema', 'tree_root': True})

    study_title: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'study_title',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'extract the paper title; if absent, use '
                                             "'not provided'."}},
         'domain_of': ['Paper']} })
    authors: list[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'authors',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'extract authors as a semicolon-separated '
                                             "list; if none, 'not provided'."}},
         'domain_of': ['Paper']} })
    doi: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "extract the DOI or 'not provided'."}},
         'domain_of': ['Paper']} })
    date: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'date',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "extract the publication date (e.g., '14 "
                                             "April 2021') or 'not provided'."}},
         'domain_of': ['Paper']} })
    biolog_experiments: Optional[list[BiologExperiment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'biolog_experiments',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'if the paper describes any Biolog '
                                             'Phenotype MicroArray assays,\n'
                                             'create one BiologExperiment object per '
                                             'plate (PM01, PM02 …);\n'
                                             'otherwise omit this slot.\n'}},
         'domain_of': ['Paper']} })
    experiments: Optional[list[Experiment]] = Field(default=None, description="""Experiments described in the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'experiments',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a list of brief descriptions of '
                                             'experiments described in the paper. This '
                                             'list must be semicolon-delimited. For '
                                             'each description, include all of the '
                                             'following details if provided: '
                                             'experiment motivation (why it was '
                                             'performed), experiment design (how it '
                                             'was performed, including methods, tools, '
                                             'organisms, and chemicals used), '
                                             'environment (the location and conditions '
                                             'in which the experiment occurred, '
                                             'including metrics like temperature), all '
                                             'organisms used and their high-level type '
                                             '(e.g., plant, animal), the biological '
                                             'system under study (e.g., rhizosphere), '
                                             'experimental conditions (temperature, '
                                             'pH, etc.), and experimental factors '
                                             'tested or measured. Also note whether '
                                             'the experiment is a Biolog experiment '
                                             'and if so, the type or subtype of '
                                             'experiment (e.g., Phenotype MicroArray), '
                                             'the Biolog plates used (e.g., PM01), the '
                                             'number of replicates, all key steps in '
                                             'the experimental protocol, the types of '
                                             'data collected by the plate reader '
                                             '(e.g., OD, respiration), the protocol '
                                             'for measuring optical density (e.g., '
                                             'OD600 measured every 2 hours),  the '
                                             'protocol for measuring respiration '
                                             '(e.g., Colorimetric change at 590 nm for '
                                             'formazan detection), the instrument or '
                                             'equipment used (e.g., OmniLog Phenotype '
                                             'MicroArray System), the software used '
                                             'for data analysis (e.g., OmniLog '
                                             'Parametric Analysis software), the '
                                             'incubation temperature (e.g., 25°C), the '
                                             'total duration of incubation (e.g., 48 '
                                             'h), and any other relevant details. If '
                                             'nothing is mentioned regarding '
                                             "experiments, use 'Not provided'. Do not "
                                             'provide any details here not related to '
                                             'experiments. Do not include newlines.'}},
         'domain_of': ['Paper']} })


class Experiment(ConfiguredBaseModel):
    """
    A single experiment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    label: Optional[str] = Field(default=None, description="""One-sentence description of this experiment.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Provide a one-sentence description of '
                                             'the experiment.'}},
         'domain_of': ['Experiment']} })
    pm01_strain_results: Optional[list[BiologPM01StrainResult]] = Field(default=None, description="""PM01 results grouped by strain.""", json_schema_extra = { "linkml_meta": {'alias': 'pm01_strain_results',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'If Biolog PM01 results are described, '
                                             'provide a semicolon-delimited list of\n'
                                             'all strains tested. For each strain, '
                                             'include the following details:\n'
                                             'the strain name, the utilization cluster '
                                             'it belongs to (I, II, or III), and a '
                                             'complete list of all wells\n'
                                             'mentioned in the text. For each well, '
                                             'include the chemical name and the result '
                                             '(positive,\n'
                                             'negative, or not provided). Do not leave '
                                             'out any wells that the text says were '
                                             'catabolized\n'
                                             '(positive) or not (negative). If no PM01 '
                                             'results are mentioned, do not provide\n'
                                             'a value for this field.\n'}},
         'domain_of': ['Experiment']} })


class BiologPM01StrainResult(ConfiguredBaseModel):
    """
    PM01 well-level results for a specific strain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    tested_strain: Optional[Microbe] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tested_strain', 'domain_of': ['BiologPM01StrainResult']} })


class BiologExperiment(ConfiguredBaseModel):
    """
    Details for one Phenotype MicroArray plate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    plate_name: Optional[PlateEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'plate_name',
         'annotations': {'examples': {'tag': 'examples', 'value': 'PM01'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'plate identifier (e.g., PM01, PM02); '
                                             'default to PM01 if unclear.'}},
         'domain_of': ['BiologExperiment']} })
    summary_by_group: Optional[list[PMUtilisationGroup]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'summary_by_group',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'optional coarse summary: for each '
                                             'utilisation group (I, II, III …)\n'
                                             'give its level (high/variable/none) and '
                                             'any compounds explicitly\n'
                                             'named in that paragraph. omit if not '
                                             'described.\n'}},
         'domain_of': ['BiologExperiment']} })
    strain_results: Optional[list[StrainResult]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'strain_results',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'for each microbial strain tested on this '
                                             'plate, create one\n'
                                             'StrainResult capturing organism, host, '
                                             'strain name, strain cluster\n'
                                             '(if stated), and every well-level result '
                                             'mentioned.\n'}},
         'domain_of': ['BiologExperiment']} })


class StrainResult(ConfiguredBaseModel):
    """
    Results for one microbial strain on a plate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    organism: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'organism',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "species name (e.g., 'Pseudomonas "
                                             "fluorescens') or 'not provided'."}},
         'domain_of': ['StrainResult']} })
    host: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'host',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "host organism or environment (e.g., 'B. "
                                             "distachyon Bd21 root');\n"
                                             "if none, 'not provided'.\n"}},
         'domain_of': ['StrainResult']} })
    strain_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'strain_name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "exact strain identifier (e.g., 'Pf-5', "
                                             "'Q8r1-96')."}},
         'domain_of': ['StrainResult']} })
    strain_group: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'strain_group',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'phylogenetic or utilisation cluster the '
                                             'strain belongs to\n'
                                             "(e.g., 'cluster I', 'P. fluorescens "
                                             "subgroup 3');\n"
                                             "if none, 'not provided'.\n"}},
         'domain_of': ['StrainResult']} })
    well_results: Optional[list[WellResult]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'well_results',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'list every chemical explicitly stated as '
                                             'catabolised (positive),\n'
                                             'not catabolised (negative), or ambiguous '
                                             '(undetermined) for\n'
                                             'this strain.\n'}},
         'domain_of': ['StrainResult']} })


class WellResult(ConfiguredBaseModel):
    """
    Outcome for one chemical well.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    chemical_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'chemical_name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'chemical exactly as written (e.g., '
                                             "'citric acid')."}},
         'domain_of': ['WellResult']} })
    result: PMResultEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'result',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'choose one: positive / negative / '
                                             'undetermined / not provided.\n'
                                             "map phrases like 'supported growth' → "
                                             'positive;\n'
                                             "'not catabolized' → negative.\n"}},
         'domain_of': ['WellResult']} })


class PMUtilisationGroup(ConfiguredBaseModel):
    """
    High-level cluster summary (optional).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    group_label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'group_label',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'group label as in text (I, II, III …).'}},
         'domain_of': ['PMUtilisationGroup']} })
    utilisation_level: Optional[GroupResultEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'utilisation_level',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'high / variable / none / not provided.'}},
         'domain_of': ['PMUtilisationGroup']} })
    compounds: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'compounds',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'list every compound explicitly mentioned '
                                             'for this utilisation group;\n'
                                             'if none, leave the list empty.\n'}},
         'domain_of': ['PMUtilisationGroup']} })


class Microbe(NamedEntity):
    """
    A microbial species or strain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""The name of the microbe.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the microbe name (e.g., '
                                             'Pseudomonas fluorescens).'}},
         'domain_of': ['Microbe', 'Host']} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })


class Host(NamedEntity):
    """
    A host organism or system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of the host organism.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the host name, e.g., '
                                             'Brachypodium distachyon.'}},
         'domain_of': ['Microbe', 'Host']} })
    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })


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
BiologPM01StrainResult.model_rebuild()
BiologExperiment.model_rebuild()
StrainResult.model_rebuild()
WellResult.model_rebuild()
PMUtilisationGroup.model_rebuild()
Microbe.model_rebuild()
Host.model_rebuild()
