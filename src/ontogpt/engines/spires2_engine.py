"""
Rewrite of SPIRES to use OpenAI function feature.

See https://github.com/monarch-initiative/ontogpt/issues/132
"""
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import openai
from linkml_runtime.linkml_model import ClassDefinition

from ontogpt.engines.knowledge_engine import (
    ANNOTATION_KEY_PROMPT,
    ANNOTATION_KEY_PROMPT_SKIP,
    EXAMPLE,
    FIELD,
    OBJECT,
    KnowledgeEngine,
    chunk_text,
)
from ontogpt.templates.core import ExtractionResult

this_path = Path(__file__).parent


logger = logging.getLogger(__name__)


@dataclass
class SPIRES2Engine(KnowledgeEngine):
    """Knowledge extractor."""

    model: str = "gpt-3.5-turbo-0613"

    def extract_from_text(
        self, text: str, cls: ClassDefinition = None, object: OBJECT = None
    ) -> ExtractionResult:
        """
        Extract annotations from the given text.

        :param text:
        :param cls:
        :param object: optional stub object
        :return:
        """
        if cls is None:
            [cls] = [c for c in self.schemaview.all_classes().values() if c.tree_root]
        py_cls = self.template_module.__dict__[cls.name]
        schema = py_cls.schema()
        functions = [
            {
                "name": "extract_data",
                #"description":  cls.description,
                "description":  "paper",
                "parameters": schema,
            },
        ]
        # TODO: introspect schema to customize system content
        messages = [
            {"role": "system",
             "content": "You are a helpful assistant that extracts summaries from text as JSON for a database."},
            {"role": "user",
             "content": 'Extract a summary from the following text: ' + text},
        ]
        logger.info(json.dumps(functions, indent=2))
        # TODO: abstract this so as not hardcoded
        response = openai.ChatCompletion.create(
            model=self.model, functions=functions, messages=messages)
        logger.info(f"Response: {response}")
        r = response.choices[0]['message']['function_call']['arguments']
        extracted_object = py_cls(**json.loads(r))
        return ExtractionResult(
            input_text=text,
            extracted_object=extracted_object,
            named_entities=self.named_entities,
        )
