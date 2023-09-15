# Auto generated from class_enrichment.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:51:45
# Schema: class-enrichment
#
# id: https://w3id.org/oak/class-enrichment
# description: A datamodel for representing the results of class enrichment on gene sets
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
BPA = CurieNamespace('bpa', 'https://bioportal.bioontology.org/annotator/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OA = CurieNamespace('oa', 'http://www.w3.org/ns/oa#')
ONTOENRICH = CurieNamespace('ontoenrich', 'https://w3id.org/oak/class-enrichment/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SH = CurieNamespace('sh', 'https://w3id.org/shacl/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SSSOM = CurieNamespace('sssom', 'http://w3id.org/sssom/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ONTOENRICH


# Types
class Position(Integer):
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "Position"
    type_model_uri = ONTOENRICH.Position


# Class references



@dataclass
class ClassEnrichmentConfiguration(YAMLRoot):
    """
    configuration for search
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOENRICH.ClassEnrichmentConfiguration
    class_class_curie: ClassVar[str] = "ontoenrich:ClassEnrichmentConfiguration"
    class_name: ClassVar[str] = "ClassEnrichmentConfiguration"
    class_model_uri: ClassVar[URIRef] = ONTOENRICH.ClassEnrichmentConfiguration

    p_value_cutoff: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.p_value_cutoff):
            self.MissingRequiredField("p_value_cutoff")
        if not isinstance(self.p_value_cutoff, float):
            self.p_value_cutoff = float(self.p_value_cutoff)

        super().__post_init__(**kwargs)


@dataclass
class ClassEnrichmentResultSet(YAMLRoot):
    """
    A collection of enrichemt results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOENRICH.ClassEnrichmentResultSet
    class_class_curie: ClassVar[str] = "ontoenrich:ClassEnrichmentResultSet"
    class_name: ClassVar[str] = "ClassEnrichmentResultSet"
    class_model_uri: ClassVar[URIRef] = ONTOENRICH.ClassEnrichmentResultSet

    results: Optional[Union[Union[dict, "ClassEnrichmentResult"], List[Union[dict, "ClassEnrichmentResult"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="results", slot_type=ClassEnrichmentResult, key_name="class_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ClassEnrichmentResult(YAMLRoot):
    """
    A single enrichment result
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ONTOENRICH.ClassEnrichmentResult
    class_class_curie: ClassVar[str] = "ontoenrich:ClassEnrichmentResult"
    class_name: ClassVar[str] = "ClassEnrichmentResult"
    class_model_uri: ClassVar[URIRef] = ONTOENRICH.ClassEnrichmentResult

    class_id: Union[str, URIorCURIE] = None
    p_value: float = None
    class_label: Optional[str] = None
    rank: Optional[int] = None
    p_value_adjusted: Optional[float] = None
    false_discovery_rate: Optional[float] = None
    fold_enrichment: Optional[float] = None
    probability: Optional[float] = None
    sample_count: Optional[int] = None
    sample_total: Optional[int] = None
    background_count: Optional[int] = None
    background_total: Optional[int] = None
    ancestor_of_more_informative_result: Optional[Union[bool, Bool]] = None
    descendant_of_more_informative_result: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.class_id):
            self.MissingRequiredField("class_id")
        if not isinstance(self.class_id, URIorCURIE):
            self.class_id = URIorCURIE(self.class_id)

        if self._is_empty(self.p_value):
            self.MissingRequiredField("p_value")
        if not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.class_label is not None and not isinstance(self.class_label, str):
            self.class_label = str(self.class_label)

        if self.rank is not None and not isinstance(self.rank, int):
            self.rank = int(self.rank)

        if self.p_value_adjusted is not None and not isinstance(self.p_value_adjusted, float):
            self.p_value_adjusted = float(self.p_value_adjusted)

        if self.false_discovery_rate is not None and not isinstance(self.false_discovery_rate, float):
            self.false_discovery_rate = float(self.false_discovery_rate)

        if self.fold_enrichment is not None and not isinstance(self.fold_enrichment, float):
            self.fold_enrichment = float(self.fold_enrichment)

        if self.probability is not None and not isinstance(self.probability, float):
            self.probability = float(self.probability)

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if self.sample_total is not None and not isinstance(self.sample_total, int):
            self.sample_total = int(self.sample_total)

        if self.background_count is not None and not isinstance(self.background_count, int):
            self.background_count = int(self.background_count)

        if self.background_total is not None and not isinstance(self.background_total, int):
            self.background_total = int(self.background_total)

        if self.ancestor_of_more_informative_result is not None and not isinstance(self.ancestor_of_more_informative_result, Bool):
            self.ancestor_of_more_informative_result = Bool(self.ancestor_of_more_informative_result)

        if self.descendant_of_more_informative_result is not None and not isinstance(self.descendant_of_more_informative_result, Bool):
            self.descendant_of_more_informative_result = Bool(self.descendant_of_more_informative_result)

        super().__post_init__(**kwargs)


# Enumerations
class SortFieldEnum(EnumDefinitionImpl):
    """
    The field to sort by
    """
    ANY = PermissibleValue(text="ANY")
    P_VALUE = PermissibleValue(text="P_VALUE")

    _defn = EnumDefinition(
        name="SortFieldEnum",
        description="The field to sort by",
    )

# Slots
class slots:
    pass

slots.classEnrichmentConfiguration__p_value_cutoff = Slot(uri=ONTOENRICH.p_value_cutoff, name="classEnrichmentConfiguration__p_value_cutoff", curie=ONTOENRICH.curie('p_value_cutoff'),
                   model_uri=ONTOENRICH.classEnrichmentConfiguration__p_value_cutoff, domain=None, range=float)

slots.classEnrichmentResultSet__results = Slot(uri=ONTOENRICH.results, name="classEnrichmentResultSet__results", curie=ONTOENRICH.curie('results'),
                   model_uri=ONTOENRICH.classEnrichmentResultSet__results, domain=None, range=Optional[Union[Union[dict, ClassEnrichmentResult], List[Union[dict, ClassEnrichmentResult]]]])

slots.classEnrichmentResult__class_id = Slot(uri=ONTOENRICH.class_id, name="classEnrichmentResult__class_id", curie=ONTOENRICH.curie('class_id'),
                   model_uri=ONTOENRICH.classEnrichmentResult__class_id, domain=None, range=Union[str, URIorCURIE])

slots.classEnrichmentResult__class_label = Slot(uri=ONTOENRICH.class_label, name="classEnrichmentResult__class_label", curie=ONTOENRICH.curie('class_label'),
                   model_uri=ONTOENRICH.classEnrichmentResult__class_label, domain=None, range=Optional[str])

slots.classEnrichmentResult__rank = Slot(uri=ONTOENRICH.rank, name="classEnrichmentResult__rank", curie=ONTOENRICH.curie('rank'),
                   model_uri=ONTOENRICH.classEnrichmentResult__rank, domain=None, range=Optional[int])

slots.classEnrichmentResult__p_value = Slot(uri=OBI['0000175'], name="classEnrichmentResult__p_value", curie=OBI.curie('0000175'),
                   model_uri=ONTOENRICH.classEnrichmentResult__p_value, domain=None, range=float)

slots.classEnrichmentResult__p_value_adjusted = Slot(uri=ONTOENRICH.p_value_adjusted, name="classEnrichmentResult__p_value_adjusted", curie=ONTOENRICH.curie('p_value_adjusted'),
                   model_uri=ONTOENRICH.classEnrichmentResult__p_value_adjusted, domain=None, range=Optional[float])

slots.classEnrichmentResult__false_discovery_rate = Slot(uri=ONTOENRICH.false_discovery_rate, name="classEnrichmentResult__false_discovery_rate", curie=ONTOENRICH.curie('false_discovery_rate'),
                   model_uri=ONTOENRICH.classEnrichmentResult__false_discovery_rate, domain=None, range=Optional[float])

slots.classEnrichmentResult__fold_enrichment = Slot(uri=ONTOENRICH.fold_enrichment, name="classEnrichmentResult__fold_enrichment", curie=ONTOENRICH.curie('fold_enrichment'),
                   model_uri=ONTOENRICH.classEnrichmentResult__fold_enrichment, domain=None, range=Optional[float])

slots.classEnrichmentResult__probability = Slot(uri=ONTOENRICH.probability, name="classEnrichmentResult__probability", curie=ONTOENRICH.curie('probability'),
                   model_uri=ONTOENRICH.classEnrichmentResult__probability, domain=None, range=Optional[float])

slots.classEnrichmentResult__sample_count = Slot(uri=ONTOENRICH.sample_count, name="classEnrichmentResult__sample_count", curie=ONTOENRICH.curie('sample_count'),
                   model_uri=ONTOENRICH.classEnrichmentResult__sample_count, domain=None, range=Optional[int])

slots.classEnrichmentResult__sample_total = Slot(uri=ONTOENRICH.sample_total, name="classEnrichmentResult__sample_total", curie=ONTOENRICH.curie('sample_total'),
                   model_uri=ONTOENRICH.classEnrichmentResult__sample_total, domain=None, range=Optional[int])

slots.classEnrichmentResult__background_count = Slot(uri=ONTOENRICH.background_count, name="classEnrichmentResult__background_count", curie=ONTOENRICH.curie('background_count'),
                   model_uri=ONTOENRICH.classEnrichmentResult__background_count, domain=None, range=Optional[int])

slots.classEnrichmentResult__background_total = Slot(uri=ONTOENRICH.background_total, name="classEnrichmentResult__background_total", curie=ONTOENRICH.curie('background_total'),
                   model_uri=ONTOENRICH.classEnrichmentResult__background_total, domain=None, range=Optional[int])

slots.classEnrichmentResult__ancestor_of_more_informative_result = Slot(uri=ONTOENRICH.ancestor_of_more_informative_result, name="classEnrichmentResult__ancestor_of_more_informative_result", curie=ONTOENRICH.curie('ancestor_of_more_informative_result'),
                   model_uri=ONTOENRICH.classEnrichmentResult__ancestor_of_more_informative_result, domain=None, range=Optional[Union[bool, Bool]])

slots.classEnrichmentResult__descendant_of_more_informative_result = Slot(uri=ONTOENRICH.descendant_of_more_informative_result, name="classEnrichmentResult__descendant_of_more_informative_result", curie=ONTOENRICH.curie('descendant_of_more_informative_result'),
                   model_uri=ONTOENRICH.classEnrichmentResult__descendant_of_more_informative_result, domain=None, range=Optional[Union[bool, Bool]])