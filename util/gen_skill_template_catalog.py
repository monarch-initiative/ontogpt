"""Generate the template catalog reference for the select-template skill.

Run from the repository root:

    uv run python util/gen_skill_template_catalog.py > skills/ontogpt-select-template/references/template-catalog.md
"""
import glob
import os

import yaml

SKIP = {"core", "halo", "personinfo", "error_analysis", "class_enrichment", "genesummary",
        "matrix_eval", "table_arrays", "table_values"}  # not text-extraction templates or internal
rows = []
for f in sorted(glob.glob("src/ontogpt/templates/*.yaml")):
    name = os.path.basename(f)[:-5]
    d = yaml.safe_load(open(f))
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
    prefixes = sorted({p for _, pref, _ in ents for p in pref})
    rows.append((name, roots, desc, prefixes, ents))

print("# Bundled template catalog\n")
print("Generated from `src/ontogpt/templates/*.yaml`. Regenerate when templates change. "
      "Use a template with `ontogpt extract -t <name>`; `<name>.<ClassName>` targets one class. "
      "Grounding prefixes tell you which identifier namespaces the output will carry.\n")
print("| Template | Root class | Grounds to | What it extracts |")
print("|---|---|---|---|")
for name, roots, desc, prefixes, ents in rows:
    if name in SKIP:
        continue
    short = desc if len(desc) <= 230 else desc[:227].rsplit(" ", 1)[0] + "..."
    print(f"| `{name}` | {', '.join(roots) or '(none; use -T)'} | {', '.join(prefixes) or 'ungrounded'} | {short} |")
print("\n## Templates that are not for text extraction\n")
print("- `core`: the upper-level schema every template imports (NamedEntity, CompoundExpression, Triple).")
print("- `halo`: schema for the HALO ontology-growing engine (`ontogpt halo`), not SPIRES.")
print("- `class_enrichment`, `genesummary`: gene-set enrichment and summary experiments (`ontogpt enrichment`, `eval`).")
print("- `error_analysis`, `matrix_eval`: data-model templates for reports and evaluations, not literature.")
print("- `personinfo`: a demo schema with no grounding.")
print("- `table_arrays`, `table_values`: numeric table capture from PDFs; no ontology grounding.")
