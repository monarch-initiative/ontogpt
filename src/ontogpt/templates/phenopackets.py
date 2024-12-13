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


linkml_meta = LinkMLMeta({'default_prefix': 'phenopackets_schema',
     'default_range': 'string',
     'description': 'A template for extracting a phenopacket, an anonymous '
                    'phenotypic description of an individual or biosample with '
                    'potential genes of interest and/or diagnoses. This template '
                    'is based on the Phenopackets schema v2, originally defined in '
                    'Protobuf. All classes are defined in a single schema here, '
                    'with their corresponding module provided in a comment (e.g., '
                    'core/individual). Much of this modeling is adapted from Chris '
                    "Mungall's linkml-phenopackets (see "
                    'https://github.com/cmungall/linkml-phenopackets).',
     'id': 'http://w3id.org/ontogpt/phenopackets',
     'imports': ['linkml:types', 'core'],
     'keywords': ['phenotype'],
     'name': 'phenopackets',
     'prefixes': {'ARGO': {'prefix_prefix': 'ARGO',
                           'prefix_reference': 'https://docs.icgc-argo.org/dictionary/'},
                  'EFO': {'prefix_prefix': 'EFO',
                          'prefix_reference': 'http://www.ebi.ac.uk/efo/EFO_'},
                  'GENO': {'prefix_prefix': 'GENO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/GENO_'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'LOINC': {'prefix_prefix': 'LOINC',
                            'prefix_reference': 'https://loinc.org/'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UCUM': {'prefix_prefix': 'UCUM',
                           'prefix_reference': 'http://unitsofmeasure.org/'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'phenopackets_schema': {'prefix_prefix': 'phenopackets_schema',
                                          'prefix_reference': 'http://w3id.org/ontogpt/phenopackets'}},
     'see_also': ['https://github.com/phenopackets/phenopacket-schema',
                  'https://github.com/cmungall/linkml-phenopackets'],
     'source_file': 'src/ontogpt/templates/phenopackets.yaml',
     'title': 'Phenopackets Schema v2'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class AcmgPathogenicityClassification(str, Enum):
    """
    ACMG Pathogenicity Classification of a genetic interpretation. See doi:10.1038/gim.2015.30
    """
    BENIGN = "BENIGN"
    LIKELY_BENIGN = "LIKELY_BENIGN"
    LIKELY_PATHOGENIC = "LIKELY_PATHOGENIC"
    NOT_PROVIDED = "NOT_PROVIDED"
    PATHOGENIC = "PATHOGENIC"
    UNCERTAIN_SIGNIFICANCE = "UNCERTAIN_SIGNIFICANCE"


class InterpretationStatus(str, Enum):
    """
    Status of a genetic interpretation.
    """
    CANDIDATE = "CANDIDATE"
    CAUSATIVE = "CAUSATIVE"
    CONTRIBUTORY = "CONTRIBUTORY"
    REJECTED = "REJECTED"
    UNKNOWN_STATUS = "UNKNOWN_STATUS"


class ProgressStatus(str, Enum):
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    SOLVED = "SOLVED"
    UNKNOWN_PROGRESS = "UNKNOWN_PROGRESS"
    UNSOLVED = "UNSOLVED"


class TherapeuticActionability(str, Enum):
    """
    Therapeutic actionability of an interpretation.
    """
    ACTIONABLE = "ACTIONABLE"
    NOT_ACTIONABLE = "NOT_ACTIONABLE"
    UNKNOWN_ACTIONABILITY = "UNKNOWN_ACTIONABILITY"


class KaryotypicSex(str, Enum):
    """
    Karyotypic sex of the individual
    """
    OTHER_KARYOTYPE = "OTHER_KARYOTYPE"
    UNKNOWN_KARYOTYPE = "UNKNOWN_KARYOTYPE"
    XO = "XO"
    XX = "XX"
    XXX = "XXX"
    XXXX = "XXXX"
    XXXY = "XXXY"
    XXY = "XXY"
    XXYY = "XXYY"
    XY = "XY"
    XYY = "XYY"


class Sex(str, Enum):
    """
    Sex of an individual FHIR mapping: AdministrativeGender (https://www.hl7.org/fhir/codesystem-administrative-gender.html)
    """
    # Female
    FEMALE = "FEMALE"
    # Male
    MALE = "MALE"
    # It is not possible, to accurately assess the applicability of MALE/FEMALE.
    OTHER_SEX = "OTHER_SEX"
    # Not assessed / available.
    UNKNOWN_SEX = "UNKNOWN_SEX"


class Status(str, Enum):
    """
    Default = false i.e. the individual is alive. MUST be true if
    """
    # Alive
    ALIVE = "ALIVE"
    # Deceased
    DECEASED = "DECEASED"
    # Status unknown
    UNKNOWN_STATUS = "UNKNOWN_STATUS"


class DrugType(str, Enum):
    """
    A simplified version of ODHSI-DRUG_EXPOSURE
    """
    ADMINISTRATION_RELATED_TO_PROCEDURE = "ADMINISTRATION_RELATED_TO_PROCEDURE"
    EHR_MEDICATION_LIST = "EHR_MEDICATION_LIST"
    PRESCRIPTION = "PRESCRIPTION"
    UNKNOWN_DRUG_TYPE = "UNKNOWN_DRUG_TYPE"


class RegimenStatus(str, Enum):
    COMPLETED = "COMPLETED"
    DISCONTINUED = "DISCONTINUED"
    STARTED = "STARTED"
    UNKNOWN_STATUS = "UNKNOWN_STATUS"


class AffectedStatus(str, Enum):
    AFFECTED = "AFFECTED"
    MISSING = "MISSING"
    UNAFFECTED = "UNAFFECTED"


class MoleculeContext(str, Enum):
    genomic = "genomic"
    protein = "protein"
    transcript = "transcript"
    unspecified_molecule_context = "unspecified_molecule_context"


class AllelicStateType(str):
    pass


class NCITDiagnosticMarkerType(str):
    pass


class NCITIntentType(str):
    pass


class NCITROAType(str):
    pass


class NCITStagingType(str):
    pass


class NCITTumorGradeType(str):
    pass


class NCITTumorProgressionType(str):
    pass


class SampleStatusType(str):
    pass


class VariantType(str):
    pass



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
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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

    subject: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['Triple', 'Phenopacket']} })
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
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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

    id: Optional[str] = Field(None, description="""The publication identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    title: Optional[str] = Field(None, description="""The title of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Publication']} })
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'abstract', 'domain_of': ['Publication']} })
    combined_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'combined_text', 'domain_of': ['Publication']} })
    full_text: Optional[str] = Field(None, description="""The full text of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'full_text', 'domain_of': ['Publication']} })


class AnnotatorResult(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    subject_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'subject_text', 'domain_of': ['AnnotatorResult']} })
    object_id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'object_id', 'domain_of': ['AnnotatorResult']} })
    object_text: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'object_text', 'domain_of': ['AnnotatorResult']} })


class PhenopacketCollection(ConfiguredBaseModel):
    """
    A collection of phenopackets. Each phenopacket is a phenotypic description of an individual or biosample with potential genes of interest and/or diagnoses. Each phenopacket describes a single individual, experimental animal, or biosample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['This is not part of the Phenopackets Schema.',
                      'It is specific to the OntoGPT implementation.'],
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'tree_root': True})

    phenopackets: Optional[List[Phenopacket]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'phenopackets',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list in which each '
                                             'object of the list includes all details '
                                             'of a single individual, experimental '
                                             'animal, or biosample. Each object should '
                                             'include the full input text, edited to '
                                             'be specific to the individual, animal, '
                                             'or biosample. Each individual should be '
                                             'assigned an identifier following that '
                                             'used in the text, or a unique identifier '
                                             'if one is not provided. Do not use a '
                                             'name or other personally identifying '
                                             'information.'}},
         'domain_of': ['PhenopacketCollection']} })


class Phenopacket(ConfiguredBaseModel):
    """
    An anonymous phenotypic description of an individual or biosample with potential genes of interest and/or diagnoses. This is a bundle of high-level concepts with no specifically defined relational concepts. It is expected that the resources sharing the phenopackets will define and enforce their own semantics and level of requirements for included fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    id: str = Field(..., description="""An identifier specific for this phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'An identifier for the individual person, '
                                             'animal, or sample described in the input '
                                             'text. This must be a unique identifier. '
                                             'Use the same identifier as that used in '
                                             'the text if possible. Otherwise, create '
                                             'a unique identifier such as "Patient 1". '
                                             'Do not use a name or other personally '
                                             'identifying information.'}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    subject: Optional[Individual] = Field(None, description="""The individual representing the focus of this packet - e.g. the proband in rare disease cases or cancer patient""", json_schema_extra = { "linkml_meta": {'alias': 'subject',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A description of the individual '
                                             'representing the focus of this packet. '
                                             'It must include the unique identifier '
                                             'used for the individual. Use the same '
                                             'identifier as that used in the text if '
                                             'possible. Otherwise, create a unique '
                                             'identifier such as "Patient 1". Do not '
                                             'use a name or other personally '
                                             'identifying information. This '
                                             'description must also include any of the '
                                             'following, if provided: the date of '
                                             'birth, gender, sex, karyotypic sex, the '
                                             'time of last encounter, and whether the '
                                             'individual is alive or deceased. Even if '
                                             'no details about the individual are '
                                             'provided, this MUST include the '
                                             'phenopacket identifier (e.g., the value '
                                             'for the id field). Do not provide an '
                                             'empty value for this field.'}},
         'domain_of': ['Triple', 'Phenopacket']} })
    phenotypic_features: Optional[List[PhenotypicFeature]] = Field(None, description="""Phenotypic features relating to the subject of the phenopacket""", json_schema_extra = { "linkml_meta": {'alias': 'phenotypic_features',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of phenotypic '
                                             'features observed in the individual or '
                                             'biosample, including any explicitly '
                                             'excluded. If this is not provided, do '
                                             'not provide a value for this field. This '
                                             'should include ALL details provided in '
                                             'the input text regarding each feature '
                                             'and may be very verbose. Include the '
                                             'following information as available: a '
                                             'description of the observed phenotype, '
                                             'evidence supporting the phenotype, '
                                             'whether it was excluded, any modifiers '
                                             'of the phenotype, age of onset, time '
                                             'required to resolve the phenotype (if '
                                             'applicable), and its severity.'}},
         'domain_of': ['Phenopacket']} })
    measurements: Optional[List[Measurement]] = Field(None, description="""Quantifiable measurements related to the individual""", json_schema_extra = { "linkml_meta": {'alias': 'measurements',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'measurements taken from the individual '
                                             'or biosample. If no measurements are '
                                             'described, do not provide any values for '
                                             'this field. Include the following '
                                             'information as available: the name of '
                                             'the assay or test performed, the value '
                                             'of the result, a free-text description '
                                             'of the result, and the time when the '
                                             'measurement was made.'}},
         'domain_of': ['Phenopacket', 'Biosample']} })
    biosample: Optional[List[Biosample]] = Field(None, description="""Biosample(s) derived from the patient or a collection of biosamples in isolation""", json_schema_extra = { "linkml_meta": {'alias': 'biosample',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of biosamples '
                                             'from which the phenopacket was derived. '
                                             'If no biosamples are described, do not '
                                             'provide values for this field. Include '
                                             'the following information as available: '
                                             'the identifier of the individual or '
                                             'source of this sample, a description of '
                                             'the biosample, the overall type of the '
                                             'sample, the tissue of the sample, '
                                             'presence of any biomarkers, a '
                                             'histological diagnosis (including any '
                                             'negative or inconclusive findings), '
                                             'procedures performed to extract or '
                                             'process the sample'}},
         'domain_of': ['Phenopacket']} })
    interpretations: Optional[List[Interpretation]] = Field(None, description="""Interpretations of the phenopacket""", json_schema_extra = { "linkml_meta": {'alias': 'interpretations',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'interpretations of the input text, '
                                             'primarily any diagnoses and summaries of '
                                             "patient status. Include the individual's "
                                             'identifier. If no interpretations are '
                                             'provided in the input text, do not '
                                             'provide a value for this field.'}},
         'domain_of': ['Phenopacket']} })
    diseases: Optional[List[Disease]] = Field(None, description="""Field for disease identifiers - could be used for listing either diagnosed or suspected conditions. The resources using these fields should define what this represents in their context.""", json_schema_extra = { "linkml_meta": {'alias': 'diseases',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of diagnosed '
                                             'or suspected disease conditions. If this '
                                             'is not provided, do not provide a value '
                                             'for this field. Also include explicitly '
                                             'excluded diseases, clearly denoting they '
                                             'are excluded with the word EXCLUDED. '
                                             'Include the following information as '
                                             'available: name of the disease, a '
                                             'free-text description of the disease, '
                                             'any cancer diagnosis or related '
                                             'findings, disease stage, laterality, '
                                             'onset, and primary disease site in the '
                                             'body.'}},
         'domain_of': ['Phenopacket']} })
    medical_actions: Optional[List[MedicalAction]] = Field(None, description="""Field for medical action identifiers - could be used for listing either performed or planned actions. The resources using these fields should define what this represents in their context.""", json_schema_extra = { "linkml_meta": {'alias': 'medical_actions',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of medical '
                                             'actions taken or planned. If this is not '
                                             'provided, do not include a value for '
                                             'this field. Include the following '
                                             'information as available: the name of '
                                             'the action, a free-text description of '
                                             'the action, any adverse events '
                                             'encountered in the process, the intent '
                                             'of the action, any response to the '
                                             'action, the condition or disease '
                                             'intended as a target of the action, and '
                                             'any reason the treatment was '
                                             'discontinued.'}},
         'domain_of': ['Phenopacket']} })
    files: Optional[List[str]] = Field(None, description="""Pointer to the relevant file(s) for the individual""", json_schema_extra = { "linkml_meta": {'alias': 'files',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of file '
                                             'identifiers specified in the input text. '
                                             'If this is not provided, do not include '
                                             'a value for this field.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort', 'Biosample']} })
    meta_data: Optional[str] = Field(None, description="""Structured definitions of the resources and ontologies used within the phenopacket. REQUIRED""", json_schema_extra = { "linkml_meta": {'alias': 'meta_data',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Additional metadata for the phenopacket. '
                                             'If this is not provided, do not provide '
                                             'a value for this field.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort']} })


