"""Utilities for CSVs and TSVs."""

import csv
import logging
from pathlib import Path
from typing import Any, List
import yaml
import pandas as pd
import uuid
from tqdm import tqdm
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


def schema_plurals_to_camelcase(schema_path):
    """
    Returns a dictionary to map the underscored plural names to the
    schema-defined entity and relation types. Assumes that the user follows the
    convention that a type defined in singular with camel case is defined as
    part of EntityContainingDocument pluralized with underscores; e.g.
    GeneProteinInteraction --> gene_protein_interactions.

    For issues, tag @serenalotreck

    parameters:
        schema_path, str: path to schema YAML file

    returns:
        schema_types, dict: keys are underscored names, values are camelcase
            names
    """
    # Read in the schema
    with open(schema_path) as stream:
        schema = yaml.load(stream, yaml.FullLoader)

    # Get underscore names
    underscore_names = [
        name for name in schema["classes"]["EntityContainingDocument"]["attributes"]
    ]

    # Convert to camelcase names
    camelcase_map = {
        name: "".join([part.capitalize() for part in name.split("_")])[:-1]
        for name in underscore_names
    }

    # Confirm that the camelcase names exist
    for name in camelcase_map.values():
        assert name in schema["classes"].keys(), f"Name {name} does not appear in classes"

    return camelcase_map


def parse_yaml_predictions(yaml_path, schema_path):
    """
    Parse named entities and relations from the YAML output of OntoGPT.
    Currently only supports binary relations.

    For issues, tag @serenalotreck

    parameters:
        yaml_path, str: path to YAML file to parse. Can contain multiple
            YAML documents.
        schema_path, str: path to schema YAML file

    returns:
        ent_df, pandas df: dataframe with entities from YAML output
        rel_df, pandas df: dataframe with relations from YAML output
    """
    # Read in the YAML file
    with open(yaml_path) as stream:
        output_docs = list(yaml.safe_load_all(stream))

    # Get type map
    type_map = schema_plurals_to_camelcase(schema_path)

    # Initialize objects to store data
    ent_rows = []
    rel_rows = []

    # Format entity label to type dict
    # Note: Have to do this here because the named entity list gets added
    # to with every doc, instead of just containing entities for one doc at a
    # time
    ent_types = {}
    for doc in tqdm(output_docs):
        for typ, ent_list in doc["extracted_object"].items():
            for ent in ent_list:
                if isinstance(ent, str):
                    ent_types[ent] = typ

    # Parse documents
    # Note: assumes that in extracted_object, types with strings in a list are
    # entities, and types with dicts in a list are relations.
    for doc in output_docs:

        # Get the elements we need
        obj = doc["extracted_object"]
        ents = doc["named_entities"]

        # Index entities by ID
        ent_labels = {ent["id"]: ent["label"] for ent in ents}

        # Format relations
        rel_types = {k: v for k, v in obj.items() if all([isinstance(rl, dict) for rl in v])}
        for rel_type, rels in rel_types.items():
            for rel in rels:
                row = {}
                for i, pair in enumerate(
                    rel.items()
                ):  # Allows parsing without needing component entity types
                    # (relies on preservation of insertion order)
                    # Enforce binary relations
                    assert len(rel) == 2, "At least one relation is n-ary"
                    # Get subject and predicate
                    if i == 0:
                        row["subject"] = pair[1]
                    elif i == 1:
                        row["object"] = pair[1]
                # Get other relation data
                row["predicate"] = type_map[rel_type]
                row["category"] = rel_type
                row["provided_by"] = obj["id"]
                row["id"] = str(uuid.uuid4())
                rel_rows.append(row)

        # Format entities
        for ent, lab in ent_labels.items():
            row = {}
            row["id"] = ent
            try:
                row["category"] = ent_types[ent]
            except KeyError:
                row["category"] = "UNKNOWN"
            row["name"] = lab
            row["provided_by"] = obj["id"]
            ent_rows.append(row)

    # Make dataframes
    ent_df = pd.DataFrame(ent_rows)
    rel_df = pd.DataFrame(rel_rows)

    # Drop repeated entities
    ent_df = ent_df.drop_duplicates()
    rel_df = rel_df.drop_duplicates()

    return ent_df, rel_df
