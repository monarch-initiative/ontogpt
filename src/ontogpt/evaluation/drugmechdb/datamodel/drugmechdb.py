"""DrugMechDB."""
from __future__ import annotations

from typing import List, Optional

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


class Mechanism(ConfiguredBaseModel):
    directed: Optional[bool] = Field(None)
    multigraph: Optional[bool] = Field(None)
    reference: Optional[List[str]] = Field(default_factory=list)
    references: Optional[str] = Field(None)
    comment: Optional[str] = Field(None)
    comments: Optional[str] = Field(None)
    commments: Optional[str] = Field(None)
    graph: Optional[Graph] = Field(None)
    links: Optional[List[Link]] = Field(default_factory=list)
    nodes: Optional[List[Node]] = Field(default_factory=list)


class Graph(ConfiguredBaseModel):
    id: Optional[str] = Field(None)
    disease: Optional[str] = Field(None)
    disease_mesh: Optional[str] = Field(None)
    drug: Optional[str] = Field(None)
    drug_mesh: Optional[str] = Field(None)
    drugbank: Optional[str] = Field(None)
    alt_ids: Optional[str] = Field(None)


class Link(ConfiguredBaseModel):
    key: Optional[str] = Field(None)
    source: Optional[str] = Field(None)
    target: Optional[str] = Field(None)
    reference: Optional[str] = Field(None)


class Node(ConfiguredBaseModel):
    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    all_id: Optional[str] = Field(None)
    alt_ids: Optional[List[str]] = Field(default_factory=list)
    alt_names: Optional[List[str]] = Field(default_factory=list)
    alt_name: Optional[str] = Field(None)
    reference: Optional[str] = Field(None)


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Mechanism.update_forward_refs()
Graph.update_forward_refs()
Link.update_forward_refs()
Node.update_forward_refs()
