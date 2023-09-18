"""Synonym engine."""
import logging
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, List, Union

from jinja2 import Template
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.prompts.qa import GENERIC_QA_PROMPT

logger = logging.getLogger(__name__)

MAX_TOKENS = 300


class Question(BaseModel):
    name: str
    question: str
    original_question: str = ""
    answer: str = ""
    accepted_answer: str = ""
    iteration: int = 0
    instructions: str = ""
    prompt: str = ""
    model: str = ""


class Instruction(BaseModel):
    name: str
    text: str = ""
    template: str = ""


class QuestionCollection(BaseModel):
    url: str = ""
    questions: List[Question] = []
    instructions: List[Instruction] = []


@dataclass
class GenericEngine(KnowledgeEngine):
    def run(
        self,
        question_collection: QuestionCollection,
        template_path: Union[str, Path] = "",
    ) -> Iterator[Question]:
        if template_path is None:
            template_path = GENERIC_QA_PROMPT
        if isinstance(template_path, Path):
            template_path = str(template_path)
        if isinstance(template_path, str):
            # create a Jinja2 template object
            with open(template_path) as file:
                template_txt = file.read()
                main_template = Template(template_txt)
        for question in question_collection.questions:
            for instruction in question_collection.instructions:
                template = main_template
                if instruction.template is not None:
                    template = Template(instruction.template)
                prompt = template.render(
                    question=question.question,
                    instructions=instruction.text,
                )
                payload = self.client.complete(prompt, max_tokens=MAX_TOKENS)
                question_with_answer = deepcopy(question)
                question_with_answer.answer = payload
                question_with_answer.instructions = instruction.name
                question_with_answer.prompt = prompt
                question_with_answer.model = self.model
                yield question_with_answer