class Family(ConfiguredBaseModel):
    """
    Phenotype, sample and pedigree data required for a genomic diagnosis. Equivalent to the Genomics England InterpretationRequestRD https://github.com/genomicsengland/GelReportModels/blob/master/schemas/IDLs/org.gel.models.report.avro/5.0.0/InterpretationRequestRD.avdl
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    id: str = Field(..., description="""An identifier specific for this family.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['Must be assigned at write time'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    proband: Optional[str] = Field(None, description="""The individual representing the focus of this packet - e.g. the proband in rare disease cases or cancer patient""", json_schema_extra = { "linkml_meta": {'alias': 'proband',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The individual representing the focus of '
                                             'this input text, as a Phenopacket '
                                             'object.'}},
         'domain_of': ['Family']} })
    relatives: Optional[List[str]] = Field(None, description="""Individuals related in some way to the patient. For instance, the individuals may be genetically related or may be members of a cohort. If this field is used, then  it is expected that a pedigree will be included for genetically related individuals for use cases such as genomic diagnostics. If a phenopacket is being used to describe one member of a cohort, then in general one phenopacket will be created for each of the individuals in the cohort.""", json_schema_extra = { "linkml_meta": {'alias': 'relatives',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of relatives '
                                             'of the proband, as Phenopacket '
                                             'objects.'}},
         'domain_of': ['Family']} })
    consanguinous_parents: Optional[bool] = Field(None, description="""flag to indicate that the parents of the proband are consanguinous""", json_schema_extra = { "linkml_meta": {'alias': 'consanguinous_parents',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Flag to indicate that the parents of the '
                                             'proband are consanguinous. This must be '
                                             'a boolean value - true or false. If '
                                             'unknown, do not include this field or a '
                                             'value for this field.'}},
         'domain_of': ['Family']} })
    pedigree: Optional[Pedigree] = Field(None, description="""The pedigree defining the relations between the proband and their relatives. Pedigree.individual_id should map to the PhenoPacket.Individual.id""", json_schema_extra = { "linkml_meta": {'alias': 'pedigree',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The pedigree defining the relations '
                                             'between the proband and their '
                                             'relatives.'}},
         'domain_of': ['Family']} })
    files: Optional[List[File]] = Field(None, description="""Pointer to the relevant file(s) for the family. These should be files relating to one or more of the family members e.g a multi-sample VCF. Files relating exclusively to individual phenopackets should be contained in the Phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'files',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of file '
                                             'identifiers specified in the input text, '
                                             'relating to the family.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort', 'Biosample']} })
    meta_data: MetaData = Field(..., description="""Structured definitions of the resources and ontologies used within the phenopacket. REQUIRED""", json_schema_extra = { "linkml_meta": {'alias': 'meta_data',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Additional metadata for the '
                                             'phenopacket.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort']} })


class Cohort(ConfiguredBaseModel):
    """
    A group of individuals related in some phenotypic or genotypic aspect.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    id: str = Field(..., description="""An identifier specific for this cohort.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['Must be assigned at write time'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    description: Optional[str] = Field(None, description="""A description of the cohort, including the phenotypic or genotypic aspect that relates the individuals.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A description of the cohort, including '
                                             'the phenotypic or genotypic aspect that '
                                             'relates the individuals.'}},
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })
    members: Optional[List[str]] = Field(None, description="""Individuals in the cohort. Each individual should be described in a separate Phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'members',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'individuals in the cohort, as '
                                             'Phenopacket objects.'}},
         'domain_of': ['Cohort', 'Member']} })
    files: Optional[List[File]] = Field(None, description="""Pointer to relevant file(s) for the cohort. Files relating exclusively to individual phenopackets should be contained in the Phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'files',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of file '
                                             'identifiers specified in the input text, '
                                             'relating to the cohort.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort', 'Biosample']} })
    meta_data: MetaData = Field(..., description="""Structured definitions of the resources and ontologies used within the phenopacket. REQUIRED""", json_schema_extra = { "linkml_meta": {'alias': 'meta_data',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Additional metadata for the '
                                             'phenopacket.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort']} })


class OntologyClass(NamedEntity):
    """
    A class (aka term, concept) in an ontology. FHIR mapping: CodeableConcept (http://www.hl7.org/fhir/datatypes.html#CodeableConcept) see also Coding (http://www.hl7.org/fhir/datatypes.html#Coding)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['For OntoGPT, considered a NamedEntity',
                      'NamedEntity already defines id and label'],
         'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class ExternalReference(ConfiguredBaseModel):
    """
    FHIR mapping: Reference (https://www.hl7.org/fhir/references.html)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    id: str = Field(..., description="""e.g. ISBN, PMID:123456, DOI:..., FHIR mapping: Reference.identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['Must be assigned at write time'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    reference: Optional[str] = Field(None, description="""A full or partial URL pointing to the external reference if no commonly resolvable identifier can be used in the `id` field FHIR mapping Reference.reference""", json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A full or partial URL pointing to the '
                                             'external reference.'}},
         'domain_of': ['ExternalReference', 'Evidence']} })
    description: Optional[str] = Field(None, description="""Human readable title or display string for the reference FHIR mapping: Reference.display""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Human readable title or display string '
                                             'for the reference.'}},
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })


class Evidence(ConfiguredBaseModel):
    """
    FHIR mapping: Condition.evidence https://www.hl7.org/fhir/condition-definitions.html#Condition.evidence
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    evidence_code: Optional[str] = Field(None, description="""The encoded evidence type using, for example the Evidence & Conclusion Ontology (ECO - http://purl.obolibrary.org/obo/eco.owl)""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The type of evidence, identified by '
                                             'NamedEntity.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'nucleotide sequencing assay '
                                                      'evidence; cognitive assay '
                                                      'phenotypic evidence'}},
         'domain_of': ['Evidence']} })
    reference: Optional[str] = Field(None, description="""FHIR mapping: Condition.evidence.detail""", json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A reference to the evidence, if '
                                             'provided. Do not include a value for '
                                             'this field if no reference is '
                                             'provided.'}},
         'domain_of': ['ExternalReference', 'Evidence']} })


class Procedure(ConfiguredBaseModel):
    """
    A clinical procedure performed on a subject. By preference a single concept to indicate both the procedure and thebody site should be used. In cases where this is not possible, the body site should be indicated using a separate ontology class. e.g. {\"code\":{\"NCIT:C51585\": \"Biopsy of Soft Palate\"}} {\"code\":{\"NCIT:C28743\": \"Punch Biopsy\"}, \"body_site\":{\"UBERON:0003403\": \"skin of forearm\"}} - a punch biopsy of the skin from the forearm FHIR mapping: Procedure (https://www.hl7.org/fhir/procedure.html)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    code: Optional[str] = Field(None, description="""FHIR mapping: Procedure.code""", json_schema_extra = { "linkml_meta": {'alias': 'code',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the procedure.'}},
         'domain_of': ['Procedure']} })
    body_site: Optional[str] = Field(None, description="""FHIR mapping: Procedure.bodySite""", json_schema_extra = { "linkml_meta": {'alias': 'body_site',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the body site of the '
                                             'procedure. This may require inference '
                                             'from the procedure, e.g., a colonoscopy '
                                             'is done on the colon, bronchoscopy is '
                                             'done on the lungs, and so on.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'colon; lungs; retina'}},
         'domain_of': ['Procedure']} })
    performed: Optional[str] = Field(None, description="""When the procedure was performed.""", json_schema_extra = { "linkml_meta": {'alias': 'performed',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The date and time the procedure was '
                                             'performed.'}},
         'domain_of': ['Procedure']} })


class GestationalAge(ConfiguredBaseModel):
    """
    The gestational age of the individual at the time of the procedure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    weeks: Optional[int] = Field(None, description="""The gestational age in weeks.""", json_schema_extra = { "linkml_meta": {'alias': 'weeks',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The gestational age in weeks. This must '
                                             'be an integer. Do not provide units or '
                                             'any non-integer value.'}},
         'domain_of': ['GestationalAge']} })
    days: Optional[int] = Field(None, description="""The gestational age in days.""", json_schema_extra = { "linkml_meta": {'alias': 'days',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The gestational age in days. This must '
                                             'be an integer. Do not provide units or '
                                             'any non-integer value.'}},
         'domain_of': ['GestationalAge']} })


class Age(ConfiguredBaseModel):
    """
    See http://build.fhir.org/datatypes and http://build.fhir.org/condition-definitions.html#Condition.onset_x_ In FHIR this is represented as a UCUM measurement - http://unitsofmeasure.org/trac/
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    iso8601duration: Optional[str] = Field(None, description="""The :ref:`ISO 8601<metadata_date_time>` age of this object as ISO8601 duration or time intervals. e.g. P40Y10M05D)""", json_schema_extra = { "linkml_meta": {'alias': 'iso8601duration',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The age as an ISO 8601 duration. Do not '
                                             'provide units.'},
                         'prompt.example': {'tag': 'prompt.example',
                                            'value': 'P40Y10M05D'}},
         'domain_of': ['Age']} })


class AgeRange(ConfiguredBaseModel):
    """
    A range of ages.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    start: Optional[Age] = Field(None, description="""The minimum age in the range.""", json_schema_extra = { "linkml_meta": {'alias': 'start',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The minimum age in the range. This '
                                             'should be an integer.'}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })
    end: Optional[Age] = Field(None, description="""The maximum age in the range.""", json_schema_extra = { "linkml_meta": {'alias': 'end',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The maximum age in the range. This '
                                             'should be an integer.'}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })


class TimeInterval(ConfiguredBaseModel):
    """
    A time interval.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    start: Optional[str] = Field(None, description="""The start of the time interval.""", json_schema_extra = { "linkml_meta": {'alias': 'start',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The start of the time interval.'}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })
    end: Optional[str] = Field(None, description="""The end of the time interval.""", json_schema_extra = { "linkml_meta": {'alias': 'end',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The end of the time interval.'}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })


class TimeElement(ConfiguredBaseModel):
    """
    A time element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    gestational_age: Optional[GestationalAge] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'gestational_age', 'domain_of': ['TimeElement']} })
    age: Optional[Age] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'age', 'domain_of': ['TimeElement']} })
    age_range: Optional[AgeRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'age_range', 'domain_of': ['TimeElement']} })
    ontology_class: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'ontology_class', 'domain_of': ['TimeElement']} })
    timestamp: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'timestamp', 'domain_of': ['TimeElement', 'Update']} })
    interval: Optional[TimeInterval] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'interval',
         'domain_of': ['TimeElement', 'DoseInterval', 'ChromosomeLocation']} })


class File(ConfiguredBaseModel):
    """
    A file or set of files.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    uri: Optional[str] = Field(None, description="""URI for the file e.g. file://data/genomes/file1.vcf.gz or https://opensnp.org/data/60.23andme-exome-vcf.231?1341012444""", json_schema_extra = { "linkml_meta": {'alias': 'uri',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A unique resource identifier for the '
                                             'file. This may be a file path (beginning '
                                             'with file://) or URL.'},
                         'prompt.example': {'tag': 'prompt.example',
                                            'value': 'file://data/genomes/file1.vcf.gz'}},
         'domain_of': ['File']} })
    individual_to_file_identifiers: Optional[str] = Field(None, description="""A map of identifiers mapping an individual to a sample in the file. The key values must correspond to the Individual::id for the individuals in the message, the values must map to the samples in the file.""", json_schema_extra = { "linkml_meta": {'alias': 'individual_to_file_identifiers',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A map of identifiers mapping an '
                                             'individual to a sample in the file. The '
                                             'key values must correspond to the '
                                             'Individual::id for the individuals.'}},
         'domain_of': ['File']} })
    file_attributes: Optional[str] = Field(None, description="""Map of attributes describing the file. For example the File format or genome assembly would be defied here. For genomic data files there MUST be a 'genomeAssembly' key.""", json_schema_extra = { "linkml_meta": {'alias': 'file_attributes',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Map of attributes describing the file.'}},
         'domain_of': ['File']} })


