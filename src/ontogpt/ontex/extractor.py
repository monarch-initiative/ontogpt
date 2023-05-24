"""Tools to extract sub-ontologies and reasoner tasks."""
import logging
import random
import re
import sys
import uuid
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, ClassVar, List, Literal, Optional, TextIO, Tuple, Type, Union

import inflection
import yaml
from oaklib.datamodels.vocabulary import DISJOINT_WITH, IS_A, OWL_CLASS, PART_OF
from oaklib.interfaces import OboGraphInterface
from oaklib.interfaces.basic_ontology_interface import RELATIONSHIP
from oaklib.interfaces.obograph_interface import GraphTraversalMethod
from oaklib.interfaces.semsim_interface import SemanticSimilarityInterface
from oaklib.types import CURIE, PRED_CURIE
from oaklib.utilities.obograph_utils import shortest_paths
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class Axiom(BaseModel):
    """Represents an individual logical axiom."""

    text: str
    """Textual representation of the axiom, e.g A SubClassOf B"""


class Ontology(BaseModel):
    """An ontology is a collection of axioms."""

    name: Optional[str] = None
    axioms: List[Axiom]
    """All axioms in the ontology"""

    terms: List[CURIE] = None
    predicates: List[PRED_CURIE] = None

    comments: Optional[List[str]] = None


class Query(BaseModel):
    """Query."""

    text: Optional[str] = None
    """Text representation of the query."""

    parameters: Optional[List[str]] = None
    """Parameters to the query.
    E.g for a query of the form 'what is the superclass of X',
    there is one parameter X, for the subclass."""


class Explanation(BaseModel):
    """The collection of axioms that entail some explained axiom."""

    axioms: List[Axiom] = []
    text: Optional[str] = None
    comments: Optional[List[str]] = None


class Answer(BaseModel):
    """Individual answer to a query."""

    _value_domain: ClassVar[str] = None
    """Class variable indicating answer types."""

    text: str
    """Textual representation of the answer."""

    explanations: Optional[List[Explanation]] = None
    """All explanations for the answer."""

    def shortest_explanation(self) -> Optional[Explanation]:
        """Return the shortest explanation for the answer."""
        if not self.explanations:
            return Explanation(axioms=[Axiom(text="No explanation found")])
        shortest = min(self.explanations, key=lambda x: len(x.axioms))
        return shortest


class ObjectAnswer(Answer):
    """Answer that is an object, e.g class."""

    _value_domain = "The name of the object."


class ClassAnswer(Answer):
    """Answer that is an OWL class."""

    _value_domain = "The name of the class."


class InstanceAnswer(Answer):
    """Answer that is an OWL individual."""

    _value_domain = "The name of the individual."


class BooleanAnswer(Answer):
    """Answer that is a boolean, e.g. true or false."""

    _value_domain = "Either TRUE or FALSE."


class AxiomAnswer(Answer):
    """Answer that is a axiom."""

    _value_domain = "An axiom written in Manchester syntax."


class ExampleQueryAnswers(BaseModel):
    """An example query, plus all expected answers."""

    query: Query
    answers: Optional[List[Answer]] = None


class Example(BaseModel):
    """An example of a query plus answers, in the context of an ontology."""

    ontology: Ontology
    query_answers: Optional[List[ExampleQueryAnswers]] = None


class GPTReasonMethodType(str, Enum):
    BASIC = "basic"
    EXPLANATION = "explanation"
    CHAIN_OF_THOUGHT = "chain_of_thought"


