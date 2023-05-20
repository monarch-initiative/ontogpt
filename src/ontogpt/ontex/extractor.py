import re
from dataclasses import dataclass
from typing import ClassVar, List, Optional, Tuple

import inflection
from kgcl_schema.datamodel import kgcl
from oaklib.datamodels.vocabulary import IS_A, DISJOINT_WITH
from oaklib.interfaces import OboGraphInterface
from oaklib.interfaces.basic_ontology_interface import RELATIONSHIP
from oaklib.interfaces.obograph_interface import GraphTraversalMethod
from oaklib.interfaces.patcher_interface import PatcherInterface
from oaklib.types import CURIE
from pydantic import BaseModel


class Axiom(BaseModel):
    """Axiom."""

    text: str


class Ontology(BaseModel):
    """Ontology."""

    axioms: List[Axiom]


class Query(BaseModel):
    """Query."""

    text: Optional[str] = None
    parameters: Optional[List[str]] = None


class Explanation(BaseModel):
    """Explanation."""

    axioms: List[Axiom]
    comments: Optional[List[str]] = None


class Answer(BaseModel):
    """Answer."""

    _value_domain: ClassVar[str] = None
    text: str
    explanations: Optional[List[Explanation]] = None


class ObjectAnswer(Answer):
    """Answer that is an object, e.g class"""

    _value_domain = "The name of the object"


class ClassAnswer(Answer):
    """Answer that is an OWL class"""

    _value_domain = "The name of the class"


class BooleanAnswer(Answer):
    """Answer that is a boolean, e.g. true or false"""

    _value_domain = "Either TRUE or FALSE"


class AxiomAnswer(Answer):
    """Answer that is a axiom"""

    _value_domain = "An axiom written in Manchester syntax"


class ExampleQueryAnswers(BaseModel):
    """ExampleQueryAnswers."""

    query: Query
    answers: Optional[List[Answer]] = None


class Example(BaseModel):
    """QueryAnswer."""

    ontology: Ontology
    query_answers: Optional[List[ExampleQueryAnswers]] = None


