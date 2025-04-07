# Auto generated from exposure_outcome.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-07T12:48:52
# Schema: exposure_outcome
#
# id: http://w3id.org/ontogpt/exposure_outcome
# description: Schema to represent metadata associated with exposure-outcome modeling
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
EXPOSURE_OUTCOME = CurieNamespace('exposure_outcome', 'http://w3id.org/ontogpt/exposure_outcome')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = EXPOSURE_OUTCOME


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ExposureEventId(NamedThingId):
    pass


class ChemicalEntityId(NamedThingId):
    pass


class PhenotypeId(NamedThingId):
    pass


@dataclass(repr=False)
class ExposureEventOutcomeCollection(YAMLRoot):
    """
    A collection of exposure events and their associated outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureEventOutcomeCollection"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureEventOutcomeCollection"
    class_name: ClassVar[str] = "ExposureEventOutcomeCollection"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureEventOutcomeCollection

    exposure_event: Optional[Union[str, ExposureEventId]] = None
    outcome: Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.exposure_event is not None and not isinstance(self.exposure_event, ExposureEventId):
            self.exposure_event = ExposureEventId(self.exposure_event)

        if not isinstance(self.outcome, list):
            self.outcome = [self.outcome] if self.outcome is not None else []
        self.outcome = [v if isinstance(v, PhenotypeId) else PhenotypeId(v) for v in self.outcome]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic class for named entities. Often used to anchor identifiers and human-readable labels for ontology
    classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["NamedThing"]
    class_class_curie: ClassVar[str] = "exposure_outcome:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEvent(NamedThing):
    """
    A record of a toxicological exposure, usually representing a chemical or environmental factor impacting an
    organism. Can be mapped to ontology concepts from ECTO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureEvent"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureEvent

    id: Union[str, ExposureEventId] = None
    exposure_substance: Optional[Union[str, URIorCURIE]] = None
    exposure_type: Optional[Union[str, "ExposureTypeEnum"]] = None
    concentration: Optional[str] = None
    duration: Optional[Union[dict, "QuantityValue"]] = None
    frequency: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventId):
            self.id = ExposureEventId(self.id)

        if self.exposure_substance is not None and not isinstance(self.exposure_substance, URIorCURIE):
            self.exposure_substance = URIorCURIE(self.exposure_substance)

        if self.concentration is not None and not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue()

        if self.frequency is not None and not isinstance(self.frequency, QuantityValue):
            self.frequency = QuantityValue()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(NamedThing):
    """
    A chemical compound or drug used as a toxicant in an exposure study. Should ideally map to a CHEBI class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(NamedThing):
    """
    A phenotypic abnormality or observable feature resulting from a toxicant exposure. Should be mapped to Human
    Phenotype Ontology (HPO) where possible.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Phenotype"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Phenotype

    id: Union[str, PhenotypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Abstract class used to group annotation-like records, including quantitative values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Annotation"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Annotation


class QuantityValue(Annotation):
    """
    A measurement represented as a numeric value and an associated unit (e.g. 5 mg/L). Useful for concentration,
    frequency, and duration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["QuantityValue"]
    class_class_curie: ClassVar[str] = "exposure_outcome:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.QuantityValue


class Concentration(QuantityValue):
    """
    A numeric concentration (e.g. 3.5 µg/mL) of a toxicant used in an exposure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Concentration"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Concentration"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Concentration


@dataclass(repr=False)
class ExposureOutcomeEvent(YAMLRoot):
    """
    A specific linkage between an exposure and the resulting phenotypes. A document that contains exposure to outcome
    relations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureOutcomeEvent"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureOutcomeEvent"
    class_name: ClassVar[str] = "ExposureOutcomeEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureOutcomeEvent

    exposure_event: Optional[Union[str, ExposureEventId]] = None
    outcome: Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.exposure_event is not None and not isinstance(self.exposure_event, ExposureEventId):
            self.exposure_event = ExposureEventId(self.exposure_event)

        if not isinstance(self.outcome, list):
            self.outcome = [self.outcome] if self.outcome is not None else []
        self.outcome = [v if isinstance(v, PhenotypeId) else PhenotypeId(v) for v in self.outcome]

        super().__post_init__(**kwargs)


# Enumerations
class ExposureTypeEnum(EnumDefinitionImpl):
    """
    Enumeration of exposure types derived from the ECTO ontology. Free-text values should be mapped to ECTO subclasses
    of 'exposure event' where possible.
    """
    _defn = EnumDefinition(
        name="ExposureTypeEnum",
        description="""Enumeration of exposure types derived from the ECTO ontology. Free-text values should be mapped to ECTO subclasses of 'exposure event' where possible.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=EXPOSURE_OUTCOME.id, name="id", curie=EXPOSURE_OUTCOME.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.id, domain=None, range=URIRef)