class Biosample(ConfiguredBaseModel):
    """
    A Biosample refers to a unit of biological material from which the substrate molecules (e.g. genomic DNA, RNA, proteins) for molecular analyses (e.g. sequencing, array hybridisation, mass-spectrometry) are extracted. Examples would be a tissue biopsy, a single cell from a culture for single cell genome sequencing or a protein fraction from a gradient centrifugation. Several instances (e.g. technical replicates) or types of experiments (e.g. genomic array as well as RNA-seq experiments) may refer to the same Biosample. FHIR mapping: Specimen (http://www.hl7.org/fhir/specimen.html).\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    derivedFromId: Optional[str] = Field(None, description="""The id of the parent biosample this biosample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'derivedFromId',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A unique identifier for the parent '
                                             'biosample of this biosample, if '
                                             'applicable. If this is not provided, do '
                                             'not include a value for this field.'}},
         'domain_of': ['Biosample']} })
    description: Optional[str] = Field(None, description="""The biosample's description. This attribute contains human readable text. The \"description\" attributes should not contain any structured data.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Description of the biosample. This '
                                             'should contain no identifiers.'}},
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })
    diagnosticMarkers: Optional[List[DiagnosticMarkerClass]] = Field(None, description="""Clinically relevant bio markers. Most of the assays such as IHC are covered by the NCIT under the sub-hierarchy NCIT:C25294 (Laboratory Procedure). e.g. NCIT:C68748 (HER2/Neu Positive), NCIT:C131711 (Human Papillomavirus-18 Positive)""", json_schema_extra = { "linkml_meta": {'alias': 'diagnosticMarkers',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-delimited list of names of '
                                             'clinically relevant bio markers observed '
                                             'in the sample, along with their status '
                                             '(e.g., Positive, present, etc.) '
                                             'including observations of laboratory '
                                             'procedures performed on the sample. If '
                                             'this is not provided, do not include a '
                                             'value for this field.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'HER2/Neu Positive; Human '
                                                      'Papillomavirus-18 Positive'}},
         'domain_of': ['Biosample']} })
    files: Optional[List[str]] = Field(None, description="""Pointer to the relevant file(s) for the biosample. Files relating to the entire individual e.g. a germline exome/genome should be associated with the Phenopacket rather than the Biosample it was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'files',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of file '
                                             'identifiers specified in the input text, '
                                             'relating to the biosample. If this is '
                                             'not provided, do not include a value for '
                                             'this field.'}},
         'domain_of': ['Phenopacket', 'Family', 'Cohort', 'Biosample']} })
    histologicalDiagnosis: Optional[str] = Field(None, description="""This is the pathologist’s diagnosis and may often represent a refinement of the clinical diagnosis given in the Patient/Clinical module. Should use the same terminology as diagnosis, but represent the pathologist’s findings. Normal samples would be tagged with the term \"NCIT:C38757\", \"Negative Finding\" ARGO mapping specimen::tumour_histological_type""", json_schema_extra = { "linkml_meta": {'alias': 'histologicalDiagnosis',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The pathologist’s diagnosis of the '
                                             'biosample. This should use the same '
                                             'terminology as the diagnosis, but '
                                             'represent the pathologist’s findings. If '
                                             'this is not provided, do not provide a '
                                             'value. Normal samples should be '
                                             'described here with the term "Negative '
                                             'Finding".'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:specimen.tumour_histological_type']} })
    id: Optional[str] = Field(None, description="""biosamples SAMN08666232 Human Cell Atlas The Biosample id This is unique in the context of the server instance. ARGO mapping specimen::submitter_specimen_id""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'prompt': {'tag': 'prompt',
                                    'value': 'A unique identifier for the biosample. '
                                             'If one is not available, create an '
                                             'identifier incorporating the '
                                             "individual's identifier, e.g. if the "
                                             'individual\'s identifier is "Patient1", '
                                             'the biosample id may be '
                                             '"Patient1_Biosample1".'}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'exact_mappings': ['ARGO:specimen.submitter_specimen_id']} })
    individualId: Optional[str] = Field(None, description="""The id of the individual this biosample was derived from. ARGO mapping specimen::submitter_donor_id""", json_schema_extra = { "linkml_meta": {'alias': 'individualId',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A unique identifier for the individual '
                                             'this biosample was derived from. If '
                                             'provided directly from an individual or '
                                             'animal, this field will be the '
                                             'identifier of that individual or '
                                             'animal.'}},
         'domain_of': ['Biosample', 'Person'],
         'exact_mappings': ['ARGO:specimen.submitter_donor_id']} })
    materialSample: Optional[str] = Field(None, description="""This element can be used to specify the status of the sample. For instance, a status may be used as a normal control, often in combination with another sample that is thought to contain a pathological finding. We recommend use of ontology terms such as: EFO:0009654 (reference sample) or EFO:0009655 (abnormal sample) ARGO mapping sample_registration::tumour_normal_designation""", json_schema_extra = { "linkml_meta": {'alias': 'materialSample',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The status of the sample. For instance, '
                                             'a status may be used as a normal '
                                             'control, often in combination with '
                                             'another sample that is thought to '
                                             'contain a pathological finding. If this '
                                             'is not provided, do not include a '
                                             'value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'reference sample; abnormal '
                                                      'sample'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:sample_registration.tumour_normal_designation']} })
    measurements: Optional[List[Measurement]] = Field(None, description="""Measurements obtained for the sample.""", json_schema_extra = { "linkml_meta": {'alias': 'measurements',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'measurements taken from the biosample. '
                                             'If this is not provided, do not provide '
                                             'any values for this field. Include the '
                                             'following information as available: the '
                                             'name of the assay or test performed, the '
                                             'value of the result, a free-text '
                                             'description of the result, and the time '
                                             'when the measurement was made.'}},
         'domain_of': ['Phenopacket', 'Biosample']} })
    pathologicalStage: Optional[str] = Field(None, description="""ARGO mapping specimen::pathological_tumour_staging_system ARGO mapping specimen::pathological_stage_group""", json_schema_extra = { "linkml_meta": {'alias': 'pathologicalStage',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The pathological stage of the biosample. '
                                             'If this is not provided, do not include '
                                             'a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Stage I; Stage II; Stage III; '
                                                      'Stage IV'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:specimen.pathological_tumour_staging_system']} })
    pathologicalTnmFinding: Optional[List[str]] = Field(None, description="""ARGO mapping specimen::pathological_t_category ARGO mapping specimen::pathological_n_category ARGO mapping specimen::pathological_m_category""", json_schema_extra = { "linkml_meta": {'alias': 'pathologicalTnmFinding',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of cancer '
                                             'findings in the TNM system that are '
                                             'relevant to the diagnosis of cancer. If '
                                             'this is not provided, do not include a '
                                             'value.'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:specimen.pathological_t_category']} })
    phenotypicFeatures: Optional[List[PhenotypicFeature]] = Field(None, description="""Phenotypic characteristics of the BioSample, for example histological findings of a biopsy.""", json_schema_extra = { "linkml_meta": {'alias': 'phenotypicFeatures',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of phenotypic '
                                             'features observed in the biosample, '
                                             'including any explicitly excluded. This '
                                             'may include histological findings of the '
                                             'sample, e.g., observations of a biopsy. '
                                             'If phenotypic features are not provided, '
                                             'write only "NA". Include the following '
                                             'information as available: a description '
                                             'of the observed phenotype, evidence '
                                             'supporting the phenotype, whether it was '
                                             'excluded, any modifiers of the '
                                             'phenotype, age of onset, time required '
                                             'to resolve the phenotype (if '
                                             'applicable), and its severity.'}},
         'domain_of': ['Biosample']} })
    procedure: Optional[Procedure] = Field(None, description="""Clinical procedure performed on the subject in order to extract the biosample. ARGO mapping specimen::specimen_anatomic_location - Procedure::body_site ARGO mapping specimen::specimen_acquisition_interval - Procedure::time_performed""", json_schema_extra = { "linkml_meta": {'alias': 'procedure',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The clinical procedure performed on the '
                                             'subject in order to extract the '
                                             'biosample. If this is not provided, do '
                                             'not include a value.'}},
         'domain_of': ['Biosample', 'Measurement', 'MedicalAction'],
         'exact_mappings': ['ARGO:specimen.specimen_anatomic_location']} })
    sampleProcessing: Optional[str] = Field(None, description="""Field to represent how the sample was processed. ARGO mapping specimen::specimen_processing""", json_schema_extra = { "linkml_meta": {'alias': 'sampleProcessing',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Field to represent how the sample was '
                                             'processed. If this is not provided, do '
                                             'not include a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Formalin fixation; Paraffin '
                                                      'embedding; DNA extraction'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:specimen.specimen_processing']} })
    sampleStorage: Optional[str] = Field(None, description="""Field to represent how the sample was stored ARGO mapping specimen::specimen_storage""", json_schema_extra = { "linkml_meta": {'alias': 'sampleStorage',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Field to represent how the sample was '
                                             'stored. If this is not provided, do not '
                                             'include a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Liquid nitrogen; storage at '
                                                      'room temperature'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:specimen.specimen_storage']} })
    sampleType: Optional[str] = Field(None, description="""Recommended use of EFO term to describe the sample. e.g. Amplified DNA, ctDNA, Total RNA, Lung tissue, Cultured cells... ARGO mapping sample_registration::sample_type""", json_schema_extra = { "linkml_meta": {'alias': 'sampleType',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The type of the sample. If this is not '
                                             'provided, do not include a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Amplified DNA; ctDNA; Total '
                                                      'RNA; Lung tissue; Cultured '
                                                      'cells'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:sample_registration.sample_type']} })
    sampledTissue: Optional[str] = Field(None, description="""UBERON class describing the tissue from which the specimen was collected. PDX-MI mapping: 'Specimen tumor tissue' FHIR mapping: Specimen.type ARGO mapping sample_registration::specimen_tissue_source\"""", json_schema_extra = { "linkml_meta": {'alias': 'sampledTissue',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The tissue from which the specimen was '
                                             'collected. If this is not provided, do '
                                             'not include a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'lung; liver; pericardium'}},
         'domain_of': ['Biosample'],
         'exact_mappings': ['ARGO:sample_registration.specimen_tissue_source']} })
    taxonomy: Optional[str] = Field(None, description="""NCBI taxonomic identifier (NCBITaxon) of the sample e.g. NCBITaxon:9606""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomy',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The NCBI taxonomic identifier of the '
                                             'sample. If this is not provided, do not '
                                             'include a value. Human samples should '
                                             'always be annotated with NCBITaxon:9606, '
                                             'though organisms isolated from human '
                                             'samples may have different taxonomic '
                                             'identifiers.'}},
         'domain_of': ['Biosample', 'Individual']} })
    timeOfCollection: Optional[str] = Field(None, description="""An TimeElement describing either the age of the individual this biosample was derived from at the time of collection, or the time itself. See http://build.fhir.org/datatypes""", json_schema_extra = { "linkml_meta": {'alias': 'timeOfCollection',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The time of collection of the biosample. '
                                             'If this is not provided, do not include '
                                             'a value.'}},
         'domain_of': ['Biosample']} })
    tumorGrade: Optional[str] = Field(None, description="""Potentially a child term of NCIT:C28076 (Disease Grade Qualifier) or equivalent See https://www.cancer.gov/about-cancer/diagnosis-staging/prognosis/tumor-grade-fact-sheet""", json_schema_extra = { "linkml_meta": {'alias': 'tumorGrade',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The grade of the tumor. If this is not '
                                             'provided, do not include a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Grade I; Grade II; Grade III; '
                                                      'Grade IV'}},
         'domain_of': ['Biosample']} })
    tumorProgression: Optional[str] = Field(None, description="""Is the specimen tissue from the primary tumor, a metastasis or a recurrence? Most likely a child term of NCIT:C7062 (Neoplasm by Special Category) NCIT:C3677 (Benign Neoplasm) NCIT:C84509 (Primary Malignant Neoplasm) NCIT:C95606 (Second Primary Malignant Neoplasm) NCIT:C3261 (Metastatic Neoplasm) NCIT:C4813 (Recurrent Malignant Neoplasm)""", json_schema_extra = { "linkml_meta": {'alias': 'tumorProgression',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Is the specimen tissue from the primary '
                                             'tumor, a metastasis or a recurrence? If '
                                             'this is not provided, do not include a '
                                             'value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Benign Neoplasm; Primary '
                                                      'Malignant Neoplasm; Second '
                                                      'Primary Malignant Neoplasm; '
                                                      'Metastatic Neoplasm; Recurrent '
                                                      'Malignant Neoplasm'}},
         'domain_of': ['Biosample']} })


class Disease(ConfiguredBaseModel):
    """
    Message to indicate a disease (diagnosis) and its recorded onset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    clinicalTnmFinding: Optional[List[str]] = Field(None, description="""Cancer findings in the TNM system that is relevant to the diagnosis of cancer. See https://www.cancer.gov/about-cancer/diagnosis-staging/staging Valid values include child terms of NCIT:C48232 (Cancer TNM Finding) ARGO mapping primary_diagnosis::clinical_t_category ARGO mapping primary_diagnosis::clinical_n_category ARGO mapping primary_diagnosis::clinical_m_category""", json_schema_extra = { "linkml_meta": {'alias': 'clinicalTnmFinding',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of cancer '
                                             'findings in the Tumor, Node, Metastasis '
                                             '(TNM) system that are relevant to the '
                                             'diagnosis of cancer. If this is not '
                                             'provided, do not include a value for '
                                             'this field.'}},
         'domain_of': ['Disease'],
         'exact_mappings': ['ARGO:primary_diagnosis.clinical_t_category']} })
    diseaseStage: Optional[List[str]] = Field(None, description="""Disease staging, the extent to which a disease has developed. For cancers, see https://www.cancer.gov/about-cancer/diagnosis-staging/staging Valid values include child terms of NCIT:C28108 (Disease Stage Qualifier) ARGO mapping primary_diagnosis::clinical_tumour_staging_system ARGO mapping primary_diagnosis::clinical_stage_group""", json_schema_extra = { "linkml_meta": {'alias': 'diseaseStage',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of disease '
                                             'staging terms. These describe the extent '
                                             'to which a disease has developed. If '
                                             'this is not provided, do not include a '
                                             'value for this field.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Stage IA; Stage M2; Stage R; '
                                                      'Postoperative Stage'}},
         'domain_of': ['Disease'],
         'exact_mappings': ['ARGO:primary_diagnosis.clinical_tumour_staging_system']} })
    excluded: Optional[str] = Field(None, description="""Flag to indicate whether the disease was observed or not. Default is 'false', in other words the disease was observed. Therefore it is only required in cases to indicate that the disease was looked for, but found to be absent. More formally, this modifier indicates the logical negation of the OntologyClass used in the 'term' field. *CAUTION* It is imperative to check this field for correct interpretation of the disease!""", json_schema_extra = { "linkml_meta": {'alias': 'excluded',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Flag to indicate whether the disease was '
                                             'observed or not. If the disease is '
                                             'explicitly EXCLUDED, this value should '
                                             "be 'true'. Otherwise, do not provide a "
                                             'value for this field, or provide '
                                             "'false'."}},
         'domain_of': ['Disease', 'PhenotypicFeature']} })
    laterality: Optional[str] = Field(None, description="""The term used to indicate laterality of diagnosis, if applicable. (Codelist reference: NCI CDE: 4122391)""", json_schema_extra = { "linkml_meta": {'alias': 'laterality',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The term used to indicate laterality of '
                                             'diagnosis, if applicable. If this is not '
                                             'provided, do not include a value.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'unilateral; bilateral'}},
         'domain_of': ['Disease']} })
    onset: Optional[str] = Field(None, description="""The onset of the disease. The values of this will come from the HPO onset hierarchy i.e. subclasses of HP:0003674 FHIR mapping:
  Condition.onset ARGO mapping primary_diagnosis::age_at_diagnosis""", json_schema_extra = { "linkml_meta": {'alias': 'onset',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The onset of the disease in terms of the '
                                             "individual's age. If this is not "
                                             'provided, do not include a value.'}},
         'domain_of': ['Disease', 'PhenotypicFeature'],
         'exact_mappings': ['ARGO:primary_diagnosis.age_at_diagnosis']} })
    primarySite: Optional[str] = Field(None, description="""The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general""", json_schema_extra = { "linkml_meta": {'alias': 'primarySite',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The text term used to describe the '
                                             'primary site of disease. If this is not '
                                             'provided, do not include a value.'}},
         'domain_of': ['Disease']} })
    resolution: Optional[str] = Field(None, description="""The time of resolution of the disease, if applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'resolution',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The time of resolution of the disease, '
                                             'if applicable. If this is not provided, '
                                             'do not include a value.'}},
         'domain_of': ['Disease', 'PhenotypicFeature']} })
    term: Optional[str] = Field(None, description="""The identifier of this disease e.g. MONDO:0007043, OMIM:101600, Orphanet:710, DOID:14705 (note these are all equivalent) ARGO mapping primary_diagnosis::submitter_primary_diagnosis_id""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the disease.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'cardio-renal syndrome; acute '
                                                      'myeloid leukemia; breast '
                                                      'cancer'}},
         'domain_of': ['Disease'],
         'exact_mappings': ['ARGO:primary_diagnosis.submitter_primary_diagnosis_id']} })


