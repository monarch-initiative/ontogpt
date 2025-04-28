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


linkml_meta = LinkMLMeta({'default_prefix': 'data_sheets_schema',
     'default_range': 'string',
     'description': 'A LinkML schema for Datasheets for Datasets.',
     'id': 'https://w3id.org/bridge2ai/data-sheets-schema',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'data-sheets-schema',
     'prefixes': {'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'csvw': {'prefix_prefix': 'csvw',
                           'prefix_reference': 'http://www.w3.org/ns/csvw#'},
                  'data_sheets_schema': {'prefix_prefix': 'data_sheets_schema',
                                         'prefix_reference': 'https://w3id.org/bridge2ai/data-sheets-schema/'},
                  'datasets': {'prefix_prefix': 'datasets',
                               'prefix_reference': 'https://w3id.org/linkml/report'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'formats': {'prefix_prefix': 'formats',
                              'prefix_reference': 'http://www.w3.org/ns/formats/'},
                  'frictionless': {'prefix_prefix': 'frictionless',
                                   'prefix_reference': 'https://specs.frictionlessdata.io/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mediatypes': {'prefix_prefix': 'mediatypes',
                                 'prefix_reference': 'https://www.iana.org/assignments/media-types/'},
                  'pav': {'prefix_prefix': 'pav',
                          'prefix_reference': 'http://purl.org/pav/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sh': {'prefix_prefix': 'sh',
                         'prefix_reference': 'https://w3id.org/shacl/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'void': {'prefix_prefix': 'void',
                           'prefix_reference': 'http://rdfs.org/ns/void#'}},
     'see_also': ['https://bridge2ai.github.io/data-sheets-schema'],
     'source_file': 'src/ontogpt/templates/data_sheets_schema.yaml',
     'subsets': {'Collection': {'description': 'The questions in this section are '
                                               'designed to elicit information '
                                               'that may help researchers and '
                                               'practitioners to create '
                                               'alternative datasets with similar '
                                               'characteristics.',
                                'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                'name': 'Collection'},
                 'Composition': {'description': 'The questions in this section are '
                                                'intended to provide dataset '
                                                'consumers with the information '
                                                'they need to make informed '
                                                'decisions about using the dataset '
                                                'for their chosen tasks. Some of '
                                                'the questions are designed to '
                                                'elicit information about '
                                                'compliance with the EU’s General '
                                                'Data Protection Regulation (GDPR) '
                                                'or comparable regulations in '
                                                'other jurisdictions.',
                                 'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                 'name': 'Composition'},
                 'Distribution': {'description': 'The questions in this section '
                                                 'pertain to dataset distribution.',
                                  'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                  'name': 'Distribution'},
                 'Maintenance': {'description': 'The questions in this section are '
                                                'intended to encourage dataset '
                                                'creators to plan for dataset '
                                                'maintenance and communicate this '
                                                'plan to dataset consumers.',
                                 'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                 'name': 'Maintenance'},
                 'Motivation': {'description': 'The questions in this section are '
                                               'primarily intended to encourage '
                                               'dataset creators to clearly '
                                               'articulate their reasons for '
                                               'creating the dataset and to '
                                               'promote transparency about funding '
                                               'interests. The latter may be '
                                               'particularly relevant for datasets '
                                               'created for research purposes.',
                                'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                'name': 'Motivation'},
                 'Preprocessing-Cleaning-Labeling': {'description': 'The questions '
                                                                    'in this '
                                                                    'section are '
                                                                    'intended to '
                                                                    'provide '
                                                                    'dataset '
                                                                    'consumers '
                                                                    'with the '
                                                                    'information '
                                                                    'they need to '
                                                                    'determine '
                                                                    'whether the '
                                                                    '“raw” data '
                                                                    'has been '
                                                                    'processed in '
                                                                    'ways that are '
                                                                    'compatible '
                                                                    'with their '
                                                                    'chosen tasks.',
                                                     'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                                     'name': 'Preprocessing-Cleaning-Labeling'},
                 'Uses': {'description': 'The questions in this section are '
                                         'intended to encourage dataset creators '
                                         'to reflect on the tasks for which the '
                                         'dataset should and should not be used.',
                          'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                          'name': 'Uses'}},
     'title': 'data-sheets-schema',
     'types': {'ror_identifier': {'description': 'Identifier from Research '
                                                 'Organization Registry.',
                                  'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                  'id_prefixes': ['ror'],
                                  'name': 'ror_identifier',
                                  'typeof': 'uriorcurie'},
               'wikidata_identifier': {'description': 'Identifier from Wikidata '
                                                      'open knowledge base.',
                                       'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
                                       'id_prefixes': ['wikidata'],
                                       'name': 'wikidata_identifier',
                                       'typeof': 'uriorcurie'}}} )

class CreatorOrMaintainerEnum(str, Enum):
    """
    The entity responsible for maintaining a dataset.
    """
    Person = "Person"
    Organization = "Organization"


class MediaTypeEnum(str, Enum):
    csv = "csv"
    rdf_xml = "rdf-xml"


class FormatEnum(str, Enum):
    JSON_LD = "JSON-LD"
    N3 = "N3"
    N_Triples = "N-Triples"
    N_Quads = "N-Quads"
    LD_Patch = "LD Patch"
    Microdata = "Microdata"
    OWL_XML_Serialization = "OWL XML Serialization"
    OWL_Functional_Syntax = "OWL Functional Syntax"
    OWL_Manchester_Syntax = "OWL Manchester Syntax"
    POWDER = "POWDER"
    POWDER_S = "POWDER-S"
    PROV_N = "PROV-N"
    PROV_XML = "PROV-XML"
    RDFa = "RDFa"
    RDFSOLIDUSJSON = "RDF/JSON"
    RDFSOLIDUSXML = "RDF/XML"
    RIF_XML_Syntax = "RIF XML Syntax"
    SPARQL_Results_in_XML = "SPARQL Results in XML"
    SPARQL_Results_in_JSON = "SPARQL Results in JSON"
    SPARQL_Results_in_CSV = "SPARQL Results in CSV"
    SPARQL_Results_in_TSV = "SPARQL Results in TSV"
    Turtle = "Turtle"
    TriG = "TriG"
    YAML = "YAML"
    JSON = "JSON"


class CompressionEnum(str, Enum):
    GZIP = "GZIP"
    TAR = "TAR"
    TARGZIP = "TARGZIP"
    ZIP = "ZIP"


class EncodingEnum(str, Enum):
    ASCII = "ASCII"
    Big5 = "Big5"
    EUC_JP = "EUC-JP"
    EUC_KR = "EUC-KR"
    EUC_TW = "EUC-TW"
    GB2312 = "GB2312"
    HZ_GB_2312 = "HZ-GB-2312"
    ISO_2022_CN_EXT = "ISO-2022-CN-EXT"
    ISO_2022_CN = "ISO-2022-CN"
    ISO_2022_JP_2 = "ISO-2022-JP-2"
    ISO_2022_JP = "ISO-2022-JP"
    ISO_2022_KR = "ISO-2022-KR"
    ISO_8859_10 = "ISO-8859-10"
    ISO_8859_11 = "ISO-8859-11"
    ISO_8859_13 = "ISO-8859-13"
    ISO_8859_14 = "ISO-8859-14"
    ISO_8859_15 = "ISO-8859-15"
    ISO_8859_16 = "ISO-8859-16"
    ISO_8859_1 = "ISO-8859-1"
    ISO_8859_2 = "ISO-8859-2"
    ISO_8859_3 = "ISO-8859-3"
    ISO_8859_4 = "ISO-8859-4"
    ISO_8859_5 = "ISO-8859-5"
    ISO_8859_6 = "ISO-8859-6"
    ISO_8859_7 = "ISO-8859-7"
    ISO_8859_8 = "ISO-8859-8"
    ISO_8859_9 = "ISO-8859-9"
    KOI8_R = "KOI8-R"
    KOI8_U = "KOI8-U"
    Shift_JIS = "Shift_JIS"
    UTF_16 = "UTF-16"
    UTF_32 = "UTF-32"
    UTF_7 = "UTF-7"
    UTF_8 = "UTF-8"



class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:Thing'],
         'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Information(ConfiguredBaseModel):
    """
    Grouping for datasets and data files
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'close_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    compression: Optional[CompressionEnum] = Field(default=None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Information']} })
    conforms_to: Optional[str] = Field(default=None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:conformsTo'} })
    conforms_to_class: Optional[str] = Field(default=None, description="""The class in the schema to which the data object instantiates.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_class',
         'domain_of': ['Information'],
         'is_a': 'conforms_to'} })
    conforms_to_schema: Optional[str] = Field(default=None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_schema',
         'domain_of': ['Information'],
         'exact_mappings': ['frictionless:schema'],
         'is_a': 'conforms_to'} })
    created_by: Optional[list[str]] = Field(default=None, description="""Agent that created the element""", json_schema_extra = { "linkml_meta": {'alias': 'created_by',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdBy'} })
    created_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was created""", json_schema_extra = { "linkml_meta": {'alias': 'created_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdOn'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })
    doi: Optional[str] = Field(default=None, description="""The Digital Object Identifier of the data, with the doi prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'domain_of': ['Information'],
         'examples': [{'value': 'doi:10.48550/arXiv.2310.03666'}]} })
    download_url: Optional[str] = Field(default=None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""", json_schema_extra = { "linkml_meta": {'alias': 'download_url',
         'close_mappings': ['frictionless:path'],
         'domain_of': ['Information'],
         'exact_mappings': ['schema:url'],
         'slot_uri': 'dcat:downloadURL'} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    issued: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'issued', 'domain_of': ['Information'], 'slot_uri': 'dcterms:issued'} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'domain_of': ['Information'],
         'exact_mappings': ['schema:keywords'],
         'singular_name': 'keyword',
         'slot_uri': 'dcat:keyword'} })
    language: Optional[str] = Field(default=None, description="""language in which the information is expressed""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Information']} })
    last_updated_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was last updated""", json_schema_extra = { "linkml_meta": {'alias': 'last_updated_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:lastUpdatedOn'} })
    license: Optional[str] = Field(default=None, description="""license for the data""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['frictionless:licenses'],
         'slot_uri': 'dcterms:license'} })
    modified_by: Optional[str] = Field(default=None, description="""agent that modified the element""", json_schema_extra = { "linkml_meta": {'alias': 'modified_by',
         'domain_of': ['Information'],
         'slot_uri': 'oslc:modifiedBy'} })
    page: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'page', 'domain_of': ['Information'], 'slot_uri': 'dcat:landingPage'} })
    publisher: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:publisher'} })
    status: Optional[str] = Field(default=None, description="""Status of the element in terms of its maturity or life cycle""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['Information'],
         'examples': [{'value': 'bibo:draft'}],
         'slot_uri': 'bibo:status'} })
    title: Optional[str] = Field(default=None, description="""the official title of the element""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Information'], 'slot_uri': 'dcterms:title'} })
    version: Optional[str] = Field(default=None, description="""particular version of schema""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion'],
         'slot_uri': 'pav:version'} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['Information'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class FormatDialect(ConfiguredBaseModel):
    """
    Additional format information for a file
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    comment_prefix: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'comment_prefix', 'domain_of': ['FormatDialect']} })
    delimiter: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'delimiter', 'domain_of': ['FormatDialect']} })
    double_quote: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'double_quote', 'domain_of': ['FormatDialect']} })
    header: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'header', 'domain_of': ['FormatDialect']} })
    quote_char: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'quote_char', 'domain_of': ['FormatDialect']} })


