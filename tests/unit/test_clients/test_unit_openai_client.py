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
        # TODO: use a mock
        # for now we have a pseudo-mock test; the test uses cached responses
        # in UNIT_CACHE_DB.
        # if the test changes (e.g. a new prompt is added) then
        # 1. temporarily remove the setting for api_key (it will be set from your env)
        # 2. run the test
        # 3. commit the new cache db
        client = OpenAIClient(
            model=engine,
            api_key="fake",
            cache_db_path=UNIT_CACHE_DB,
        )
        return client

    def test_all_prompts(self):
        """Test all prompts."""
        prompt_doc = yaml.safe_load(open(PROMPTS_FILE))
        default_engine = prompt_doc.get("default_engine", "gpt-3.5-turbo")
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