class Diagnosis(ConfiguredBaseModel):
    """
    Diagnosis of clinical findings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    disease: Optional[str] = Field(None, description="""The disease/condition assigned to the diagnosis. Details about this disease may be contained in the `diseases` field in the Phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'disease',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The disease or condition assigned to the '
                                             'diagnosis, identified by name.'}},
         'domain_of': ['Diagnosis']} })
    genomicInterpretations: Optional[List[GenomicInterpretation]] = Field(None, description="""genomic features containing the status of their contribution towards the diagnosis""", json_schema_extra = { "linkml_meta": {'alias': 'genomicInterpretations',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of genomic '
                                             'features containing the status of their '
                                             'contribution towards the diagnosis. '
                                             'Include the following information as '
                                             'available: the identifier of the '
                                             'individual or biosample, the gene '
                                             'implicated in the diagnosis, the status '
                                             'of the interpretation, and any details '
                                             'describing interpretation of the '
                                             'variant. If no genomic features are '
                                             'specified, do not include a value.'}},
         'domain_of': ['Diagnosis']} })


class GenomicInterpretation(ConfiguredBaseModel):
    """
    A statement about the contribution of a genomic element towards the observed phenotype. Note that this does not intend to encode any knowledge or results of specific computations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'gene': {'name': 'gene',
                                                                                        'required': True}}},
                                                          {'slot_conditions': {'variantInterpretation': {'name': 'variantInterpretation',
                                                                                                         'required': True}}}]}}]})

    gene: Optional[str] = Field(None, description="""A specific gene implicated in a phenotype.""", json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A specific gene implicated in a '
                                             'phenotype. This should be a '
                                             'human-readable name.'}},
         'domain_of': ['GenomicInterpretation', 'CopyNumber', 'Feature']} })
    interpretationStatus: Optional[InterpretationStatus] = Field(None, description="""Status of the interpretation.""", json_schema_extra = { "linkml_meta": {'alias': 'interpretationStatus',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The status of the interpretation. Must '
                                             'be one of the following: CANDIDATE, '
                                             'CAUSATIVE, CONTRIBUTORY, REJECTED, or '
                                             'UNKNOWN_STATUS.'}},
         'domain_of': ['GenomicInterpretation']} })
    subjectOrBiosampleId: Optional[str] = Field(None, description="""identifier for the subject of the interpretation. This MUST be the individual id or a biosample id of the enclosing phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'subjectOrBiosampleId',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'An identifier for the subject of the '
                                             'interpretation. This MUST be identical '
                                             'to the provided individual id or a '
                                             'biosample id.'}},
         'domain_of': ['GenomicInterpretation']} })
    variantInterpretation: Optional[VariantInterpretation] = Field(None, description="""Interpretation of the genetic variant.""", json_schema_extra = { "linkml_meta": {'alias': 'variantInterpretation',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Interpretation of the genetic variant. '
                                             'Include the following, as available: the '
                                             'ACMG pathogenicity classification, the '
                                             'therapeutic actionability, and the '
                                             'variation descriptor. If none of this is '
                                             'specified, do not include a value for '
                                             'this field.'}},
         'domain_of': ['GenomicInterpretation']} })


class Interpretation(ConfiguredBaseModel):
    """
    Interpretation of clinical findings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    diagnosis: Optional[Diagnosis] = Field(None, description="""The diagnosis made in this interpretation.""", json_schema_extra = { "linkml_meta": {'alias': 'diagnosis',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The diagnosis made in this '
                                             'interpretation. If this is not provided, '
                                             'do not include a value for this field. '
                                             'Include the following, as available: the '
                                             'name of the disease or condition with '
                                             'all acronyms spelled out, the identifier '
                                             'of the individual or biosample, and any '
                                             'details regarding genetic or genomic '
                                             'interpretation (including the gene, the '
                                             'status of the genetic interpretation, '
                                             'and/or any details regarding the '
                                             'specific variant). Include this '
                                             'information even if it is also present '
                                             'in the summary field.'}},
         'domain_of': ['Interpretation']} })
    id: Optional[str] = Field(None, description="""id of the interpretation""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A unique identifier for the '
                                             'interpretation. This must be unique '
                                             'within the phenopacket but may be based '
                                             "on the individual's identifier. For "
                                             "example, if the individual's identifier "
                                             'is "Patient1", the interpretation id may '
                                             'be "Patient1_Interpretation1".'}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    progressStatus: Optional[ProgressStatus] = Field(None, description="""The status of the interpretation.""", json_schema_extra = { "linkml_meta": {'alias': 'progressStatus',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The status of the interpretation. Must '
                                             'be one of the following: COMPLETED, '
                                             'IN_PROGRESS, SOLVED, UNKNOWN_PROGRESS, '
                                             'or UNSOLVED.'}},
         'domain_of': ['Interpretation']} })
    summary: Optional[str] = Field(None, description="""A brief summary of the interpretation.""", json_schema_extra = { "linkml_meta": {'alias': 'summary',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A brief summary of the interpretation.'}},
         'domain_of': ['Interpretation']} })


class VariantInterpretation(ConfiguredBaseModel):
    """
    Interpretation of a genetic variant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    acmgPathogenicityClassification: Optional[AcmgPathogenicityClassification] = Field(None, description="""ACMG pathogenicity classification.""", json_schema_extra = { "linkml_meta": {'alias': 'acmgPathogenicityClassification',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The ACMG pathogenicity classification of '
                                             'the variant. Must be one of the '
                                             'following: BENIGN, LIKELY_BENIGN, '
                                             'LIKELY_PATHOGENIC, PATHOGENIC, '
                                             'UNCERTAIN_SIGNIFICANCE, or '
                                             'NOT_PROVIDED.'}},
         'domain_of': ['VariantInterpretation']} })
    therapeuticActionability: Optional[TherapeuticActionability] = Field(None, description="""Therapeutic actionability of the variant.""", json_schema_extra = { "linkml_meta": {'alias': 'therapeuticActionability',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The therapeutic actionability of the '
                                             'variant. Must be one of the following: '
                                             'ACTIONABLE, NOT_ACTIONABLE, or '
                                             'UNKNOWN_ACTIONABILITY.'}},
         'domain_of': ['VariantInterpretation']} })
    variationDescriptor: Optional[VariationDescriptor] = Field(None, description="""A descriptor of the variant.""", json_schema_extra = { "linkml_meta": {'alias': 'variationDescriptor',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A description of the variant. This '
                                             'should include the following, as '
                                             'available: the allelic state, any '
                                             'alternate labels of the variant, a brief '
                                             'description of the variant, and any '
                                             'additional information about the '
                                             'variant.'}},
         'domain_of': ['VariantInterpretation']} })


class Individual(ConfiguredBaseModel):
    """
    An individual (or subject) typically corresponds to an individual human or another organism. FHIR mapping: Patient (https://www.hl7.org/fhir/patient.html).\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    alternateIds: Optional[List[str]] = Field(None, description="""An optional list of alternative identifiers for this individual. This field is provided for the convenience of users who may have multiple mappings to an individual which they need to track.""", json_schema_extra = { "linkml_meta": {'alias': 'alternateIds',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of '
                                             'alternative identifiers for this '
                                             'individual, if any.'}},
         'domain_of': ['Individual', 'GeneDescriptor']} })
    dateOfBirth: Optional[str] = Field(None, description="""The date of birth of the individual as an ISO8601 UTC timestamp - rounded down to the closest known year/month/day/hour/minute e.g. \"2018-03-01T00:00:00Z\" for someone born on an unknown day in March 2018 or \"2018-01-01T00:00:00Z\" for someone born on an unknown day in 2018 or empty if unknown/ not stated.""", json_schema_extra = { "linkml_meta": {'alias': 'dateOfBirth',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The date of birth of the individual as '
                                             'an ISO8601 UTC timestamp. This should be '
                                             'rounded down to the closest known '
                                             'year/month/day. If the day is unknown, '
                                             'use the first day of the month. If the '
                                             'month is unknown, use the first month of '
                                             'the year. If the year is unknown, do not '
                                             'provide a value.'}},
         'domain_of': ['Individual']} })
    gender: Optional[str] = Field(None, description="""Self-identified gender""", json_schema_extra = { "linkml_meta": {'alias': 'gender',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The self-identified gender of the '
                                             'individual. This may or may not be the '
                                             "same as the individual's sex."},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'female gender identity; male '
                                                      'gender identity; nobinary '
                                                      'gender identity; agendered'}},
         'domain_of': ['Individual']} })
    id: Optional[str] = Field(None, description="""An identifier for the individual. This must be unique within the record. ARGO mapping donor::submitter_donor_id""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The identifier for the individual. These '
                                             'may also be present in the '
                                             'alternativeIds field. If an individual '
                                             'is referred to with a phrase like '
                                             '"identified as", this is the identifier. '
                                             'Must not be blank. May be identical to '
                                             "the individual's alternate identifier. "
                                             'If no identifier is provided, create '
                                             'one.'}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'exact_mappings': ['ARGO:donor.submitter_donor_id']} })
    karyotypicSex: Optional[KaryotypicSex] = Field(None, description="""The karyotypic sex of the individual""", json_schema_extra = { "linkml_meta": {'alias': 'karyotypicSex',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The karyotypic sex of the individual '
                                             '(their karyotype, or the sex chromosomes '
                                             'they have). Must be one of XO, XX, XY, '
                                             'XXY, XYY, XXX, XXXX, XXYY, XXXY, '
                                             'OTHER_KARYOTYPE (if not among the '
                                             'previous values) or UNKNOWN (if not '
                                             'specified)'}},
         'domain_of': ['Individual']} })
    sex: Optional[Sex] = Field(None, description="""The phenotypic sex of the individual ARGO mapping sample_registration::gender (this is complicated as ARGO only have male/female/other which maps to the phenopacket Sex field)""", json_schema_extra = { "linkml_meta": {'alias': 'sex',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The phenotypic sex of the individual. '
                                             'Must be one of FEMALE, MALE, OTHER_SEX '
                                             '(if it is not possible to accurately '
                                             'assess the applicability of MALE/FEMALE) '
                                             'or UNKNOWN_SEX if the information is '
                                             "unknown. IF the individual's gender is "
                                             'known and sex is not specified, use the '
                                             'corresponding value for sex (e.g., if '
                                             'the individual has female gender, '
                                             'specify female sex unless there is '
                                             'information to the contrary).'}},
         'domain_of': ['Individual', 'Person'],
         'exact_mappings': ['ARGO:sample_registration.gender']} })
    taxonomy: Optional[str] = Field(None, description="""NCBI taxonomic identifier NCBITaxon e.g. NCBITaxon:9606 or NCBITaxon:1337 For resources where there may be more than one organism being studied it is advisable to indicate the taxonomic identifier of that organism, to its most specific level""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomy',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The NCBI taxonomic identifier of the '
                                             'individual. If this is a human, this '
                                             'value is always NCBITaxon:9606.'}},
         'domain_of': ['Biosample', 'Individual']} })
    timeAtLastEncounter: Optional[str] = Field(None, description="""An TimeElement object describing the age of the individual at the last time of collection. The Age object allows the encoding of the age either as ISO8601 duration or time interval (preferred), or as ontology term object. See http://build.fhir.org/datatypes""", json_schema_extra = { "linkml_meta": {'alias': 'timeAtLastEncounter',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The age of the individual at the last '
                                             'time of encounter. This should be an '
                                             'ISO8601 duration or time interval. Do '
                                             'not provide units.'}},
         'domain_of': ['Individual']} })
    vitalStatus: Optional[VitalStatus] = Field(None, description="""Vital status of the individual. If not present it is assumed that the individual is alive. If present it will default to 'false' i.e. the individual was alive when the data was collected. ARGO mapping donor::vital_status""", json_schema_extra = { "linkml_meta": {'alias': 'vitalStatus',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The vital status of the individual. Must '
                                             'include any of the following '
                                             'information, as available: the cause of '
                                             'death, the status (alive or dead at time '
                                             'of data collection), the survival time '
                                             'in days (integer only), and/or the time '
                                             'of death. This must be included.'}},
         'domain_of': ['Individual'],
         'exact_mappings': ['ARGO:donor.vital_status']} })


