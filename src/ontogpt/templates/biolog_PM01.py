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
version = "0.2.0"


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
                    'Biolog Phenotype MicroArray experiments. Extended to capture '
                    'PM01 well-level results.',
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
     'source_file': 'src/ontogpt/templates/biolog_PM01.yaml',
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


class PlateEnum(str, Enum):
    """
    Biolog phenotype microarray plates.
    """
    PM01 = "PM01"
    PM1 = "PM1"


class PM01ResultEnum(str, Enum):
    """
    Whether a PM01 well was positive, negative, or not provided.

    """
    positive = "positive"
    negative = "negative"
    not_provided = "not provided"


class PM01ChemicalEnum(str, Enum):
    """
    Known chemicals in Biolog PM01 (free-text fallback allowed).

    """
    L_Arabinose = "L-Arabinose"
    N_Acetyl_D_Glucosamine = "N-Acetyl-D-Glucosamine"
    D_Saccharic_acid = "D-Saccharic acid"
    Succinic_acid = "Succinic acid"
    D_Galactose = "D-Galactose"
    L_Aspartic_acid = "L-Aspartic acid"
    L_Proline = "L-Proline"
    D_Alanine = "D-Alanine"
    D_Trehalose = "D-Trehalose"
    D_Mannose = "D-Mannose"
    Dulcitol = "Dulcitol"
    D_Serine = "D-Serine"
    D_Sorbitol = "D-Sorbitol"
    Glycerol = "Glycerol"
    L_Fucose = "L-Fucose"
    D_Glucuronic_acid = "D-Glucuronic acid"
    D_Gluconic_acid = "D-Gluconic acid"
    DL_a_Glycerol_Phosphate = "DL-a-Glycerol Phosphate"
    D_Xylose = "D-Xylose"
    L_Lactic_acid = "L-Lactic acid"
    Formic_acid = "Formic acid"
    D_Mannitol = "D-Mannitol"
    L_Glutamic_acid = "L-Glutamic acid"
    D_Glucose_6_Phosphate = "D-Glucose-6-Phosphate"
    D_Galactonic_acid_g_Lactone = "D-Galactonic acid-g-Lactone"
    DL_Malic_acid = "DL-Malic acid"
    D_Ribose = "D-Ribose"
    Tween_20 = "Tween 20"
    L_Rhamnose = "L-Rhamnose"
    D_Fructose = "D-Fructose"
    Acetic_acid = "Acetic acid"
    a_D_Glucose = "a-D-Glucose"
    Maltose = "Maltose"
    D_Melibiose = "D-Melibiose"
    Thymidine = "Thymidine"
    L_Asparagine = "L-Asparagine"
    D_Aspartic_acid = "D-Aspartic acid"
    D_Glucosaminic_acid = "D-Glucosaminic acid"
    number_12_Propanediol = "1,2-Propanediol"
    Tween_40 = "Tween 40"
    a_Ketoglutaric_acid = "a-Ketoglutaric acid"
    a_Ketobutyric_acid = "a-Ketobutyric acid"
    a_Methyl_D_Galactoside = "a-Methyl-D-Galactoside"
    a_D_Lactose = "a-D-Lactose"
    Lactulose = "Lactulose"
    Sucrose = "Sucrose"
    Uridine = "Uridine"
    L_Glutamine = "L-Glutamine"
    m_Tartaric_acid = "m-Tartaric acid"
    D_Glucose_1_Phosphate = "D-Glucose-1-Phosphate"
    D_Fructose_6_Phosphate = "D-Fructose-6-Phosphate"
    Tween_80 = "Tween 80"
    a_Hydroxyglutaric_acid_g_Lactone = "a-Hydroxyglutaric acid-g-Lactone"
    a_Hydroxybutyric_acid = "a-Hydroxybutyric acid"
    b_Methyl_D_Glucoside = "b-Methyl-D-Glucoside"
    Adonitol = "Adonitol"
    Maltotriose = "Maltotriose"
    number_2GRAVE_ACCENT_Deoxyadenosine = "2`-Deoxyadenosine"
    Adenosine = "Adenosine"
    Gly_Asp = "Gly-Asp"
    Citric_acid = "Citric acid"
    m_Inositol = "m-Inositol"
    D_Threonine = "D-Threonine"
    Fumaric_acid = "Fumaric acid"
    Bromosuccinic_acid = "Bromosuccinic acid"
    Propionic_acid = "Propionic acid"
    Mucic_acid = "Mucic acid"
    Glycolic_acid = "Glycolic acid"
    Glyoxylic_acid = "Glyoxylic acid"
    D_Cellobiose = "D-Cellobiose"
    Inosine = "Inosine"
    Gly_Glu = "Gly-Glu"
    Tricarballylic_acid = "Tricarballylic acid"
    L_Serine = "L-Serine"
    L_Threonine = "L-Threonine"
    L_Alanine = "L-Alanine"
    Ala_Gly = "Ala-Gly"
    Acetoacetic_acid = "Acetoacetic acid"
    N_Acetyl_D_Mannosamine = "N-Acetyl-D-Mannosamine"
    Mono_Methylsuccinate = "Mono-Methylsuccinate"
    Methylpyruvate = "Methylpyruvate"
    D_Malic_acid = "D-Malic acid"
    L_Malic_acid = "L-Malic acid"
    Gly_Pro = "Gly-Pro"
    p_Hydroxyphenyl_Acetic_acid = "p-Hydroxyphenyl Acetic acid"
    m_Hydroxyphenyl_Acetic_acid = "m-Hydroxyphenyl Acetic acid"
    Tyramine = "Tyramine"
    D_Psicose = "D-Psicose"
    L_Lyxose = "L-Lyxose"
    Glucuronamide = "Glucuronamide"
    Pyruvic_acid = "Pyruvic acid"
    L_Galactonic_acid_g_Lactone = "L-Galactonic acid-g-Lactone"
    D_Galacturonic_acid = "D-Galacturonic acid"
    Phenylethylamine = "Phenylethylamine"
    number_2_Aminoethanol = "2-Aminoethanol"



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
                                             "return 'Not provided'."}},
         'domain_of': ['Paper']} })
    authors: List[str] = Field(default=..., description="""Authors of the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'authors',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract authors as a semicolon-delimited '
                                             "list. If missing, 'Not provided'."}},
         'domain_of': ['Paper']} })
    doi: Optional[str] = Field(default=None, description="""DOI of the publication.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': "Extract the DOI. If not found, 'Not "
                                             "provided'."}},
         'domain_of': ['Paper']} })
    date: Optional[str] = Field(default=None, description="""Publication date.""", json_schema_extra = { "linkml_meta": {'alias': 'date',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the publication date. If not '
                                             "found, 'Not provided'."}},
         'domain_of': ['Paper']} })
    traits: Optional[List[str]] = Field(default=None, description="""Organismal traits measured or observed.""", json_schema_extra = { "linkml_meta": {'alias': 'traits',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract a semicolon-delimited list of '
                                             'traits focused on in the study.'}},
         'domain_of': ['Paper']} })
    experiments: Optional[List[Experiment]] = Field(default=None, description="""Experiments described in the paper.""", json_schema_extra = { "linkml_meta": {'alias': 'experiments',
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
         'domain_of': ['NamedEntity', 'Experiment']} })
    pm01_strain_results: Optional[List[BiologPM01StrainResult]] = Field(default=None, description="""PM01 results grouped by strain.""", json_schema_extra = { "linkml_meta": {'alias': 'pm01_strain_results',
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

    tested_strain: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tested_strain',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the strain name. If missing, '
                                             "emit 'Not provided'.\n"},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Pseudomonas sp. R1-43-08'}},
         'domain_of': ['BiologPM01StrainResult']} })
    pm01_well_results: Optional[List[BiologPM01WellResult]] = Field(default=None, description="""Well-level PM01 results.""", json_schema_extra = { "linkml_meta": {'alias': 'pm01_well_results', 'domain_of': ['BiologPM01StrainResult']} })


