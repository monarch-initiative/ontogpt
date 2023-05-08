from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from linkml_runtime.linkml_model import Decimal
from pydantic import BaseModel as BaseModel
from pydantic import Field

metamodel_version = "None"
version = "None"


class WeakRefShimBaseModel(BaseModel):
    __slots__ = "__weakref__"


class ConfiguredBaseModel(
    WeakRefShimBaseModel,
    validate_assignment=True,
    validate_all=True,
    underscore_attrs_are_private=True,
    extra="forbid",
    arbitrary_types_allowed=True,
):
    pass


class SortFieldEnum(str, Enum):
    ANY = "ANY"
    P_VALUE = "P_VALUE"


class ClassEnrichmentConfiguration(ConfiguredBaseModel):
    """
    configuration for search
    """

    p_value_cutoff: float = Field(None, description="""p-value cutoff for enrichment""")


class ClassEnrichmentResultSet(ConfiguredBaseModel):
    """
    A collection of enrichemt results
    """

    results: Optional[List[ClassEnrichmentResult]] = Field(
        default_factory=list, description="""The enrichment results"""
    )


class ClassEnrichmentResult(ConfiguredBaseModel):
    """
    A single enrichment result
    """

    class_id: str = Field(None, description="""The class id""")
    class_label: Optional[str] = Field(None, description="""The class label""")
    rank: Optional[int] = Field(None, description="""The rank of this result""")
    p_value: float = Field(None, description="""The p-value""")
    p_value_adjusted: Optional[float] = Field(None, description="""The adjusted p-value""")
    false_discovery_rate: Optional[float] = Field(None, description="""The false discovery rate""")
    fold_enrichment: Optional[float] = Field(None, description="""The fold enrichment""")
    probability: Optional[float] = Field(
        None, description="""The probability, as estimated by model-based approaches""", ge=0, le=1
    )
    sample_count: Optional[int] = Field(
        None, description="""The number of entities in the sample with this class"""
    )
    sample_total: Optional[int] = Field(
        None, description="""The total number of entities in the sample"""
    )
    background_count: Optional[int] = Field(None, description="""The background count""")
    background_total: Optional[int] = Field(None, description="""The background total""")
    ancestor_of_more_informative_result: Optional[bool] = Field(
        None, description="""This term is more general than a previously reported result"""
    )
    descendant_of_more_informative_result: Optional[bool] = Field(
        None, description="""This term is more specific than a previously reported result"""
    )


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
ClassEnrichmentConfiguration.update_forward_refs()
ClassEnrichmentResultSet.update_forward_refs()
ClassEnrichmentResult.update_forward_refs()
