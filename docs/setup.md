# Setup

## Prerequisites

OntoGPT may be installed through `pip` or used directly from the GitHub repository. In the latter case, you will need to install the `uv` dependency manager and precede commands with `uv run`. [See the uv installation documentation for more details.](https://docs.astral.sh/uv/getting-started/installation/)

OntoGPT uses `litellm` to interface with LLM endpoints. Familiarity with this framework is not necessary to use OntoGPT but may be helpful for troubleshooting. See the `litellm` [docs here](https://litellm.vercel.app/docs/).

### Additional requirements and options

* Python 3.9 to 3.13.

* OpenAI API key: necessary for using OpenAI's GPT models. This is a paid API and you will be charged based on usage. If you do not have an OpenAI account, [you may sign up here](https://platform.openai.com/signup).

You may also set additional API keys for optional resources:

* [BioPortal](https://bioportal.bioontology.org/) account (for grounding). The BioPortal key is necessary for using ontologies from [BioPortal](https://bioportal.bioontology.org/). You may get a key by signing up for an account on their web site.
* [NCBI E-utilities](https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/). The NCBI email address and API key are used for retrieving text and metadata from PubMed. You may still access these resources without identifying yourself, but you may encounter rate limiting and errors.

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

* `dev` - dependencies for testing
* `docs` - dependencies for building documentation
* `recipes` - dependencies for recipe scraping and parsing
* `web` - dependencies for the web application

For installation from the GitHub repository, particularly if you plan to contribute to feature development or other package code:

```bash
git clone https://github.com/monarch-initiative/ontogpt.git
cd ontogpt/
uv pip install .
```

Extras listed above may be installed as:

```bash
uv pip install -e .[extra_name]
```

All commands should then be preceded by `uv run`.

### Setting API keys

One OntoGPT and all of its dependencies are installed, you will need to set your API keys using the [Ontology Access Kit](https://github.com/INCATools/ontology-access-kit):

```bash
runoak set-apikey -e openai <your openai api key>
```

Other optional keys may be set as follows:

```bash
runoak set-apikey -e bioportal <your bioportal api key>
runoak set-apikey -e ncbi-email <your email address>
runoak set-apikey -e ncbi-key <your NCBI api key>
```

Other API keys may also be set this way, generally by using the name of the service hosting the API:

```bash
runoak set-apikey -e mistral-key <your Mistral api key>
runoak set-apikey -e anthropic-key <your Anthropic api key>
runoak set-apikey -e huggingface-key <your HuggingFace api key>
```

This is also a convenient way to set details for custom endpoints, e.g., for Azure OpenAI (set API key, API base URL, and API version):

```bash
runoak set-apikey -e azure-key <your Azure api key>
runoak set-apikey -e azure-base <your Azure base URL, like 'https://example-endpoint.openai.azure.com'>
runoak set-apikey -e azure-version <your Azure API version, like '2023-05-15'>
```

### Setup for local models

OntoGPT uses `ollama` to retrieve and run local models.

You will need to install `ollama` (see their [GitHub repo](https://github.com/ollama/ollama)), and you may need to start it as a service.

This may require a command like `ollama serve` or `sudo systemctl start ollama`.

Then retrieve a model with `ollama pull <modelname>`, e.g., `ollama pull llama3`.

The model may then be used in OntoGPT by prefixing its name with `ollama/`, e.g., `ollama/llama3`, along with the `--model` option.

See the list of all downloaded LLMs with the `ollama list` command.
