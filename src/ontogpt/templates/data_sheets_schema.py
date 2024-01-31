from __future__ import annotations
from datetime import datetime, date
from enum import Enum

from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict,  Field, field_validator
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra = 'forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)
    pass


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
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Information(ConfiguredBaseModel):
    """
    Grouping for datasets and data files
    """
    compression: Optional[CompressionEnum] = Field(None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""")
    conforms_to: Optional[str] = Field(None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""")
    conforms_to_class: Optional[str] = Field(None, description="""The class in the schema to which the data object instantiates.""")
    conforms_to_schema: Optional[str] = Field(None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""")
    created_by: Optional[List[str]] = Field(default_factory=list, description="""Agent that created the element""")
    created_on: Optional[str] = Field(None, description="""Date and Time at which the element was created""")
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    doi: Optional[str] = Field(None, description="""The Digital Object Identifier of the data, with the doi prefix.""")
    download_url: Optional[str] = Field(None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    issued: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""")
    language: Optional[str] = Field(None, description="""language in which the information is expressed""")
    last_updated_on: Optional[str] = Field(None, description="""Date and Time at which the element was last updated""")
    license: Optional[str] = Field(None, description="""license for the data""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    page: Optional[str] = Field(None)
    publisher: Optional[str] = Field(None)
    status: Optional[str] = Field(None, description="""Status of the element in terms of its maturity or life cycle""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    version: Optional[str] = Field(None, description="""particular version of schema""")
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""")
    
    

class FormatDialect(ConfiguredBaseModel):
    """
    Additional format information for a file
    """
    comment_prefix: Optional[str] = Field(None)
    delimiter: Optional[str] = Field(None)
    double_quote: Optional[str] = Field(None)
    header: Optional[str] = Field(None)
    quote_char: Optional[str] = Field(None)
    
    

class Person(NamedThing):
    """
    An individual human being.
    """
    affiliation: Optional[List[str]] = Field(default_factory=list, description="""The organization(s) to which the person belongs.""")
    email: Optional[str] = Field(None, description="""The email address of the person.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Organization(NamedThing):
    """
    A collection of people acting in common interests.
    """
    email: Optional[str] = Field(None, description="""The email address of the organization.""")
    ror_id: Optional[str] = Field(None, description="""Unique ROR identifier.""")
    wikidata_id: Optional[str] = Field(None, description="""Unique Wikidata identifier.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class DatasetProperty(NamedThing):
    """
    Represents a single property of a dataset, or a set of related properties.
    """
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class DatasetCollection(Information):
    """
    A collection of related datasets, likely containing multiple files of multiple potential purposes and properties.
    """
    resources: Optional[List[str]] = Field(default_factory=list)
    compression: Optional[CompressionEnum] = Field(None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""")
    conforms_to: Optional[str] = Field(None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""")
    conforms_to_class: Optional[str] = Field(None, description="""The class in the schema to which the data object instantiates.""")
    conforms_to_schema: Optional[str] = Field(None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""")
    created_by: Optional[List[str]] = Field(default_factory=list, description="""Agent that created the element""")
    created_on: Optional[str] = Field(None, description="""Date and Time at which the element was created""")
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    doi: Optional[str] = Field(None, description="""The Digital Object Identifier of the data, with the doi prefix.""")
    download_url: Optional[str] = Field(None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    issued: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""")
    language: Optional[str] = Field(None, description="""language in which the information is expressed""")
    last_updated_on: Optional[str] = Field(None, description="""Date and Time at which the element was last updated""")
    license: Optional[str] = Field(None, description="""license for the data""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    page: Optional[str] = Field(None)
    publisher: Optional[str] = Field(None)
    status: Optional[str] = Field(None, description="""Status of the element in terms of its maturity or life cycle""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    version: Optional[str] = Field(None, description="""particular version of schema""")
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""")
    
    

class Dataset(Information):
    """
    A single component of related observations and/or information that can be read, manipulated, transformed, and otherwise interpreted.
    """
    bytes: Optional[int] = Field(None, description="""Size of the data in bytes.""")
    dialect: Optional[str] = Field(None)
    encoding: Optional[EncodingEnum] = Field(None, description="""The encoding of the data. This is not the same as the media type. Rather, this is the encoding of the data in a more specific sense, e.g., UTF-8, ASCII, etc.""")
    format: Optional[FormatEnum] = Field(None, description="""The format of the data. This is not the same as the media type. Rather, this is the format of the data in a more specific sense, e.g., CSV, JSON, etc.""")
    hash: Optional[str] = Field(None, description="""The hash representation of the data, e.g., sha256, md5, etc. Subtypes have their own slots.""")
    md5: Optional[str] = Field(None, description="""The md5 hash representation of the data.""")
    media_type: Optional[str] = Field(None, description="""The media type of the data. This is not the same as the format. Rather, this is the media type of the data in a more general sense, e.g., text/csv, application/json, etc., though as it is defined here the media type can be any string.""")
    path: Optional[str] = Field(None)
    sha256: Optional[str] = Field(None, description="""The sha256 hash representation of the data.""")
    purposes: Optional[List[str]] = Field(default_factory=list)
    tasks: Optional[List[str]] = Field(default_factory=list)
    addressing_gaps: Optional[List[str]] = Field(default_factory=list)
    creators: Optional[List[str]] = Field(default_factory=list)
    funders: Optional[List[str]] = Field(default_factory=list)
    subsets: Optional[List[str]] = Field(default_factory=list)
    instances: Optional[List[str]] = Field(default_factory=list)
    anomalies: Optional[List[str]] = Field(default_factory=list)
    external_resources: Optional[List[str]] = Field(default_factory=list)
    confidential_elements: Optional[List[str]] = Field(default_factory=list)
    content_warnings: Optional[List[str]] = Field(default_factory=list)
    subpopulations: Optional[List[str]] = Field(default_factory=list)
    sensitive_elements: Optional[List[str]] = Field(default_factory=list)
    acquisition_methods: Optional[List[str]] = Field(default_factory=list)
    collection_mechanisms: Optional[List[str]] = Field(default_factory=list)
    sampling_strategies: Optional[List[str]] = Field(default_factory=list)
    data_collectors: Optional[List[str]] = Field(default_factory=list)
    collection_timeframes: Optional[List[str]] = Field(default_factory=list)
    ethical_reviews: Optional[List[str]] = Field(default_factory=list)
    data_protection_impacts: Optional[List[str]] = Field(default_factory=list)
    preprocessing_strategies: Optional[List[str]] = Field(default_factory=list)
    cleaning_strategies: Optional[List[str]] = Field(default_factory=list)
    labeling_strategies: Optional[List[str]] = Field(default_factory=list)
    raw_sources: Optional[List[str]] = Field(default_factory=list)
    existing_uses: Optional[List[str]] = Field(default_factory=list)
    use_repository: Optional[List[str]] = Field(default_factory=list)
    other_tasks: Optional[List[str]] = Field(default_factory=list)
    future_use_impacts: Optional[List[str]] = Field(default_factory=list)
    discouraged_uses: Optional[List[str]] = Field(default_factory=list)
    distribution_formats: Optional[List[str]] = Field(default_factory=list)
    distribution_dates: Optional[List[str]] = Field(default_factory=list)
    license_and_use_terms: Optional[str] = Field(None)
    ip_restrictions: Optional[str] = Field(None)
    regulatory_restrictions: Optional[str] = Field(None)
    maintainers: Optional[List[str]] = Field(default_factory=list)
    errata: Optional[List[str]] = Field(default_factory=list)
    updates: Optional[str] = Field(None)
    retention_limit: Optional[str] = Field(None)
    version_access: Optional[str] = Field(None)
    extension_mechanism: Optional[str] = Field(None)
    is_deidentified: Optional[str] = Field(None)
    is_tabular: Optional[str] = Field(None)
    compression: Optional[CompressionEnum] = Field(None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""")
    conforms_to: Optional[str] = Field(None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""")
    conforms_to_class: Optional[str] = Field(None, description="""The class in the schema to which the data object instantiates.""")
    conforms_to_schema: Optional[str] = Field(None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""")
    created_by: Optional[List[str]] = Field(default_factory=list, description="""Agent that created the element""")
    created_on: Optional[str] = Field(None, description="""Date and Time at which the element was created""")
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    doi: Optional[str] = Field(None, description="""The Digital Object Identifier of the data, with the doi prefix.""")
    download_url: Optional[str] = Field(None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    issued: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""")
    language: Optional[str] = Field(None, description="""language in which the information is expressed""")
    last_updated_on: Optional[str] = Field(None, description="""Date and Time at which the element was last updated""")
    license: Optional[str] = Field(None, description="""license for the data""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    page: Optional[str] = Field(None)
    publisher: Optional[str] = Field(None)
    status: Optional[str] = Field(None, description="""Status of the element in terms of its maturity or life cycle""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    version: Optional[str] = Field(None, description="""particular version of schema""")
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""")
    
    

class DataSubset(Dataset):
    """
    A subset of a dataset, likely containing multiple files of multiple potential purposes and properties.
    """
    is_data_split: Optional[str] = Field(None, description="""Is this subset a split of the larger dataset, e.g., is it a set for model training, testing, or validation?""")
    is_subpopulation: Optional[str] = Field(None, description="""Is this subset a subpopulation of the larger dataset, e.g., is it a set of data for a specific demographic?""")
    bytes: Optional[int] = Field(None, description="""Size of the data in bytes.""")
    dialect: Optional[str] = Field(None)
    encoding: Optional[EncodingEnum] = Field(None, description="""The encoding of the data. This is not the same as the media type. Rather, this is the encoding of the data in a more specific sense, e.g., UTF-8, ASCII, etc.""")
    format: Optional[FormatEnum] = Field(None, description="""The format of the data. This is not the same as the media type. Rather, this is the format of the data in a more specific sense, e.g., CSV, JSON, etc.""")
    hash: Optional[str] = Field(None, description="""The hash representation of the data, e.g., sha256, md5, etc. Subtypes have their own slots.""")
    md5: Optional[str] = Field(None, description="""The md5 hash representation of the data.""")
    media_type: Optional[str] = Field(None, description="""The media type of the data. This is not the same as the format. Rather, this is the media type of the data in a more general sense, e.g., text/csv, application/json, etc., though as it is defined here the media type can be any string.""")
    path: Optional[str] = Field(None)
    sha256: Optional[str] = Field(None, description="""The sha256 hash representation of the data.""")
    purposes: Optional[List[str]] = Field(default_factory=list)
    tasks: Optional[List[str]] = Field(default_factory=list)
    addressing_gaps: Optional[List[str]] = Field(default_factory=list)
    creators: Optional[List[str]] = Field(default_factory=list)
    funders: Optional[List[str]] = Field(default_factory=list)
    subsets: Optional[List[str]] = Field(default_factory=list)
    instances: Optional[List[str]] = Field(default_factory=list)
    anomalies: Optional[List[str]] = Field(default_factory=list)
    external_resources: Optional[List[str]] = Field(default_factory=list)
    confidential_elements: Optional[List[str]] = Field(default_factory=list)
    content_warnings: Optional[List[str]] = Field(default_factory=list)
    subpopulations: Optional[List[str]] = Field(default_factory=list)
    sensitive_elements: Optional[List[str]] = Field(default_factory=list)
    acquisition_methods: Optional[List[str]] = Field(default_factory=list)
    collection_mechanisms: Optional[List[str]] = Field(default_factory=list)
    sampling_strategies: Optional[List[str]] = Field(default_factory=list)
    data_collectors: Optional[List[str]] = Field(default_factory=list)
    collection_timeframes: Optional[List[str]] = Field(default_factory=list)
    ethical_reviews: Optional[List[str]] = Field(default_factory=list)
    data_protection_impacts: Optional[List[str]] = Field(default_factory=list)
    preprocessing_strategies: Optional[List[str]] = Field(default_factory=list)
    cleaning_strategies: Optional[List[str]] = Field(default_factory=list)
    labeling_strategies: Optional[List[str]] = Field(default_factory=list)
    raw_sources: Optional[List[str]] = Field(default_factory=list)
    existing_uses: Optional[List[str]] = Field(default_factory=list)
    use_repository: Optional[List[str]] = Field(default_factory=list)
    other_tasks: Optional[List[str]] = Field(default_factory=list)
    future_use_impacts: Optional[List[str]] = Field(default_factory=list)
    discouraged_uses: Optional[List[str]] = Field(default_factory=list)
    distribution_formats: Optional[List[str]] = Field(default_factory=list)
    distribution_dates: Optional[List[str]] = Field(default_factory=list)
    license_and_use_terms: Optional[str] = Field(None)
    ip_restrictions: Optional[str] = Field(None)
    regulatory_restrictions: Optional[str] = Field(None)
    maintainers: Optional[List[str]] = Field(default_factory=list)
    errata: Optional[List[str]] = Field(default_factory=list)
    updates: Optional[str] = Field(None)
    retention_limit: Optional[str] = Field(None)
    version_access: Optional[str] = Field(None)
    extension_mechanism: Optional[str] = Field(None)
    is_deidentified: Optional[str] = Field(None)
    is_tabular: Optional[str] = Field(None)
    compression: Optional[CompressionEnum] = Field(None, description="""The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc.""")
    conforms_to: Optional[str] = Field(None, description="""The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc.""")
    conforms_to_class: Optional[str] = Field(None, description="""The class in the schema to which the data object instantiates.""")
    conforms_to_schema: Optional[str] = Field(None, description="""The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to.""")
    created_by: Optional[List[str]] = Field(default_factory=list, description="""Agent that created the element""")
    created_on: Optional[str] = Field(None, description="""Date and Time at which the element was created""")
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    doi: Optional[str] = Field(None, description="""The Digital Object Identifier of the data, with the doi prefix.""")
    download_url: Optional[str] = Field(None, description="""URL from which the data can be downloaded. This is not the same as the landing page, which is a page that describes the dataset. Rather, this URL points directly to the data itself.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    issued: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(default_factory=list, description="""Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner.""")
    language: Optional[str] = Field(None, description="""language in which the information is expressed""")
    last_updated_on: Optional[str] = Field(None, description="""Date and Time at which the element was last updated""")
    license: Optional[str] = Field(None, description="""license for the data""")
    modified_by: Optional[str] = Field(None, description="""agent that modified the element""")
    page: Optional[str] = Field(None)
    publisher: Optional[str] = Field(None)
    status: Optional[str] = Field(None, description="""Status of the element in terms of its maturity or life cycle""")
    title: Optional[str] = Field(None, description="""the official title of the element""")
    version: Optional[str] = Field(None, description="""particular version of schema""")
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en""")
    
    

class Software(NamedThing):
    """
    A software program or library.
    """
    version: Optional[str] = Field(None)
    license: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Purpose(DatasetProperty):
    """
    For what purpose was the dataset created?
    """
    response: Optional[str] = Field(None)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Task(DatasetProperty):
    """
    Was there a specific task in mind for the dataset's application?
    """
    response: Optional[str] = Field(None)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class AddressingGap(DatasetProperty):
    """
    Was there a specific gap that needed to be filled by creation of the dataset?
    """
    response: Optional[str] = Field(None)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Creator(DatasetProperty):
    """
    Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)? This may also be considered a team.
    """
    principal_investigator: Optional[str] = Field(None)
    affiliation: Optional[str] = Field(None)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class FundingMechanism(DatasetProperty):
    """
    Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number.
    """
    grantor: Optional[str] = Field(None)
    grant: Optional[str] = Field(None)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Grantor(Organization):
    """
    What is the name and/or identifier of the organization providing monetary support or other resources supporting creation of the dataset?
    """
    email: Optional[str] = Field(None, description="""The email address of the organization.""")
    ror_id: Optional[str] = Field(None, description="""Unique ROR identifier.""")
    wikidata_id: Optional[str] = Field(None, description="""Unique Wikidata identifier.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Grant(NamedThing):
    """
    What is the name and/or identifier of the specific mechanism providing monetary support or other resources supporting creation of the dataset?
    """
    grant_number: Optional[str] = Field(None, description="""The alphanumeric identifier for the grant.""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Instance(DatasetProperty):
    """
    What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?
    """
    representation: Optional[str] = Field(None)
    instance_type: Optional[str] = Field(None, description="""Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)?""")
    data_type: Optional[str] = Field(None, description="""What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.""")
    counts: Optional[int] = Field(None, description="""How many instances are there in total (of each type, if appropriate)?""")
    label: Optional[str] = Field(None, description="""Is there a label or target associated with each instance?""")
    sampling_strategies: Optional[List[str]] = Field(default_factory=list)
    missing_information: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class SamplingStrategy(DatasetProperty):
    """
    Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
    """
    is_sample: Optional[List[str]] = Field(default_factory=list)
    is_random: Optional[List[str]] = Field(default_factory=list)
    source_data: Optional[List[str]] = Field(default_factory=list)
    is_representative: Optional[List[str]] = Field(default_factory=list)
    representative_verification: Optional[List[str]] = Field(default_factory=list)
    why_not_representative: Optional[List[str]] = Field(default_factory=list)
    strategies: Optional[List[str]] = Field(default_factory=list, description="""If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?""")
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class MissingInfo(DatasetProperty):
    """
    Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.
    """
    missing: Optional[List[str]] = Field(default_factory=list)
    why_missing: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Relationships(DatasetProperty):
    """
    Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)? If so, please describe how these relationships are made explicit.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class Splits(DatasetProperty):
    """
    Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DataAnomaly(DatasetProperty):
    """
    Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ExternalResource(DatasetProperty):
    """
    Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.
    """
    external_resources: Optional[List[str]] = Field(default_factory=list)
    future_guarantees: Optional[List[str]] = Field(default_factory=list)
    archival: Optional[List[str]] = Field(default_factory=list)
    restrictions: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Confidentiality(DatasetProperty):
    """
    Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor patient confidentiality, data that includes the content of individuals’ non-public communications)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ContentWarning(DatasetProperty):
    """
    Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
    """
    warnings: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Subpopulation(DatasetProperty):
    """
    Does the dataset identify any subpopulations (e.g., by age, gender)? If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.
    """
    identification: Optional[List[str]] = Field(default_factory=list)
    distribution: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""human readable description of the information""")
    
    

