import logging
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from time import sleep
from typing import Iterator, Tuple

import openai
from oaklib.utilities.apikey_manager import get_apikey_value
from openai.error import APIConnectionError

logger = logging.getLogger(__name__)
NUM_RETRIES = 3


@dataclass
class OpenAIClient:
    max_tokens: int = field(default_factory=lambda: 3000)
    engine: str = field(default_factory=lambda: "text-davinci-003")
    cache_db_path: str = None
    api_key: str = None

    def __post_init__(self):
        self.api_key = get_apikey_value("openai")
        openai.api_key = self.api_key

    def complete(self, prompt, **kwargs) -> str:
        engine = self.engine
        cur = self.db_connection()
        res = cur.execute("SELECT payload FROM cache WHERE prompt=? AND engine=?", (prompt, engine))
        payload = res.fetchone()
        if payload:
            prompt_peek = str(prompt)[0:80].replace("\n", "\\n")
            logger.info(f"Using cached payload for prompt: {prompt_peek}...")
            return payload[0]
        response = None
        i = 0
        while not response:
            i += 1
            logging.debug(f"Calling OpenAI API (attempt {i})...")
            try:
                response = openai.Completion.create(
                    engine=engine,
                    prompt=prompt,
                    max_tokens=self.max_tokens,
                    **kwargs,
                )
                break
            except Exception as e:
                logger.error(f"OpenAI API connection error: {e}")
                if i >= NUM_RETRIES:
                    raise e
                sleep_time = 4**i
                logger.info(f"Retrying {i} of {NUM_RETRIES} after {sleep_time} seconds...")
                sleep(sleep_time)
        payload = response.choices[0].text
        logger.info(f"Storing payload of len: {len(payload)}")
        cur.execute(
            "INSERT INTO cache (prompt, engine, payload) VALUES (?, ?, ?)",
            (prompt, engine, payload),
        )
        cur.connection.commit()
        return payload

    def db_connection(self):
        if not self.cache_db_path:
            self.cache_db_path = ".openai_cache.db"
        logger.info(f"Caching OpenAI responses to {Path(self.cache_db_path).absolute()}")
        create = not Path(self.cache_db_path).exists()
        con = sqlite3.connect(self.cache_db_path)
        cur = con.cursor()
        if create:
            cur.execute("CREATE TABLE cache (prompt, engine, payload)")
        return cur

    def cached_completions(
        self, search_term: str = None, engine: str = None
    ) -> Iterator[Tuple[str, str, str]]:
        if search_term:
            search_term = search_term.lower()
        cur = self.db_connection()
        res = cur.execute("SELECT engine, prompt, payload FROM cache")
        for row in res:
            if (
                search_term
                and search_term not in row[1].lower()
                and search_term not in row[2].lower()
            ):
                continue
            if engine and engine != row[0]:
                continue
            yield row
