# Agent Skills for OntoGPT

These directories are [Agent Skills](https://agentskills.io): folders with a `SKILL.md` that an AI coding agent loads when a task matches the skill's description. They teach an agent to operate OntoGPT, whose job is to turn unstructured text into structured, ontology-grounded data.

| Skill | Use it to |
|---|---|
| [`ontogpt-extract`](ontogpt-extract/SKILL.md) | run extractions: install, keys, models, inputs, `ontogpt extract` and friends, reading and converting output |
| [`ontogpt-select-template`](ontogpt-select-template/SKILL.md) | pick the bundled template that fits a text and a goal, or decide none does. Includes a catalog of every template and a script that prints what a template asks for and grounds to |
| [`ontogpt-author-template`](ontogpt-author-template/SKILL.md) | write or change a template: schema reference, a guide to choosing ontologies and OAK annotators, a skeleton, and a validator |
| [`ontogpt-troubleshoot`](ontogpt-troubleshoot/SKILL.md) | diagnose empty outputs, `AUTO:` values, wrong ids, model and credential errors, cache and download surprises |

They are written for the agent, not the end user. Each `SKILL.md` gives a procedure; `references/` holds detail the agent reads on demand; `scripts/` holds helpers that run inside the OntoGPT environment (`uv run python <script>` or an activated venv).

## Installing the skills into an agent

The skills are plain directories, so installation is copying or linking.

**Claude Code, this repository.** Already done: `.claude/skills/` holds symlinks to these directories, so a Claude Code session opened in the repo sees them. To use them from other projects, copy or link the directories into `~/.claude/skills/`:

```bash
for s in skills/ontogpt-*; do ln -s "$(pwd)/$s" ~/.claude/skills/; done
```

**Claude Code, another project that uses OntoGPT.** Copy the four directories into that project's `.claude/skills/`.

**Other agents that implement Agent Skills** (Codex, Cursor, Gemini CLI, and others). Point the agent's skills directory at these folders, or copy them there. The format is the open specification; nothing here is Claude-specific.

**Skills-aware agents without a skills directory.** Paste the contents of the relevant `SKILL.md` into the system prompt and attach the `references/` files as documents.

## Keeping them current

- `ontogpt-select-template/references/template-catalog.md` is generated from `src/ontogpt/templates/*.yaml`. Regenerate it when templates are added or their descriptions change: the generator is `util/gen_skill_template_catalog.py`.
- The helper scripts import `ontogpt` and `linkml_runtime`; run them from the repository environment.
- The CLI tables in `ontogpt-extract/references/cli.md` mirror `ontogpt --help`. Update them when options change.

## Validating

The reference validator from the Agent Skills project checks frontmatter and naming:

```bash
pip install skills-ref
skills-ref validate skills/ontogpt-extract
```