slots.name = Slot(uri=EXPOSURE_OUTCOME.name, name="name", curie=EXPOSURE_OUTCOME.curie('name'),
                   model_uri=EXPOSURE_OUTCOME.name, domain=None, range=Optional[str])

slots.exposure_type = Slot(uri=EXPOSURE_OUTCOME.exposure_type, name="exposure_type", curie=EXPOSURE_OUTCOME.curie('exposure_type'),
                   model_uri=EXPOSURE_OUTCOME.exposure_type, domain=None, range=Optional[Union[str, "ExposureTypeEnum"]])

slots.has_unit = Slot(uri=EXPOSURE_OUTCOME.has_unit, name="has_unit", curie=EXPOSURE_OUTCOME.curie('has_unit'),
                   model_uri=EXPOSURE_OUTCOME.has_unit, domain=None, range=Optional[str])

slots.has_numeric_value = Slot(uri=EXPOSURE_OUTCOME.has_numeric_value, name="has_numeric_value", curie=EXPOSURE_OUTCOME.curie('has_numeric_value'),
                   model_uri=EXPOSURE_OUTCOME.has_numeric_value, domain=None, range=Optional[str])

slots.treated_with = Slot(uri=EXPOSURE_OUTCOME.treated_with, name="treated_with", curie=EXPOSURE_OUTCOME.curie('treated_with'),
                   model_uri=EXPOSURE_OUTCOME.treated_with, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.exposure_substance = Slot(uri=EXPOSURE_OUTCOME.exposure_substance, name="exposure_substance", curie=EXPOSURE_OUTCOME.curie('exposure_substance'),
                   model_uri=EXPOSURE_OUTCOME.exposure_substance, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.concentration = Slot(uri=EXPOSURE_OUTCOME.concentration, name="concentration", curie=EXPOSURE_OUTCOME.curie('concentration'),
                   model_uri=EXPOSURE_OUTCOME.concentration, domain=None, range=Optional[str])

slots.duration = Slot(uri=EXPOSURE_OUTCOME.duration, name="duration", curie=EXPOSURE_OUTCOME.curie('duration'),
                   model_uri=EXPOSURE_OUTCOME.duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exposure_event = Slot(uri=EXPOSURE_OUTCOME.exposure_event, name="exposure_event", curie=EXPOSURE_OUTCOME.curie('exposure_event'),
                   model_uri=EXPOSURE_OUTCOME.exposure_event, domain=None, range=Optional[Union[str, ExposureEventId]])

slots.outcome = Slot(uri=EXPOSURE_OUTCOME.outcome, name="outcome", curie=EXPOSURE_OUTCOME.curie('outcome'),
                   model_uri=EXPOSURE_OUTCOME.outcome, domain=None, range=Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]])

slots.frequency = Slot(uri=EXPOSURE_OUTCOME.frequency, name="frequency", curie=EXPOSURE_OUTCOME.curie('frequency'),
                   model_uri=EXPOSURE_OUTCOME.frequency, domain=None, range=Optional[Union[dict, QuantityValue]])
