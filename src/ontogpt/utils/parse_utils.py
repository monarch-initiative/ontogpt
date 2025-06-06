"""Utilities for parsing text."""

import re

from typing import List


def split_on_one_of(text: str, separators: List[str]) -> List[str]:
    """Split text on the first separator found."""
    for sep in separators:
        if sep in text:
            return text.split(sep)
    return [text]


def get_section_of_interest(data, tag_of_interest):
    # I blame adobe
    # Find the index of the element that matches the case-insensitive regex pattern
    start_index = None
    pattern = re.compile(tag_of_interest, re.IGNORECASE)
    if isinstance(data, str):
        data = data.split("\n")
    for i, item in enumerate(data):
        if pattern.search(item):
            start_index = i
            break

    if start_index is not None:
        # Find the index of the next element that starts with '<p>'
        next_index = next(
            (
                i
                for i, item in enumerate(data[start_index + 1:], start=start_index + 1)
                if item.startswith("<p>")
            ),
            None,
        )

        if next_index is not None:
            # Extract the desired element
            result = data[next_index]
            return result
        else:
            raise ValueError("No element starting with '<p>' found after the tag_of_interest")
    else:
        raise ValueError("No element matching the tag_of_interest found in the list.")


def get_span_values(text: str, find_text: str) -> List[str]:
    """
    Find spans in text.

    Given an input text and a text to find, return a list of span values
    containing the text to find. This is a list because the text may appear
    multiple times.
    The coordinates are inclusive. For example, "10:25" means the span starting
    from the 10th character and ending with the 25th character. The first
    character in the text has index 0.
    All newlines are treated as single characters.
    """
    span_values = []
    start = 0

    pattern = re.compile(re.escape(find_text), re.IGNORECASE)

    # Remove all newlines, replace with space
    text = text.replace("\n", " ")

    for match in pattern.finditer(text):
        start = match.start()
        end = match.end() - 1
        span_values.append(f"{start}:{end}")

    return span_values