class Person(NamedThing):
    """
    An individual human being.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    affiliation: Optional[list[str]] = Field(default=None, description="""The organization(s) to which the person belongs.""", json_schema_extra = { "linkml_meta": {'alias': 'affiliation', 'domain_of': ['Person', 'Creator']} })
    email: Optional[str] = Field(default=None, description="""The email address of the person.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Person', 'Organization']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Organization(NamedThing):
    """
    A collection of people acting in common interests.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    email: Optional[str] = Field(default=None, description="""The email address of the organization.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Person', 'Organization']} })
    ror_id: Optional[str] = Field(default=None, description="""Unique ROR identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'ror_id',
         'domain_of': ['Organization'],
         'examples': [{'value': 'ROR:02mp31p96'}],
         'values_from': ['ROR']} })
    wikidata_id: Optional[str] = Field(default=None, description="""Unique Wikidata identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'wikidata_id',
         'domain_of': ['Organization'],
         'examples': [{'value': 'WIKIDATA:Q282186'}],
         'values_from': ['WIKIDATA']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class DatasetProperty(NamedThing):
    """
    Represents a single property of a dataset, or a set of related properties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class DatasetCollection(Information):
    """
    A collection of related datasets, likely containing multiple files of multiple potential purposes and properties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['file collection',
                     'dataset collection',
                     'data resource collection'],
         'close_mappings': ['dcat:Catalog'],
         'exact_mappings': ['dcat:Dataset'],
         'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'tree_root': True})

    resources: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'resources', 'domain_of': ['DatasetCollection']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Information']} })
    conforms_to: Optional[str] = Field(default=None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:conformsTo'} })
    conforms_to_class: Optional[str] = Field(default=None, description="""The class in the schema to which the data object instantiates.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_class',
         'domain_of': ['Information'],
         'is_a': 'conforms_to'} })
    conforms_to_schema: Optional[str] = Field(default=None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_schema',
         'domain_of': ['Information'],
         'exact_mappings': ['frictionless:schema'],
         'is_a': 'conforms_to'} })
    created_by: Optional[list[str]] = Field(default=None, description="""Agent that created the element""", json_schema_extra = { "linkml_meta": {'alias': 'created_by',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdBy'} })
    created_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was created""", json_schema_extra = { "linkml_meta": {'alias': 'created_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdOn'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })
    doi: Optional[str] = Field(default=None, description="""The Digital Object Identifier of the data, with the doi prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'domain_of': ['Information'],
         'examples': [{'value': 'doi:10.48550/arXiv.2310.03666'}]} })
    download_url: Optional[str] = Field(default=None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""", json_schema_extra = { "linkml_meta": {'alias': 'download_url',
         'close_mappings': ['frictionless:path'],
         'domain_of': ['Information'],
         'exact_mappings': ['schema:url'],
         'slot_uri': 'dcat:downloadURL'} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    issued: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'issued', 'domain_of': ['Information'], 'slot_uri': 'dcterms:issued'} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'domain_of': ['Information'],
         'exact_mappings': ['schema:keywords'],
         'singular_name': 'keyword',
         'slot_uri': 'dcat:keyword'} })
    language: Optional[str] = Field(default=None, description="""language in which the information is expressed""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Information']} })
    last_updated_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was last updated""", json_schema_extra = { "linkml_meta": {'alias': 'last_updated_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:lastUpdatedOn'} })
    license: Optional[str] = Field(default=None, description="""license for the data""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['frictionless:licenses'],
         'slot_uri': 'dcterms:license'} })
    modified_by: Optional[str] = Field(default=None, description="""agent that modified the element""", json_schema_extra = { "linkml_meta": {'alias': 'modified_by',
         'domain_of': ['Information'],
         'slot_uri': 'oslc:modifiedBy'} })
    page: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'page', 'domain_of': ['Information'], 'slot_uri': 'dcat:landingPage'} })
    publisher: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:publisher'} })
    status: Optional[str] = Field(default=None, description="""Status of the element in terms of its maturity or life cycle""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['Information'],
         'examples': [{'value': 'bibo:draft'}],
         'slot_uri': 'bibo:status'} })
    title: Optional[str] = Field(default=None, description="""the official title of the element""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Information'], 'slot_uri': 'dcterms:title'} })
    version: Optional[str] = Field(default=None, description="""particular version of schema""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion'],
         'slot_uri': 'pav:version'} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['Information'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Dataset(Information):
    """
    A single component of related observations and/or information that can be read, manipulated, transformed, and otherwise interpreted.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['data resource', 'data file', 'data package'],
         'class_uri': 'dcat:Distribution',
         'exact_mappings': ['schema:DataDownload'],
         'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'see_also': ['https://specs.frictionlessdata.io/data-resource']})

    bytes: Optional[int] = Field(default=None, description="""Size of the data in bytes.""", json_schema_extra = { "linkml_meta": {'alias': 'bytes', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:byteSize'} })
    dialect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'dialect', 'domain_of': ['Dataset'], 'slot_uri': 'csvw:dialect'} })
    encoding: Optional[EncodingEnum] = Field(default=None, description="""The encoding of the data. This is not the same as the media type. Rather, this is the encoding of the data in a more specific sense, e.g., UTF-8, ASCII, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'encoding', 'domain_of': ['Dataset']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format of the data. This is not the same as the media type. Rather, this is the format of the data in a more specific sense, e.g., CSV, JSON, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Dataset'], 'slot_uri': 'dcterms:format'} })
    hash: Optional[str] = Field(default=None, description="""The hash representation of the data, e.g., sha256, md5, etc. Subtypes have their own slots.""", json_schema_extra = { "linkml_meta": {'alias': 'hash', 'domain_of': ['Dataset']} })
    md5: Optional[str] = Field(default=None, description="""The md5 hash representation of the data.""", json_schema_extra = { "linkml_meta": {'alias': 'md5', 'domain_of': ['Dataset'], 'is_a': 'hash'} })
    media_type: Optional[str] = Field(default=None, description="""The media type of the data. This is not the same as the format. Rather, this is the media type of the data in a more general sense, e.g., text/csv, application/json, etc., though as it is defined here the media type can be any string.""", json_schema_extra = { "linkml_meta": {'alias': 'media_type',
         'domain_of': ['Dataset'],
         'exact_mappings': ['frictionless:mediatype', 'schema:encodingFormat'],
         'examples': [{'value': 'text/csv'}, {'value': 'application/json'}],
         'slot_uri': 'dcat:mediaType'} })
    path: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'path',
         'close_mappings': ['frictionless:path'],
         'domain_of': ['Dataset']} })
    sha256: Optional[str] = Field(default=None, description="""The sha256 hash representation of the data.""", json_schema_extra = { "linkml_meta": {'alias': 'sha256', 'domain_of': ['Dataset'], 'is_a': 'hash'} })
    purposes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'purposes', 'domain_of': ['Dataset']} })
    tasks: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tasks', 'domain_of': ['Dataset']} })
    addressing_gaps: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'addressing_gaps', 'domain_of': ['Dataset']} })
    creators: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'creators', 'domain_of': ['Dataset']} })
    funders: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'funders', 'domain_of': ['Dataset']} })
    subsets: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subsets',
         'domain_of': ['Dataset'],
         'exact_mappings': ['schema:distribution'],
         'slot_uri': 'dcat:distribution'} })
    instances: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instances', 'domain_of': ['Dataset']} })
    anomalies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'anomalies', 'domain_of': ['Dataset']} })
    external_resources: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'external_resources', 'domain_of': ['Dataset', 'ExternalResource']} })
    confidential_elements: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'confidential_elements', 'domain_of': ['Dataset']} })
    content_warnings: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'content_warnings', 'domain_of': ['Dataset']} })
    subpopulations: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subpopulations', 'domain_of': ['Dataset']} })
    sensitive_elements: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sensitive_elements', 'domain_of': ['Dataset']} })
    acquisition_methods: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'acquisition_methods', 'domain_of': ['Dataset']} })
    collection_mechanisms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collection_mechanisms', 'domain_of': ['Dataset']} })
    sampling_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sampling_strategies', 'domain_of': ['Dataset', 'Instance']} })
    data_collectors: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_collectors', 'domain_of': ['Dataset']} })
    collection_timeframes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collection_timeframes', 'domain_of': ['Dataset']} })
    ethical_reviews: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ethical_reviews', 'domain_of': ['Dataset']} })
    data_protection_impacts: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_protection_impacts', 'domain_of': ['Dataset']} })
    preprocessing_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'preprocessing_strategies', 'domain_of': ['Dataset']} })
    cleaning_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cleaning_strategies', 'domain_of': ['Dataset']} })
    labeling_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'labeling_strategies', 'domain_of': ['Dataset']} })
    raw_sources: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'raw_sources', 'domain_of': ['Dataset']} })
    existing_uses: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'existing_uses', 'domain_of': ['Dataset']} })
    use_repository: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'use_repository', 'domain_of': ['Dataset']} })
    other_tasks: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'other_tasks', 'domain_of': ['Dataset']} })
    future_use_impacts: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'future_use_impacts', 'domain_of': ['Dataset']} })
    discouraged_uses: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'discouraged_uses', 'domain_of': ['Dataset']} })
    distribution_formats: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'distribution_formats', 'domain_of': ['Dataset']} })
    distribution_dates: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'distribution_dates', 'domain_of': ['Dataset']} })
    license_and_use_terms: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'license_and_use_terms', 'domain_of': ['Dataset']} })
    ip_restrictions: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ip_restrictions', 'domain_of': ['Dataset']} })
    regulatory_restrictions: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'regulatory_restrictions', 'domain_of': ['Dataset']} })
    maintainers: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'maintainers', 'domain_of': ['Dataset']} })
    errata: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'errata', 'domain_of': ['Dataset']} })
    updates: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'updates', 'domain_of': ['Dataset']} })
    retention_limit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'retention_limit', 'domain_of': ['Dataset']} })
    version_access: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version_access', 'domain_of': ['Dataset']} })
    extension_mechanism: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extension_mechanism', 'domain_of': ['Dataset']} })
    is_deidentified: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_deidentified', 'domain_of': ['Dataset']} })
    is_tabular: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_tabular', 'domain_of': ['Dataset']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Information']} })
    conforms_to: Optional[str] = Field(default=None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:conformsTo'} })
    conforms_to_class: Optional[str] = Field(default=None, description="""The class in the schema to which the data object instantiates.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_class',
         'domain_of': ['Information'],
         'is_a': 'conforms_to'} })
    conforms_to_schema: Optional[str] = Field(default=None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_schema',
         'domain_of': ['Information'],
         'exact_mappings': ['frictionless:schema'],
         'is_a': 'conforms_to'} })
    created_by: Optional[list[str]] = Field(default=None, description="""Agent that created the element""", json_schema_extra = { "linkml_meta": {'alias': 'created_by',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdBy'} })
    created_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was created""", json_schema_extra = { "linkml_meta": {'alias': 'created_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdOn'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })
    doi: Optional[str] = Field(default=None, description="""The Digital Object Identifier of the data, with the doi prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'domain_of': ['Information'],
         'examples': [{'value': 'doi:10.48550/arXiv.2310.03666'}]} })
    download_url: Optional[str] = Field(default=None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""", json_schema_extra = { "linkml_meta": {'alias': 'download_url',
         'close_mappings': ['frictionless:path'],
         'domain_of': ['Information'],
         'exact_mappings': ['schema:url'],
         'slot_uri': 'dcat:downloadURL'} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    issued: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'issued', 'domain_of': ['Information'], 'slot_uri': 'dcterms:issued'} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'domain_of': ['Information'],
         'exact_mappings': ['schema:keywords'],
         'singular_name': 'keyword',
         'slot_uri': 'dcat:keyword'} })
    language: Optional[str] = Field(default=None, description="""language in which the information is expressed""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Information']} })
    last_updated_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was last updated""", json_schema_extra = { "linkml_meta": {'alias': 'last_updated_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:lastUpdatedOn'} })
    license: Optional[str] = Field(default=None, description="""license for the data""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['frictionless:licenses'],
         'slot_uri': 'dcterms:license'} })
    modified_by: Optional[str] = Field(default=None, description="""agent that modified the element""", json_schema_extra = { "linkml_meta": {'alias': 'modified_by',
         'domain_of': ['Information'],
         'slot_uri': 'oslc:modifiedBy'} })
    page: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'page', 'domain_of': ['Information'], 'slot_uri': 'dcat:landingPage'} })
    publisher: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:publisher'} })
    status: Optional[str] = Field(default=None, description="""Status of the element in terms of its maturity or life cycle""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['Information'],
         'examples': [{'value': 'bibo:draft'}],
         'slot_uri': 'bibo:status'} })
    title: Optional[str] = Field(default=None, description="""the official title of the element""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Information'], 'slot_uri': 'dcterms:title'} })
    version: Optional[str] = Field(default=None, description="""particular version of schema""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion'],
         'slot_uri': 'pav:version'} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['Information'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class DataSubset(Dataset):
    """
    A subset of a dataset, likely containing multiple files of multiple potential purposes and properties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    is_data_split: Optional[str] = Field(default=None, description="""Is this subset a split of the larger dataset, e.g., is it a set for model training, testing, or validation?""", json_schema_extra = { "linkml_meta": {'alias': 'is_data_split', 'domain_of': ['DataSubset']} })
    is_subpopulation: Optional[str] = Field(default=None, description="""Is this subset a subpopulation of the larger dataset, e.g., is it a set of data for a specific demographic?""", json_schema_extra = { "linkml_meta": {'alias': 'is_subpopulation', 'domain_of': ['DataSubset']} })
    bytes: Optional[int] = Field(default=None, description="""Size of the data in bytes.""", json_schema_extra = { "linkml_meta": {'alias': 'bytes', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:byteSize'} })
    dialect: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'dialect', 'domain_of': ['Dataset'], 'slot_uri': 'csvw:dialect'} })
    encoding: Optional[EncodingEnum] = Field(default=None, description="""The encoding of the data. This is not the same as the media type. Rather, this is the encoding of the data in a more specific sense, e.g., UTF-8, ASCII, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'encoding', 'domain_of': ['Dataset']} })
    format: Optional[FormatEnum] = Field(default=None, description="""The format of the data. This is not the same as the media type. Rather, this is the format of the data in a more specific sense, e.g., CSV, JSON, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['Dataset'], 'slot_uri': 'dcterms:format'} })
    hash: Optional[str] = Field(default=None, description="""The hash representation of the data, e.g., sha256, md5, etc. Subtypes have their own slots.""", json_schema_extra = { "linkml_meta": {'alias': 'hash', 'domain_of': ['Dataset']} })
    md5: Optional[str] = Field(default=None, description="""The md5 hash representation of the data.""", json_schema_extra = { "linkml_meta": {'alias': 'md5', 'domain_of': ['Dataset'], 'is_a': 'hash'} })
    media_type: Optional[str] = Field(default=None, description="""The media type of the data. This is not the same as the format. Rather, this is the media type of the data in a more general sense, e.g., text/csv, application/json, etc., though as it is defined here the media type can be any string.""", json_schema_extra = { "linkml_meta": {'alias': 'media_type',
         'domain_of': ['Dataset'],
         'exact_mappings': ['frictionless:mediatype', 'schema:encodingFormat'],
         'examples': [{'value': 'text/csv'}, {'value': 'application/json'}],
         'slot_uri': 'dcat:mediaType'} })
    path: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'path',
         'close_mappings': ['frictionless:path'],
         'domain_of': ['Dataset']} })
    sha256: Optional[str] = Field(default=None, description="""The sha256 hash representation of the data.""", json_schema_extra = { "linkml_meta": {'alias': 'sha256', 'domain_of': ['Dataset'], 'is_a': 'hash'} })
    purposes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'purposes', 'domain_of': ['Dataset']} })
    tasks: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tasks', 'domain_of': ['Dataset']} })
    addressing_gaps: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'addressing_gaps', 'domain_of': ['Dataset']} })
    creators: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'creators', 'domain_of': ['Dataset']} })
    funders: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'funders', 'domain_of': ['Dataset']} })
    subsets: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subsets',
         'domain_of': ['Dataset'],
         'exact_mappings': ['schema:distribution'],
         'slot_uri': 'dcat:distribution'} })
    instances: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instances', 'domain_of': ['Dataset']} })
    anomalies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'anomalies', 'domain_of': ['Dataset']} })
    external_resources: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'external_resources', 'domain_of': ['Dataset', 'ExternalResource']} })
    confidential_elements: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'confidential_elements', 'domain_of': ['Dataset']} })
    content_warnings: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'content_warnings', 'domain_of': ['Dataset']} })
    subpopulations: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subpopulations', 'domain_of': ['Dataset']} })
    sensitive_elements: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sensitive_elements', 'domain_of': ['Dataset']} })
    acquisition_methods: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'acquisition_methods', 'domain_of': ['Dataset']} })
    collection_mechanisms: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collection_mechanisms', 'domain_of': ['Dataset']} })
    sampling_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sampling_strategies', 'domain_of': ['Dataset', 'Instance']} })
    data_collectors: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_collectors', 'domain_of': ['Dataset']} })
    collection_timeframes: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collection_timeframes', 'domain_of': ['Dataset']} })
    ethical_reviews: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ethical_reviews', 'domain_of': ['Dataset']} })
    data_protection_impacts: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_protection_impacts', 'domain_of': ['Dataset']} })
    preprocessing_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'preprocessing_strategies', 'domain_of': ['Dataset']} })
    cleaning_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cleaning_strategies', 'domain_of': ['Dataset']} })
    labeling_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'labeling_strategies', 'domain_of': ['Dataset']} })
    raw_sources: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'raw_sources', 'domain_of': ['Dataset']} })
    existing_uses: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'existing_uses', 'domain_of': ['Dataset']} })
    use_repository: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'use_repository', 'domain_of': ['Dataset']} })
    other_tasks: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'other_tasks', 'domain_of': ['Dataset']} })
    future_use_impacts: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'future_use_impacts', 'domain_of': ['Dataset']} })
    discouraged_uses: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'discouraged_uses', 'domain_of': ['Dataset']} })
    distribution_formats: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'distribution_formats', 'domain_of': ['Dataset']} })
    distribution_dates: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'distribution_dates', 'domain_of': ['Dataset']} })
    license_and_use_terms: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'license_and_use_terms', 'domain_of': ['Dataset']} })
    ip_restrictions: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ip_restrictions', 'domain_of': ['Dataset']} })
    regulatory_restrictions: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'regulatory_restrictions', 'domain_of': ['Dataset']} })
    maintainers: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'maintainers', 'domain_of': ['Dataset']} })
    errata: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'errata', 'domain_of': ['Dataset']} })
    updates: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'updates', 'domain_of': ['Dataset']} })
    retention_limit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'retention_limit', 'domain_of': ['Dataset']} })
    version_access: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version_access', 'domain_of': ['Dataset']} })
    extension_mechanism: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extension_mechanism', 'domain_of': ['Dataset']} })
    is_deidentified: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_deidentified', 'domain_of': ['Dataset']} })
    is_tabular: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_tabular', 'domain_of': ['Dataset']} })
    compression: Optional[CompressionEnum] = Field(default=None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'compression', 'domain_of': ['Information']} })
    conforms_to: Optional[str] = Field(default=None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:conformsTo'} })
    conforms_to_class: Optional[str] = Field(default=None, description="""The class in the schema to which the data object instantiates.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_class',
         'domain_of': ['Information'],
         'is_a': 'conforms_to'} })
    conforms_to_schema: Optional[str] = Field(default=None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to_schema',
         'domain_of': ['Information'],
         'exact_mappings': ['frictionless:schema'],
         'is_a': 'conforms_to'} })
    created_by: Optional[list[str]] = Field(default=None, description="""Agent that created the element""", json_schema_extra = { "linkml_meta": {'alias': 'created_by',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdBy'} })
    created_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was created""", json_schema_extra = { "linkml_meta": {'alias': 'created_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:createdOn'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })
    doi: Optional[str] = Field(default=None, description="""The Digital Object Identifier of the data, with the doi prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'domain_of': ['Information'],
         'examples': [{'value': 'doi:10.48550/arXiv.2310.03666'}]} })
    download_url: Optional[str] = Field(default=None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""", json_schema_extra = { "linkml_meta": {'alias': 'download_url',
         'close_mappings': ['frictionless:path'],
         'domain_of': ['Information'],
         'exact_mappings': ['schema:url'],
         'slot_uri': 'dcat:downloadURL'} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    issued: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'issued', 'domain_of': ['Information'], 'slot_uri': 'dcterms:issued'} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'domain_of': ['Information'],
         'exact_mappings': ['schema:keywords'],
         'singular_name': 'keyword',
         'slot_uri': 'dcat:keyword'} })
    language: Optional[str] = Field(default=None, description="""language in which the information is expressed""", json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['Information']} })
    last_updated_on: Optional[str] = Field(default=None, description="""Date and Time at which the element was last updated""", json_schema_extra = { "linkml_meta": {'alias': 'last_updated_on',
         'domain_of': ['Information'],
         'slot_uri': 'pav:lastUpdatedOn'} })
    license: Optional[str] = Field(default=None, description="""license for the data""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['frictionless:licenses'],
         'slot_uri': 'dcterms:license'} })
    modified_by: Optional[str] = Field(default=None, description="""agent that modified the element""", json_schema_extra = { "linkml_meta": {'alias': 'modified_by',
         'domain_of': ['Information'],
         'slot_uri': 'oslc:modifiedBy'} })
    page: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'page', 'domain_of': ['Information'], 'slot_uri': 'dcat:landingPage'} })
    publisher: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Information'],
         'slot_uri': 'dcterms:publisher'} })
    status: Optional[str] = Field(default=None, description="""Status of the element in terms of its maturity or life cycle""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['Information'],
         'examples': [{'value': 'bibo:draft'}],
         'slot_uri': 'bibo:status'} })
    title: Optional[str] = Field(default=None, description="""the official title of the element""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Information'], 'slot_uri': 'dcterms:title'} })
    version: Optional[str] = Field(default=None, description="""particular version of schema""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['Information', 'Software'],
         'exact_mappings': ['schema:version', 'dcterms:hasVersion'],
         'slot_uri': 'pav:version'} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['Information'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Software(NamedThing):
    """
    A software program or library.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Information', 'Software']} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Information', 'Software']} })
    url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Software']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Purpose(DatasetProperty):
    """
    For what purpose was the dataset created?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Motivation']})

    response: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'response', 'domain_of': ['Purpose', 'Task', 'AddressingGap']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Task(DatasetProperty):
    """
    Was there a specific task in mind for the dataset's application?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Motivation']})

    response: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'response', 'domain_of': ['Purpose', 'Task', 'AddressingGap']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class AddressingGap(DatasetProperty):
    """
    Was there a specific gap that needed to be filled by creation of the dataset?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Motivation']})

    response: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'response', 'domain_of': ['Purpose', 'Task', 'AddressingGap']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Creator(DatasetProperty):
    """
    Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)? This may also be considered a team.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Motivation']})

    principal_investigator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'principal_investigator', 'domain_of': ['Creator']} })
    affiliation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'affiliation', 'domain_of': ['Person', 'Creator']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class FundingMechanism(DatasetProperty):
    """
    Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Motivation']})

    grantor: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'grantor', 'domain_of': ['FundingMechanism']} })
    grant: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'grant', 'domain_of': ['FundingMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Grantor(Organization):
    """
    What is the name and/or identifier of the organization providing monetary support or other resources supporting creation of the dataset?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    email: Optional[str] = Field(default=None, description="""The email address of the organization.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Person', 'Organization']} })
    ror_id: Optional[str] = Field(default=None, description="""Unique ROR identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'ror_id',
         'domain_of': ['Organization'],
         'examples': [{'value': 'ROR:02mp31p96'}],
         'values_from': ['ROR']} })
    wikidata_id: Optional[str] = Field(default=None, description="""Unique Wikidata identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'wikidata_id',
         'domain_of': ['Organization'],
         'examples': [{'value': 'WIKIDATA:Q282186'}],
         'values_from': ['WIKIDATA']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Grant(NamedThing):
    """
    What is the name and/or identifier of the specific mechanism providing monetary support or other resources supporting creation of the dataset?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema'})

    grant_number: Optional[str] = Field(default=None, description="""The alphanumeric identifier for the grant.""", json_schema_extra = { "linkml_meta": {'alias': 'grant_number', 'domain_of': ['Grant']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Instance(DatasetProperty):
    """
    What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    representation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'representation', 'domain_of': ['Instance']} })
    instance_type: Optional[str] = Field(default=None, description="""Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)?""", json_schema_extra = { "linkml_meta": {'alias': 'instance_type', 'domain_of': ['Instance']} })
    data_type: Optional[str] = Field(default=None, description="""What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.""", json_schema_extra = { "linkml_meta": {'alias': 'data_type', 'domain_of': ['Instance']} })
    counts: Optional[int] = Field(default=None, description="""How many instances are there in total (of each type, if appropriate)?""", json_schema_extra = { "linkml_meta": {'alias': 'counts', 'domain_of': ['Instance']} })
    label: Optional[str] = Field(default=None, description="""Is there a label or target associated with each instance?""", json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['Instance']} })
    sampling_strategies: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sampling_strategies', 'domain_of': ['Dataset', 'Instance']} })
    missing_information: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'missing_information', 'domain_of': ['Instance']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class SamplingStrategy(DatasetProperty):
    """
    Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition', 'Collection']})

    is_sample: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_sample', 'domain_of': ['SamplingStrategy']} })
    is_random: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_random', 'domain_of': ['SamplingStrategy']} })
    source_data: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'source_data', 'domain_of': ['SamplingStrategy']} })
    is_representative: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'is_representative', 'domain_of': ['SamplingStrategy']} })
    representative_verification: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'representative_verification', 'domain_of': ['SamplingStrategy']} })
    why_not_representative: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'why_not_representative', 'domain_of': ['SamplingStrategy']} })
    strategies: Optional[list[str]] = Field(default=None, description="""If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?""", json_schema_extra = { "linkml_meta": {'alias': 'strategies', 'domain_of': ['SamplingStrategy']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class MissingInfo(DatasetProperty):
    """
    Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    missing: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'missing', 'domain_of': ['MissingInfo']} })
    why_missing: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'why_missing', 'domain_of': ['MissingInfo']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Relationships(DatasetProperty):
    """
    Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)? If so, please describe how these relationships are made explicit.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class Splits(DatasetProperty):
    """
    Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DataAnomaly(DatasetProperty):
    """
    Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ExternalResource(DatasetProperty):
    """
    Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    external_resources: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'external_resources', 'domain_of': ['Dataset', 'ExternalResource']} })
    future_guarantees: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'future_guarantees', 'domain_of': ['ExternalResource']} })
    archival: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'archival', 'domain_of': ['ExternalResource']} })
    restrictions: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'restrictions', 'domain_of': ['ExternalResource']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Confidentiality(DatasetProperty):
    """
    Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor patient confidentiality, data that includes the content of individuals’ non-public communications)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ContentWarning(DatasetProperty):
    """
    Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    warnings: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'warnings', 'domain_of': ['ContentWarning']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Subpopulation(DatasetProperty):
    """
    Does the dataset identify any subpopulations (e.g., by age, gender)? If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    identification: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'identification', 'domain_of': ['Subpopulation']} })
    distribution: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'distribution', 'domain_of': ['Subpopulation']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""human readable description of the information""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism'],
         'slot_uri': 'dcterms:description'} })


