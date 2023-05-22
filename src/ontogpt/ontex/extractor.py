"""Tools to extract sub-ontologies and reasoner tasks."""
import re
from dataclasses import dataclass
from typing import Any, ClassVar, List, Optional, Tuple, Type, Union

import inflection
from oaklib.datamodels.vocabulary import DISJOINT_WITH, IS_A, OWL_CLASS
from oaklib.interfaces import OboGraphInterface
from oaklib.interfaces.basic_ontology_interface import RELATIONSHIP
from oaklib.interfaces.obograph_interface import GraphTraversalMethod
from oaklib.types import CURIE, PRED_CURIE
from pydantic import BaseModel


class Axiom(BaseModel):
    """Represents an individual logical axiom."""

    text: str
    """Textual representation of the axiom, e.g A SubClassOf B"""


class Ontology(BaseModel):
    """An ontology is a collection of axioms."""

    axioms: List[Axiom]
    """All axioms in the ontology"""

    terms: List[CURIE] = None
    predicates: List[PRED_CURIE] = None


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

    axioms: List[Axiom]
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


class ObjectAnswer(Answer):
    """Answer that is an object, e.g class."""

    _value_domain = "The name of the object."


class ClassAnswer(Answer):
    """Answer that is an OWL class."""

    _value_domain = "The name of the class."


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


class Task(BaseModel):
    """
    A task is a query on an ontology that has a set of defined answers.

    For example, a task group might be to determine if an ontology is consistent.
    """

    _query_format: ClassVar[str] = None
    has_multiple_answers: ClassVar[bool] = True

    ontology: Ontology
    name: Optional[str] = None
    description: Optional[str] = None
    query: Query = None
    answers: Optional[List[Answer]] = None
    examples: Optional[List[Example]] = None
    description: Optional[str] = None

    include_explanations: Optional[bool] = False
    """If true then completing the task must involve providing explanations for each answer."""

    chain_of_thought: Optional[bool] = False
    """If true explanations come first, providing chain of thought reasoning."""

    abductive: Optional[bool] = False
    """If true then the task is to find explanations for answers that are given."""

    def populate(self) -> None:
        qf = self._query_format
        for example in self.examples:
            for query_answer in example.query_answers:
                query_answer.query.text = qf.format(params=query_answer.query.parameters)
        if not self.query.text:
            self.query.text = qf.format(params=self.query.parameters)


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


class EntailedSubClassOfExpressionTask(Task):
    """A task to determine the subclasses of a class expression."""

    _query_format = """
    What are the entailed subclasses of the expression {params[0]} Some {params[0]}?
    Include indirect (transitive) descendants.
    """

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

    answers: Optional[List[ClassAnswer]] = None

    # TODO: examples


class MostRecentCommonSubsumerTask(Task):
    """A task to determine the most specific common ancestors."""

    _query_format = """
    What are the most specific common entailed superclasses of {params[0]} and {params[1]}?.
    """

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
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="D SubClassOf B"),
                                    ]
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
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                        Axiom(text="C SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ]
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
                                    axioms=[
                                        Axiom(text="E2 SubClassOf E"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="B SubClassOf A"),
                                    ]
                                )
                            ],
                        ),
                        ClassAnswer(
                            text="B",
                            explanations=[
                                Explanation(
                                    axioms=[
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="E2 SubClassOf E"),
                                    ]
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ]


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
        ancs = list(adapter.ancestors(terms, predicates=predicates))
        if roots is not None:
            roots = set(roots)
            ancs = [
                t for t in ancs if roots.intersection(adapter.ancestors(t, predicates=predicates))
            ]
        axioms = []
        already_have = set()
        terms = set()
        used_predicates = set()
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
        ontology = Ontology(axioms=axioms, terms=terms, predicates=used_predicates)
        return ontology

    def extract_indirect_superclasses_task(
        self,
        subclass: CURIE,
        siblings: List[CURIE],
        roots: Optional[List[CURIE]] = None,
        predicates: Optional[List[PRED_CURIE]] = None,
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
        subclass_ancestors = list(adapter.ancestors(subclass, predicates=predicates))
        terms = [subclass] + siblings
        ontology = self.extract_ontology(terms, roots)
        answers = []
        if roots is not None:
            roots = set(roots)
        subclass_parents = {r[2] for r in adapter.relationships([subclass], predicates=predicates)}
        for anc in subclass_ancestors:
            if roots is not None:
                if not roots.intersection(adapter.ancestors(anc, predicates=predicates)):
                    continue
            if anc in subclass_parents or anc == subclass:
                # exclude direct
                continue
            explanations = [
                Explanation(axioms=[self._axiom((s, IS_A, x)), self._axiom((x, IS_A, o))])
                for s, o, x in adapter.paths([subclass], [anc], predicates=predicates)
                if s != x and x != o
            ]
            answers.append(ClassAnswer(text=self._name(anc), explanations=explanations))
        task = EntailedIndirectSuperClassTask(
            ontology=ontology,
            query=Query(parameters=[self._name(subclass)]),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def extract_subclass_of_expression_task(
        self,
        superclass: CURIE,
        predicate: PRED_CURIE,
        siblings: List[CURIE],
        predicates: Optional[List[PRED_CURIE]] = None,
        **kwargs,
    ) -> EntailedSubClassOfExpressionTask:
        if predicates is None:
            predicates = [IS_A, predicate]
        adapter = self.adapter
        descendants = list(adapter.descendants(superclass, predicates=predicates))
        terms = descendants + siblings
        roots = [superclass] + siblings
        ontology = self.extract_ontology(terms, roots)
        answers = []
        if roots is not None:
            roots = set(roots)
        for desc in descendants:
            if desc == superclass:
                continue
            # if desc not in ontology.terms:
            #    continue
            explanations = []
            answers.append(ClassAnswer(text=self._name(desc), explanations=explanations))
        task = EntailedSubClassOfExpressionTask(
            ontology=ontology,
            query=Query(parameters=[self._name(superclass)]),
            answers=answers,
            **kwargs,
        )
        task.populate()
        return task

    def extract_incoherent_ontology_task(
        self,
        incoherents: List[CURIE],
        siblings: List[CURIE],
        disjoints: List[Tuple[CURIE, CURIE]],
        spiked_relationships: List[RELATIONSHIP],
        roots: Optional[List[CURIE]] = None,
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