class VitalStatus(ConfiguredBaseModel):
    """
    The vital status of an individual.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    causeOfDeath: Optional[str] = Field(None, description="""ARGO mapping donor::cause_of_death""", json_schema_extra = { "linkml_meta": {'alias': 'causeOfDeath',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The cause of death of the individual. Do '
                                             'not provide a value if the individual is '
                                             'alive or the cause of death is '
                                             'unknown.'}},
         'domain_of': ['VitalStatus'],
         'exact_mappings': ['ARGO:donor.cause_of_death']} })
    status: Optional[Status] = Field(None, description="""Status of an individual.""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The status of the individual. Must be '
                                             'one of ALIVE, DECEASED, or '
                                             'UNKNOWN_STATUS.'}},
         'domain_of': ['VitalStatus']} })
    survivalTimeInDays: Optional[str] = Field(None, description="""ARGO mapping donor::survival_time""", json_schema_extra = { "linkml_meta": {'alias': 'survivalTimeInDays',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The survival time of the individual in '
                                             'days. This should be an integer.'}},
         'domain_of': ['VitalStatus'],
         'exact_mappings': ['ARGO:donor.survival_time']} })
    timeOfDeath: Optional[str] = Field(None, description="""The time of death, if applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'timeOfDeath',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The time of death of the individual. '
                                             'This should be an ISO 8601 timestamp.'}},
         'domain_of': ['VitalStatus']} })


class ComplexValue(ConfiguredBaseModel):
    """
    A value expressed as multiple quantities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    typedQuantities: Optional[List[TypedQuantity]] = Field(None, description="""The quantities required to fully describe the complex value. For example the systolic and diastolic blood pressure quantities""", json_schema_extra = { "linkml_meta": {'alias': 'typedQuantities',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-delimited list of the '
                                             'quantities required to fully describe '
                                             'the complex value. For example, the '
                                             'systolic and diastolic blood pressure '
                                             'quantities.'}},
         'domain_of': ['ComplexValue']} })


class Measurement(ConfiguredBaseModel):
    """
    FHIR mapping: Observation (https://www.hl7.org/fhir/observation.html)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'value': {'name': 'value',
                                                                                         'required': True}}},
                                                          {'slot_conditions': {'complexValue': {'name': 'complexValue',
                                                                                                'required': True}}}]}}]})

    assay: Optional[str] = Field(None, description="""An ontology class which describes the assay used to produce the measurement. For example \"body temperature\" (CMO:0000015) or \"Platelets [#/volume] in Blood\" (LOINC:26515-7) FHIR mapping: Observation.code'""", json_schema_extra = { "linkml_meta": {'alias': 'assay',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the assay used to produce '
                                             'the measurement. This will generally be '
                                             'the name of a property rather than a '
                                             'procedure, e.g., "plasma immunoglobulin '
                                             'G level" is an assay but "biopsy" is not '
                                             '- that is a procedure. Do not include '
                                             'acronyms or abbreviations; if the assay '
                                             'is referred to with an acronym then '
                                             'expand to its full name.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'body temperature; platelets in '
                                                      'blood'}},
         'domain_of': ['Measurement']} })
    complexValue: Optional[ComplexValue] = Field(None, description="""The measurement result, expressed as multiple values.""", json_schema_extra = { "linkml_meta": {'alias': 'complexValue',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The measurement result, expressed as '
                                             'multiple values.'}},
         'domain_of': ['Measurement']} })
    description: Optional[str] = Field(None, description="""Free-text description of the feature. Note this is not a acceptable place to document/describe the phenotype - the type and onset etc... fields should be used for this purpose.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Free-text description of the feature. '
                                             'Describe only the observed feature, not '
                                             'the phenotype. Do not include type or '
                                             'onset.'}},
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })
    procedure: Optional[Procedure] = Field(None, description="""Clinical procedure performed on the subject in order to produce the measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'procedure',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The clinical procedure performed on the '
                                             'subject in order to produce the '
                                             'measurement. This should include the '
                                             'name of the procedure, the name of the '
                                             'body site, and the time the procedure '
                                             'was performed, if known. If the '
                                             'procedure is not specified, do not '
                                             'include a value for this field.'}},
         'domain_of': ['Biosample', 'Measurement', 'MedicalAction']} })
    timeObserved: Optional[str] = Field(None, description="""The time at which the measurement was made""", json_schema_extra = { "linkml_meta": {'alias': 'timeObserved',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The time at which the measurement was '
                                             'made. This should be an ISO 8601 '
                                             'timestamp.'}},
         'domain_of': ['Measurement']} })
    value: Optional[Value] = Field(None, description="""The result of the measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The result of the measurement. This '
                                             'should be a single value. If the '
                                             'measurement is complex, use the '
                                             'complexValue field.'}},
         'domain_of': ['Measurement',
                       'Quantity',
                       'Expression',
                       'Extension',
                       'IndefiniteRange',
                       'Number']} })


class Quantity(ConfiguredBaseModel):
    """
    A single quantifiable value, along with its units and reference range, if known.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    referenceRange: Optional[ReferenceRange] = Field(None, description="""Reference range for the quantity e.g. The normal range of platelets is 150,000 to 450,000 platelets/uL.""", json_schema_extra = { "linkml_meta": {'alias': 'referenceRange',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The reference range for the quantity. If '
                                             'the reference range is not known, do not '
                                             'include a value for this field.'}},
         'domain_of': ['Quantity']} })
    unit: Optional[str] = Field(None, description="""For instance, NCIT subhierarchy, Unit of Measure (Code C25709), https://www.ebi.ac.uk/ols/ontologies/uo""", json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The unit of measure for the quantity. '
                                             'This should be a human-readable string, '
                                             "e.g. 'mg/dL'. If the unit is not known, "
                                             'this value should be UNKNOWN.'}},
         'domain_of': ['Quantity', 'ReferenceRange']} })
    value: Optional[str] = Field(None, description="""the value of the quantity in the units e.g. 2.0 mg""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The value of the quantity in the units. '
                                             'This should be a single value. Do not '
                                             'include units or any non-numeric value. '
                                             'If the value is not known, this value '
                                             'should be UNKNOWN.'}},
         'domain_of': ['Measurement',
                       'Quantity',
                       'Expression',
                       'Extension',
                       'IndefiniteRange',
                       'Number']} })


class ReferenceRange(ConfiguredBaseModel):
    """
    Reference range of a quantity, or the acceptable \"normal\" range for values of a quantity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    high: Optional[str] = Field(None, description="""Highest value in the reference range.""", json_schema_extra = { "linkml_meta": {'alias': 'high',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Highest value in the reference range. If '
                                             'the high value is not known, do not '
                                             'include a value for this field.'}},
         'domain_of': ['ReferenceRange']} })
    low: Optional[str] = Field(None, description="""Lowest value in the reference range.""", json_schema_extra = { "linkml_meta": {'alias': 'low',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Lowest value in the reference range. If '
                                             'the low value is not known, do not '
                                             'include a value for this field.'}},
         'domain_of': ['ReferenceRange']} })
    unit: Optional[str] = Field(None, description="""Unit of the reference range.""", json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The unit of the reference range. This '
                                             'should be a human-readable string, e.g. '
                                             "'mg/dL'. If the unit is not known, this "
                                             'value should be UNKNOWN.'}},
         'domain_of': ['Quantity', 'ReferenceRange']} })


class TypedQuantity(ConfiguredBaseModel):
    """
    For complex measurements, such as blood pressure where more than one component quantity is required to describe the measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    quantity: Optional[Quantity] = Field(None, description="""e.g. mm Hg""", json_schema_extra = { "linkml_meta": {'alias': 'quantity',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A single quantifiable value of the '
                                             'measurement, along with its units and '
                                             'reference range, if known.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': '120 kg; 55.5 cm; 120 mg/dL '
                                                      '(normal range 70-100 mg/dL)'}},
         'domain_of': ['TypedQuantity', 'Value', 'DoseInterval']} })
    type: Optional[str] = Field(None, description="""e.g. diastolic, systolic""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A categorical or descriptive value of '
                                             'the measurement.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'diastolic blood pressure; '
                                                      'systolic blood pressure'}},
         'domain_of': ['TypedQuantity', 'PhenotypicFeature']} })


class Value(ConfiguredBaseModel):
    """
    A single specific value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'quantity': {'name': 'quantity',
                                                                                            'required': True}}},
                                                          {'slot_conditions': {'ontologyClass': {'name': 'ontologyClass',
                                                                                                 'required': True}}}]}}]})

    ontologyClass: Optional[str] = Field(None, description="""for use with things such as categories 'red', 'yellow' or 'absent'/'present'""", json_schema_extra = { "linkml_meta": {'alias': 'ontologyClass',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A categorical or descriptive value of '
                                             "the measurement, e.g., 'red', 'yellow', "
                                             "'absent', or 'present'."}},
         'domain_of': ['Value', 'TherapeuticRegimen']} })
    quantity: Optional[Quantity] = Field(None, description="""A single quantifiable value.""", json_schema_extra = { "linkml_meta": {'alias': 'quantity',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A single quantifiable value of the '
                                             'measurement, along with its units and '
                                             'reference range, if known.'}},
         'domain_of': ['TypedQuantity', 'Value', 'DoseInterval']} })


class DoseInterval(ConfiguredBaseModel):
    """
    e.g. 50mg/ml 3 times daily for two weeks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    interval: Optional[TimeInterval] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'interval',
         'domain_of': ['TimeElement', 'DoseInterval', 'ChromosomeLocation']} })
    quantity: Optional[Quantity] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'quantity', 'domain_of': ['TypedQuantity', 'Value', 'DoseInterval']} })
    scheduleFrequency: Optional[OntologyClass] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'scheduleFrequency', 'domain_of': ['DoseInterval']} })


class MedicalAction(ConfiguredBaseModel):
    """
    medication, procedure, other actions taken for clinical management
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'procedure': {'name': 'procedure',
                                                                                             'required': True}}},
                                                          {'slot_conditions': {'treatment': {'name': 'treatment',
                                                                                             'required': True}}},
                                                          {'slot_conditions': {'radiationTherapy': {'name': 'radiationTherapy',
                                                                                                    'required': True}}},
                                                          {'slot_conditions': {'therapeuticRegimen': {'name': 'therapeuticRegimen',
                                                                                                      'required': True}}}]}}]})

    adverseEvents: Optional[List[str]] = Field(None, description="""ARGO mapping treatment::adverse_events""", json_schema_extra = { "linkml_meta": {'alias': 'adverseEvents',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-separated list of adverse '
                                             'events associated with the medical '
                                             'action. If no adverse events are '
                                             'specified, do not include a value for '
                                             'this field.'}},
         'domain_of': ['MedicalAction'],
         'exact_mappings': ['ARGO:treatment.adverse_events']} })
    procedure: Optional[Procedure] = Field(None, description="""The procedure performed as part of the medical action.""", json_schema_extra = { "linkml_meta": {'alias': 'procedure',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The procedure performed as part of the '
                                             'medical action. This should include the '
                                             'name of the procedure, the name of the '
                                             'body site, and the time the procedure '
                                             'was performed, if known. If the '
                                             'procedure is not specified, use the same '
                                             'value as the assay field.'}},
         'domain_of': ['Biosample', 'Measurement', 'MedicalAction']} })
    radiationTherapy: Optional[RadiationTherapy] = Field(None, description="""Radiation therapy performed as part of the medical action.""", json_schema_extra = { "linkml_meta": {'alias': 'radiationTherapy',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The radiation therapy performed as part '
                                             'of the medical action. This should '
                                             'include the anatomical site where '
                                             'radiation therapy was administered, the '
                                             'total dose given in units of Gray (Gy), '
                                             'the total number of fractions delivered '
                                             'as part of treatment, and the modality '
                                             'of radiation therapy. If radiation '
                                             'therapy is not specified, do not include '
                                             'a value for this field.'}},
         'domain_of': ['MedicalAction']} })
    responseToTreatment: Optional[str] = Field(None, description="""ARGO mapping treatment::response_to_treatment""", json_schema_extra = { "linkml_meta": {'alias': 'responseToTreatment',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The response to the treatment, described '
                                             'as the phenotype observed as a result of '
                                             'the treatment. If the response is not '
                                             'specified, do not include a value for '
                                             'this field.'}},
         'domain_of': ['MedicalAction'],
         'exact_mappings': ['ARGO:treatment.response_to_treatment']} })
    therapeuticRegimen: Optional[TherapeuticRegimen] = Field(None, description="""The therapeutic regimen established as part of the medical action.""", json_schema_extra = { "linkml_meta": {'alias': 'therapeuticRegimen',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The therapeutic regimen established as '
                                             'part of the medical action. This should '
                                             'include the start and end times of the '
                                             'regimen, the status of the regimen, and '
                                             'any external references to the regimen. '
                                             'If the therapeutic regimen is not '
                                             'specified, do not include a value for '
                                             'this field.'}},
         'domain_of': ['MedicalAction']} })
    treatment: Optional[Treatment] = Field(None, description="""The treatment administered as part of the medical action.""", json_schema_extra = { "linkml_meta": {'alias': 'treatment',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The treatment administered as part of '
                                             'the medical action. If the treatment is '
                                             'not specified, do not include a value '
                                             'for this field.'}},
         'domain_of': ['MedicalAction']} })
    treatmentIntent: Optional[str] = Field(None, description="""Whether the intention of the treatment was curative, palliative, ARGO mapping treatment::treatment_intent""", json_schema_extra = { "linkml_meta": {'alias': 'treatmentIntent',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The intention of the treatment. If the '
                                             'intention is not specified, do not '
                                             'include a value for this field.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Curative Therapy; Palliative '
                                                      'Therapy; Functional '
                                                      'Improvement; Chronic '
                                                      'Management; Diagnostic '
                                                      'Procedure; Preventative '
                                                      'Intervention'}},
         'domain_of': ['MedicalAction'],
         'exact_mappings': ['ARGO:treatment.treatment_intent']} })
    treatmentTarget: Optional[str] = Field(None, description="""The condition or disease that this treatment was intended to address. FHIR mapping Procedure::reasonCode""", json_schema_extra = { "linkml_meta": {'alias': 'treatmentTarget',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The condition or disease that this '
                                             'treatment was intended to address, '
                                             'identified by name. If the treatment '
                                             'target is not specified, do not include '
                                             'a value for this field.'}},
         'domain_of': ['MedicalAction']} })
    treatmentTerminationReason: Optional[str] = Field(None, description="""ARGO mapping treatment::treatment_outcome""", json_schema_extra = { "linkml_meta": {'alias': 'treatmentTerminationReason',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The reason for termination of the '
                                             'treatment. If the reason is not '
                                             'specified, or the treatment was not '
                                             'stopped, do not include a value for this '
                                             'field.'}},
         'domain_of': ['MedicalAction'],
         'exact_mappings': ['ARGO:treatment.treatment_outcome']} })