class Task(BaseModel):
    """
    A task is a query on an ontology that has a set of defined answers

    For example, a task group might be to determine if an ontology is consistent.
    """

    _query_format: ClassVar[str] = None
    has_multiple_answers: ClassVar[bool] = True

    ontology: Ontology
    query: Query = None
    answers: Optional[List[Answer]] = None
    examples: Optional[List[Example]] = None
    description: Optional[str] = None

    include_explanations: Optional[bool] = False
    """If true then completing the task must involve providing explanations for each answer."""

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
    Is the ontology coherent? i.e. is it free of unsatisfiable classes and
    logical contradictions? If so, answer TRUE. If the ontology is not incoherent,
    DO NOT write FALSE, just list all unsatisfiable classes.
    One way a class can be unsastisfiable is if it is inferred to be a subclass of two
    classes that are disjoint.
    """
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
                                    axioms=[
                                        Axiom(text="D SubClassOf B"),
                                        Axiom(text="D SubClassOf C"),
                                        Axiom(text="B DisjointWith C"),
                                    ]
                                )
                            ],
                        )
                    ],
                ),
            ],
        )
    ]


class EntailedIndirectSuperClassTask(Task):
    """
    A task to determine the indirect superclasses of a class.
    """

    _query_format = "What are the indirect entailed superclasses of {params[0]}? Do not include direct (one-hop) superclasses."

    answers: Optional[List[ClassAnswer]] = None

    examples: Optional[List[Example]] = [
        Example(
            ontology=Ontology(
                axioms=[
                    Axiom(text="B SubClassOf A"),
                    Axiom(text="C SubClassOf A"),
                    Axiom(text="D SubClassOf B"),
                    Axiom(text="E SubClassOf B"),
                    Axiom(text="E2 SubClassOf E"),
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
                                    axioms=[
                                        Axiom(text="B SubClassOf A"),
                                        Axiom(text="E SubClassOf B"),
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
                                        Axiom(text="B SubClassOf A"),
                                        Axiom(text="E SubClassOf B"),
                                        Axiom(text="E2 SubClassOf E"),
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


class EntailedDirectSuperClassTask(Task):
    """
    A task to determine the direct superclasses of a class entailed by
    other axioms, e.g. equivalence axioms.

    Context: a standard pattern in bio-ontologies is to infer the structure
    of one ontology from another - e.g. the metabolic process branch in GO
    may be entailed by GO equivalence axioms plus the IS_A links in CHEBI.
    """

    _query_format = """
    What are the direct entailed superclasses of {params[0]}?.
    Make use of all axioms in the provided ontology.
    """

    answers: Optional[List[ClassAnswer]] = None


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

    def extract_ontology(self, terms: List[CURIE], roots: Optional[List[CURIE]] = None) -> Ontology:
        adapter = self.adapter
        ancs = list(adapter.ancestors(terms, predicates=[IS_A]))
        if roots is not None:
            roots = set(roots)
            ancs = [t for t in ancs if roots.intersection(adapter.ancestors(t, predicates=[IS_A]))]
        axioms = []
        for t in ancs:
            for s, p, o in adapter.relationships([t], predicates=[IS_A]):
                if not set(adapter.ancestors(o, predicates=[IS_A])).intersection(roots):
                    continue
                axioms.append(self._axiom((s, p, o)))
        ontology = Ontology(axioms=axioms)
        return ontology

    def extract_indirect_superclasses_task(
        self, subclass: CURIE, siblings: List[CURIE], roots: Optional[List[CURIE]] = None
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
        adapter = self.adapter
        subclass_ancestors = list(adapter.ancestors(subclass, predicates=[IS_A]))
        terms = [subclass] + siblings
        ontology = self.extract_ontology(terms, roots)
        answers = []
        if roots is not None:
            roots = set(roots)
        subclass_parents = {r[2] for r in adapter.relationships([subclass], predicates=[IS_A])}
        for anc in subclass_ancestors:
            if roots is not None:
                if not roots.intersection(adapter.ancestors(anc, predicates=[IS_A])):
                    continue
            if anc in subclass_parents or anc == subclass:
                # exclude direct
                continue
            explanations = [
                Explanation(axioms=[self._axiom((s, IS_A, x)), self._axiom((x, IS_A, o))])
                for s, o, x in adapter.paths([subclass], [anc], predicates=[IS_A])
                if s != x and x != o
            ]
            answers.append(ClassAnswer(text=self._name(anc), explanations=explanations))
        task = EntailedIndirectSuperClassTask(
            ontology=ontology,
            query=Query(parameters=[self._name(subclass)]),
            answers=answers,
        )
        task.populate()
        return task

    def extract_incoherent_ontology_task(
        self, incoherents: List[CURIE], siblings: List[CURIE], disjoints: List[Tuple[CURIE, CURIE]], spiked_relationships: List[RELATIONSHIP], roots: Optional[List[CURIE]] = None
    ) -> OntologyCoherencyTask:
        """
        Extract a task for detecting incohorent ontologies.

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
        for s, p, o in spiked_relationships:
            if not isinstance(adapter, PatcherInterface):
                raise ValueError("Cannot patch ontology")
            adapter.apply_patch(kgcl.EdgeCreation(id='tmp', subject=s, predicate=p, object=o))
        answers = []
        if roots is not None:
            roots = set(roots)
        for incoherent in incoherents:
            ancestors = list(adapter.ancestors(incoherent, predicates=[IS_A], method=GraphTraversalMethod.HOP))
            explanations = []
            # TODO:
            for s, o in disjoints:
                if s in ancestors and o in ancestors:
                    explanation =  Explanation(axioms=[self._axiom((incoherent, IS_A, s)),
                                                       self._axiom((incoherent, IS_A, o))])
                    explanations.append(explanation)
            if not explanations:
                explanations = [Explanation(axioms=[self._axiom(rel) for rel in spiked_relationships])]
            answers.append(ClassAnswer(text=self._name(incoherent), explanations=explanations))
        task = OntologyCoherencyTask(
            ontology=ontology,
            query=Query(),
            answers=answers,
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
        else:
            raise ValueError(f"Only IS_A relationships are supported; got={rel}")

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
