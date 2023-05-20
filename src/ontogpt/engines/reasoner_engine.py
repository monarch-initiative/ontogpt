"""Reasoner engine."""
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from jinja2 import Template
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.ontex.extractor import Answer, Axiom, Explanation, Task
from ontogpt.prompts.reasoning import DEFAULT_REASONING_PROMPT
from ontogpt.utils.parse_utils import split_on_one_of

logger = logging.getLogger(__name__)


class ReasonerResult(BaseModel):
    """The result of a reason query."""

    answers: Optional[List[Answer]] = None
    prompt: Optional[str] = None
    completion: Optional[str] = None
    jaccard_score: Optional[float] = None
    false_positives: Optional[List[str]] = None
    false_negatives: Optional[List[str]] = None


@dataclass
class ReasonerEngine(KnowledgeEngine):
    """Engine for performing reasoning using GPT.

    This engine takes as input an Ontology, and a query Task,
    and then translates this to a GPT prompt that asks GPT to
    perform the task over the ontology after reasoning over it.

    The Task is typically a query such as finding superclasses of
    a given class.

    This is intended primarily for investigation purposes. For practical
    scenarios, it is recommended to use a dedicated OWL reasoner. The goal
    of this engine is to evaluate the extent to which GPT can perform
    reasoning-like tasks, including deduction and abduction (explanation).

    Due to token-length constraints on GPT models, it is usually necessary
    to extract a submodule prior to reasoning. This can be done using the
    OntologyExtractor:

    >>> from oaklib import get_adapter
    >>> from ontogpt.ontex.extractor import OntologyExtractor, Task
    >>> adapter = get_adapter("sqlite:obo:go")
    >>> extractor = OntologyExtractor(adapter=adapter)
    >>> task = extractor.extract_indirect_superclasses_task(
    ...    subclass="GO:0005634", siblings=["GO:0005773"], roots=["GO:0043226"]
    ... )

    The extractor will actually perform the intended reasoning task, and include
    the expected answer in the Task object. This may seem a little circular, but
    the goal here is to evaluate.

    The task can then be passed to the reasoner engine:

    >>> from ontogpt.engines.reasoner_engine import ReasonerEngine
    >>> reasoner = ReasonerEngine()
    >>> result = reasoner.reason(task)

    We can expand on this:

    >>> for answer in result.answers:
    ...    print(f"PARENT: {answer.text}")
    <BLANKLINE>
    PARENT: MembraneBoundedOrganelle
    ...
    PARENT: IntracellularOrganelle

    We can also ask for explanations:

    >>> task.include_explanations = True
    >>> result = reasoner.reason(task)
    >>> for answer in result.answers:
    ...    print(f"PARENT: {answer.text}")
    ...    if answer.explanations:
    ...        print("  EXPLANATION:")
    ...        for e in answer.explanations:
    ...            for axiom in e.axioms:
    ...                print(f"    AXIOM: {axiom.text}")
    <BLANKLINE>
    ...
    PARENT: IntracellularOrganelle
        EXPLANATION:
            AXIOM: Nucleus SubClassOf IntracellularMembraneBoundedOrganelle
            AXIOM: IntracellularMembraneBoundedOrganelle SubClassOf IntracellularOrganelle

    """

    def reason(self, task: Task, template_path=None) -> ReasonerResult:
        """Reason over axioms and query entailments."""
        if template_path is None:
            template_path = DEFAULT_REASONING_PROMPT
        if isinstance(template_path, Path):
            template_path = str(template_path)
        if isinstance(template_path, str):
            # create a Jinja2 template object
            with open(template_path) as file:
                template_txt = file.read()
                template = Template(template_txt)
        prompt = template.render(
            task=task,
            ontology=task.ontology,
            query=task.query,
            examples=task.examples,
        )
        logger.info(f"Prompt: {prompt}")
        payload = self.client.complete(prompt)
        if task.has_multiple_answers:
            elements = payload.split("- ")
            answers = [self._parse(e) for e in elements]
        else:
            answers = [self._parse(payload)]
        rr = ReasonerResult(prompt=prompt, completion=payload, answers=[a for a in answers if a])
        self.evaluate(rr, task)
        return rr

    def _parse(self, payload: str) -> Optional[Answer]:
        """Parse answer from payload."""
        payload = payload.strip()
        if not payload:
            return None
        payload = payload.replace("\n", " ")
        pattern = r"^(.*?)\s*\[\s*(.*?)\s*\]\s*(.*?)$"
        match = re.match(pattern, payload)
        if match:
            text = match.group(1)
            explanation = match.group(2)
            rest = match.group(3)
            axioms = [x.strip() for x in split_on_one_of(explanation, [";", ","])]
            explanation = Explanation(axioms=[Axiom(text=a) for a in axioms if a])
            if rest:
                explanation.comments = [rest]
            return Answer(text=text, explanations=[explanation])
        else:
            return Answer(text=payload)

    def evaluate(self, result: ReasonerResult, task: Task):
        """Evaluate result against task."""
        task_answer_texts = {t.text for t in task.answers}
        result_answer_texts = {a.text for a in result.answers}
        ixn = task_answer_texts.intersection(result_answer_texts)
        all_texts = task_answer_texts.union(result_answer_texts)
        j_score = len(ixn) / len(all_texts)
        result.jaccard_score = j_score
        result.false_positives = list(result_answer_texts - task_answer_texts)
        result.false_negatives = list(task_answer_texts - result_answer_texts)
