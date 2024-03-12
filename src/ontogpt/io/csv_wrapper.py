"""Utilities for CSVs and TSVs."""
import csv
import logging
from pathlib import Path
from typing import Any, List

from oaklib import get_adapter
from pydantic import BaseModel

logger = logging.getLogger(__name__)


def output_parser(obj: Any, file) -> List[str]:
    # Declare initial variables
    NULL_VALS = [
        "",
        "Not mentioned",
        "none mentioned",
        "Not mentioned in the text",
        "Not mentioned in the provided text.",
        "No exposures mentioned in the text.",
        "No exposures mentioned in the text.",
        "None mentioned in the text.",
        "None mentioned in the text",
        "Not mentioned in the text.",
        "None relevant",
        "No gene to molecular activity relationships mentioned in the text.",
        "No genes mentioned",
        "No genes mentioned in the text.",
        "None",
        "N/A",
    ]
    lines = []
    output_file = file

    # Extract all 'subject', 'predicate', and 'object' output lines
    with open(output_file, "r") as file:
        to_print = False
        perpetuators = tuple(["  subject:", "  predicate:", "  object:", "    "])
        for line in file:
            line = line.strip("\n")
            if line.startswith("extracted_object:"):
                to_print = True
            elif not line.startswith(perpetuators):
                to_print = False
            if to_print:
                lines.append(line)

    # Clean & strip lines
    lines = list(filter(lambda elem: not (elem.isspace()), lines))
    cleaned_lines = [x for x in lines if x.strip()]
    cleaned_lines = [x for x in cleaned_lines if x != "extracted_object: {}"]
    i = 1
    while i < len(cleaned_lines):
        if cleaned_lines[i].startswith("    "):
            cleaned_lines[i - 1] += " "
            cleaned_lines[i - 1] += cleaned_lines[i][4:]
            del cleaned_lines[i]
        else:
            i += 1
    # Remove any underdeveloped extracted objects
    i = 0
    while i < len(cleaned_lines):
        if cleaned_lines[i].startswith("extracted_object"):
            for index, elem in enumerate(cleaned_lines[i + 1 : i + 4]):
                if elem.startswith("extracted_object"):
                    next_index = i + 1 + index
                    del cleaned_lines[i:next_index]
                    i -= 1
        i += 1

    # Separate extracted values into indexed items in dictionary of lists
    grouped_lines = [cleaned_lines[n : n + 4] for n in range(0, len(cleaned_lines), 4)]
    trimmed_dict: dict = {"genes": [], "relationships": [], "exposures": []}
    for group in grouped_lines:
        group.pop(0)
    for group in grouped_lines:
        gene = group[0].split(":", 1)[1].strip()
        relation = group[1].split(":", 1)[1].strip()
        exposure = group[2].split(":", 1)[1].strip()
        trimmed_dict["genes"].append(gene)
        trimmed_dict["relationships"].append(relation)
        trimmed_dict["exposures"].append(exposure)

    # Remove all null values
    for _, value in trimmed_dict.copy().items():
        for i, elem in enumerate(value):
            if elem.lower() in (val.lower() for val in NULL_VALS):
                for _, value in trimmed_dict.items():
                    del value[i]

    # Find names for all ID entries in OBO Foundry
    for key, value in trimmed_dict.copy().items():
        for index, elem in enumerate(value):
            if ":" in elem:
                try:
                    prefix = elem[: (elem.index(":"))]
                    adapter_str = "sqlite:obo:" + str(prefix)
                    curr_adapter = get_adapter(adapter_str)
                    trimmed_dict[key][index] = curr_adapter.label(elem)
                except KeyError:
                    continue

    return lines


def write_obj_as_csv(obj: Any, file, minimize=True, index_field=None) -> None:
    if isinstance(obj, BaseModel):
        obj = obj.model_dump()
    if isinstance(obj, list):
        rows = obj
    elif not isinstance(obj, dict):
        if not index_field:
            index_fields = [k for k, v in obj.items() if v and isinstance(v, list)]
            if len(index_fields) == 1:
                index_field = index_fields[0]
                logger.warning(f"Using {index_field} as index field")
        rows = obj[index_field]
    else:
        raise ValueError(f"Cannot dump {obj} as CSV")
    if isinstance(file, Path) or isinstance(file, str):
        file = open(file, "w", encoding="utf-8")
    rows = [row.model_dump() if isinstance(row, BaseModel) else row for row in rows]
    writer = csv.DictWriter(file, fieldnames=rows[0].keys(), delimiter="\t")
    writer.writeheader()
    for row in rows:

        def _str(s):
            if s is None:
                return ""
            return str(s)

        # row = {k: v for k, v in row.items() if "\n" not in str(v)}
        row = {k: _str(v).replace("\n", r"\n").replace("\t", " ") for k, v in row.items()}
        writer.writerow(row)
