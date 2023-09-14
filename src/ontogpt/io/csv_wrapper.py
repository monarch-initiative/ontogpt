"""Utilities for CSVs and TSVs."""
import csv
import logging
from pathlib import Path
from typing import Any

from pydantic import BaseModel

logger = logging.getLogger(__name__)


def write_obj_as_csv(obj: Any, file, minimize=True, index_field=None) -> None:
    if isinstance(obj, BaseModel):
        obj = obj.dict()
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
    rows = [row.dict() if isinstance(row, BaseModel) else row for row in rows]
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
