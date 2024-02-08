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


class NullDataOptions(str, Enum):
    
    
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    
    NOT_APPLICABLE = "NOT_APPLICABLE"
    
    NOT_MENTIONED = "NOT_MENTIONED"
    
    

class GeneToReaction(ConfiguredBaseModel):
    
    gene: Optional[str] = Field(None, description="""name of the gene that catalyzes the reaction""")
    reactions: Optional[Dict[str, Reaction]] = Field(default_factory=dict, description="""semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed by the gene""")
    organism: Optional[str] = Field(None)
    
    

class ReactionDocument(ConfiguredBaseModel):
    
    genes: Optional[List[str]] = Field(default_factory=list, description="""semicolon separated list of genes that catalyzes the mentioned reactions""")
    reactions: Optional[Dict[str, Reaction]] = Field(default_factory=dict, description="""semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed by the gene""")
    gene_reaction_pairings: Optional[List[GeneReactionPairing]] = Field(default_factory=list, description="""semicolon separated list of gene to reaction pairings""")
    organism: Optional[str] = Field(None)
    has_evidence: Optional[List[str]] = Field(default_factory=list, description="""evidence for the reaction""")
    
    

class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")
    
    

class NamedEntity(ConfiguredBaseModel):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Reaction(NamedEntity):
    
    label: Optional[str] = Field(None, description="""the name of the reaction""")
    description: Optional[str] = Field(None, description="""a textual description of the reaction""")
    synonyms: Optional[List[str]] = Field(default_factory=list, description="""alternative names of the reaction""")
    subclass_of: Optional[str] = Field(None, description="""the category to which this biological process belongs""")
    left_side: Optional[List[str]] = Field(default_factory=list, description="""semicolon separated list of chemical entities on the left side""")
    right_side: Optional[List[str]] = Field(default_factory=list, description="""semicolon separated list of chemical entities on the right side""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    
    

class ReactionGrouping(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class ChemicalEntity(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Evidence(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Gene(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Organism(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class CompoundExpression(ConfiguredBaseModel):
    
    None
    
    

class GeneReactionPairing(CompoundExpression):
    
    gene: Optional[str] = Field(None, description="""name of the gene that catalyzes the reaction""")
    reaction: Optional[str] = Field(None, description="""equation describing the reaction (e.g. A+B = C+D) catalyzed by the gene""")
    
    

class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    
    

class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)
    
    

class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    publication: Optional[Publication] = Field(None)
    entities: Optional[List[str]] = Field(default_factory=list)
    
    

class RelationshipType(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Publication(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")
    
    

class AnnotatorResult(ConfiguredBaseModel):
    
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)
    
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
GeneToReaction.model_rebuild()
ReactionDocument.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
Reaction.model_rebuild()
ReactionGrouping.model_rebuild()
ChemicalEntity.model_rebuild()
Evidence.model_rebuild()
Gene.model_rebuild()
Organism.model_rebuild()
CompoundExpression.model_rebuild()
GeneReactionPairing.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

