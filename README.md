# OntoGPT

![OntoGPT Logo](/images/ontogpt_logo_3.jpg)

[![DOI](https://zenodo.org/badge/13996/monarch-initiative/ontogpt.svg)](https://zenodo.org/badge/latestdoi/13996/monarch-initiative/ontogpt)
![PyPI](https://img.shields.io/pypi/v/ontogpt)

## Introduction

_OntoGPT_ is a Python package for extracting structured information from text with large language models (LLMs), _instruction prompts_, and ontology-based grounding.

[For more details, please see the full documentation.](https://monarch-initiative.github.io/ontogpt/)

## Quick Start

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

## Model APIs

OntoGPT uses the `litellm` package (<https://litellm.vercel.app/>) to interface with LLMs.

This means most APIs are supported, including OpenAI, Azure, Anthropic, Mistral, Replicate, and beyond.

The model name to use may be found from the command `ontogpt list-models` - use the name in the first column with the `--model` option.

In most cases, this will require setting the API key for a particular service as above:

```bash
runoak set-apikey -e anthropic-key <your anthropic api key>
```

Some endpoints, such as OpenAI models through Azure, require setting additional details. These may be set similarly:

```bash
runoak set-apikey -e azure-key <your azure api key>
runoak set-apikey -e azure-base <your azure endpoint url>
runoak set-apikey -e azure-version <your azure api version, e.g. "2023-05-15">
```

These details may also be set as environment variables as follows:

```bash
export AZURE_API_KEY="my-azure-api-key"
export AZURE_API_BASE="https://example-endpoint.openai.azure.com"
export AZURE_API_VERSION="2023-05-15"
```

## Open Models

Open LLMs may be retrieved and run through the `ollama` package (<https://ollama.com/>).

You will need to install `ollama` (see the [GitHub repo](https://github.com/ollama/ollama)), and you may need to start it as a service with a command like `ollama serve` or `sudo systemctl start ollama`.

Then retrieve a model with `ollama pull <modelname>`, e.g., `ollama pull llama3`.

The model may then be used in OntoGPT by prefixing its name with `ollama/`, e.g., `ollama/llama3`, along with the `--model` option.

Some ollama models may not be listed in `ontogpt list-models` but the full list of downloaded LLMs can be seen with `ollama list` command.

## Evaluations

OntoGPT's functions have been evaluated on test data. Please see the full documentation for details on these evaluations and how to reproduce them.

## Related Projects

* [TALISMAN](https://github.com/monarch-initiative/talisman/), a tool for generating summaries of functions enriched within a gene set. TALISMAN uses OntoGPT to work with LLMs.

## Tutorials and Presentations

* Presentation: "Staying grounded: assembling structured biological knowledge with help from large language models" - presented by Harry Caufield as part of the AgBioData Consortium webinar series (September 2023)
  * [Slides](https://docs.google.com/presentation/d/1rMQVWaMju-ucYFif5nx4Xv3bNX2SVI_w89iBIT1bkV4/edit?usp=sharing)
  * [Video](https://www.youtube.com/watch?v=z38lI6WyBsY)
* Presentation: "Transforming unstructured biomedical texts with large language models" - presented by Harry Caufield as part of the BOSC track at ISMB/ECCB 2023 (July 2023)
  * [Slides](https://docs.google.com/presentation/d/1LsOTKi-rXYczL9vUTHB1NDkaEqdA9u3ZFC5ANa0x1VU/edit?usp=sharing)
  * [Video](https://www.youtube.com/watch?v=a34Yjz5xPp4)
* Presentation: "OntoGPT: A framework for working with ontologies and large language models" - talk by Chris Mungall at Joint Food Ontology Workgroup (May 2023)
  * [Slides](https://docs.google.com/presentation/d/1CosJJe8SqwyALyx85GWkw9eOT43B4HwDlAY2CmkmJgU/edit)
  * [Video](https://www.youtube.com/watch?v=rt3wobA9hEs&t=1955s)

## Citation

The information extraction approach used in OntoGPT, SPIRES, is described further in: Caufield JH, Hegde H, Emonet V, Harris NL, Joachimiak MP, Matentzoglu N, et al. Structured prompt interrogation and recursive extraction of semantics (SPIRES): A method for populating knowledge bases using zero-shot learning. _Bioinformatics_, Volume 40, Issue 3, March 2024, btae104, [https://doi.org/10.1093/bioinformatics/btae104](https://doi.org/10.1093/bioinformatics/btae104).

## Acknowledgements

This project is part of the [Monarch Initiative](https://monarchinitiative.org/). We also gratefully acknowledge [Bosch Research](https://www.bosch.com/research) for their support of this research project.