class Task(BaseModel):
    """
    A task is a query on an ontology that has a set of defined answers.

    For example, a task group might be to determine if an ontology is consistent.
    """

    _query_format: ClassVar[str] = None

    type: Literal["Task"] = Field("Task")

    has_multiple_answers: ClassVar[bool] = True

    ontology: Ontology
    name: Optional[str] = None
    description: Optional[str] = None
    query: Query = None
    answers: Optional[List[Answer]] = None
    examples: Optional[List[Example]] = None
    description: Optional[str] = None

    method: Optional[GPTReasonMethodType] = None

    include_explanations: Optional[bool] = False
    """If true then completing the task must involve providing explanations for each answer."""

    chain_of_thought: Optional[bool] = False
    """If true explanations come first, providing chain of thought reasoning."""

    abductive: Optional[bool] = False
    """If true then the task is to find explanations for answers that are given."""

    shortest_explanation: Optional[Explanation] = None

    len_shortest_explanation: Optional[int] = None

    class Config:
        """Pydantic configuration."""

        use_enum_values = True

    def populate(self) -> None:
        qf = self._query_format
        for example in self.examples:
            for query_answer in example.query_answers:
                if not query_answer.query.text:
                    query_answer.query.text = qf.format(params=query_answer.query.parameters)
        if not self.query.text:
            self.query.text = qf.format(params=self.query.parameters)
        if len(self.answers) == 0:
            self.shortest_explanation = None
            self.len_shortest_explanation = 0
        else:
            most_complex_answer = max(
                self.answers, key=lambda x: len(x.shortest_explanation().axioms)
            )
            self.shortest_explanation = most_complex_answer.shortest_explanation()
            self.len_shortest_explanation = len(self.shortest_explanation.axioms)
        if not self.name:
            self.name = f"{self.type}-{uuid.uuid4()}"
        self.init_method()

    def init_method(self):
        if self.method:
            logger.info(f"Initializing method for {self.name}")
            if not isinstance(self.method, GPTReasonMethodType):
                self.method = GPTReasonMethodType(self.method)
            if self.method == GPTReasonMethodType.EXPLANATION:
                self.include_explanations = True
            elif self.method == GPTReasonMethodType.CHAIN_OF_THOUGHT:
                self.chain_of_thought = True
        else:
            if self.include_explanations:
                self.method = GPTReasonMethodType.EXPLANATION
            elif self.chain_of_thought:
                self.method = GPTReasonMethodType.CHAIN_OF_THOUGHT
            else:
                self.method = GPTReasonMethodType.BASIC


class OntologyCoherencyTask(Task):
    """
    A task to determine if an ontology is coherent.

    There should be a single answer, which is a boolean.
    """

    _query_format = """
    What are the unsatisfiable classes in the ontology?
    A class X is unsatisfiable if X is a subclass of DC1 and also a subclass of DC2,
    where there is an axiom DC1 DisjointWith DC2.
    Here, SubClassOf can mean either direct or indirect subclass, entailed
    through the transitivity of SubClassOf.
    List all unsatisfiable classes that can be found with this rule.
    If there are no unsatisfiable classes, just write NONE."""

    type: Literal["OntologyCoherencyTask"] = Field("OntologyCoherencyTask")

    has_multiple_answers = False
    answers: Optional[List[ClassAnswer]] = None

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="B SubClassOf A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf B"),
                    Axiom(text="D SubClassOf C"),
                    Axiom(text="B DisjointWith C"),
                ]
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(),
                    answers=[
                        ClassAnswer(
                            text="D",
                            explanations=[
                                Explanation(
                                    text="""D is unsatisfiable because it is a subclass
                                            of two disjoint classes (B and C).""",
                                    axioms=[
                                        Axiom(text="D SubClassOf B"),
                                        Axiom(text="D SubClassOf C"),
                                        Axiom(text="B DisjointWith C"),
                                    ],
                                )
                            ],
                        )
                    ],
                ),
            ],
        ),
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="B SubClassOf A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf B"),
                    Axiom(text="B DisjointWith A"),
                ]
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(),
                    answers=[
                        ClassAnswer(
                            text="NONE",
                            explanations=[
                                Explanation(
                                    text="""There is only one Disjointness Axiom (B DisjointWith A),
                                    and B and A do not share either direct
                                    or indirect subclasses.""",
                                    axioms=[],
                                )
                            ],
                        )
                    ],
                ),
            ],
        ),
    ]


