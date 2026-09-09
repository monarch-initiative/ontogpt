#!/usr/bin/env python3
"""Check an OntoGPT template before running an extraction with it.

Usage:
    python validate_template.py path/to/template.yaml [--codegen] [--check-annotators]

Checks:
  * the file parses as LinkML and imports core
  * exactly one class has tree_root: true
  * every class descending from NamedEntity has id_prefixes and annotators
  * every id_prefix is declared under prefixes:
  * every slot range names a class, enum, or type that exists
  * multivalued slots say how values are separated (semicolons)
  * annotator strings use a known OAK selector scheme
  * (--codegen) the pydantic model generates and imports, as OntoGPT does at load time
  * (--check-annotators) each annotator can be opened with OAK; sqlite:obo: ones download

Exit status is 1 when any error is found. Warnings do not change the exit status.
Run inside the OntoGPT environment (``uv run python ...``).
"""

import argparse
import importlib.util
import re
import shutil
import sys
import tempfile
from pathlib import Path

try:
    from linkml_runtime import SchemaView

    from ontogpt.io.template_loader import get_template_path
except ImportError as e:  # pragma: no cover
    sys.exit(
        f"Missing dependency ({e}). Run this inside the OntoGPT environment, "
        "e.g. `uv run python validate_template.py my_template.yaml`."
    )

KNOWN_SELECTOR_SCHEMES = (
    "sqlite:", "bioportal:", "gilda:", "ols:", "ubergraph:", "pronto:", "obo:", "ontobee:",
    "translator:", "sparql:", "wikidata:", "simpleobo:", "funowl:", "agrkb:", "pantherdb:",
)
BUILTIN_TYPES = {"string", "integer", "float", "double", "boolean", "uriorcurie", "uri", "curie",
                 "date", "datetime", "decimal", "time", "ncname", "objectidentifier", "nodeidentifier",
                 "jsonpointer", "jsonpath", "sparqlpath"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


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


def check_schema(path: Path) -> SchemaView:
    core = get_template_path("core")
    try:
        sv = SchemaView(str(path), importmap={"core": str(core.with_suffix(""))})
        sv.all_classes()
    except Exception as e:  # noqa: BLE001
        sys.exit(f"ERROR: schema failed to load: {e}")
    schema = sv.schema

    if "core" not in (schema.imports or []):
        err("imports must include `core` (gives you NamedEntity and CompoundExpression)")
    if "linkml:types" not in (schema.imports or []):
        err("imports must include `linkml:types`")
    if not schema.default_prefix:
        err("default_prefix is missing")
    elif schema.default_prefix not in (schema.prefixes or {}):
        err(f"default_prefix {schema.default_prefix!r} is not declared under prefixes:")
    if not schema.description:
        warn("schema has no description; `ontogpt list-templates` and template selection use it")

    local_names = set((schema.classes or {}).keys())
    local = {n: c for n, c in sv.all_classes().items() if n in local_names}
    if not local:
        err("schema defines no classes of its own")

    roots = [n for n, c in local.items() if c.tree_root]
    if len(roots) == 0:
        err("no class has tree_root: true; OntoGPT needs exactly one root")
    elif len(roots) > 1:
        err(f"more than one tree_root: {roots}")

    declared_prefixes = set(schema.prefixes or {})
    all_enums = sv.all_enums()
    all_types = set(sv.all_types()) | BUILTIN_TYPES

    for name, cls in local.items():
        ancestors = sv.class_ancestors(name)
        if "NamedEntity" in ancestors and name != "NamedEntity":
            if not cls.id_prefixes:
                warn(f"{name}: NamedEntity without id_prefixes; any CURIE the annotator returns is accepted")
            for p in cls.id_prefixes or []:
                if p not in declared_prefixes:
                    warn(f"{name}: id_prefix {p!r} is not declared under prefixes:; grounding still "
                         "works but OWL/RDF export cannot expand it")
                if p != p.strip() or ":" in p:
                    err(f"{name}: id_prefix {p!r} should be the bare prefix, no colon")
            annotators = annotation(cls, "annotators")
            if not annotators:
                if not cls.tree_root:
                    warn(f"{name}: NamedEntity without annotators; values will never be grounded "
                         "(they come back as AUTO:... or as raw text)")
            else:
                for a in [x.strip() for x in str(annotators).split(",")]:
                    if not a.startswith(KNOWN_SELECTOR_SCHEMES):
                        err(f"{name}: annotator {a!r} does not look like an OAK selector "
                            "(expected e.g. sqlite:obo:mondo, bioportal:SNOMEDCT, gilda:)")
                if ", " not in str(annotators) and "," in str(annotators):
                    err(f"{name}: separate annotators with a comma AND a space (', '); "
                        "OntoGPT splits on that exact string")
        for slot in sv.class_induced_slots(name):
            rng = slot.range
            if rng and rng not in sv.all_classes() and rng not in all_enums and rng not in all_types:
                err(f"{name}.{slot.name}: range {rng!r} is not a class, enum, or type in this schema")
            if slot.multivalued and not str(annotation(slot, "prompt.skip")).lower() == "true":
                text = str(annotation(slot, "prompt") or slot.description or "")
                if "semicolon" not in text.lower() and ";" not in text:
                    warn(f"{name}.{slot.name}: multivalued but the prompt text does not say "
                         "'semicolon-separated'; the model may use commas and values will merge")
    return sv


def check_codegen(path: Path) -> None:
    from linkml.generators.pydanticgen import PydanticGenerator

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        shutil.copy(get_template_path("core"), tmpdir / "core.yaml")
        target = tmpdir / path.name
        shutil.copy(path, target)
        try:
            src = PydanticGenerator(str(target)).serialize()
        except Exception as e:  # noqa: BLE001
            err(f"pydantic generation failed: {e}")
            return
        module_path = tmpdir / (target.stem + ".py")
        module_path.write_text(src, encoding="utf-8")
        spec = importlib.util.spec_from_file_location(target.stem, module_path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:  # noqa: BLE001
            err(f"generated pydantic module does not import: {e}")


def check_annotators(sv: SchemaView) -> None:
    from oaklib import get_adapter

    seen = set()
    for cls in sv.all_classes().values():
        annotators = annotation(cls, "annotators")
        if not annotators:
            continue
        for a in [x.strip() for x in str(annotators).split(",")]:
            if a in seen:
                continue
            seen.add(a)
            try:
                adapter = get_adapter(a)
                # Touch the adapter so lazy downloads happen now rather than mid-extraction.
                next(iter(adapter.entities(owl_type=None)), None) if a.startswith("sqlite:") else None
                print(f"  ok  {a}")
            except Exception as e:  # noqa: BLE001
                err(f"annotator {a!r} could not be opened: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("template", help="path to the LinkML YAML template")
    parser.add_argument("--codegen", action="store_true", help="also generate and import the pydantic model")
    parser.add_argument("--check-annotators", action="store_true",
                        help="also open every annotator with OAK (downloads sqlite:obo: ontologies)")
    args = parser.parse_args()

    path = Path(args.template)
    if not path.exists():
        sys.exit(f"No such file: {path}")
    if not re.match(r"^[a-z][a-z0-9_]*\.ya?ml$", path.name):
        warn(f"file name {path.name!r}: use lowercase letters, digits, underscores; OntoGPT imports it as "
             "a Python module named after the file")

    sv = check_schema(path)
    if args.codegen:
        check_codegen(path)
    if args.check_annotators:
        print("Opening annotators:")
        check_annotators(sv)

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1)
    print(f"\nOK: {len(warnings)} warning(s), no errors")


if __name__ == "__main__":
    main()
