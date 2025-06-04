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


linkml_meta = LinkMLMeta({'default_prefix': 'aop',
     'default_range': 'string',
     'description': 'Template for extracting Adverse Outcome Pathways (AOPs) from '
                    'literature. AOPs are conceptual frameworks  that link a '
                    'molecular initiating event to an adverse outcome through a '
                    'series of key events.',
     'id': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
     'imports': ['linkml:types', 'core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'adverse_outcome_pathway',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'aop': {'prefix_prefix': 'aop',
                          'prefix_reference': 'http://w3id.org/ontogpt/adverse_outcome_pathway/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}},
     'source_file': 'src/ontogpt/templates/adverse_outcome_pathway.yaml',
     'title': 'Template for extracting Adverse Outcome Pathways'} )

class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class LevelOfBiologicalOrganizationEnum(str, Enum):
    """
    The level of biological organization at which an event occurs
    """
    molecular = "molecular"
    """
    Molecular level events involving interactions with DNA, proteins, etc.
    """
    cellular = "cellular"
    """
    Effects at the level of the cell
    """
    tissue = "tissue"
    """
    Effects at the level of tissues
    """
    organ = "organ"
    """
    Effects at the level of organs
    """
    organism = "organism"
    """
    Effects at the level of the whole organism
    """
    individual = "individual"
    """
    Effects at the individual level, which may include physiological or behavioral changes
    """
    population = "population"
    """
    Effects at the population level
    """


class EventTypeEnum(str, Enum):
    """
    The type of event happening at some biological level.
    """
    activation = "activation"
    """
    Activation of a biomolecule by a stressor
    """
    inhibition = "inhibition"
    """
    Inhibition of a biomolecule's activity by a stressor
    """
    increase = "increase"
    """
    Increase in a biomolecule's activity or concentration
    """
    decrease = "decrease"
    """
    Decrease in a biomolecule's activity or concentration
    """
    impairment = "impairment"
    """
    Impairment of a biological function or process
    """
    agonism = "agonism"
    """
    Mechanistic interaction between two biomolecules or processes
    """
    antagonism = "antagonism"
    """
    Antagonistic interaction between two biomolecules or processes
    """
    formation = "formation"
    """
    Formation of a new biomolecule or complex
    """
    alkylation = "alkylation"
    """
    Addition of an alkyl group to a biomolecule, often affecting its function
    """
    phosphorylation = "phosphorylation"
    """
    Addition of a phosphate group to a biomolecule, often regulating its activity
    """
    failure = "failure"
    """
    Failure of a biological process or function
    """
    occurrence = "occurrence"
    """
    General occurrence of a biological event without specific details
    """



class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    input_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_id', 'domain_of': ['ExtractionResult']} })
    input_title: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_title', 'domain_of': ['ExtractionResult']} })
    input_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_text', 'domain_of': ['ExtractionResult']} })
    raw_completion_output: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'raw_completion_output', 'domain_of': ['ExtractionResult']} })
    prompt: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'prompt', 'domain_of': ['ExtractionResult']} })
    extracted_object: Optional[Any] = Field(default=None, description="""The complex objects extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'extracted_object', 'domain_of': ['ExtractionResult']} })
    named_entities: Optional[list[Any]] = Field(default=None, description="""Named entities extracted from the text""", json_schema_extra = { "linkml_meta": {'alias': 'named_entities', 'domain_of': ['ExtractionResult']} })


class NamedEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class CompoundExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    pass


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'http://w3id.org/ontogpt/core'})

    subject: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['Triple']} })
    predicate: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['Triple']} })
    object: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object', 'domain_of': ['Triple']} })
    qualifier: Optional[str] = Field(default=None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""", json_schema_extra = { "linkml_meta": {'alias': 'qualifier', 'domain_of': ['Triple']} })
    subject_qualifier: Optional[str] = Field(default=None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""", json_schema_extra = { "linkml_meta": {'alias': 'subject_qualifier', 'domain_of': ['Triple']} })
    object_qualifier: Optional[str] = Field(default=None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""", json_schema_extra = { "linkml_meta": {'alias': 'object_qualifier', 'domain_of': ['Triple']} })


