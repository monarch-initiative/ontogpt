# Setup

## Prerequisites

OntoGPT may be installed through `pip` or used directly from the GitHub repository. In the latter case, you will need to install the `poetry` dependency manager and precede commands with `poetry run`. [See the poetry installation documentation for more details.](https://python-poetry.org/docs/#installation)

### Additional requirements and options

* Python 3.9+

* OpenAI API key: necessary for using OpenAI's GPT models. This is a paid API and you will be charged based on usage. If you do not have an OpenAI account, [you may sign up here](https://platform.openai.com/signup).

You may also set additional API keys for optional resources:

* [BioPortal](https://bioportal.bioontology.org/) account (for grounding). The BioPortal key is necessary for using ontologies from [BioPortal](https://bioportal.bioontology.org/). You may get a key by signing up for an account on their web site.
* [NCBI E-utilities](https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/). The NCBI email address and API key are used for retrieving text and metadata from PubMed. You may still access these resources without identifying yourself, but you may encounter rate limiting and errors.
* [HuggingFace Hub](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token). This API key is necessary to retrieve models from the HuggingFace Hub service.

## Installation

To simply start using the package in your workspace:

```bash
pip install ontogpt
```

Note that some features require installing additional, optional dependencies. These may be installed as:

```bash
pip install ontogpt[extra_name]
```

where `extra_name` is one of the following:

* `docs` - dependencies for building documentation
* `gpt4all` - dependencies for running local models
* `huggingface` - dependencies for accessing LLMs from HuggingFace Hub, remotely or locally
* `recipes` - dependencies for recipe scraping and parsing
* `textract` - the textract plugin
* `web` - dependencies for the web application

For installation from the GitHub repository, particularly if you plan to contribute to feature development or other package code:

```bash
git clone https://github.com/monarch-initiative/ontogpt.git
cd ontogpt/
poetry install
```

Extras listed above may be installed as:

```bash
poetry install --extras extra_name
```

All commands should then be preceded by `poetry run`, or simply run `poetry shell` to create and enter a virtual environment for the project.

### Setting API keys

One OntoGPT and all of its dependencies are installed, you will need to set your API keys using the [Ontology Access Kit](https://github.com/INCATools/ontology-access-kit):

```bash
runoak set-apikey -e openai <your openai api key>
```

The optional keys may be set as follows:

```bash
runoak set-apikey -e bioportal <your bioportal api key>
runoak set-apikey -e ncbi-email <your email address>
runoak set-apikey -e ncbi-key <your NCBI api key>
runoak set-apikey -e hfhub-key <your HuggingFace Hub api key>
```

### Running local models

Using local models currently depends upon using the `gpt4all` package and may require additional setup steps specific to your computing environment.

See the [gpt4all documentation](https://docs.gpt4all.io/) for more details.