class Deidentification(DatasetProperty):
    """
    Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class SensitiveElement(DatasetProperty):
    """
    Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals race or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class InstanceAcquisition(DatasetProperty):
    """
    How was the data associated with each instance acquired? Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If the data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    was_directly_observed: Optional[str] = Field(None, description="""Was the data directly observable (e.g., raw text, movie ratings)?""")
    was_reported_by_subjects: Optional[str] = Field(None, description="""Was the data reported by subjects (e.g., survey responses)?""")
    was_inferred_derived: Optional[str] = Field(None, description="""Was the data indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)?""")
    was_validated_verified: Optional[str] = Field(None, description="""Was the data validated/verified?""")
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class CollectionMechanism(DatasetProperty):
    """
    What mechanisms or procedures were used to collect the data (e.g., hardware apparatuses or sensors, manual human curation, software programs, software APIs)? How were these mechanisms or procedures validated?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DataCollector(DatasetProperty):
    """
    Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class CollectionTimeframe(DatasetProperty):
    """
    Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class EthicalReview(DatasetProperty):
    """
    Were any ethical review processes conducted (e.g., by an institutional review board)? If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DirectCollection(DatasetProperty):
    """
    Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class CollectionNotification(DatasetProperty):
    """
    Were the individuals in question notified about the data collection? If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class CollectionConsent(DatasetProperty):
    """
    Did the individuals in question consent to the collection and use of their data? If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ConsentRevocation(DatasetProperty):
    """
    If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or 8 for certain uses? If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DataProtectionImpact(DatasetProperty):
    """
    Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted? If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class PreprocessingStrategy(DatasetProperty):
    """
    Was any preprocessing of the data done (e.g., discretization or bucketing, tokenization, SIFT feature extraction)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class CleaningStrategy(DatasetProperty):
    """
    Was any cleaning of the data done (e.g., removal of instances, processing of missing values)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class LabelingStrategy(DatasetProperty):
    """
    Was any preprocessing/cleaning/labeling of the data done (e.g., part-of-speech tagging)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class RawData(DatasetProperty):
    """
    Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ExistingUse(DatasetProperty):
    """
    Has the dataset been used for any tasks already?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class UseRepository(DatasetProperty):
    """
    Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class OtherTask(DatasetProperty):
    """
    What (other) tasks could the dataset be used for?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class FutureUseImpact(DatasetProperty):
    """
    Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other risks or harms (e.g., legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DiscouragedUse(DatasetProperty):
    """
    Are there tasks for which the dataset should not be used?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ThirdPartySharing(DatasetProperty):
    """
    Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?
    """
    description: Optional[str] = Field(None)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DistributionFormat(DatasetProperty):
    """
    How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class DistributionDate(DatasetProperty):
    """
    When will the dataset be distributed?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class LicenseAndUseTerms(DatasetProperty):
    """
    Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class IPRestrictions(DatasetProperty):
    """
    Have any third parties imposed IP-based or other restrictions on the data associated with the instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ExportControlRegulatoryRestrictions(DatasetProperty):
    """
    Do any export controls or other regulatory restrictions apply to the dataset or to individual instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class Maintainer(DatasetProperty):
    """
    Who will be supporting/hosting/maintaining the dataset?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class Erratum(DatasetProperty):
    """
    Is there an erratum? If so, please provide a link or other access point.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class UpdatePlan(DatasetProperty):
    """
    Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)? If so, please describe how often, by whom, and how updates will be communicated to dataset consumers (e.g., mailing list, GitHub)?
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class RetentionLimits(DatasetProperty):
    """
    If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were the individuals in question told that their data would be retained for a fixed period of time and then deleted)? If so, please describe these limits and explain how they will be enforced.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class VersionAccess(DatasetProperty):
    """
    Will older versions of the dataset continue to be supported/hosted/maintained? If so, please describe how. If not, please describe how its obsolescence will be communicated to dataset consumers.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    

class ExtensionMechanism(DatasetProperty):
    """
    If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to dataset consumers? If so, please provide a description.
    """
    description: Optional[List[str]] = Field(default_factory=list)
    used_software: Optional[List[str]] = Field(default_factory=list, description="""What software was used as part of this dataset property?""")
    id: str = Field(..., description="""the unique name of the dataset""")
    name: Optional[str] = Field(None)
    
    


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