class Deidentification(DatasetProperty):
    """
    Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class SensitiveElement(DatasetProperty):
    """
    Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals race or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Composition']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class InstanceAcquisition(DatasetProperty):
    """
    How was the data associated with each instance acquired? Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If the data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    was_directly_observed: Optional[str] = Field(default=None, description="""Was the data directly observable (e.g., raw text, movie ratings)?""", json_schema_extra = { "linkml_meta": {'alias': 'was_directly_observed', 'domain_of': ['InstanceAcquisition']} })
    was_reported_by_subjects: Optional[str] = Field(default=None, description="""Was the data reported by subjects (e.g., survey responses)?""", json_schema_extra = { "linkml_meta": {'alias': 'was_reported_by_subjects', 'domain_of': ['InstanceAcquisition']} })
    was_inferred_derived: Optional[str] = Field(default=None, description="""Was the data indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)?""", json_schema_extra = { "linkml_meta": {'alias': 'was_inferred_derived', 'domain_of': ['InstanceAcquisition']} })
    was_validated_verified: Optional[str] = Field(default=None, description="""Was the data validated/verified?""", json_schema_extra = { "linkml_meta": {'alias': 'was_validated_verified', 'domain_of': ['InstanceAcquisition']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class CollectionMechanism(DatasetProperty):
    """
    What mechanisms or procedures were used to collect the data (e.g., hardware apparatuses or sensors, manual human curation, software programs, software APIs)? How were these mechanisms or procedures validated?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DataCollector(DatasetProperty):
    """
    Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class CollectionTimeframe(DatasetProperty):
    """
    Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class EthicalReview(DatasetProperty):
    """
    Were any ethical review processes conducted (e.g., by an institutional review board)? If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DirectCollection(DatasetProperty):
    """
    Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class CollectionNotification(DatasetProperty):
    """
    Were the individuals in question notified about the data collection? If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class CollectionConsent(DatasetProperty):
    """
    Did the individuals in question consent to the collection and use of their data? If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ConsentRevocation(DatasetProperty):
    """
    If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or 8 for certain uses? If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DataProtectionImpact(DatasetProperty):
    """
    Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted? If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Collection']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class PreprocessingStrategy(DatasetProperty):
    """
    Was any preprocessing of the data done (e.g., discretization or bucketing, tokenization, SIFT feature extraction)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Preprocessing-Cleaning-Labeling']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class CleaningStrategy(DatasetProperty):
    """
    Was any cleaning of the data done (e.g., removal of instances, processing of missing values)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Preprocessing-Cleaning-Labeling']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class LabelingStrategy(DatasetProperty):
    """
    Was any preprocessing/cleaning/labeling of the data done (e.g., part-of-speech tagging)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Preprocessing-Cleaning-Labeling']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class RawData(DatasetProperty):
    """
    Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Preprocessing-Cleaning-Labeling']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ExistingUse(DatasetProperty):
    """
    Has the dataset been used for any tasks already?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Uses', 'Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class UseRepository(DatasetProperty):
    """
    Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Uses']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class OtherTask(DatasetProperty):
    """
    What (other) tasks could the dataset be used for?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Uses']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class FutureUseImpact(DatasetProperty):
    """
    Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other risks or harms (e.g., legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Uses']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DiscouragedUse(DatasetProperty):
    """
    Are there tasks for which the dataset should not be used?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Uses']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ThirdPartySharing(DatasetProperty):
    """
    Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Distribution']})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DistributionFormat(DatasetProperty):
    """
    How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Distribution']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class DistributionDate(DatasetProperty):
    """
    When will the dataset be distributed?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Distribution']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class LicenseAndUseTerms(DatasetProperty):
    """
    Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Distribution']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class IPRestrictions(DatasetProperty):
    """
    Have any third parties imposed IP-based or other restrictions on the data associated with the instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Distribution']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ExportControlRegulatoryRestrictions(DatasetProperty):
    """
    Do any export controls or other regulatory restrictions apply to the dataset or to individual instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Distribution']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class Maintainer(DatasetProperty):
    """
    Who will be supporting/hosting/maintaining the dataset?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class Erratum(DatasetProperty):
    """
    Is there an erratum? If so, please provide a link or other access point.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class UpdatePlan(DatasetProperty):
    """
    Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)? If so, please describe how often, by whom, and how updates will be communicated to dataset consumers (e.g., mailing list, GitHub)?
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class RetentionLimits(DatasetProperty):
    """
    If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were the individuals in question told that their data would be retained for a fixed period of time and then deleted)? If so, please describe these limits and explain how they will be enforced.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class VersionAccess(DatasetProperty):
    """
    Will older versions of the dataset continue to be supported/hosted/maintained? If so, please describe how. If not, please describe how its obsolescence will be communicated to dataset consumers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


