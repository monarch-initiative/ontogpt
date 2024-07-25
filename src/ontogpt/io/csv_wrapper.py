"""Utilities for CSVs and TSVs."""

import csv
import logging
from pathlib import Path
from typing import Any, List, Optional
import yaml
import pandas as pd
import uuid
from tqdm import tqdm
from oaklib import get_adapter
from pydantic import BaseModel

from linkml_runtime import SchemaView

logger = logging.getLogger(__name__)

# TODO: reconsider pandas here - may not need a full DF

# These slots will not be included in entity list outputs
SKIP_SLOTS = ["id", "label"]


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


def schema_process(schema_path: str, root_class: Optional[str]):
    """
    Process schema with SchemaView to prepare for parsing.

    parameters:
        schema_path, str: path to schema YAML file
        root_class, str: name of the class to use as root for the schema

    returns:
        sv, SchemaView: schema view object for the schema
        classdef, ClassDefinition: class definition for the root class
    """
    # Read in the schema
    sv = SchemaView(schema_path)

    # Find root if needed, or use provided name
    if root_class is None:
        roots = [c.name for c in sv.all_classes().values() if c.tree_root]
        if len(roots) != 1:
            raise ValueError(f"Schema does not have singular root: {roots}")
        root_class = roots[0]
    classdef = sv.get_class(root_class)

    return sv, classdef


def parse_yaml_predictions(yaml_path: str, schema_path: str, root_class=None):
    """
    Parse named entities and relations from the YAML output of OntoGPT.

    Currently only supports binary relations. Assumes relations are named
    with subject, predicate, and object.

    For issues, tag @serenalotreck

    parameters:
        yaml_path, str: path to YAML file to parse. Can contain multiple
            YAML documents.
        schema_path, str: path to schema YAML file
        root_class, str: name of the class to use as root for the schema

    returns:
        ent_df, pandas df: dataframe with entities from YAML output
        rel_df, pandas df: dataframe with relations from YAML output
    """
    # Read in the YAML file
    with open(yaml_path) as stream:
        logger.info(f"Parsing documents in {yaml_path}")
        output_docs = list(yaml.safe_load_all(stream))
        if len(output_docs) == 0:
            logger.error(f"No documents found in {yaml_path}")
        else:
            logger.info(f"Found {len(output_docs)} documents.")

    # Get schemaview and target root class
    # This root may not be the same as the schema's root
    sv, classdef = schema_process(schema_path, root_class)

    # Initialize objects to store data
    ent_rows = []
    rel_rows = []

    # Format entity label to type dict
    # Note: Have to do this here because the named entity list gets added
    # to with every doc, instead of just containing entities for one doc at a
    # time
    # TODO: update once issue #351 is addressed
    # because then we could just use the named entities
    ent_types = {}
    for doc in tqdm(output_docs):
        try:
            for typ, ent_list in doc["extracted_object"].items():
                if typ in SKIP_SLOTS:
                    continue
                if isinstance(ent_list, list):
                    for ent in ent_list:
                        if isinstance(ent, str):
                            ent_types[ent] = typ
                elif isinstance(ent_list, str):
                    ent_types[ent_list] = typ
        except KeyError:
            logger.warning("No extracted_object found in document")

    logger.info(f"Entity types: {ent_types}")

    # Parse documents
    # Note: assumes that in extracted_object, types with strings in a list are
    # entities, and types with dicts in a list are relations.
    # TODO: map categories to external model like Biolink
    # (though this may not always be necessary)
    i = 0
    for doc in output_docs:

        # Get the elements we need
        try:
            obj = doc["extracted_object"]
        except KeyError:
            logger.warning(f"No extracted_object found in document {i}")
            i = i + 1
            continue
        try:
            ents = doc["named_entities"]
        except KeyError:
            logger.warning(f"No named_entities found in document {i}")
            i = i + 1
            continue

        # Get document ID, or generate one if not present
        try:
            doc_id = obj["id"]
        except KeyError:
            doc_id = str(i)
            logger.warning(f"No id found for document, will assign {doc_id}")
        i = i + 1

        # Index entities by ID
        ent_labels = {ent["id"]: ent["label"] for ent in ents}

        # Format relations
        # TODO: translate to SchemaView
        rel_types = {k: v for k, v in obj.items() if all([isinstance(rl, dict) for rl in v])}
        for rel_type, rels in rel_types.items():
            for rel in rels:

                row = {}
                row["id"] = str(uuid.uuid4())

                class_name = sv.get_slot(rel_type).range

                row["category"] = class_name
                row["provided_by"] = doc_id
                # TODO: permit n-ary relations, given we know what to do with them

                # If s, p, o are explicitly defined, use them
                if "subject" in rel.keys() and "object" in rel.keys():
                    row["subject"] = rel["subject"]
                    row["object"] = rel["object"]

                if "predicate" in rel.keys():
                    row["predicate"] = rel["predicate"]
                else:
                    row["predicate"] = class_name

                # If s, p, o are not explicitly defined, try to infer them
                if not row.get("subject") or not row.get("object"):
                    logger.info("s, p, o not explicitly defined in relation - inferring")
                    try:
                        for i, rel_part in enumerate(rel.values()):
                            if not isinstance(rel_part, str):
                                raise ValueError
                            if i == 0:
                                row["subject"] = rel_part
                            elif i == 1:
                                row["object"] = rel_part
                        rel_rows.append(row)
                    except KeyError:
                        logger.warning(f"Relation {rel} missing part")
                        continue
                    except ValueError:
                        logger.warning(f"Relation {rel} looks n-ary: {rel_part}")
                        continue
                else:
                    rel_rows.append(row)

        # Format entities
        for ent, lab in ent_labels.items():
            row = {}
            row["id"] = ent
            try:
                class_name = sv.get_slot(ent_types[ent]).range
                row["category"] = class_name
            except KeyError:
                row["category"] = "UNKNOWN"
            row["name"] = lab
            row["provided_by"] = doc_id
            ent_rows.append(row)

    # Check for empties
    # They will still be valid outputs, but may indicate an issue
    if len(ent_rows) == 0:
        logger.warning("No entities found in output")
    if len(rel_rows) == 0:
        logger.warning("No relations found in output")

    # Make dataframes
    ent_df = pd.DataFrame(ent_rows)
    rel_df = pd.DataFrame(rel_rows)

    # Drop repeated entities
    # TODO: provide option to retain repeated entities
    ent_df = ent_df.drop_duplicates()
    rel_df = rel_df.drop_duplicates()

    return ent_df, rel_df


def write_graph(nodes: pd.DataFrame, edges: pd.DataFrame):
    """
    Convert dataframes to string representation for nodes and edges.

    parameters:
        nodes, pandas df: dataframe with nodes
        edges, pandas df: dataframe with edges
        outdir, str: directory to write files to
    """
    nodes_str = nodes.to_csv(sep="\t", index=False)
    edges_str = edges.to_csv(sep="\t", index=False)

    return nodes_str, edges_str
