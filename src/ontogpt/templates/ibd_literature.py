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
    
    

class IBDAnnotations(ConfiguredBaseModel):
    
    genes: Optional[List[str]] = Field(default_factory=list, description="""semicolon-separated list of genes""")
    exposures: Optional[List[str]] = Field(default_factory=list, description="""semicolon-separated list of exposures""")
    gene_exposures_relationships: Optional[List[GeneExposureRelationship]] = Field(default_factory=list, description="""semicolon-separated list of gene to molecular activity relationships""")
    diseases: Optional[List[str]] = Field(default_factory=list, description="""semicolon-separated list of diseases""")
    cellular_process: Optional[List[str]] = Field(default_factory=list, description="""semicolon-separated list of cellular processes""")
    disease_cellular_process_relationships: Optional[List[DiseaseCellularProcessRelationship]] = Field(default_factory=list, description="""semicolon-separated list of disease to cellular process relationships""")
    
    

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
    
    

class Gene(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class ChemicalExposure(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class ChemicalExposureToGenePredicate(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Disease(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class CellularProcess(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class DiseaseToCellularProcessPredicate(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class CompoundExpression(ConfiguredBaseModel):
    
    None
    
    

class GeneExposureRelationship(CompoundExpression):
    
    subject: Optional[str] = Field(None, description="""The name of the exposure, such as a exposure to a chemical toxin.""")
    predicate: Optional[str] = Field(None, description="""The name of the type of relationship between a chemical exposure and a gene.""")
    object: Optional[str] = Field(None, description="""The name of the gene in the pair. This comes second in the pair.""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the chemical exposure.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the gene.""")
    
    

class DiseaseCellularProcessRelationship(CompoundExpression):
    
    subject: Optional[str] = Field(None, description="""The name of the disease.""")
    predicate: Optional[str] = Field(None, description="""The name of the type of relationship between a disease and a cellular process.""")
    object: Optional[str] = Field(None, description="""The name of the cellular process.""")
    subject_qualifier: Optional[str] = Field(None)
    object_qualifier: Optional[str] = Field(None)
    
    

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
IBDAnnotations.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
Gene.model_rebuild()
ChemicalExposure.model_rebuild()
ChemicalExposureToGenePredicate.model_rebuild()
Disease.model_rebuild()
CellularProcess.model_rebuild()
DiseaseToCellularProcessPredicate.model_rebuild()
CompoundExpression.model_rebuild()
GeneExposureRelationship.model_rebuild()
DiseaseCellularProcessRelationship.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

