"""Generate the template catalog reference for the select-template skill.

Run from the repository root:

    uv run python util/gen_skill_template_catalog.py > skills/ontogpt-select-template/references/template-catalog.md
"""
import glob
import os

import yaml


def annotator_prefix(annotator: str, canonical: dict) -> str:
    """Guess the CURIE prefix an annotator grounds to, e.g. ``sqlite:obo:vbo`` -> ``VBO``.

    The ontology name is the last colon-separated part; its spelling is taken from
    an ``id_prefixes`` entry elsewhere in the templates when one matches, else upper-cased.
    """
    name = annotator.strip().strip('"').rstrip(":").rsplit(":", 1)[-1]
    if name.lower().endswith("-nr"):  # bioportal:hgnc-nr
        name = name[:-3]
    return canonical.get(name.lower(), name.upper())


def annotators_of(value) -> list:
    if not value:
        return []
    return [a for a in str(value).split(",") if a.strip().strip('"')]


SKIP = {"core", "halo", "personinfo", "error_analysis", "class_enrichment", "genesummary",
        "matrix_eval", "table_arrays", "table_values"}  # not text-extraction templates or internal
templates = []
for f in sorted(glob.glob("src/ontogpt/templates/*.yaml")):
    with open(f) as fh:
        templates.append((os.path.basename(f)[:-5], yaml.safe_load(fh)))
canonical = {}
for _, d in templates:
    for v in (d.get("classes") or {}).values():
        if isinstance(v, dict):
            for p in v.get("id_prefixes") or []:
                canonical.setdefault(p.lower(), p)
rows = []
for name, d in templates:
    classes = d.get("classes") or {}
    roots = [c for c, v in classes.items() if isinstance(v, dict) and v.get("tree_root")]
    desc = " ".join((d.get("description") or "").split())
    ents = []
    for c, v in classes.items():
        if not isinstance(v, dict):
            continue
        ann = (v.get("annotations") or {}).get("annotators")
        pref = v.get("id_prefixes") or []
        if ann or pref:
            ents.append((c, pref, ann))
    declared = {p for _, pref, _ in ents for p in pref}
    # A class with annotators but no id_prefixes still grounds: whatever CURIE the
    # annotator returns is kept. Report those prefixes too, marked with *.
    derived = {annotator_prefix(a, canonical) for _, pref, ann in ents if not pref
               for a in annotators_of(ann)} - declared
    prefixes = sorted([*declared, *(p + "*" for p in derived)], key=lambda p: p.rstrip("*"))
    rows.append((name, roots, desc, prefixes, ents))

print("# Bundled template catalog\n")
print("Generated from `src/ontogpt/templates/*.yaml` by `util/gen_skill_template_catalog.py`; "
      "rerun it from the repository root when templates change. "
      "Use a template with `ontogpt extract -t <name>`; `<name>.<ClassName>` targets one class. "
      "Grounding prefixes tell you which identifier namespaces the output will carry. "
      "A prefix marked `*` is inferred from the `annotators` of a class that declares no "
      "`id_prefixes`, so any CURIE that annotator returns is accepted; "
      "check it with `scripts/describe_template.py`.\n")
print("| Template | Root class | Grounds to | What it extracts |")
print("|---|---|---|---|")
for name, roots, desc, prefixes, ents in rows:
    if name in SKIP:
        continue
    # Full descriptions: the detail that decides between templates is often near the end.
    cell = desc.replace("|", "\\|")
    print(f"| `{name}` | {', '.join(roots) or '(none; use -T)'} | {', '.join(prefixes) or 'ungrounded'} | {cell} |")
print("\n## Templates that are not for text extraction\n")
print("- `core`: the upper-level schema every template imports (NamedEntity, CompoundExpression, Triple).")
print("- `halo`: schema for the HALO ontology-growing engine (`ontogpt halo`), not SPIRES.")
print("- `class_enrichment`, `genesummary`: gene-set enrichment and summary experiments (`ontogpt enrichment`, `eval`).")
print("- `error_analysis`, `matrix_eval`: data-model templates for reports and evaluations, not literature.")
print("- `personinfo`: a demo schema with no grounding.")
print("- `table_arrays`, `table_values`: numeric table capture from PDFs; no ontology grounding.")
