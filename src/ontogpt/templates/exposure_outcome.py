# Auto generated from exposure_outcome.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-07T11:22:55
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
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
EXPOSURE_OUTCOME = CurieNamespace('exposure_outcome', 'http://w3id.org/ontogpt/exposure_outcome')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = EXPOSURE_OUTCOME


# Types

# Class references
class NamedThingId(extended_str):
    pass


class ExposureEventId(NamedThingId):
    pass


class ChemicalEntityId(NamedThingId):
    pass


class PhenotypeId(NamedThingId):
    pass


@dataclass(repr=False)
class ExposureOutcome(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureOutcome"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureOutcome"
    class_name: ClassVar[str] = "ExposureOutcome"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureOutcome

    main_exposure_outcome_event: Optional[Union[dict, "ResultExposureOutcome"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.main_exposure_outcome_event is not None and not isinstance(self.main_exposure_outcome_event, ResultExposureOutcome):
            self.main_exposure_outcome_event = ResultExposureOutcome(**as_dict(self.main_exposure_outcome_event))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A named entity.
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
    An instance of a toxicological exposure event in the study.  According to ECTO,  an exposure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureEvent"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureEvent

    id: Union[str, ExposureEventId] = None
    exposure_substance: Optional[Union[str, ChemicalEntityId]] = None
    exposure_type: Optional[Union[str, "ExposureTypeEnum"]] = None
    concentration: Optional[Union[dict, "Concentration"]] = None
    duration: Optional[Union[dict, "QuantityValue"]] = None
    frequency: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventId):
            self.id = ExposureEventId(self.id)

        if self.exposure_substance is not None and not isinstance(self.exposure_substance, ChemicalEntityId):
            self.exposure_substance = ChemicalEntityId(self.exposure_substance)

        if self.concentration is not None and not isinstance(self.concentration, Concentration):
            self.concentration = Concentration(**as_dict(self.concentration))

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue(**as_dict(self.duration))

        if self.frequency is not None and not isinstance(self.frequency, QuantityValue):
            self.frequency = QuantityValue(**as_dict(self.frequency))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(NamedThing):
    """
    A chemical compound used as a toxicant in the study.
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

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(NamedThing):
    """
    A phenotype observed in the fish as a result of exposure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Phenotype"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Phenotype

    id: Union[str, PhenotypeId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Annotation"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Annotation


@dataclass(repr=False)
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["QuantityValue"]
    class_class_curie: ClassVar[str] = "exposure_outcome:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.QuantityValue

    has_unit: Optional[str] = None
    has_numeric_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, str):
            self.has_numeric_value = str(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concentration(QuantityValue):
    """
    The concentration of a chemical.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Concentration"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Concentration"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Concentration

    has_unit: Optional[str] = None
    has_numeric_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, str):
            self.has_numeric_value = str(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResultExposureOutcome(YAMLRoot):
    """
    A representation of the phenotype observed in the fish as a result of exposure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ResultExposureOutcome"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ResultExposureOutcome"
    class_name: ClassVar[str] = "ResultExposureOutcome"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ResultExposureOutcome

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
    An enumeration of exposure types derived from the ECTO ontology.
    """
    _defn = EnumDefinition(
        name="ExposureTypeEnum",
        description="An enumeration of exposure types derived from the ECTO ontology.",
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

slots.exposureOutcome__main_exposure_outcome_event = Slot(uri=EXPOSURE_OUTCOME.main_exposure_outcome_event, name="exposureOutcome__main_exposure_outcome_event", curie=EXPOSURE_OUTCOME.curie('main_exposure_outcome_event'),
                   model_uri=EXPOSURE_OUTCOME.exposureOutcome__main_exposure_outcome_event, domain=None, range=Optional[Union[dict, ResultExposureOutcome]])

slots.NamedThing_id = Slot(uri=EXPOSURE_OUTCOME.id, name="NamedThing_id", curie=EXPOSURE_OUTCOME.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.NamedThing_id, domain=NamedThing, range=Union[str, NamedThingId])

slots.NamedThing_name = Slot(uri=EXPOSURE_OUTCOME.name, name="NamedThing_name", curie=EXPOSURE_OUTCOME.curie('name'),
                   model_uri=EXPOSURE_OUTCOME.NamedThing_name, domain=NamedThing, range=Optional[str])

slots.ExposureEvent_exposure_substance = Slot(uri=EXPOSURE_OUTCOME.exposure_substance, name="ExposureEvent_exposure_substance", curie=EXPOSURE_OUTCOME.curie('exposure_substance'),
                   model_uri=EXPOSURE_OUTCOME.ExposureEvent_exposure_substance, domain=ExposureEvent, range=Optional[Union[str, ChemicalEntityId]])

slots.ExposureEvent_concentration = Slot(uri=EXPOSURE_OUTCOME.concentration, name="ExposureEvent_concentration", curie=EXPOSURE_OUTCOME.curie('concentration'),
                   model_uri=EXPOSURE_OUTCOME.ExposureEvent_concentration, domain=ExposureEvent, range=Optional[Union[dict, "Concentration"]])

slots.ChemicalEntity_id = Slot(uri=EXPOSURE_OUTCOME.id, name="ChemicalEntity_id", curie=EXPOSURE_OUTCOME.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.ChemicalEntity_id, domain=ChemicalEntity, range=Union[str, ChemicalEntityId],
                   pattern=re.compile(r'^CHEBI:\d+$'))

slots.ChemicalEntity_name = Slot(uri=EXPOSURE_OUTCOME.name, name="ChemicalEntity_name", curie=EXPOSURE_OUTCOME.curie('name'),
                   model_uri=EXPOSURE_OUTCOME.ChemicalEntity_name, domain=ChemicalEntity, range=Optional[str])

slots.Phenotype_id = Slot(uri=EXPOSURE_OUTCOME.id, name="Phenotype_id", curie=EXPOSURE_OUTCOME.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.Phenotype_id, domain=Phenotype, range=Union[str, PhenotypeId],
                   pattern=re.compile(r'^ZP:\d+$'))

slots.Phenotype_name = Slot(uri=EXPOSURE_OUTCOME.name, name="Phenotype_name", curie=EXPOSURE_OUTCOME.curie('name'),
                   model_uri=EXPOSURE_OUTCOME.Phenotype_name, domain=Phenotype, range=Optional[str])

slots.Concentration_has_unit = Slot(uri=EXPOSURE_OUTCOME.has_unit, name="Concentration_has_unit", curie=EXPOSURE_OUTCOME.curie('has_unit'),
                   model_uri=EXPOSURE_OUTCOME.Concentration_has_unit, domain=Concentration, range=Optional[str])

slots.Concentration_has_numeric_value = Slot(uri=EXPOSURE_OUTCOME.has_numeric_value, name="Concentration_has_numeric_value", curie=EXPOSURE_OUTCOME.curie('has_numeric_value'),
                   model_uri=EXPOSURE_OUTCOME.Concentration_has_numeric_value, domain=Concentration, range=Optional[str])