class ExtensionMechanism(DatasetProperty):
    """
    If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to dataset consumers? If so, please provide a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bridge2ai/data-sheets-schema',
         'in_subset': ['Maintenance']})

    description: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing',
                       'Information',
                       'Relationships',
                       'Splits',
                       'DataAnomaly',
                       'Confidentiality',
                       'Deidentification',
                       'SensitiveElement',
                       'InstanceAcquisition',
                       'CollectionMechanism',
                       'DataCollector',
                       'CollectionTimeframe',
                       'EthicalReview',
                       'DirectCollection',
                       'CollectionNotification',
                       'CollectionConsent',
                       'ConsentRevocation',
                       'DataProtectionImpact',
                       'PreprocessingStrategy',
                       'CleaningStrategy',
                       'LabelingStrategy',
                       'RawData',
                       'ExistingUse',
                       'UseRepository',
                       'OtherTask',
                       'FutureUseImpact',
                       'DiscouragedUse',
                       'ThirdPartySharing',
                       'DistributionFormat',
                       'DistributionDate',
                       'LicenseAndUseTerms',
                       'IPRestrictions',
                       'ExportControlRegulatoryRestrictions',
                       'Maintainer',
                       'Erratum',
                       'UpdatePlan',
                       'RetentionLimits',
                       'VersionAccess',
                       'ExtensionMechanism']} })
    used_software: Optional[list[str]] = Field(default=None, description="""What software was used as part of this dataset property?""", json_schema_extra = { "linkml_meta": {'alias': 'used_software', 'domain_of': ['DatasetProperty']} })
    id: str = Field(default=..., description="""the unique name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['NamedThing', 'Information'],
         'exact_mappings': ['schema:name'],
         'slot_uri': 'dcterms:identifier'} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Information.model_rebuild()