class RadiationTherapy(ConfiguredBaseModel):
    """
    RadiationTherapy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    bodySite: str = Field(..., description="""The anatomical site where radiation therapy was administered. REQUIRED. ARGO mapping radiation::anatomical_site_irradiated""", json_schema_extra = { "linkml_meta": {'alias': 'bodySite',
         'domain_of': ['RadiationTherapy'],
         'exact_mappings': ['ARGO:radiation.anatomical_site_irradiated']} })
    dosage: Optional[str] = Field(None, description="""The total dose given in units of Gray (Gy). REQUIRED. ARGO mapping radiation::radiation_therapy_dosage""", json_schema_extra = { "linkml_meta": {'alias': 'dosage',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The total dose given in units of Gray '
                                             '(Gy). If the dose is not specified, do '
                                             'not include a value for this field.'}},
         'domain_of': ['RadiationTherapy'],
         'exact_mappings': ['ARGO:radiation.radiation_therapy_dosage']} })
    fractions: Optional[str] = Field(None, description="""The total number of fractions delivered as part of treatment. REQUIRED. ARGO mapping radiation::radiation_therapy_fractions""", json_schema_extra = { "linkml_meta": {'alias': 'fractions',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The total number of fractions delivered '
                                             'as part of treatment. If the number of '
                                             'fractions is not specified, do not '
                                             'include a value for this field.'}},
         'domain_of': ['RadiationTherapy'],
         'exact_mappings': ['ARGO:radiation.radiation_therapy_fractions']} })
    modality: Optional[str] = Field(None, description="""The modality of radiation therapy (e.g., electron, photon,…). REQUIRED. ARGO mapping radiation::radiation_therapy_modality""", json_schema_extra = { "linkml_meta": {'alias': 'modality',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The modality of radiation therapy. If '
                                             'the modality is not specified, do not '
                                             'include a value for this field.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'electron; photon'}},
         'domain_of': ['RadiationTherapy'],
         'exact_mappings': ['ARGO:radiation.radiation_therapy_modality']} })


class TherapeuticRegimen(ConfiguredBaseModel):
    """
    ARGO mapping radiation::radiation_therapy_type (missing)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'externalReference': {'name': 'externalReference',
                                                                                                     'required': True}}},
                                                          {'slot_conditions': {'ontologyClass': {'name': 'ontologyClass',
                                                                                                 'required': True}}}]}}]})

    endTime: Optional[str] = Field(None, description="""end time can be empty which would indicate ongoing""", json_schema_extra = { "linkml_meta": {'alias': 'endTime',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The end time for the regimen. If the '
                                             'regimen is ongoing, do not provide a '
                                             'value for this field.'}},
         'domain_of': ['TherapeuticRegimen']} })
    externalReference: Optional[str] = Field(None, description="""An external reference for the regimen.""", json_schema_extra = { "linkml_meta": {'alias': 'externalReference',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'An external reference for the regimen. '
                                             'If the regimen is not specified or does '
                                             'not have a reference, do not include a '
                                             'value for this field.'}},
         'domain_of': ['TherapeuticRegimen']} })
    ontologyClass: Optional[ProcedureClass] = Field(None, description="""The ontology class for the therapeutic regimen.""", json_schema_extra = { "linkml_meta": {'alias': 'ontologyClass',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The name of the therapeutic regimen. If '
                                             'the regimen is not specified, do not '
                                             'include a value for this field.'}},
         'domain_of': ['Value', 'TherapeuticRegimen']} })
    regimenStatus: Optional[RegimenStatus] = Field(None, description="""Status of the regimen.""", json_schema_extra = { "linkml_meta": {'alias': 'regimenStatus',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The status of the regimen. Must be one '
                                             'of the following: COMPLETED, '
                                             'DISCONTINUED, STARTED, or '
                                             'UNKNOWN_STATUS.'}},
         'domain_of': ['TherapeuticRegimen']} })
    startTime: Optional[str] = Field(None, description="""Start time for the regimen.""", json_schema_extra = { "linkml_meta": {'alias': 'startTime', 'domain_of': ['TherapeuticRegimen']} })


class Treatment(ConfiguredBaseModel):
    """
    ARGO mapping treatment::is_primary_treatment (missing) treatment with an agent, such as a drug
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    agent: Optional[str] = Field(None, description="""Treatment agent""", json_schema_extra = { "linkml_meta": {'alias': 'agent',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The treatment agent, such as a drug or '
                                             'other therapeutic material. If the agent '
                                             'is not specified, do not include a value '
                                             'for this field.'}},
         'domain_of': ['Treatment']} })
    cumulativeDose: Optional[Quantity] = Field(None, description="""ARGO mapping chemotherapy::cumulative_drug_dosage""", json_schema_extra = { "linkml_meta": {'alias': 'cumulativeDose',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The cumulative dose of the treatment '
                                             'agent, with value and units. If the '
                                             'cumulative dose is not specified, do not '
                                             'include a value for this field.'}},
         'domain_of': ['Treatment'],
         'exact_mappings': ['ARGO:chemotherapy.cumulative_drug_dosage']} })
    doseIntervals: Optional[List[str]] = Field(None, description="""Intervals at which the treatment agent is administered.""", json_schema_extra = { "linkml_meta": {'alias': 'doseIntervals', 'domain_of': ['Treatment']} })
    drugType: Optional[DrugType] = Field(None, description="""Type of drug used in the treatment.""", json_schema_extra = { "linkml_meta": {'alias': 'drugType',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The type of drug used in the treatment. '
                                             'Must be one of: '
                                             'ADMINISTRATION_RELATED_TO_PROCEDURE, '
                                             'EHR_MEDICATION_LIST, PRESCRIPTION, or '
                                             'UNKNOWN_DRUG_TYPE. If the drug type is '
                                             'not specified, do not include a value '
                                             'for this field.'}},
         'domain_of': ['Treatment']} })
    routeOfAdministration: Optional[str] = Field(None, description="""Route of administration of the treatment agent.""", json_schema_extra = { "linkml_meta": {'alias': 'routeOfAdministration',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The route of administration of the '
                                             'treatment agent. If the route of '
                                             'administration is not specified, do not '
                                             'include a value for this field.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'Intravenous; Oral; '
                                                      'Subcutaneous; Intramuscular'}},
         'domain_of': ['Treatment']} })


class MetaData(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    created: Optional[str] = Field(None, description="""ISO8601 UTC timestamp for when this phenopacket was created in ISO \"2018-03-01T00:00:00Z\"""", json_schema_extra = { "linkml_meta": {'alias': 'created', 'domain_of': ['MetaData']} })
    createdBy: Optional[str] = Field(None, description="""some kind of identifier for the contributor/ program ARGO sample_registration::program_id""", json_schema_extra = { "linkml_meta": {'alias': 'createdBy', 'domain_of': ['MetaData']} })
    externalReferences: Optional[List[ExternalReference]] = Field(None, description="""External identifiers for this message. These are considered different representation of the same record, not records which are in some other relation with the record at hand. For example this might be a PubMed reference to a study in which the individuals are reported.""", json_schema_extra = { "linkml_meta": {'alias': 'externalReferences', 'domain_of': ['MetaData']} })
    phenopacketSchemaVersion: Optional[str] = Field(None, description="""phenopacket-schema-version used to create this phenopacket""", json_schema_extra = { "linkml_meta": {'alias': 'phenopacketSchemaVersion', 'domain_of': ['MetaData']} })
    resources: Optional[List[Resource]] = Field(None, description="""a listing of the ontologies and resources referenced in the phenopacket""", json_schema_extra = { "linkml_meta": {'alias': 'resources', 'domain_of': ['MetaData']} })
    submittedBy: Optional[str] = Field(None, description="""information about the person/organisation/network that has submitted this phenopacket""", json_schema_extra = { "linkml_meta": {'alias': 'submittedBy', 'domain_of': ['MetaData']} })
    updates: Optional[List[Update]] = Field(None, description="""An OPTIONAL list of Updates to the phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'updates', 'domain_of': ['MetaData']} })


class Resource(ConfiguredBaseModel):
    """
    Description of an external resource used for referencing an object. For example the resource may be an ontology such as the HPO or SNOMED. FHIR mapping: CodeSystem (http://www.hl7.org/fhir/codesystem.html)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    id: Optional[str] = Field(None, description="""for OBO Ontologies, the value of this string MUST always be the official OBO ID, which is always equivalent to the ID prefix in lower case. Examples: hp, go, mp, mondo Consult http://obofoundry.org for a complete list For other ontologies (e.g. SNOMED), use the prefix in identifiers.org\"""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    iriPrefix: Optional[str] = Field(None, description="""Full IRI prefix which can be used with the namespace_prefix and the OntologyClass::id to resolve to an IRI for a term. Tools such as the curie-util (https://github.com/prefixcommons/curie-util) can utilise this to produce fully-resolvable IRIs for an OntologyClass. e.g. Using the HPO term encoding the concept of 'Severe' OntologyClass: id: 'HP:0012828' label: 'Severe' Resource: namespace_prefix: 'HP' iri_prefix: 'http://purl.obolibrary.org/obo/HP_' the term can be resolved to http://purl.obolibrary.org/obo/HP_0012828\"""", json_schema_extra = { "linkml_meta": {'alias': 'iriPrefix', 'domain_of': ['Resource']} })
    name: Optional[str] = Field(None, description="""e.g. The Human Phenotype Ontology for OBO Ontologies, the value of this string SHOULD be the same as the title field on http://obofoundry.org however, this field is purely for information purposes and software should not encode any assumptions""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Extension']} })
    namespacePrefix: Optional[str] = Field(None, description="""The prefix used in the CURIE of an OntologyClass e.g. HP, MP, ECO For example an HPO term will have a CURIE like this - HP:0012828 which should be used in combination with the iri_prefix to form a fully-resolvable IRI""", json_schema_extra = { "linkml_meta": {'alias': 'namespacePrefix', 'domain_of': ['Resource']} })
    url: Optional[str] = Field(None, description="""For OBO ontologies, this should always be the PURL, e.g. http://purl.obolibrary.org/obo/hp.owl, http://purl.obolibrary.org/obo/hp.obo""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Resource']} })
    version: Optional[str] = Field(None, description="""for OBO ontologies, this should be the versionIRI""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Resource', 'Expression']} })


class Update(ConfiguredBaseModel):
    """
    Information about when an update to a record occurred, who or what made the update and any pertinent information regarding the content and/or reason for the update
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    comment: Optional[str] = Field(None, description="""Textual comment about the changes made to the content and/or reason for the update. OPTIONAL""", json_schema_extra = { "linkml_meta": {'alias': 'comment', 'domain_of': ['Update']} })
    timestamp: str = Field(..., description="""ISO8601 UTC timestamps at which this record was updated, in the format YYYY-MM-DDTHH:MM:SS.SSSZ e.g. 2007-12-03T10:15:30.00Z REQUIRED""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp', 'domain_of': ['TimeElement', 'Update']} })
    updatedBy: Optional[str] = Field(None, description="""Information about the person/organisation/network that has updated the phenopacket. OPTIONAL""", json_schema_extra = { "linkml_meta": {'alias': 'updatedBy', 'domain_of': ['Update']} })


class Pedigree(ConfiguredBaseModel):
    """
    https://software.broadinstitute.org/gatk/documentation/article?id=11016
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    persons: Optional[List[Person]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'persons', 'domain_of': ['Pedigree']} })


class Person(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    affectedStatus: Optional[AffectedStatus] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'affectedStatus', 'domain_of': ['Person']} })
    familyId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'familyId', 'domain_of': ['Person']} })
    individualId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'individualId', 'domain_of': ['Biosample', 'Person']} })
    maternalId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'maternalId', 'domain_of': ['Person']} })
    paternalId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'paternalId', 'domain_of': ['Person']} })
    sex: Optional[Sex] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sex', 'domain_of': ['Individual', 'Person']} })


class PhenotypicFeature(ConfiguredBaseModel):
    """
    An individual phenotypic feature, observed as either present or absent (negated), with possible onset, modifiers and frequency FHIR mapping: Condition (https://www.hl7.org/fhir/condition.html) or Observation (https://www.hl7.org/fhir/observation.html)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    description: Optional[str] = Field(None, description="""Free-text description of the phenotype. Note this is not a acceptable place to document/describe the phenotype - the type and onset etc... fields should be used for this purpose.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A free-text description of the observed '
                                             'phenotype. This should be a description '
                                             'of the observation, not the phenotype '
                                             'itself. Do not include type, onset, or '
                                             'other classifications.'}},
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })
    evidence: Optional[List[Evidence]] = Field(None, description="""Evidences for how the phenotype was determined.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Semicolon-delimited list of evidences '
                                             'for how the phenotype was determined. If '
                                             'evidence is not specified, do not '
                                             'include a value for this field.'}},
         'domain_of': ['PhenotypicFeature']} })
    excluded: Optional[str] = Field(None, description="""Flag to indicate whether the phenotype was observed or not. Default is 'false', in other words the phenotype was observed. Therefore it is only required in cases to indicate that the phenotype was looked for, but found to be absent. More formally, this modifier indicates the logical negation of the OntologyClass used in the 'type' field. *CAUTION* It is imperative to check this field for correct interpretation of the phenotype!""", json_schema_extra = { "linkml_meta": {'alias': 'excluded',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A boolean flag to indicate whether the '
                                             'phenotype was observed or not. If the '
                                             'phenotype was observed, this field '
                                             'should be left empty. If the phenotype '
                                             'was not observed, set this field to '
                                             "'true'."}},
         'domain_of': ['Disease', 'PhenotypicFeature']} })
    modifiers: Optional[List[str]] = Field(None, description="""subclasses of HP:0012823 ! Clinical modifier apart from Severity HP:0012824 - Severity""", json_schema_extra = { "linkml_meta": {'alias': 'modifiers',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Semicolon-delimited list of modifiers '
                                             'for the phenotype. This should not '
                                             'include severity modifiers. Do not '
                                             'include a value for this field if no '
                                             'modifiers apply.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'tender; compression fracture; '
                                                      'triggered by stress'}},
         'domain_of': ['PhenotypicFeature']} })
    onset: Optional[str] = Field(None, description="""the values of this will come from the HPO onset hierarchy i.e. subclasses of HP:0003674 FHIR mapping: Condition.onset""", json_schema_extra = { "linkml_meta": {'alias': 'onset',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The onset of the phenotype, or the '
                                             'period of life in which this phenotype '
                                             'was first observed in the individual. '
                                             'For example, "Late onset", "Congenital '
                                             'onset", or "Early young adult onset".'}},
         'domain_of': ['Disease', 'PhenotypicFeature']} })
    resolution: Optional[str] = Field(None, description="""Time required to resolve the phenotype, if applicable.""", json_schema_extra = { "linkml_meta": {'alias': 'resolution',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The time required to resolve the '
                                             'phenotype, if applicable.'}},
         'domain_of': ['Disease', 'PhenotypicFeature']} })
    severity: Optional[str] = Field(None, description="""Severity of the condition e.g. subclasses of HP:0012824-Severity or SNOMED:272141005-Severities FHIR mapping: Condition.severity""", json_schema_extra = { "linkml_meta": {'alias': 'severity',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The severity of the phenotype. If this '
                                             'is not specified, do not include a value '
                                             'for this field.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'borderline; mild; moderate; '
                                                      'profound; severe'}},
         'domain_of': ['PhenotypicFeature']} })
    type: Optional[str] = Field(None, description="""The primary ontology class which describes the phenotype. For example \"HP:0001363\"  \"Craniosynostosis\" FHIR mapping: Condition.identifier'""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A short name for the phenotype.'}},
         'domain_of': ['TypedQuantity', 'PhenotypicFeature']} })


