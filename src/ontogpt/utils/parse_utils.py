"""Utilities for parsing text."""
from typing import List


def split_on_one_of(text: str, separators: List[str]) -> List[str]:
    """Split text on the first separator found."""
    for sep in separators:
        if sep in text:
            return text.split(sep)
    return [text]
