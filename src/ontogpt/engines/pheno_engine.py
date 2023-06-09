"""Reasoner engine."""
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

from jinja2 import Template
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.engines.models import MODEL_GPT_4
from ontogpt.ontex.extractor import (
    Answer,
    Axiom,
    Explanation,
    GPTReasonMethodType,
    Task,
    TaskCollection,
)
from ontogpt.prompts.phenopacket import DEFAULT_PHENOPACKET_PROMPT
from ontogpt.prompts.reasoning import DEFAULT_REASONING_PROMPT
from ontogpt.utils.parse_utils import split_on_one_of

logger = logging.getLogger(__name__)



class Diagnosis(BaseModel):

    id: str
    label: str


@dataclass
class PhenoEngine(KnowledgeEngine):

    completion_length = 250

    def predict_disease(
        self, phenopacket: dict, template_path: Union[str, Path] = None
    ) -> str:
        if template_path is None:
            template_path = DEFAULT_PHENOPACKET_PROMPT
        if isinstance(template_path, Path):
            template_path = str(template_path)
        if isinstance(template_path, str):
            # create a Jinja2 template object
            with open(template_path) as file:
                template_txt = file.read()
                template = Template(template_txt)
        prompt = template.render(
            phenopacket=phenopacket,
        )
        payload = self.client.complete(prompt, max_tokens=self.completion_length)
        return payload


