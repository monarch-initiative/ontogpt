# Introduction

_OntoGPT_ is a Python package for extracting structured information from text with large language models (LLMs), _instruction prompts_, and ontology-based grounding. It works well with OpenAI's GPT models as well as a broad range of other providers through LiteLLM. OntoGPT's output can be used for general-purpose natural language tasks (e.g., named entity recognition and relation extraction), summarization, knowledge base and knowledge graph construction, and more.

## Methods

The primary extraction method currently implemented in OntoGPT is SPIRES:

* SPIRES: _Structured Prompt Interrogation and Recursive Extraction of Semantics_
  * A Zero-shot learning (ZSL) approach to extracting nested semantic structures from text
  * This approach takes two inputs - 1) LinkML schema 2) free text, and outputs knowledge in a structure conformant with the supplied schema in JSON, YAML, RDF or OWL formats
  * Uses OpenAI GPT models, many LiteLLM-supported hosted providers, or local models through Ollama

## Why OntoGPT?

A modern LLM can turn text into structured data on its own. OntoGPT exists for the parts of that job that LLMs, and the agents built on them, still get wrong or do inefficiently.

* **Grounding without hallucination.** Ask an LLM for an ontology identifier and it will often invent one, or attach a real identifier to the wrong term. OntoGPT does not ask the model for identifiers. It asks for names, grounds each name against the actual ontology through [OAK](https://github.com/INCATools/ontology-access-kit) annotators, and then validates every grounded identifier against its source ontology. A name that cannot be grounded is marked with the `AUTO:` prefix instead of being guessed. The only identifiers in the output are ones that exist.

* **Schema adherence without loading the whole schema.** A large data model does not fit well in a context window, and an agent that searches the model field by field for each document is slow and expensive. OntoGPT's SPIRES method walks a [LinkML](https://linkml.io) schema recursively. The model is prompted for one class at a time, with only that class's fields, so each prompt stays small and the assembled output conforms to the full schema.

* **Repeatable, batchable extraction.** A template plus a model gives the same procedure for every document. It runs from the command line or from Python over one abstract or thousands of papers, with prompt caching and output as YAML, JSON, RDF, or OWL, and with no agent in the loop deciding what to do next.

* **A library of ready templates.** Dozens of bundled templates cover diseases, phenotypes, drugs, genes, GO terms, environmental samples, and more, each already wired to the right ontologies. A new template is a LinkML schema with a few annotations; see the [documentation](custom.md).

* **Functions for agents.** When an AI agent does need to extract and ground, the bundled [Agent Skills](agent_skills.md) teach it to call OntoGPT for that step rather than reinvent grounding and schema-walking inside its own context.

## Quick Start

Please see the Setup page on the left for more detailed instructions.

OntoGPT runs on the command line, though there's also a minimal web app interface (see `Web Application` section below).

1. Ensure you have Python (3.10 to 3.13) installed.
2. Install with `pip`:

    ```bash
    pip install ontogpt
    ```

3. Set your OpenAI API key:

    ```bash
    runoak set-apikey -e openai <your openai api key>
    ```

4. See the list of all OntoGPT commands:

    ```bash
    ontogpt --help
    ```

5. Try a simple example of information extraction:

    ```bash
    echo "One treatment for high blood pressure is carvedilol." > example.txt
    ontogpt extract -i example.txt -t drug
    ```

    OntoGPT will retrieve the necessary ontologies and output results to the command line. Your output will provide all extracted objects under the heading `extracted_object`.

## Web Applications

There is a bare bones web application for running OntoGPT and viewing results.

First, install the required dependencies with `pip` by running the following command:

```bash
pip install ontogpt[web]
```

Then run this command to start the web application:

```bash
web-ontogpt
```

NOTE: We do not recommend hosting this webapp publicly without authentication.

## Citation

SPIRES is described further in: Caufield JH, Hegde H, Emonet V, Harris NL, Joachimiak MP, Matentzoglu N, et al. Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning. Bioinformatics. 2024;40. doi:[10.1093/bioinformatics/btae104](http://dx.doi.org/10.1093/bioinformatics/btae104)

## Contributing

Contributions are welcome! One way to get started with contributing to OntoGPT is to submit an issue.

Contributions on recipes to test welcome from anyone! Just make a PR [here](https://github.com/monarch-initiative/ontogpt/blob/main/tests/input/recipe-urls.csv). See [this list](https://github.com/hhursev/recipe-scrapers) for accepted URLs

## Acknowledgements

We gratefully acknowledge [Bosch Research](https://www.bosch.com/research) for their support of this research project.