class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    triples: Optional[list[Triple]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'triples', 'domain_of': ['TextWithTriples']} })


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    publication: Optional[Publication] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'publication',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'domain_of': ['TextWithTriples', 'TextWithEntity']} })
    entities: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'entities', 'domain_of': ['TextWithEntity']} })


class RelationshipType(NamedEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core',
         'id_prefixes': ['RO', 'biolink']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class Publication(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    id: Optional[str] = Field(default=None, description="""The publication identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedEntity', 'Publication']} })
    title: Optional[str] = Field(default=None, description="""The title of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Publication']} })
    abstract: Optional[str] = Field(default=None, description="""The abstract of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'abstract', 'domain_of': ['Publication']} })
    combined_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'combined_text', 'domain_of': ['Publication']} })
    full_text: Optional[str] = Field(default=None, description="""The full text of the publication""", json_schema_extra = { "linkml_meta": {'alias': 'full_text', 'domain_of': ['Publication']} })


class AnnotatorResult(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/core'})

    subject_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'subject_text', 'domain_of': ['AnnotatorResult']} })
    object_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object_id', 'domain_of': ['AnnotatorResult']} })
    object_text: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'object_text', 'domain_of': ['AnnotatorResult']} })


class AOPExtraction(ConfiguredBaseModel):
    """
    A container for Adverse Outcome Pathway (AOP) information extracted from text
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
         'tree_root': True})

    aop_pathways: Optional[list[AOPPathway]] = Field(default=None, description="""A semicolon-delimited list of adverse outcome pathways extracted from the text. Each should take the form of free text describing the molecular initiating event (including the stressor), a sequence of key events, and the adverse outcome. For all events, include the biological target, event type, and biological context (for context, include the level of biological organization as well as any applicable cell types or organ types). Examples of event type include activation, inhibition, increase, decrease, impairment, agonism, antagonism, formation, alkylation, phosphorylation, failure, or occurrence. Examples of level of biological organization include molecular, cellular, tissue, organ, organism, individual, or population. If the molecular initiating event is not known, use \"Unknown Initiator (UI)\". Do not split onto new lines. Do not use semicolons unless separating multiple complete AOPs. Do not include a summary of the AOPs or any additional information not directly related to the AOPs. An example of a complete AOP pathway is: The molecular initiating event is formation of pro-mutagenic DNA Adducts. Key events are an increase in induced mutations in critical genes, metabolism of AFB1 and production of reactive electrophiles, clonal expansion and cell proliferation to form Altered Hepatic Foci (AHF), and an increase in insufficient repair or mis-repair of pro-mutagenic DNA adducts. The adverse outcome is tumorigenesis of hepatocellular carcinoma.""", json_schema_extra = { "linkml_meta": {'alias': 'aop_pathways', 'domain_of': ['AOPExtraction']} })


class AOPPathway(ConfiguredBaseModel):
    """
    A representation of an Adverse Outcome Pathway, linking molecular initiating events  to adverse outcomes through key events.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway'})

    molecular_initiating_event: Optional[MolecularInitiatingEvent] = Field(default=None, description="""A free-text description of the molecular initiating event (MIE) that starts the adverse outcome pathway. Include all details necessary to understand the MIE, such as the stressor involved, the biological target, and the biological level at which the MIE occurs.""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_initiating_event', 'domain_of': ['AOPPathway']} })
    key_events: Optional[list[KeyEvent]] = Field(default=None, description="""A semicolon-delimited list of the sequence of key events (KEs) that link the molecular initiating event to the adverse outcome. For each key event, include a free-text description that captures the biological target, event type, and biological level at which the key event occurs.""", json_schema_extra = { "linkml_meta": {'alias': 'key_events', 'domain_of': ['AOPPathway']} })
    adverse_outcome: Optional[list[AdverseOutcome]] = Field(default=None, description="""A semicolon-delimited list of the final adverse outcome (AO) or outcomes. This may be a disease, phenotype, or impact on an organism or population.""", json_schema_extra = { "linkml_meta": {'alias': 'adverse_outcome', 'domain_of': ['AOPPathway']} })


class MolecularInitiatingEvent(ConfiguredBaseModel):
    """
    The initial interaction between a stressor and a biomolecule that starts the adverse outcome pathway. The stressor can be a chemical, physical, or biological agent, or may not be known.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway'})

    target: Optional[str] = Field(default=None, description="""The biological molecule or structure that participates in the event. This may be a gene, protein, or other biomolecule (e.g., PARP1) or a chemical species (e.g., reactive oxygen species).""", json_schema_extra = { "linkml_meta": {'alias': 'target', 'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    event_type: Optional[EventTypeEnum] = Field(default=None, description="""The type of event. Must be one of the following: activation, inhibition, increase, decrease, impairment, agonism, antagonism, formation, alkylation, phosphorylation, failure, or occurrence. For diseases or phenotypes, the event type is often \"increase\", representing an increase in the severity or prevalence of the condition. Occurrence is a general event type that should be used when other types do not apply.""", json_schema_extra = { "linkml_meta": {'alias': 'event_type',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    biological_level: Optional[LevelOfBiologicalOrganizationEnum] = Field(default=None, description="""The level of biological organization at which the event occurs. Must be one of the following: molecular, cellular, tissue, organ, organism, individual, or population.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_level',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    short_name: Optional[str] = Field(default=None, description="""A short name or identifier for the event. This is generally a combination of the target and event type, such as \"Formation, Pro-mutagenic DNA Adducts\" or \"Increase, reactive oxygen species\".""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    stressor: Optional[str] = Field(default=None, description="""The chemical or physical agent that initiates the molecular initiating event. In the case of a chemical stressor, this may be referred to as a Chemical Initiator (CI). If the stressor is not known, it may be referred to as an Unknown Initiator (UI), so the value for this attribute should be \"UI\". Examples: aflatoxin B1, lead, radiation.""", json_schema_extra = { "linkml_meta": {'alias': 'stressor', 'domain_of': ['MolecularInitiatingEvent']} })


class KeyEvent(ConfiguredBaseModel):
    """
    A measurable biological change that is essential to the progression of the adverse outcome pathway.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway'})

    target: Optional[str] = Field(default=None, description="""The biological molecule or structure that participates in the event. This may be a gene, protein, or other biomolecule (e.g., PARP1) or a chemical species (e.g., reactive oxygen species).""", json_schema_extra = { "linkml_meta": {'alias': 'target', 'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    event_type: Optional[EventTypeEnum] = Field(default=None, description="""The type of event. Must be one of the following: activation, inhibition, increase, decrease, impairment, agonism, antagonism, formation, alkylation, phosphorylation, failure, or occurrence. For diseases or phenotypes, the event type is often \"increase\", representing an increase in the severity or prevalence of the condition. Occurrence is a general event type that should be used when other types do not apply.""", json_schema_extra = { "linkml_meta": {'alias': 'event_type',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    biological_level: Optional[LevelOfBiologicalOrganizationEnum] = Field(default=None, description="""The level of biological organization at which the event occurs. Must be one of the following: molecular, cellular, tissue, organ, organism, individual, or population.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_level',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    short_name: Optional[str] = Field(default=None, description="""A short name or identifier for the event. This is generally a combination of the target and event type, such as \"Formation, Pro-mutagenic DNA Adducts\" or \"Increase, reactive oxygen species\".""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })


class AdverseOutcome(ConfiguredBaseModel):
    """
    An adverse effect of regulatory significance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway'})

    event_type: Optional[EventTypeEnum] = Field(default=None, description="""The type of event. Must be one of the following: activation, inhibition, increase, decrease, impairment, agonism, antagonism, formation, alkylation, phosphorylation, failure, or occurrence. For diseases or phenotypes, the event type is often \"increase\", representing an increase in the severity or prevalence of the condition. Occurrence is a general event type that should be used when other types do not apply.""", json_schema_extra = { "linkml_meta": {'alias': 'event_type',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    biological_level: Optional[LevelOfBiologicalOrganizationEnum] = Field(default=None, description="""The level of biological organization at which the event occurs. Must be one of the following: molecular, cellular, tissue, organ, organism, individual, or population.""", json_schema_extra = { "linkml_meta": {'alias': 'biological_level',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    short_name: Optional[str] = Field(default=None, description="""A short name or identifier for the event. This is generally a combination of the target and event type, such as \"Formation, Pro-mutagenic DNA Adducts\" or \"Increase, reactive oxygen species\".""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['MolecularInitiatingEvent', 'KeyEvent', 'AdverseOutcome']} })
    outcome: Optional[str] = Field(default=None, description="""The adverse outcome or effect that results from the key events in the pathway.""", json_schema_extra = { "linkml_meta": {'alias': 'outcome', 'domain_of': ['AdverseOutcome']} })


class Stressor(NamedEntity):
    """
    A chemical, physical, or biological agent that initiates the molecular initiating event.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:chebi, sqlite:obo:envo, '
                                                 'sqlite:obo:opmi'},
                         'prompt': {'tag': 'prompt',
                                    'value': 'The name of the stressor, which may be a '
                                             'chemical, physical, or biological agent. '
                                             'Examples include: acetaminophen, lead, '
                                             'radiation, or a specific biological '
                                             'pathogen.'}},
         'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
         'id_prefixes': ['CHEBI', 'ENVO', 'OPMI']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class BiologicalTarget(NamedEntity):
    """
    The biological molecule or structure that is affected by the stressor or key event. This may be a gene, protein, or other biomolecule (e.g., PARP1) or a chemical species (e.g., reactive oxygen species).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:go, sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
         'id_prefixes': ['GO', 'NCIT']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class Outcome(NamedEntity):
    """
    The outcome or effect that results from the key events in the pathway. This may not include the adverse outcome itself, but rather the phenomenon describing the outcome. It may be a disease (e.g.,  neurodegeneration, cancer, heart failure), a phenotype (e.g., developmental delay, immune response), or a process (e.g., learning and memory, cognitive function, population growth rate, mortality).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:mondo, sqlite:obo:ncit'}},
         'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
         'id_prefixes': ['MONDO', 'NCIT']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class CellTerm(NamedEntity):
    """
    The cell type or tissue in which the event occurs, if applicable. This may be a specific cell type (e.g., hepatocyte, neuron) or a general tissue type (e.g., liver, brain).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators', 'value': 'sqlite:obo:cl'}},
         'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
         'id_prefixes': ['CL']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
        return v


class OrganTerm(NamedEntity):
    """
    The organ in which the event occurs, if applicable. This may be a specific organ (e.g., liver, heart) or a general organ system (e.g., cardiovascular, respiratory).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annotators': {'tag': 'annotators',
                                        'value': 'sqlite:obo:uberon'}},
         'from_schema': 'http://w3id.org/ontogpt/adverse_outcome_pathway',
         'id_prefixes': ['UBERON']})

    id: str = Field(default=..., description="""A unique identifier for the named entity""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['this is populated during the grounding and normalization step'],
         'domain_of': ['NamedEntity', 'Publication']} })
    label: Optional[str] = Field(default=None, description="""The label (name) of the named thing""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'aliases': ['name'],
         'annotations': {'owl': {'tag': 'owl',
                                 'value': 'AnnotationProperty, AnnotationAssertion'}},
         'domain_of': ['NamedEntity'],
         'slot_uri': 'rdfs:label'} })
    original_spans: Optional[list[str]] = Field(default=None, description="""The coordinates of the original text span from which the named entity was extracted, inclusive. For example, \"10:25\" means the span starting from the 10th character and ending with the 25th character. The first character in the text has index 0. Newlines are treated as single characters. Multivalued as there may be multiple spans for a single text.""", json_schema_extra = { "linkml_meta": {'alias': 'original_spans',
         'annotations': {'prompt.skip': {'tag': 'prompt.skip', 'value': 'true'}},
         'comments': ['This is determined during grounding and normalization',
                      'But is based on the full input text'],
         'domain_of': ['NamedEntity']} })

    @field_validator('original_spans')
    def pattern_original_spans(cls, v):
        pattern=re.compile(r"^\d+:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid original_spans format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid original_spans format: {v}"
            raise ValueError(err_msg)
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
AOPExtraction.model_rebuild()
AOPPathway.model_rebuild()
MolecularInitiatingEvent.model_rebuild()
KeyEvent.model_rebuild()
AdverseOutcome.model_rebuild()
Stressor.model_rebuild()
BiologicalTarget.model_rebuild()
Outcome.model_rebuild()
CellTerm.model_rebuild()
OrganTerm.model_rebuild()