class Expression(ConfiguredBaseModel):
    """
    https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#expression
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    syntax: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'syntax', 'domain_of': ['Expression']} })
    value: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['Measurement',
                       'Quantity',
                       'Expression',
                       'Extension',
                       'IndefiniteRange',
                       'Number']} })
    version: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Resource', 'Expression']} })


class Extension(ConfiguredBaseModel):
    """
    https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#extension
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    name: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Resource', 'Extension']} })
    value: Optional[List[str]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['Measurement',
                       'Quantity',
                       'Expression',
                       'Extension',
                       'IndefiniteRange',
                       'Number']} })


class GeneDescriptor(ConfiguredBaseModel):
    """
    https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#gene-descriptor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    alternateIds: Optional[List[str]] = Field(None, description="""Alternate IDs (should be CURIE) for the same concept may be placed in alternate_ids""", json_schema_extra = { "linkml_meta": {'alias': 'alternateIds', 'domain_of': ['Individual', 'GeneDescriptor']} })
    alternateSymbols: Optional[List[str]] = Field(None, description="""Takes the place of alternate_labels field in a generic descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'alternateSymbols', 'domain_of': ['GeneDescriptor']} })
    description: Optional[str] = Field(None, description="""A free-text description of the value object""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })
    symbol: Optional[str] = Field(None, description="""The primary gene symbol. Takes the place of the label field in a generic descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'symbol', 'domain_of': ['GeneDescriptor']} })
    valueId: Optional[str] = Field(None, description="""The official gene identifier as designated by the organism gene nomenclature committee e.g. HGNC:3477 or MGI:2385071 This should be a CURIE linking the reference to a namespace where it can be retrieved. Mirrors the value_id field of a generic value object descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'valueId', 'domain_of': ['GeneDescriptor']} })
    xrefs: Optional[List[str]] = Field(None, description="""Related concept IDs (e.g. gene ortholog IDs) may be placed in xrefs""", json_schema_extra = { "linkml_meta": {'alias': 'xrefs', 'domain_of': ['GeneDescriptor', 'VariationDescriptor']} })


class VariationDescriptor(ConfiguredBaseModel):
    """
    Variation descriptions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    allelicState: Optional[str] = Field(None, description="""We RECOMMEND that the allelic_state of variant be described by terms from the Genotype Ontology (GENO). These SHOULD descend from concept GENO:0000875.""", json_schema_extra = { "linkml_meta": {'alias': 'allelicState',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The allelic state of the variant, i.e., '
                                             'the allelic variability at a specific '
                                             'locus. This may specify zygosity (such '
                                             'as whether the allele is homozygous or '
                                             'heterozygous) or other allelic states '
                                             'such as heteroplasmy. If the allelic '
                                             'state is not known, this value should '
                                             'not be included.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'homozygous; heterozygous'}},
         'domain_of': ['VariationDescriptor']} })
    alternateLabels: Optional[List[str]] = Field(None, description="""Common aliases for a variant, e.g. EGFR vIII, are alternate labels""", json_schema_extra = { "linkml_meta": {'alias': 'alternateLabels',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-delimited list of common '
                                             'aliases for a variation.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'EGFR vIII'}},
         'domain_of': ['VariationDescriptor']} })
    description: Optional[str] = Field(None, description="""A description of the variant.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A free-text description of the variant. '
                                             'This should be a description of the '
                                             'variant, not the variation itself.'}},
         'domain_of': ['Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Measurement',
                       'PhenotypicFeature',
                       'GeneDescriptor',
                       'VariationDescriptor']} })
    expressions: Optional[List[str]] = Field(None, description="""HGVS, SPDI, and gnomAD-style strings should be represented as Expressions""", json_schema_extra = { "linkml_meta": {'alias': 'expressions',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-delimited list of '
                                             'expressions for the variant, in a string '
                                             'representation such as the Human Genome '
                                             'Variation Society (HGVS) nomenclature.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'NM_000256.3:c.1504C>T'}},
         'domain_of': ['VariationDescriptor']} })
    extensions: Optional[List[str]] = Field(None, description="""Extension field for the variant.""", json_schema_extra = { "linkml_meta": {'alias': 'extensions',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-delimited list of extensions '
                                             'for the variant.'}},
         'domain_of': ['VariationDescriptor']} })
    geneContext: Optional[str] = Field(None, description="""A specific gene context that applies to this variant.""", json_schema_extra = { "linkml_meta": {'alias': 'geneContext',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A specific gene context that applies to '
                                             'this variant.'}},
         'domain_of': ['VariationDescriptor']} })
    id: Optional[str] = Field(None, description="""identifier for the variant, specific to this phenopacket.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'An identifier for the variant, specific '
                                             'to this phenopacket.'}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""A label for this variant.""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A label for this variant. This should be '
                                             'a human-readable string that describes '
                                             'the variant.'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor']} })
    moleculeContext: Optional[str] = Field(None, description="""The molecular context of the vrs variation. Must be one of “genomic”, “transcript”, or “protein”. Defaults to \"unspecified_molecule_context\"""", json_schema_extra = { "linkml_meta": {'alias': 'moleculeContext',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The molecular context of the variant. '
                                             'Must be one of "genomic", "transcript", '
                                             '"protein", or '
                                             '"unspecified_molecule_context".'}},
         'domain_of': ['VariationDescriptor']} })
    structuralType: Optional[str] = Field(None, description="""The structural variant type associated with this variant, such as a substitution, deletion, or fusion. We RECOMMEND using a descendent term of SO:0001537.""", json_schema_extra = { "linkml_meta": {'alias': 'structuralType',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'The structural variant type associated '
                                             'with this variant.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'substitution; deletion; '
                                                      'fusion'}},
         'domain_of': ['VariationDescriptor']} })
    variation: Optional[str] = Field(None, description="""Details on the variation, including its membership in a set of alleles.""", json_schema_extra = { "linkml_meta": {'alias': 'variation',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'Details on the variation, including its '
                                             'membership in a set of alleles.'}},
         'domain_of': ['VariationDescriptor']} })
    vcfRecord: Optional[str] = Field(None, description="""A VCF Record of the variant. This SHOULD be a single allele, the VCF genotype (GT) field should be represented in the allelic_state""", json_schema_extra = { "linkml_meta": {'alias': 'vcfRecord',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A VCF Record of the variant. This should '
                                             'be a single allele. The VCF genotype '
                                             '(GT) field should be represented in the '
                                             'allelic_state.'}},
         'domain_of': ['VariationDescriptor']} })
    vrsRefAlleleSeq: Optional[str] = Field(None, description="""A Sequence corresponding to a “ref allele”, describing the sequence expected at a SequenceLocation reference.""", json_schema_extra = { "linkml_meta": {'alias': 'vrsRefAlleleSeq',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A Sequence corresponding to a “ref '
                                             'allele”, describing the sequence '
                                             'expected at a SequenceLocation '
                                             'reference.'}},
         'domain_of': ['VariationDescriptor']} })
    xrefs: Optional[List[str]] = Field(None, description="""Allele registry, ClinVar, or other related IDs should be included as xrefs""", json_schema_extra = { "linkml_meta": {'alias': 'xrefs',
         'annotations': {'prompt': {'tag': 'prompt',
                                    'value': 'A semicolon-delimited list of related '
                                             'IDs for the variant.'},
                         'prompt.examples': {'tag': 'prompt.examples',
                                             'value': 'ClinVar:12345; dbSNP:rs12345'}},
         'domain_of': ['GeneDescriptor', 'VariationDescriptor']} })


class VcfRecord(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    alt: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'alt', 'domain_of': ['VcfRecord']} })
    chrom: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'chrom', 'domain_of': ['VcfRecord']} })
    filter: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'filter', 'domain_of': ['VcfRecord']} })
    genomeAssembly: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'genomeAssembly', 'domain_of': ['VcfRecord']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    info: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'info', 'domain_of': ['VcfRecord']} })
    pos: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'pos', 'domain_of': ['VcfRecord']} })
    qual: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'qual', 'domain_of': ['VcfRecord']} })
    ref: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'ref', 'domain_of': ['VcfRecord']} })


class Abundance(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'copyNumber': {'name': 'copyNumber',
                                                                                              'required': True}}}]}}]})

    copyNumber: Optional[CopyNumber] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'copyNumber',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Abundance', 'Member', 'SystemicVariation', 'Variation']} })


class Allele(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'literalSequenceExpression': {'name': 'literalSequenceExpression',
                                                                                                             'required': True}}},
                                                          {'slot_conditions': {'derivedSequenceExpression': {'name': 'derivedSequenceExpression',
                                                                                                             'required': True}}},
                                                          {'slot_conditions': {'repeatedSequenceExpression': {'name': 'repeatedSequenceExpression',
                                                                                                              'required': True}}}]}}]})

    chromosomeLocation: Optional[ChromosomeLocation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'chromosomeLocation',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['Allele', 'Location']} })
    curie: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'curie',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Allele', 'CopyNumber', 'Member']} })
    derivedSequenceExpression: Optional[DerivedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'derivedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 6}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    literalSequenceExpression: Optional[LiteralSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'literalSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 5}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    repeatedSequenceExpression: Optional[RepeatedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'repeatedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 7}},
         'domain_of': ['Allele', 'CopyNumber', 'SequenceExpression']} })
    sequenceLocation: Optional[SequenceLocation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sequenceLocation',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['Allele', 'Location']} })


class ChromosomeLocation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    chr: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'chr',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['ChromosomeLocation']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    interval: Optional[CytobandInterval] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'interval',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['TimeElement', 'DoseInterval', 'ChromosomeLocation']} })
    speciesId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'speciesId',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['ChromosomeLocation']} })


class CopyNumber(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'number': {'name': 'number',
                                                                                          'required': True}}},
                                                          {'slot_conditions': {'indefiniteRange': {'name': 'indefiniteRange',
                                                                                                   'required': True}}},
                                                          {'slot_conditions': {'definiteRange': {'name': 'definiteRange',
                                                                                                 'required': True}}}]}}]})

    allele: Optional[Allele] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'allele',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    curie: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'curie',
         'annotations': {'rank': {'tag': 'rank', 'value': 8}},
         'domain_of': ['Allele', 'CopyNumber', 'Member']} })
    definiteRange: Optional[DefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'definiteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 11}},
         'domain_of': ['CopyNumber', 'RepeatedSequenceExpression']} })
    derivedSequenceExpression: Optional[DerivedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'derivedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 6}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    gene: Optional[Gene] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['GenomicInterpretation', 'CopyNumber', 'Feature']} })
    haplotype: Optional[Haplotype] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'haplotype',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    indefiniteRange: Optional[IndefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'indefiniteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 10}},
         'domain_of': ['CopyNumber', 'RepeatedSequenceExpression']} })
    literalSequenceExpression: Optional[LiteralSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'literalSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 5}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    number: Optional[Number] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'number',
         'annotations': {'rank': {'tag': 'rank', 'value': 9}},
         'domain_of': ['CopyNumber', 'RepeatedSequenceExpression']} })
    repeatedSequenceExpression: Optional[RepeatedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'repeatedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 7}},
         'domain_of': ['Allele', 'CopyNumber', 'SequenceExpression']} })


class CytobandInterval(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    end: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'end',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })
    start: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'start',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })


class DefiniteRange(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    max: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'max',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['DefiniteRange']} })
    min: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'min',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['DefiniteRange']} })


class DerivedSequenceExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    location: Optional[SequenceLocation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'location',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['DerivedSequenceExpression']} })
    reverseComplement: Optional[bool] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'reverseComplement',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['DerivedSequenceExpression']} })


class Feature(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'gene': {'name': 'gene',
                                                                                        'required': True}}}]}}]})

    gene: Optional[Gene] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['GenomicInterpretation', 'CopyNumber', 'Feature']} })


class Gene(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    geneId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'geneId',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Gene']} })


class Haplotype(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    pass


class IndefiniteRange(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    comparator: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'comparator',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['IndefiniteRange']} })
    value: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'value',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Measurement',
                       'Quantity',
                       'Expression',
                       'Extension',
                       'IndefiniteRange',
                       'Number']} })


class LiteralSequenceExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    sequence: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['LiteralSequenceExpression', 'SequenceState']} })


