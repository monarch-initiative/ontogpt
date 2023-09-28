# Introduction

_OntoGPT_ is a Python package for extracting structured information from text with large language models (LLMs), _instruction prompts_, and ontology-based grounding. It works well with OpenAI's GPT-3.5 and GPT-4 models as well as a selection of other LLMs. OntoGPT's output can be used for general-purpose natural language tasks (e.g., named entity recognition and relation extraction), summarization, knowledge base and knowledge graph construction, and more.

## Methods

Two different strategies for knowledge extraction are currently implemented in OntoGPT:

* SPIRES: *Structured Prompt Interrogation and Recursive Extraction of Semantics*
  * A Zero-shot learning (ZSL) approach to extracting nested semantic structures from text
  * This approach takes two inputs - 1) LinkML schema 2) free text, and outputs knowledge in a structure conformant with the supplied schema in JSON, YAML, RDF or OWL formats
  * Uses GPT-3.5-turbo, GPT-4, or one of a variety of open LLMs on your local machine
* SPINDOCTOR: *Structured Prompt Interpolation of Narrative Descriptions Or Controlled Terms for Ontological Reporting*
  * Summarizes gene set descriptions (pseudo gene-set enrichment)
  * Uses GPT-3.5-turbo or GPT-4

## Quick Start

Please see the Setup page on the left for more detailed instructions.

OntoGPT runs on the command line, though there's also a minimal web app interface (see `Web Application` section below).

1. Ensure you have Python 3.9 or greater installed.
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

## Web Application

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

### OWL Exports

The `extract` command will let you export the results as OWL axioms, utilizing [linkml-owl](https://linkml.io/linkml-owl) mappings in the schema.

Ex.:

```bash
ontogpt extract -t recipe -i recipe-spaghetti.txt -o recipe-spaghetti.owl -O owl
```

[src/ontogpt/templates/recipe.yaml](src/ontogpt/templates/recipe.yaml) is an example schema that uses linkml-owl mappings.

See the [Makefile](Makefile) for a full pipeline that involves using robot to extract a subset of FOODON
and merge in the extracted results. This uses [recipe-scrapers](https://github.com/hhursev/recipe-scrapers).

OWL output: [recipe-all-merged.owl](tests/output/owl/merged/recipe-all-merged.owl)

Classification:

![OWL in the Protege editor](https://user-images.githubusercontent.com/50745/230427663-20d845e9-f1d5-490e-b1ad-cdccdd0dca70.png "OWL in the Protege editor")

## Web Application Setup

There is a bare bones web application for running OntoGPT and viewing results.

Install the required dependencies by running the following command:

```bash
poetry install -E web
```

Then run this command to start the web application:

```bash
poetry run web-ontogpt
```

Note: The agent running uvicorn must have the API key set, so for obvious reasons don't host this publicly without authentication, unless you want your credits drained.

### SPINDOCTOR web app

To start:

```bash
poetry run streamlit run src/ontogpt/streamlit/spindoctor.py
```

### HuggingFace Hub

Note: support for HuggingFace-provided models is currently a work in progress.

A select number of LLMs may be accessed through HuggingFace Hub. See the full list using `ontogpt list-models`

Specify a model name with the `-m` option.

Example:

```bash
ontogpt extract -t mendelian_disease.MendelianDisease -i tests/input/cases/mendelian-disease-sly.txt -m FLAN_T5_BASE
```

## Citation

SPIRES is described further in: Caufield JH, Hegde H, Emonet V, Harris NL, Joachimiak MP, Matentzoglu N, et al. Structured prompt interrogation and recursive extraction of semantics (SPIRES): A method for populating knowledge bases using zero-shot learning. arXiv publication: <http://arxiv.org/abs/2304.02711>

SPINDOCTOR is described further in: Joachimiak MP, Caufield JH, Harris NL, Kim H, Mungall CJ. Gene Set Summarization using Large Language Models. arXiv publication: <http://arxiv.org/abs/2305.13338>

## Contributing

Contributions on recipes to test welcome from anyone! Just make a PR [here](https://github.com/monarch-initiative/ontogpt/blob/main/tests/input/recipe-urls.csv). See [this list](https://github.com/hhursev/recipe-scrapers) for accepted URLs

## Acknowledgements

We gratefully acknowledge [Bosch Research](https://www.bosch.com/research) for their support of this research project.
