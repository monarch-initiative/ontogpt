# Operation

## Getting Started

OntoGPT is run from the command line. See the full list of commands with:

```bash
ontogpt --help
```

For a simple example of text completion and testing to ensure OntoGPT is set up correctly, create a text file containing the following, saving the file as `example.txt`:

```bash
Why did the squid cross the coral reef?
```

Then try the following command:

```bash
ontogpt complete example.txt
```

You should get text output like the following:

```bash
Perhaps the squid crossed the coral reef for a variety of reasons:

1. Food: Squids are known to feed on small fish and other marine organisms, and there could have been a rich food source on the other side of the reef.

...
```

OntoGPT is intended to be used for information extraction. The following examples show how to accomplish this.

### Knowledge extraction using SPIRES

#### Working Mechanism

1. You provide an arbitrary data model, describing the structure you want to extract text into. This can be nested (but see limitations below). The predefined templates may be used.
2. Provide your preferred annotations for grounding `NamedEntity` fields
3. OntoGPT will:
    * Generate a prompt
    * Feed the prompt to a language model
    * Parse the results into a dictionary structure
    * Ground the results using a preferred annotator (e.g., an ontology)

#### Input

Consider some text from one of the input files being used in the OntoGPT test suite. You can find the text file [here](https://github.com/monarch-initiative/ontogpt/blob/main/tests/input/cases/gocam-betacat.txt). You can download the raw file from the GitHub link to that input text file, or copy its contents over into another file, say, `abstract.txt`. An excerpt:

  > The cGAS/STING-mediated DNA-sensing signaling pathway is crucial
  for interferon (IFN) production and host antiviral
  responses
  >
  > ...
  > [snip]
  > ...
  >
  > The underlying mechanism was the
  interaction of US3 with β-catenin and its hyperphosphorylation of
  β-catenin at Thr556 to block its nuclear translocation
  > ...
  > ...

We can extract knowledge from the above text this into the [GO pathway datamodel](https://github.com/monarch-initiative/ontogpt/blob/main/src/ontogpt/templates/gocam.yaml) by running the following command:

#### Command

```bash
ontogpt extract -t gocam.GoCamAnnotations -i ~/path/to/abstract.txt
```

Note: The value accepted by the `-t` / `--template` argument is the base name of one of the LinkML schema / data model available to OntoGPT.

Use the command `ontogpt list-templates` to see all templates. Use the name in the first column with the `--template` option.

Or, if you create your own schema (see the page on [custom schemas](custom.md)), you may pass the path to the .yaml file.

#### Output

The output returned from the above command can be optionally redirected into an output file using the `-o` / `--output`.

The following is a small part of what the larger schema-compliant output looks like:

```yaml
genes:
- HGNC:2514
- HGNC:21367
- HGNC:27962
- US3
- FPLX:Interferon
- ISG
gene_gene_interactions:
- gene1: US3
  gene2: HGNC:2514
gene_localizations:
- gene: HGNC:2514
  location: Nuclear
gene_functions:
- gene: HGNC:2514
  molecular_activity: Transcription
- gene: HGNC:21367
  molecular_activity: Production
...
```

#### Local Models

To use a local model, download it through `ollama` (see the setup page for more details: <https://monarch-initiative.github.io/ontogpt/setup/>)

Then specify it with the `-m` or `--model` option.

Example:

```bash
ontogpt extract -t drug -i ~/path/to/abstract.txt -m ollama/llama3
```

See the list of all downloaded models with this command:

```bash
ollama list
```

Note that models can and will vary in performance and larger models will not always perform more accurately or more efficiently.

#### OpenAI-compatible Proxy Servers

If accessing an LLM though an OpenAI client-compatible proxy server, you will need to set the following:

* Your API key. Set this the same way as the OpenAI API key, either as

```bash
runoak set-apikey -e openai <your openai api key>
```

or

```bash
export OPENAI_API_KEY="key goes here"
```

* The model name. This will go with the `--model` parameter.

* The base URL. This will go with the `--api-base` parameter.

* The provider name. Because this is an OpenAI-style proxy, this value should be `openai` and will go with the `--model-provider` parameter.

Here is an example with the `extract` command (this is not a public proxy and will not work without an API key):

```bash
ontogpt -vvv extract -t go_terms -i temp/genetest.txt -m anthropic/claude-opus --model-provider openai --api-base "https://api.cborg.lbl.gov"
```

## Caching

OntoGPT uses LiteLLM to work with multiple LLM APIs and providers.

LiteLLM caches prompts and responses by default.

OntoGPT uses LiteLLM's local disk cache.

Find more information about what is cached here:
* <https://docs.litellm.ai/docs/proxy/caching>
* <https://docs.litellm.ai/docs/completion/prompt_caching>

You may use the option `--cache-db` to specify the directory where the cache should be stored.