class Location(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'chromosomeLocation': {'name': 'chromosomeLocation',
                                                                                                      'required': True}}},
                                                          {'slot_conditions': {'sequenceLocation': {'name': 'sequenceLocation',
                                                                                                    'required': True}}}]}}]})

    chromosomeLocation: Optional[ChromosomeLocation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'chromosomeLocation',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Allele', 'Location']} })
    sequenceLocation: Optional[SequenceLocation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sequenceLocation',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Allele', 'Location']} })


class Member(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'curie': {'name': 'curie',
                                                                                         'required': True}}},
                                                          {'slot_conditions': {'allele': {'name': 'allele',
                                                                                          'required': True}}},
                                                          {'slot_conditions': {'haplotype': {'name': 'haplotype',
                                                                                             'required': True}}},
                                                          {'slot_conditions': {'copyNumber': {'name': 'copyNumber',
                                                                                              'required': True}}},
                                                          {'slot_conditions': {'text': {'name': 'text',
                                                                                        'required': True}}},
                                                          {'slot_conditions': {'variationSet': {'name': 'variationSet',
                                                                                                'required': True}}}]}}]})

    allele: Optional[Allele] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'allele',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    copyNumber: Optional[CopyNumber] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'copyNumber',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['Abundance', 'Member', 'SystemicVariation', 'Variation']} })
    curie: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'curie',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Allele', 'CopyNumber', 'Member']} })
    haplotype: Optional[Haplotype] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'haplotype',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    members: Optional[List[Member]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'members',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Cohort', 'Member']} })
    text: Optional[Text] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'text',
         'annotations': {'rank': {'tag': 'rank', 'value': 5}},
         'domain_of': ['Member', 'UtilityVariation', 'Variation']} })
    variationSet: Optional[VariationSet] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'variationSet',
         'annotations': {'rank': {'tag': 'rank', 'value': 6}},
         'domain_of': ['Member', 'UtilityVariation', 'Variation']} })


class MolecularVariation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'allele': {'name': 'allele',
                                                                                          'required': True}}},
                                                          {'slot_conditions': {'haplotype': {'name': 'haplotype',
                                                                                             'required': True}}}]}}]})

    allele: Optional[Allele] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'allele',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    haplotype: Optional[Haplotype] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'haplotype',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })


class Number(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    value: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'value',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Measurement',
                       'Quantity',
                       'Expression',
                       'Extension',
                       'IndefiniteRange',
                       'Number']} })


class RepeatedSequenceExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'number': {'name': 'number',
                                                                                          'required': True}}},
                                                          {'slot_conditions': {'indefiniteRange': {'name': 'indefiniteRange',
                                                                                                   'required': True}}},
                                                          {'slot_conditions': {'definiteRange': {'name': 'definiteRange',
                                                                                                 'required': True}}}]}}]})

    definiteRange: Optional[DefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'definiteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 5}},
         'domain_of': ['CopyNumber', 'RepeatedSequenceExpression']} })
    derivedSequenceExpression: Optional[DerivedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'derivedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    indefiniteRange: Optional[IndefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'indefiniteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['CopyNumber', 'RepeatedSequenceExpression']} })
    literalSequenceExpression: Optional[LiteralSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'literalSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    number: Optional[Number] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'number',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['CopyNumber', 'RepeatedSequenceExpression']} })


class SequenceExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'literalSequenceExpression': {'name': 'literalSequenceExpression',
                                                                                                             'required': True}}},
                                                          {'slot_conditions': {'derivedSequenceExpression': {'name': 'derivedSequenceExpression',
                                                                                                             'required': True}}},
                                                          {'slot_conditions': {'repeatedSequenceExpression': {'name': 'repeatedSequenceExpression',
                                                                                                              'required': True}}}]}}]})

    derivedSequenceExpression: Optional[DerivedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'derivedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    literalSequenceExpression: Optional[LiteralSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'literalSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Allele',
                       'CopyNumber',
                       'RepeatedSequenceExpression',
                       'SequenceExpression']} })
    repeatedSequenceExpression: Optional[RepeatedSequenceExpression] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'repeatedSequenceExpression',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['Allele', 'CopyNumber', 'SequenceExpression']} })


class SequenceInterval(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'endNumber': {'name': 'endNumber',
                                                                                             'required': True}}},
                                                          {'slot_conditions': {'endIndefiniteRange': {'name': 'endIndefiniteRange',
                                                                                                      'required': True}}},
                                                          {'slot_conditions': {'endDefiniteRange': {'name': 'endDefiniteRange',
                                                                                                    'required': True}}}]}}]})

    endDefiniteRange: Optional[DefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'endDefiniteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 6}},
         'domain_of': ['SequenceInterval']} })
    endIndefiniteRange: Optional[IndefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'endIndefiniteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 5}},
         'domain_of': ['SequenceInterval']} })
    endNumber: Optional[Number] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'endNumber',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['SequenceInterval']} })
    startDefiniteRange: Optional[DefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'startDefiniteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['SequenceInterval']} })
    startIndefiniteRange: Optional[IndefiniteRange] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'startIndefiniteRange',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['SequenceInterval']} })
    startNumber: Optional[Number] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'startNumber',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['SequenceInterval']} })


class SequenceLocation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'sequenceInterval': {'name': 'sequenceInterval',
                                                                                                    'required': True}}}]}}]})

    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    sequenceId: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sequenceId',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['SequenceLocation']} })
    sequenceInterval: Optional[SequenceInterval] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sequenceInterval',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['SequenceLocation']} })


class SequenceState(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    sequence: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['LiteralSequenceExpression', 'SequenceState']} })


class SimpleInterval(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    end: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'end',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })
    start: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'start',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['AgeRange',
                       'TimeInterval',
                       'CytobandInterval',
                       'SimpleInterval']} })


class SystemicVariation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'copyNumber': {'name': 'copyNumber',
                                                                                              'required': True}}}]}}]})

    copyNumber: Optional[CopyNumber] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'copyNumber',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Abundance', 'Member', 'SystemicVariation', 'Variation']} })


class Text(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    definition: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'definition',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Text']} })
    id: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'percent_encoded': {'tag': 'percent_encoded', 'value': True},
                         'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })


class UtilityVariation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'text': {'name': 'text',
                                                                                        'required': True}}},
                                                          {'slot_conditions': {'variationSet': {'name': 'variationSet',
                                                                                                'required': True}}}]}}]})

    text: Optional[Text] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'text',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['Member', 'UtilityVariation', 'Variation']} })
    variationSet: Optional[VariationSet] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'variationSet',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['Member', 'UtilityVariation', 'Variation']} })


class Variation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'allele': {'name': 'allele',
                                                                                          'required': True}}},
                                                          {'slot_conditions': {'haplotype': {'name': 'haplotype',
                                                                                             'required': True}}},
                                                          {'slot_conditions': {'copyNumber': {'name': 'copyNumber',
                                                                                              'required': True}}},
                                                          {'slot_conditions': {'text': {'name': 'text',
                                                                                        'required': True}}},
                                                          {'slot_conditions': {'variationSet': {'name': 'variationSet',
                                                                                                'required': True}}}]}}]})

    allele: Optional[Allele] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'allele',
         'annotations': {'rank': {'tag': 'rank', 'value': 1}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    copyNumber: Optional[CopyNumber] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'copyNumber',
         'annotations': {'rank': {'tag': 'rank', 'value': 3}},
         'domain_of': ['Abundance', 'Member', 'SystemicVariation', 'Variation']} })
    haplotype: Optional[Haplotype] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'haplotype',
         'annotations': {'rank': {'tag': 'rank', 'value': 2}},
         'domain_of': ['CopyNumber', 'Member', 'MolecularVariation', 'Variation']} })
    text: Optional[Text] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'text',
         'annotations': {'rank': {'tag': 'rank', 'value': 4}},
         'domain_of': ['Member', 'UtilityVariation', 'Variation']} })
    variationSet: Optional[VariationSet] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'variationSet',
         'annotations': {'rank': {'tag': 'rank', 'value': 5}},
         'domain_of': ['Member', 'UtilityVariation', 'Variation']} })


class VariationSet(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/phenopackets'})

    pass


class AllelicStateClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:geno'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['GENO'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['AllelicStateType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['AllelicStateType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class AdverseEventClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators', 'value': 'bioportal:OAE'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['OAE']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class AnatomyClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:uberon, sqlite:obo:cl'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['UBERON', 'CL']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class AssayClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:cmo'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['CMO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class ChemicalClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:chebi, '
                                                 'sqlite:obo:drugbank'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['CHEBI', 'DRUGBANK']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class DescriptiveClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:pato, sqlite:obo:hp'}},
         'comments': ['HP annotation is specifically for severity subclasses '
                      '(HP:0012823)'],
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['PATO', 'HP']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class DiagnosticMarkerClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['NCIT'],
         'slot_usage': {'id': {'name': 'id',
                               'values_from': ['NCITDiagnosticMarkerType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['NCITDiagnosticMarkerType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class DiseaseClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:mondo'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['MONDO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class EvidenceClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:eco'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['ECO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class GenderClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:gsso'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['GSSO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class IntentClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['NCIT'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['NCITIntentType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['NCITIntentType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class PhenotypeClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators', 'value': 'sqlite:obo:hp'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['HP']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class ProcedureClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:maxo'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['MAXO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class RouteOfAdministrationClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['NCIT'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['NCITROAType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['NCITROAType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class SampleClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:efo'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['EFO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class SampleStatusClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:efo'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['EFO'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['SampleStatusType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['SampleStatusType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class StagingClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['NCIT'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['NCITStagingType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['NCITStagingType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class TumorGradeClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['NCIT'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['NCITTumorGradeType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['NCITTumorGradeType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class TumorProgressionClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['NCIT'],
         'slot_usage': {'id': {'name': 'id',
                               'values_from': ['NCITTumorProgressionType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['NCITTumorProgressionType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class UnitClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators', 'value': 'sqlite:obo:uo'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['UO']})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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


class VariantTypeClass(OntologyClass):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators', 'value': 'sqlite:obo:so'}},
         'from_schema': 'http://w3id.org/ontogpt/phenopackets',
         'id_prefixes': ['SO'],
         'slot_usage': {'id': {'name': 'id', 'values_from': ['VariantType']}}})

    id: str = Field(..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity',
                       'Publication',
                       'Phenopacket',
                       'Family',
                       'Cohort',
                       'ExternalReference',
                       'Biosample',
                       'Interpretation',
                       'Individual',
                       'Resource',
                       'VariationDescriptor',
                       'VcfRecord',
                       'Allele',
                       'ChromosomeLocation',
                       'CopyNumber',
                       'Member',
                       'SequenceLocation',
                       'Text'],
         'values_from': ['VariantType']} })
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity', 'VariationDescriptor'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[List[str]] = Field(None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
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
PhenopacketCollection.model_rebuild()
Phenopacket.model_rebuild()
Family.model_rebuild()
Cohort.model_rebuild()
OntologyClass.model_rebuild()
ExternalReference.model_rebuild()
Evidence.model_rebuild()
Procedure.model_rebuild()
GestationalAge.model_rebuild()
Age.model_rebuild()
AgeRange.model_rebuild()
TimeInterval.model_rebuild()
TimeElement.model_rebuild()
File.model_rebuild()
Biosample.model_rebuild()
Disease.model_rebuild()
Diagnosis.model_rebuild()
GenomicInterpretation.model_rebuild()
Interpretation.model_rebuild()
VariantInterpretation.model_rebuild()
Individual.model_rebuild()
VitalStatus.model_rebuild()
ComplexValue.model_rebuild()
Measurement.model_rebuild()
Quantity.model_rebuild()
ReferenceRange.model_rebuild()
TypedQuantity.model_rebuild()
Value.model_rebuild()
DoseInterval.model_rebuild()
MedicalAction.model_rebuild()
RadiationTherapy.model_rebuild()
TherapeuticRegimen.model_rebuild()
Treatment.model_rebuild()
MetaData.model_rebuild()
Resource.model_rebuild()
Update.model_rebuild()
Pedigree.model_rebuild()
Person.model_rebuild()
PhenotypicFeature.model_rebuild()
Expression.model_rebuild()
Extension.model_rebuild()
GeneDescriptor.model_rebuild()
VariationDescriptor.model_rebuild()
VcfRecord.model_rebuild()
Abundance.model_rebuild()
Allele.model_rebuild()
ChromosomeLocation.model_rebuild()
CopyNumber.model_rebuild()
CytobandInterval.model_rebuild()
DefiniteRange.model_rebuild()
DerivedSequenceExpression.model_rebuild()
Feature.model_rebuild()
Gene.model_rebuild()
Haplotype.model_rebuild()
IndefiniteRange.model_rebuild()
LiteralSequenceExpression.model_rebuild()
Location.model_rebuild()
Member.model_rebuild()
MolecularVariation.model_rebuild()
Number.model_rebuild()
RepeatedSequenceExpression.model_rebuild()
SequenceExpression.model_rebuild()
SequenceInterval.model_rebuild()
SequenceLocation.model_rebuild()
SequenceState.model_rebuild()
SimpleInterval.model_rebuild()
SystemicVariation.model_rebuild()
Text.model_rebuild()
UtilityVariation.model_rebuild()
Variation.model_rebuild()
VariationSet.model_rebuild()
AllelicStateClass.model_rebuild()
AdverseEventClass.model_rebuild()
AnatomyClass.model_rebuild()
AssayClass.model_rebuild()
ChemicalClass.model_rebuild()
DescriptiveClass.model_rebuild()
DiagnosticMarkerClass.model_rebuild()
DiseaseClass.model_rebuild()
EvidenceClass.model_rebuild()
GenderClass.model_rebuild()
IntentClass.model_rebuild()
PhenotypeClass.model_rebuild()
ProcedureClass.model_rebuild()
RouteOfAdministrationClass.model_rebuild()
SampleClass.model_rebuild()
SampleStatusClass.model_rebuild()
StagingClass.model_rebuild()
TumorGradeClass.model_rebuild()
TumorProgressionClass.model_rebuild()
UnitClass.model_rebuild()
VariantTypeClass.model_rebuild()

