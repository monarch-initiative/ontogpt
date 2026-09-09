#!/usr/bin/env python3
"""Describe an OntoGPT extraction template: what it asks the model for and how it grounds.

Usage:
    python describe_template.py <template>
    python describe_template.py <template> --class <ClassName>

<template> is a bundled template name (e.g. ``drug``) or a path to a LinkML
YAML file. The output lists the root class, every promptable slot with the text
the model will see, every NamedEntity class with its identifier prefixes and
annotators, and every enum. Run it inside the OntoGPT environment
(``uv run python ...`` or an activated venv) because it imports ontogpt.
"""

import argparse
import sys
from pathlib import Path

try:
    from linkml_runtime import SchemaView
    from linkml_runtime.linkml_model import ClassDefinition

    from ontogpt.io.template_loader import get_template_path
except ImportError as e:  # pragma: no cover
    sys.exit(
        f"Missing dependency ({e}). Run this inside the OntoGPT environment, "
        "e.g. `uv run python describe_template.py drug`."
    )

CORE_CLASSES = {"NamedEntity", "CompoundExpression", "Triple", "Publication", "ExtractionResult",
                "TextWithTriples", "TextWithEntity", "RelationshipType", "AnnotatorResult", "Any"}


def load_schemaview(template: str) -> SchemaView:
    """Load a SchemaView for a bundled template name or a YAML path."""
    if template.endswith(".yaml") or template.endswith(".yml"):
        path = Path(template)
        if not path.exists():
            sys.exit(f"No such file: {path}")
    else:
        path = get_template_path(template.split(".", 1)[0])
        if not path.exists():
            sys.exit(f"No bundled template named {template!r}. Try `ontogpt list-templates`.")
    core_path = get_template_path("core")
    # Custom schemas live outside the templates directory, so map the core import explicitly.
    return SchemaView(str(path), importmap={"core": str(core_path.with_suffix(""))})


def annotation(obj, key: str):
    """Return the value of a LinkML annotation, or None.

    linkml_runtime returns annotations as a dict of Annotation objects, or as a
    JsonObj on slots induced from imports, so handle both.
    """
    anns = getattr(obj, "annotations", None)
    if not anns:
        return None
    if isinstance(anns, dict):
        ann = anns.get(key)
    else:
        as_dict = getattr(anns, "_as_dict", None)
        ann = as_dict.get(key) if isinstance(as_dict, dict) else None
    if ann is None:
        return None
    if isinstance(ann, dict):
        return ann.get("value")
    return getattr(ann, "value", ann)


def slot_prompt(sv: SchemaView, slot) -> str:
    """Reproduce the text SPIRES puts in the prompt for a slot."""
    text = annotation(slot, "prompt") or slot.description
    if not text:
        text = f"semicolon-separated list of {slot.name}s" if slot.multivalued else f"the value for {slot.name}"
    text = " ".join(str(text).split())
    if slot.range in sv.all_enums():
        enum = sv.get_enum(slot.range)
        if enum and enum.permissible_values:
            text += " Must be one of: " + ", ".join(enum.permissible_values.keys())
    return text


def is_named_entity(sv: SchemaView, cls: ClassDefinition) -> bool:
    return "NamedEntity" in sv.class_ancestors(cls.name)


def describe_class(sv: SchemaView, cls: ClassDefinition, indent: str = "") -> None:
    print(f"{indent}{cls.name}" + (" (tree_root)" if cls.tree_root else ""))
    if cls.description:
        print(f"{indent}  {' '.join(cls.description.split())}")
    for slot in sv.class_induced_slots(cls.name):
        skipped = str(annotation(slot, "prompt.skip")).lower() == "true"
        if skipped:
            print(f"{indent}  - {slot.name}: [not prompted; filled by OntoGPT]")
            continue
        flags = []
        if slot.multivalued:
            flags.append("multivalued")
        if slot.range and slot.range in sv.all_classes():
            rc = sv.get_class(slot.range)
            flags.append("grounded -> " + slot.range if is_named_entity(sv, rc) else "nested -> " + slot.range)
        elif slot.range in sv.all_enums():
            flags.append(f"enum {slot.range}")
        elif slot.range:
            flags.append(slot.range)
        examples = annotation(slot, "prompt.examples")
        line = f"{indent}  - {slot.name} ({', '.join(flags)}): {slot_prompt(sv, slot)}"
        print(line)
        if examples:
            print(f"{indent}      examples shown to the model: {examples}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("template", help="bundled template name or path to a LinkML YAML file")
    parser.add_argument("--class", dest="cls", help="describe this class instead of the root")
    args = parser.parse_args()

    sv = load_schemaview(args.template)
    schema = sv.schema
    print(f"# {schema.title or schema.name}")
    if schema.description:
        print(" ".join(schema.description.split()))
    print()

    # Only classes defined in this file, not the ones pulled in from core.
    local_names = set((schema.classes or {}).keys())
    local_classes = [c for c in sv.all_classes().values() if c.name in local_names]
    roots = [c for c in local_classes if c.tree_root]

    print("## Root class and prompted slots")
    if args.cls:
        target = sv.get_class(args.cls)
        if target is None:
            sys.exit(f"No class named {args.cls!r} in this schema.")
        describe_class(sv, target)
    elif roots:
        for r in roots:
            describe_class(sv, r)
    else:
        print("  (no tree_root; OntoGPT will pick the first non-core class, so pass --target-class)")
    print()

    nested = [c for c in local_classes if not c.tree_root and not is_named_entity(sv, c)
              and c.name != (args.cls or "")]
    if nested:
        print("## Nested (compound) classes")
        for c in nested:
            describe_class(sv, c, indent="")
        print()

    entities = [c for c in local_classes if is_named_entity(sv, c) and not c.tree_root]
    print("## Grounded entity classes")
    if not entities:
        print("  (none: nothing in this template is grounded to an ontology)")
    for c in entities:
        prefixes = ", ".join(c.id_prefixes) if c.id_prefixes else "(no id_prefixes: any CURIE accepted)"
        annotators = annotation(c, "annotators") or "(no annotators: values are never grounded)"
        print(f"  {c.name}: prefixes {prefixes}; annotators {annotators}")
        id_slot = sv.induced_slot("id", c.name) if "id" in sv.class_slots(c.name) else None
        if id_slot is not None and id_slot.values_from:
            print(f"    restricted to enum value sets: {', '.join(id_slot.values_from)}")
        if id_slot is not None and id_slot.pattern:
            print(f"    id must match: {id_slot.pattern}")
    print()

    enums = {k: sv.get_enum(k) for k in (schema.enums or {}).keys()}
    if enums:
        print("## Enums")
        for name, enum in enums.items():
            if enum.permissible_values:
                print(f"  {name}: fixed values {', '.join(list(enum.permissible_values.keys())[:12])}"
                      + (" ..." if len(enum.permissible_values) > 12 else ""))
            elif enum.reachable_from or enum.include:
                print(f"  {name}: dynamic value set (descendants of ontology terms)")
            else:
                print(f"  {name}")


if __name__ == "__main__":
    main()