class EntailedIndirectSuperClassTask(Task):
    """A task to determine the indirect superclasses of a class."""

    _query_format = """
    What are the indirect entailed superclasses of {params[0]}?
    Include answers entailed by the transitivity of SubClassOf.
    Do not include direct (one-hop) superclasses.
    """

    type: Literal["EntailedIndirectSuperClassTask"] = Field("EntailedIndirectSuperClassTask")

    answers: Optional[List[ClassAnswer]] = None

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="E2 SubClassOf E"),
                    Axiom(text="E SubClassOf B"),
                    Axiom(text="B SubClassOf A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf B"),
                ]
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(parameters=["E"]),
                    answers=[
                        ClassAnswer(
                            text="A",
                            explanations=[
                                Explanation(
                                    text="""A is an indirect entailed superclass of E because
                                    E SubClassOf B, and B SubClassOf A, and SubClassOf is
                                    transitive.""",
                                    axioms=[
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["E2"]),
                    answers=[
                        ClassAnswer(
                            text="A",
                            explanations=[
                                Explanation(
                                    text="""A is an indirect entailed superclass of E2 because
                                    E2 SubClassOf E, and E SubClassOf B, and B SubClassOf A,
                                    and because SubClassOf is transitive.""",
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ],
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="B",
                            explanations=[
                                Explanation(
                                    text="""B is an indirect entailed superclass of E2 because
                                    E2 SubClassOf E, and E SubClassOf B, and because SubClassOf
                                    is transitive.""",
                                    axioms=[
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="E2 SubClassOf E"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ]


class EntailedTransitiveSuperClassTask(Task):
    """A task to determine the all transitive superclasses of a class."""

    _query_format = """
    What are the transitive superclasses of {params[0]}?
    Include answers entailed by the transitivity of SubClassOf.
    Also direct (one-hop) superclasses.
    """

    type: Literal["EntailedTransitiveSuperClassTask"] = Field("EntailedTransitiveSuperClassTask")

    answers: Optional[List[ClassAnswer]] = None

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="E2 SubClassOf E"),
                    Axiom(text="E SubClassOf B"),
                    Axiom(text="B SubClassOf A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf B"),
                ]
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(parameters=["E"]),
                    answers=[
                        ClassAnswer(
                            text="A",
                            explanations=[
                                Explanation(
                                    text="""A is an entailed superclass of E because
                                    E SubClassOf B, and B SubClassOf A, and SubClassOf is
                                    transitive.""",
                                    axioms=[
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ],
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="B",
                            explanations=[
                                Explanation(
                                    text="""B is an indirect entailed superclass of E because
                                        it is already asserted.""",
                                    axioms=[
                                        Axiom(text="B SubClassOf A"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["E2"]),
                    answers=[
                        ClassAnswer(
                            text="A",
                            explanations=[
                                Explanation(
                                    text="""A is an indirect entailed superclass of E2 because
                                    E2 SubClassOf E, and E SubClassOf B, and B SubClassOf A,
                                    and because SubClassOf is transitive.""",
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ],
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="B",
                            explanations=[
                                Explanation(
                                    text="""B is an entailed superclass of E2 because
                                    E2 SubClassOf E, and E SubClassOf B, and because SubClassOf
                                    is transitive.""",
                                    axioms=[
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="E2 SubClassOf E"),
                                    ],
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="E",
                            explanations=[
                                Explanation(
                                    text="""E is an entailed superclass of E2 because
                                    it is directly asserted.""",
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ]


class EntailedSubClassOfExpressionTask(Task):
    """A task to determine the subclasses of a class expression."""

    _query_format = """
    What are the entailed subclasses of the expression {params[0]} Some {params[1]}?
    Include indirect (transitive) descendants.
    """

    type: Literal["EntailedSubClassOfExpressionTask"] = Field("EntailedSubClassOfExpressionTask")

    answers: Optional[List[ClassAnswer]] = None

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="P type TransitiveProperty"),
                    Axiom(text="E2 SubClassOf P some E"),
                    Axiom(text="E SubClassOf B"),
                    Axiom(text="B SubClassOf P some A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf Q some B"),
                ]
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(parameters=["P", "A"]),
                    answers=[
                        ClassAnswer(
                            text="B",
                            explanations=[
                                Explanation(
                                    text="""B is an entailed subclass of P some A because
                                    it is directly asserted in the ontology.""",
                                    axioms=[
                                        Axiom(text="B SubClassOf P some A"),
                                    ],
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="E",
                            explanations=[
                                Explanation(
                                    text="""E is an entailed subclass of P some A because
                                    E SubClassOf B and B SubClassOf P some A
                                    (i.e. every B stands in relation P to some A)""",
                                    axioms=[
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf P some A"),
                                    ],
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="E2",
                            explanations=[
                                Explanation(
                                    text="""E2 is an entailed subclass of P some A because
                                    E2 SubClassOf E and E SubClassOf B and B SubClassOf P some A
                                    (i.e. every B stands in relation P to some A)""",
                                    axioms=[
                                        Axiom(text="B SubClassOf P some A"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="E2 SubClassOf P some E"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["Q", "B"]),
                    answers=[
                        ClassAnswer(
                            text="D",
                            explanations=[
                                Explanation(
                                    text="""D is an entailed subclass of Q some B because
                                    it is directly asserted in the ontology. This is the only
                                    answer because Q is not declared transitive.""",
                                    axioms=[
                                        Axiom(text="D SubClassOf Q some B"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ]


class EntailedDirectSuperClassTask(Task):
    """
    A task to determine the direct superclasses of a class.

    Includes those entailed by other axioms, e.g. equivalence axioms.

    Context: a standard pattern in bio-ontologies is to infer the structure
    of one ontology from another - e.g. the metabolic process branch in GO
    may be entailed by GO equivalence axioms plus the IS_A links in CHEBI.
    """

    _query_format = """
    What are the direct entailed superclasses of {params[0]}?.
    Make use of all axioms in the provided ontology.
    """

    type: Literal["EntailedDirectSuperClassTask"] = Field("EntailedDirectSuperClassTask")

    answers: Optional[List[ClassAnswer]] = None

    # TODO: examples


class MostRecentCommonSubsumerTask(Task):
    """A task to determine the most specific common ancestors."""

    _query_format = """
    What are the most specific common entailed superclasses of {params[0]} and {params[1]}?.
    """

    type: Literal["MostRecentCommonSubsumerTask"] = Field("MostRecentCommonSubsumerTask")

    answers: Optional[List[ClassAnswer]] = None

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="E2 SubClassOf E"),
                    Axiom(text="E SubClassOf B"),
                    Axiom(text="B SubClassOf A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf B"),
                ]
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(parameters=["E2", "D"]),
                    answers=[
                        ClassAnswer(
                            text="B",
                            explanations=[
                                Explanation(
                                    text="""B is the most specific common entailed superclass
                                    of E2 and D because E2 is a SubClassOf B via E, and D is
                                    a direct SubClassOf B, and there are no more specific common
                                    ancestors.""",
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="D SubClassOf B"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["E2", "C"]),
                    answers=[
                        ClassAnswer(
                            text="A",
                            explanations=[
                                Explanation(
                                    text="""A is the most specific common entailed superclass
                                    of E2 and C because E2 is a SubClassOf A via E then B, and C is
                                    a SubClassOf A via B, and there are no more specific common
                                    ancestors.""",
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                        Axiom(text="C SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["E2", "E"]),
                    answers=[
                        ClassAnswer(
                            text="E",
                            explanations=[
                                Explanation(
                                    text="""E is the most specific common entailed superclass of E2 and E because
                                    trivially E2 SubClassOf E""",
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ]


class ABoxPropertyChainPlusTransitivityTask(Task):
    """A task to infer assertions over property chains and transitvity in aboxes."""

    _query_format = """
    What instances <I> satisfy {params[0]} {params[1]} <I> ?.
    Make use of property chain axioms of the form
    PROPERTY1 o PROPERTY2 SubPropertyOf PROPERTY3.
    This means that if x PROPERTY1 y and y PROPERTY2 z then x PROPERTY3 z.
    Also make use of transitivity axioms of the form
    PROPERTY type TransitiveProperty.
    This means that if x PROPERTY y and y PROPERTY z then x PROPERTY z.
    """

    type: Literal["ABoxPropertyChainTask"] = Field("ABoxPropertyChainTask")

    answers: Optional[List[InstanceAnswer]] = None

    # TODO: examples

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="p1 o p2 SubPropertyOf p3"),
                    Axiom(text="p1 type TransitiveProperty"),
                    Axiom(text="i0 p1 i1"),
                    Axiom(text="i1 p1 i2"),
                    Axiom(text="i2 p2 i3"),
                    Axiom(text="i3 p1 i4"),
                ],
                comments=["""a chain of two transitive properties followed by a property chain."""],
            ),
            query_answers=[
                ExampleQueryAnswers(
                    query=Query(parameters=["i0", "p3"]),
                    answers=[
                        InstanceAnswer(
                            text="i3",
                            explanations=[
                                Explanation(
                                    text="""i0 p3 i3 because
                                    i0 p1 i1 and i1 p1 i2 and p1 is transitive, so i0 p1 i2.
                                    i2 p2 i3 and p1 o p2 SubPropertyOf p3, so i0 p3 i3""",
                                    axioms=[
                                        Axiom(text="i0 p1 i1"),
                                        Axiom(text="i1 p1 i2"),
                                        Axiom(text="p1 type TransitiveProperty"),
                                        Axiom(text="i2 p2 i3"),
                                        Axiom(text="p1 o p2 SubPropertyOf p3"),
                                    ],
                                )
                            ],
                        ),
                        InstanceAnswer(
                            text="i2",
                            explanations=[
                                Explanation(
                                    text="""i0 p3 i2 because
                                        i0 p1 i1 and i1 p1 i2 and p1 is transitive, so i0 p1 i2.""",
                                    axioms=[
                                        Axiom(text="i0 p1 i1"),
                                        Axiom(text="i1 p1 i2"),
                                        Axiom(text="p1 type TransitiveProperty"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["i1", "p3"]),
                    answers=[
                        InstanceAnswer(
                            text="i3",
                            explanations=[
                                Explanation(
                                    text="""i1 p3 i3 because
                                            i1 p1 i2 and
                                            i2 p2 i3 and p1 o p2 SubPropertyOf p3, so i1 p3 i3""",
                                    axioms=[
                                        Axiom(text="i1 p1 i2"),
                                        Axiom(text="i2 p2 i3"),
                                        Axiom(text="p1 o p2 SubPropertyOf p3"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                ExampleQueryAnswers(
                    query=Query(parameters=["i0", "p1"]),
                    answers=[
                        InstanceAnswer(
                            text="i1",
                            explanations=[
                                Explanation(
                                    text="""i0 p1 i1 is directly asserted""",
                                    axioms=[
                                        Axiom(text="i0 p1 i1"),
                                    ],
                                )
                            ],
                        ),
                        InstanceAnswer(
                            text="i2",
                            explanations=[
                                Explanation(
                                    text="""i0 p1 i2 because
                                            i0 p1 i1 and i1 p1 i2 and p1 is transitive,
                                            so i0 p1 i2.""",
                                    axioms=[
                                        Axiom(text="i0 p1 i1"),
                                        Axiom(text="i1 p1 i2"),
                                        Axiom(text="p1 type TransitiveProperty"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ]


class TaskCollection(BaseModel):
    tasks: List[Task] = None

    @staticmethod
    def load(file_or_object: Union[dict, str, Path, TextIO]):
        if isinstance(file_or_object, Path):
            file_or_object = str(file_or_object)
        if isinstance(file_or_object, str):
            with open(file_or_object) as f:
                tc_dict = yaml.safe_load(f)
        else:
            tc_dict = yaml.safe_load(file_or_object)
        current_module = sys.modules[__name__]
        tasks = []
        for task_dict in tc_dict["tasks"]:
            typ = task_dict["type"]
            cls = current_module.__dict__[typ]
            task = cls(**task_dict)
            if not isinstance(task.method, GPTReasonMethodType):
                # TODO: figure how to get pydantic to do this
                task.method = GPTReasonMethodType(task.method)
            tasks.append(task)
        tc_dict["tasks"] = tasks
        return TaskCollection(**tc_dict)


@dataclass
class OntologyExtractor:
    """
    Ontology extractor.

    This will extract Task objects from an ontology. These Task objects
    can be used by a ReasonerEngine object as queries or evaluation tests.

    Examples of types of Task objects include:

    - OntologyCoherencyTask: determine if an ontology is coherent
    - EntailedIndirectSuperClassTask: determine the indirect superclasses of a class

    The extraction process is guided by seed classes or objects, and the resulting Task
    object contains a minimal ontology (similar to a SLME module) that should be sufficient
    to answer the query, as well as a specification of the task.
    """

    adapter: OboGraphInterface
    use_identifiers: bool = False

    def create_task(
        self, task_type: Union[str, Type[Task]], parameters: Optional[List[Any]] = None, **kwargs
    ) -> Task:
        terms = list(self.adapter.entities(filter_obsoletes=True, owl_type=OWL_CLASS))
        ontology = self.extract_ontology(terms)
        if isinstance(task_type, str):
            task_type = globals()[task_type]
        task = task_type(ontology=ontology, query=Query(parameters=parameters))
        task.populate()
        return task

    def create_random_tasks(
        self, num_tasks_per_type: int = 10, methods: List = None
    ) -> TaskCollection:
        if methods is None:
            methods = [
                self.extract_indirect_superclasses_task,
                self.extract_transitive_superclasses_task,
                self.extract_most_recent_common_subsumers_task,
                self.extract_subclass_of_expression_task,
                self.extract_incoherent_ontology_task,
            ]
        objs = []
        for method in methods:
            for _n in range(num_tasks_per_type):
                task = method(select_random=True)
                objs.append(task)
                logger.info(f"  {task.name}")
        return TaskCollection(tasks=objs)

    def extract_ontology(
        self,
        terms: List[CURIE],
        roots: Optional[List[CURIE]] = None,
        predicates: Optional[List[PRED_CURIE]] = None,
    ) -> Ontology:
        """
        Extract an ontology module following specified terms up the hierarchy.

        :param terms: leaf nodes to traverse up from
        :param roots: optional root nodes to stop at
        :param predicates: defaults to IS_A
        :return:
        """
        if predicates is None:
            predicates = [IS_A]
        adapter = self.adapter
        onts = list(adapter.ontologies())
        ancs = list(adapter.ancestors(terms, predicates=predicates))
        if roots:
            roots = set(roots)
            ancs = [
                t for t in ancs if roots.intersection(adapter.ancestors(t, predicates=predicates))
            ]
        axioms = []
        already_have = set()
        terms = set()
        used_predicates = set()
        if not ancs:
            raise ValueError(f"No ancestors found for {terms} over {predicates}")
        for t in ancs:
            for rel in adapter.relationships([t], predicates=predicates):
                if rel in already_have:
                    continue
                s, p, o = rel
                terms.add(s)
                terms.add(o)
                used_predicates.add(p)
                if roots and not set(adapter.ancestors(o, predicates=predicates)).intersection(
                    roots
                ):
                    continue
                axioms.append(self._axiom(rel))
                already_have.add(rel)
        if not axioms:
            raise ValueError(
                f"No axioms found for ancestors {ancs} over {predicates} (roots={roots})"
            )
        ontology = Ontology(
            name="-".join(onts), axioms=axioms, terms=terms, predicates=used_predicates
        )
        return ontology

    def extract_indirect_superclasses_task(
        self,
        subclass: CURIE = None,
        siblings: List[CURIE] = None,
        roots: Optional[List[CURIE]] = None,
        predicates: Optional[List[PRED_CURIE]] = None,
        select_random=False,
        **kwargs,
    ) -> EntailedIndirectSuperClassTask:
        """
        Extract a task for finding all indirect superclasses of a class.

        >>> from oaklib import get_adapter
        >>> from ontogpt.ontex.extractor import OntologyExtractor
        >>> adapter = get_adapter("sqlite:obo:go")
        >>> extractor = OntologyExtractor(adapter=adapter)
        >>> task = extractor.extract_indirect_superclasses_task(
        ...    subclass="GO:0005634", siblings=["GO:0005773"], roots=["GO:0043226"]
        ... )

        :param subclass: the main focus of the query
        :param siblings: other terms to include (to make the task harder)
        :param roots: only include descendants of these terms
        :return: An EntailedIndirectSuperClassTask
        """
        if predicates is None:
            predicates = [IS_A]
        adapter = self.adapter
        if select_random:
            all_classes = list(adapter.entities(filter_obsoletes=True, owl_type=OWL_CLASS))
            subclass = random.choice(all_classes)
            siblings = random.sample(all_classes, 3)
        subclass_ancestors = list(adapter.ancestors(subclass, predicates=predicates))
        terms = [subclass] + siblings
        ontology = self.extract_ontology(terms, roots)
        if roots is not None:
            roots = set(roots)
        subclass_parents = {r[2] for r in adapter.relationships([subclass], predicates=predicates)}

        def _filter(anc: CURIE) -> bool:
            if anc == subclass:
                return True
            if anc in subclass_parents:
                return True
            if roots is not None:
                if not roots.intersection(adapter.ancestors(anc, predicates=predicates)):
                    return True

        filtered_ancestors = [anc for anc in subclass_ancestors if not _filter(anc)]
        answers = self._answers_from_ancestors(subclass, filtered_ancestors, predicates=predicates)
        task = EntailedIndirectSuperClassTask(
            ontology=ontology,
            query=Query(parameters=[self._name(subclass)]),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def _answers_from_ancestors(
        self, start: CURIE, ends: List[CURIE], predicates: List[PRED_CURIE]
    ) -> List[ClassAnswer]:
        graph = self.adapter.ancestor_graph([start], predicates=predicates)
        answer_map = defaultdict(list)
        for _s, end, path in shortest_paths(graph, [start], ends, directed=True):
            axioms = []
            for i in range(len(path) - 1):
                axioms.append(self._axiom((path[i], IS_A, path[i + 1])))
            answer_map[end].append(Explanation(axioms=axioms))
        return [ClassAnswer(text=self._name(end), explanations=answer_map[end]) for end in ends]

    def extract_transitive_superclasses_task(
        self,
        subclass: CURIE = None,
        siblings: List[CURIE] = None,
        roots: Optional[List[CURIE]] = None,
        predicates: Optional[List[PRED_CURIE]] = None,
        select_random=False,
        **kwargs,
    ) -> EntailedTransitiveSuperClassTask:
        """
        Extract a task for finding all transitive superclasses of a class.

        >>> from oaklib import get_adapter
        >>> from ontogpt.ontex.extractor import OntologyExtractor
        >>> adapter = get_adapter("sqlite:obo:go")
        >>> extractor = OntologyExtractor(adapter=adapter)
        >>> task = extractor.extract_transitive_superclasses_task(
        ...    subclass="GO:0005634", siblings=["GO:0005773"], roots=["GO:0043226"]
        ... )

        :param subclass: the main focus of the query
        :param siblings: other terms to include (to make the task harder)
        :param roots: only include descendants of these terms
        :return: An EntailedIndirectSuperClassTask
        """
        if predicates is None:
            predicates = [IS_A]
        adapter = self.adapter
        if select_random:
            all_classes = list(adapter.entities(filter_obsoletes=True, owl_type=OWL_CLASS))
            subclass = random.choice(all_classes)
            siblings = random.sample(all_classes, 3)
        subclass_ancestors = list(adapter.ancestors(subclass, predicates=predicates))
        terms = [subclass] + siblings
        ontology = self.extract_ontology(terms, roots)
        answers = []
        if roots is not None:
            roots = set(roots)

        def _filter(anc: CURIE) -> bool:
            if anc == subclass:
                return True
            if roots is not None:
                if not roots.intersection(adapter.ancestors(anc, predicates=predicates)):
                    return True

        filtered_ancestors = [anc for anc in subclass_ancestors if not _filter(anc)]
        answers = self._answers_from_ancestors(subclass, filtered_ancestors, predicates=predicates)
        task = EntailedTransitiveSuperClassTask(
            ontology=ontology,
            query=Query(parameters=[self._name(subclass)]),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def extract_most_recent_common_subsumers_task(
        self,
        subclass1: CURIE = None,
        subclass2: CURIE = None,
        siblings: List[CURIE] = None,
        roots: Optional[List[CURIE]] = None,
        predicates: Optional[List[PRED_CURIE]] = None,
        select_random=False,
        **kwargs,
    ) -> MostRecentCommonSubsumerTask:
        """Extract a task for finding all MRCAs of a pair of classes."""
        if predicates is None:
            predicates = [IS_A]
        adapter = self.adapter
        if select_random:
            all_classes = list(adapter.entities(filter_obsoletes=True, owl_type=OWL_CLASS))
            subclass1 = random.choice(all_classes)
            subclass2 = random.choice(all_classes)
            siblings = random.sample(all_classes, 2)
        terms = [subclass1, subclass2] + siblings
        ontology = self.extract_ontology(terms, roots)
        answers = []
        if not isinstance(adapter, SemanticSimilarityInterface):
            raise ValueError("Adapter must implement SemanticSimilarityInterface")
        mrcas = list(
            adapter.most_recent_common_ancestors(subclass1, subclass2, predicates=predicates)
        )
        for mrca in mrcas:
            explanations = [
                Explanation(
                    axioms=[
                        self._axiom((mrca, IS_A, subclass1)),
                        self._axiom((mrca, IS_A, subclass2)),
                    ]
                )
            ]
            answers.append(ClassAnswer(text=self._name(mrca), explanations=explanations))
        task = MostRecentCommonSubsumerTask(
            ontology=ontology,
            query=Query(parameters=[self._name(subclass1), self._name(subclass2)]),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def extract_subclass_of_expression_task(
        self,
        superclass: CURIE = None,
        predicate: PRED_CURIE = None,
        siblings: List[CURIE] = None,
        predicates: Optional[List[PRED_CURIE]] = None,
        select_random=False,
        **kwargs,
    ) -> EntailedSubClassOfExpressionTask:
        adapter = self.adapter
        if predicate is None:
            predicate = PART_OF
        if not predicates:
            predicates = [IS_A, predicate]
        if select_random:
            all_classes = list(adapter.entities(filter_obsoletes=True, owl_type=OWL_CLASS))
            siblings = random.sample(all_classes, 2)
            n = 0
            while True:
                superclass = random.choice(all_classes)
                descendants = list(adapter.descendants(superclass, predicates=predicates))
                isa_descendants = list(adapter.descendants(superclass, predicates=[IS_A]))
                if (
                    len(descendants) < 15
                    and len(descendants) > 0
                    and len(descendants) != len(isa_descendants)
                ):
                    break
                n += 1
                if n > 100:
                    raise ValueError(
                        f"Could not find suitable parent (ontology MUST have {predicate}"
                    )
        logger.info(f"Extracting subclass of expression task for {superclass}, preds={predicates}")
        descendants = list(adapter.descendants(superclass, predicates=predicates))
        isa_descendants = list(adapter.descendants(superclass, predicates=[IS_A]))
        terms = descendants + siblings
        roots = [superclass] + siblings
        ontology = self.extract_ontology(terms, roots, predicates=predicates)
        answers = []
        if roots is not None:
            roots = set(roots)
        for desc in descendants:
            if desc == superclass:
                continue
            if desc in isa_descendants:
                # TODO: Reflexive scenario
                continue
            # if desc not in ontology.terms:
            #    continue
            explanations = []
            answers.append(ClassAnswer(text=self._name(desc), explanations=explanations))
        task = EntailedSubClassOfExpressionTask(
            ontology=ontology,
            query=Query(parameters=[self._name(predicate), self._name(superclass)]),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def extract_incoherent_ontology_task(
        self,
        incoherents: List[CURIE] = None,
        siblings: List[CURIE] = None,
        disjoints: List[Tuple[CURIE, CURIE]] = None,
        spiked_relationships: List[RELATIONSHIP] = None,
        roots: Optional[List[CURIE]] = None,
        select_random=False,
        **kwargs,
    ) -> OntologyCoherencyTask:
        """
        Extract task for testing ability to find incoherencies based on disjointness axioms.

        :param incoherents: expected incoherent classes
        :param siblings:
        :param disjoints: pairs of disjoint classes
        :param spiked_relationships: edges to insert into ontology
        :param roots:
        :return:
        """
        adapter = self.adapter
        if select_random:
            all_classes = list(adapter.entities(filter_obsoletes=True, owl_type=OWL_CLASS))
            siblings = random.sample(all_classes, 2)
            candidates = []
            for c in all_classes:
                parents = {rel[2] for rel in adapter.relationships(subjects=[c], predicates=[IS_A])}
                if len(parents) > 1:
                    candidates.append((c, parents))
            if len(candidates) == 0:
                raise ValueError("No suitable candidates")
            root_incoherent, parents = random.choice(candidates)
            incoherents = [
                random.choice(list(adapter.descendants(root_incoherent, predicates=[IS_A])))
            ]
            parents = list(parents)
            random.shuffle(parents)
            disjoints = [(parents[0], parents[1])]
        if not incoherents or not siblings or not disjoints:
            raise ValueError("Must specify incoherents, siblings, and disjoints")
        if not spiked_relationships:
            spiked_relationships = []
        terms = incoherents + siblings
        for s, _p, o in spiked_relationships:
            terms += [s, o]
        terms = list(set(terms))
        ontology = self.extract_ontology(terms, roots)
        for s, p, o in spiked_relationships:
            ontology.axioms.append(self._axiom((s, p, o)))
        for s, o in disjoints:
            ontology.axioms.append(self._axiom((s, DISJOINT_WITH, o)))
        # for s, p, o in spiked_relationships:
        #     if not isinstance(adapter, PatcherInterface):
        #         raise ValueError("Cannot patch ontology")
        #     adapter.apply_patch(kgcl.EdgeCreation(id='tmp', subject=s, predicate=p, object=o))
        answers = []
        if roots is not None:
            roots = set(roots)
        for incoherent in incoherents:
            ancestors = list(
                adapter.ancestors(incoherent, predicates=[IS_A], method=GraphTraversalMethod.HOP)
            )
            explanations = []
            # TODO:
            for s, o in disjoints:
                if s in ancestors and o in ancestors:
                    explanation = Explanation(
                        axioms=[
                            self._axiom((incoherent, IS_A, s)),
                            self._axiom((incoherent, IS_A, o)),
                        ]
                    )
                    explanations.append(explanation)
            if not explanations:
                explanations = [
                    Explanation(axioms=[self._axiom(rel) for rel in spiked_relationships])
                ]
            answers.append(ClassAnswer(text=self._name(incoherent), explanations=explanations))
        task = OntologyCoherencyTask(
            ontology=ontology,
            query=Query(),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def _axiom(self, rel: RELATIONSHIP, tbox=True) -> Axiom:
        s, p, o = rel
        s_n, p_n, o_n = self._name(s), self._name(p), self._name(o)
        if p == IS_A:
            return Axiom(text=f"{s_n} SubClassOf {o_n}")
        elif p == DISJOINT_WITH:
            return Axiom(text=f"{s_n} DisjointWith {o_n}")
        elif tbox:
            return Axiom(text=f"{s_n} SubClassOf {p_n} Some {o_n}")
        else:
            raise ValueError(f"Cannot translate {rel}")

    def _name(self, curie: CURIE) -> str:
        if self.use_identifiers:
            return curie
        else:
            lbl = self.adapter.label(curie)
            if lbl is None:
                return curie
            else:
                lbl = re.sub(r"\W+", "_", lbl)
                return inflection.camelize(lbl)
