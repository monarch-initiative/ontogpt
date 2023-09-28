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

### Strategy 1: Knowledge extraction using SPIRES

#### Working Mechanism

1. You provide an arbitrary data model, describing the structure you want to extract text into. This can be nested (but see limitations below). The predefined [templates](src/ontogpt/templates/) may be used.
2. Provide your preferred annotations for grounding `NamedEntity` fields
3. OntoGPT will:
    * Generate a prompt
    * Feed the prompt to a language model
    * Parse the results into a dictionary structure
    * Ground the results using a preferred annotator (e.g., an ontology)

#### Input

Consider some text from one of the input files being used in the OntoGPT test suite. You can find the text file [here](tests/input/cases/gocam-betacat.txt). You can download the raw file from the GitHub link to that input text file, or copy its contents over into another file, say, `abstract.txt`. An excerpt:

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

We can extract knowledge from the above text this into the [GO pathway datamodel](src/ontogpt/templates/gocam.yaml) by running the following command:

#### Command

```bash
ontogpt extract -t gocam.GoCamAnnotations -i ~/path/to/abstract.txt
```

Note: The value accepted by the `-t` / `--template` argument is the base name of one of the LinkML schema / data model which can be found in the [templates](src/ontogpt/templates/) folder.

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

To use a local model, specify it with the `-m` or `--model` option.

Example:

```bash
ontogpt extract -t drug -i ~/path/to/abstract.txt -m nous-hermes-13b
```

See the list of all available models with this command:

```bash
ontogpt list-models
```

When specifying a local model for the first time, it will be downloaded to your local system.

## Strategy 2: Gene Enrichment using SPINDOCTOR

Given a set of genes, OntoGPT can find similarities among them.

Ex.:

```bash
ontogpt enrichment -U tests/input/genesets/sensory-ataxia.yaml
```

The default is to use ontological gene function synopses (via the Alliance API).

* To use narrative/RefSeq summaries, use the `--no-ontological-synopses` flag
* To run without any gene descriptions, use the `--no-annotations` flag

This strategy does not currently support using local models.