FormatDialect.model_rebuild()
Person.model_rebuild()
Organization.model_rebuild()
DatasetProperty.model_rebuild()
DatasetCollection.model_rebuild()
Dataset.model_rebuild()
DataSubset.model_rebuild()
Software.model_rebuild()
Purpose.model_rebuild()
Task.model_rebuild()
AddressingGap.model_rebuild()
Creator.model_rebuild()
FundingMechanism.model_rebuild()
Grantor.model_rebuild()
Grant.model_rebuild()
Instance.model_rebuild()
SamplingStrategy.model_rebuild()
MissingInfo.model_rebuild()
Relationships.model_rebuild()
Splits.model_rebuild()
DataAnomaly.model_rebuild()
ExternalResource.model_rebuild()
Confidentiality.model_rebuild()
ContentWarning.model_rebuild()
Subpopulation.model_rebuild()
Deidentification.model_rebuild()
SensitiveElement.model_rebuild()
InstanceAcquisition.model_rebuild()
CollectionMechanism.model_rebuild()
DataCollector.model_rebuild()
CollectionTimeframe.model_rebuild()
EthicalReview.model_rebuild()
DirectCollection.model_rebuild()
CollectionNotification.model_rebuild()
CollectionConsent.model_rebuild()
ConsentRevocation.model_rebuild()
DataProtectionImpact.model_rebuild()
PreprocessingStrategy.model_rebuild()
CleaningStrategy.model_rebuild()
LabelingStrategy.model_rebuild()
RawData.model_rebuild()
ExistingUse.model_rebuild()
UseRepository.model_rebuild()
OtherTask.model_rebuild()
FutureUseImpact.model_rebuild()
DiscouragedUse.model_rebuild()
ThirdPartySharing.model_rebuild()
DistributionFormat.model_rebuild()
DistributionDate.model_rebuild()
LicenseAndUseTerms.model_rebuild()
IPRestrictions.model_rebuild()
ExportControlRegulatoryRestrictions.model_rebuild()
Maintainer.model_rebuild()
Erratum.model_rebuild()
UpdatePlan.model_rebuild()
RetentionLimits.model_rebuild()
VersionAccess.model_rebuild()
ExtensionMechanism.model_rebuild()

