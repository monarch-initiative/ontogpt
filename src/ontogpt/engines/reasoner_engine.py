"""Reasoner engine."""
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

from jinja2 import Template
from pydantic import BaseModel

from ontogpt import MODELS
from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.ontex.extractor import (
    Answer,
    Axiom,
    Explanation,
    GPTReasonMethodType,
    Task,
    TaskCollection,
)
from ontogpt.prompts.reasoning import DEFAULT_REASONING_PROMPT
from ontogpt.utils.parse_utils import split_on_one_of

logger = logging.getLogger(__name__)


MODEL_GPT_4_NAMES = [model["alternative_names"][0] for model in MODELS if model["name"] == "MODEL_GPT_4"][0]

def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


class ReasonerResult(BaseModel):
    """The result of a reason query."""

    name: Optional[str] = None
    completed: Optional[bool] = True
    task_name: Optional[str] = None
    task_type: Optional[str] = None
    task_obfuscated: Optional[bool] = None
    method: Optional[GPTReasonMethodType] = None
    model: Optional[str] = None
    description: Optional[str] = None
    answers: Optional[List[Answer]] = None
    prompt: Optional[str] = None
    completion: Optional[str] = None
    jaccard_score: Optional[float] = 0.0
    false_positives: Optional[List[str]] = None
    false_negatives: Optional[List[str]] = None
    num_false_positives: Optional[int] = None
    num_false_negatives: Optional[int] = None
    num_true_positives: Optional[int] = None
    num_true_negatives: Optional[int] = None
    precision: Optional[float] = 0.0
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    len_shortest_explanation: Optional[int] = None

    class Config:
        """Pydantic config."""

        use_enum_values = True


class ReasonerResultSet(BaseModel):
    name: str = None
    results: List[ReasonerResult]


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

    completion_length = 250

    def reason(
        self, task: Task, template_path=None, strict=False, evaluate: bool = None
    ) -> ReasonerResult:
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
        completion_length = self.completion_length
        if task.method == GPTReasonMethodType.EXPLANATION:
            completion_length *= 2
        elif task.method == GPTReasonMethodType.CHAIN_OF_THOUGHT:
            completion_length *= 2
        logger.info(f"Prompt: {prompt}")
        prompt_length = len(self.encoding.encode(prompt)) + 10
        max_len_total = 4097
        if self.model in MODEL_GPT_4_NAMES:
            max_len_total = 8193
        max_len = max_len_total - completion_length
        completed = True
        logger.info(f"PROMPT LENGTH: {prompt_length} [max={max_len}]")
        if prompt_length > max_len:
            if strict:
                raise ValueError(f"Prompt length ({prompt_length}) exceeds maximum ({max_len})")
            logger.warning(f"Prompt length ({prompt_length}) exceeds maximum ({max_len})")
            answers = []
            completed = False
            payload = ""
        else:
            payload = self.client.complete(prompt, max_tokens=completion_length)
            if task.has_multiple_answers:
                elements = payload.split("- ")
                answers = [self._parse_single_answer(e, task) for e in elements]
            else:
                answers = [self._parse_single_answer(payload, task)]
            answers = [a for a in flatten_list(answers) if a is not None]
        result = ReasonerResult(
            completed=completed,
            task_name=task.name,
            task_type=task.type,
            task_obfuscated=task.obfuscated,
            method=task.method,
            len_shortest_explanation=task.len_shortest_explanation,
            model=self.model,
            prompt=prompt,
            completion=payload,
        )
        # TODO: determine which it doesn't work to initialize with this
        result.answers = answers
        logger.debug(f"Answers: {task.answers} // {answers}")
        result.name = f"{task.name}-{task.method.value}-{self.model}"
        if not task.answers and evaluate:
            raise ValueError(f"Cannot evaluate without expected answers: {task}")
        if task.answers is not None:
            self.evaluate(result, task)
        return result

    def reason_multiple(self, task_collection: TaskCollection, **kwargs) -> ReasonerResultSet:
        """
        Reason over multiple tasks.

        :param task_collection:
        :param kwargs:
        :return:
        """
        results = [self.reason(task, **kwargs) for task in task_collection.tasks]
        return ReasonerResultSet(results=results)

    def _parse_single_answer(
        self, payload: str, task: Task
    ) -> Optional[Union[Answer, List[Answer]]]:
        """Parse single answer from payload.

        In some cases for COT reasoning the model may compress multiple
        answers into a single answer line.
        """
        payload = payload.strip()
        if not payload:
            return None
        payload = payload.replace("\n", " ")
        if task.chain_of_thought:
            pattern = r"^REASONING:\s*\[\s*(.*?)\s*\]\s*CONCLUSION:\s*(.*?)$"
            match = re.match(pattern, payload)
            print(f"CHAIN OF THOUGHT: {payload}")
            if match:
                print(f"MATCH: {match.groups()}")
                explanation = match.group(1)
                text = match.group(2)
                # rest = match.group(3)
                axioms = [x.strip() for x in split_on_one_of(explanation, [";", ","])]
                explanation = Explanation(axioms=[Axiom(text=a) for a in axioms if a])
                axiom_texts = split_on_one_of(text, [";", ","])
                if len(axiom_texts) == 1:
                    return Answer(text=text, explanations=[explanation])
                else:
                    return [
                        Answer(text=axiom_text, explanations=[explanation])
                        for axiom_text in axiom_texts
                    ]
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
        logger.debug(f"Evaluating result: {result}")
        positives = {t.text for t in task.answers}
        result_answer_texts = {a.text for a in result.answers}
        ixn = positives.intersection(result_answer_texts)
        all_texts = positives.union(result_answer_texts)
        result.false_positives = list(result_answer_texts - positives)
        result.false_negatives = list(positives - result_answer_texts)
        result.num_false_positives = len(result.false_positives)
        result.num_false_negatives = len(result.false_negatives)
        result.num_true_positives = len(ixn)
        tp_plus_tn = result.num_true_positives + result.num_false_positives
        if tp_plus_tn == 0:
            result.precision = 0.0
        else:
            result.precision = result.num_true_positives / tp_plus_tn
        result.recall = result.num_true_positives / len(positives)
        if len(all_texts) == 0:
            result.jaccard_score = 0.0
        else:
            result.jaccard_score = len(ixn) / len(all_texts)
        if result.num_true_positives == 0:
            result.f1_score = 0.0
        else:
            result.f1_score = (
                2 * (result.precision * result.recall) / (result.precision + result.recall)
            )
