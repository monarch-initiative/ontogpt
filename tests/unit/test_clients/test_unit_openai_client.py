"""Open AI client tests."""
import re
import unittest

import yaml

from ontogpt.clients.openai_client import OpenAIClient
from tests import PROMPTS_FILE
from tests.unit import UNIT_CACHE_DB


class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def _client(self, engine: str) -> OpenAIClient:
        client = OpenAIClient(engine=engine)
        client.cache_db_path = UNIT_CACHE_DB
        return client

    def test_all_prompts(self):
        """Test all prompts."""
        prompt_doc = yaml.safe_load(open(PROMPTS_FILE))
        default_engine = prompt_doc.get("default_engine", "text-davinci-003")
        for prompt in prompt_doc["prompts"]:
            prompt_text = prompt["prompt"]
            if not isinstance(prompt_text, str):
                prompt_text = yaml.dump(prompt_text)
            engine = prompt.get("engine", default_engine)
            client = self._client(engine)
            pre_prompt = prompt.get("pre_prompt", "")
            prompt_text = "".join([pre_prompt, prompt_text])
            print(f"## Testing prompt [{engine}: [{len(prompt_text)}] {prompt_text}")
            ann = client.complete(prompt_text)
            print(f"## Response: len={len(ann)}")
            print(ann)
            for expected in prompt.get("expected", []):
                self.assertTrue(re.search(expected, ann, re.IGNORECASE))