class BiologPM01WellResult(ConfiguredBaseModel):
    """
    Result for a single well on PM01.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    chemical_name: Optional[PM01ChemicalEnum] = Field(default=None, description="""Name of the chemical tested.""", json_schema_extra = { "linkml_meta": {'alias': 'chemical_name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the chemical tested in this '
                                             'well.\n'
                                             'If no chemical is mentioned or if it’s '
                                             'not in the PM01 enumeration,\n'
                                             'emit exactly "not provided" (do not '
                                             'leave it blank).\n'}},
         'domain_of': ['BiologPM01WellResult']} })
    result: PM01ResultEnum = Field(default=..., description="""Positive, negative, or not provided.""", json_schema_extra = { "linkml_meta": {'alias': 'result', 'domain_of': ['BiologPM01WellResult']} })


class Host(NamedEntity):
    """
    A host organism or system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of the host.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the host name.'}},
         'domain_of': ['Host', 'Microbe', 'MicrobeGroup']} })
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
    A microbial species or strain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of the microbe.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the microbe name.'}},
         'domain_of': ['Host', 'Microbe', 'MicrobeGroup']} })
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
    A group of microbes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    name: Optional[str] = Field(default=None, description="""Name of the microbe group.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Extract the group name.'}},
         'domain_of': ['Host', 'Microbe', 'MicrobeGroup']} })
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
    An experimental factor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    placeholder: Optional[str] = Field(default=None, description="""Details of the factor.""", json_schema_extra = { "linkml_meta": {'alias': 'placeholder',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe the experimental factor.'}},
         'domain_of': ['ExperimentalFactor']} })
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
    A measured trait.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'prompt': {'tag': 'prompt', 'value': 'Extract a trait.'}},
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


class ProtocolStep(ConfiguredBaseModel):
    """
    A step in a protocol.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/PaperExtractionSchema'})

    description: Optional[str] = Field(default=None, description="""Protocol step description.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Describe the protocol step.'}},
         'domain_of': ['ProtocolStep']} })


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
BiologPM01WellResult.model_rebuild()
Host.model_rebuild()
Microbe.model_rebuild()
MicrobeGroup.model_rebuild()
ExperimentalFactor.model_rebuild()
Trait.model_rebuild()
ProtocolStep.model_rebuild()

