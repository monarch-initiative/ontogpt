"""Tests for oak-ai."""
import logging
import os
from pathlib import Path

logger = logging.getLogger()
# logger.setLevel(level=logging.INFO)


ROOT = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = Path(ROOT) / "input"
CASES_DIR = INPUT_DIR / "cases"
INSTANCES_DIR = INPUT_DIR / "instances"
PROMPTS_DIR = INPUT_DIR / "prompts"
PROMPTS_FILE = PROMPTS_DIR / "prompts.yaml"
OUTPUT_DIR = Path(ROOT) / "output"
