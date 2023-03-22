"""Command line interface for oak-ai."""
import codecs
import logging
import pickle
import sys
from dataclasses import dataclass
from io import BytesIO, TextIOWrapper
from pathlib import Path
from typing import Optional, List

import click
import jsonlines
import yaml

from ontogpt import __version__
from ontogpt.clients import OpenAIClient
from ontogpt.clients.pubmed_client import PubmedClient
from ontogpt.clients.soup_client import SoupClient
from ontogpt.engines.halo_engine import HALOEngine
from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.engines.synonym_engine import SynonymEngine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.resolver import create_evaluator
from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.io.markdown_exporter import MarkdownExporter

__all__ = [
    "main",
]

from ontogpt.io.owl_exporter import OWLExporter

from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.templates.core import ExtractionResult


@dataclass
class Settings:
    """
    Global command line settings.
    """
    cache_db: Optional[str] = None
    skip_annotators: Optional[List[str]] = None


settings = Settings()

def write_extraction(results: ExtractionResult, output: BytesIO, output_format: str = None, knowledge_engine: KnowledgeEngine = None):
    def _as_text_writer(f):
        if isinstance(f, TextIOWrapper):
            return f
        else:
            return codecs.getwriter("utf-8")(f)
    if output_format == "pickle":
        output.write(pickle.dumps(results))
    elif output_format == "md":
        output = _as_text_writer(output)
        exporter = MarkdownExporter()
        exporter.export(results, output)
    elif output_format == "html":
        output = _as_text_writer(output)
        exporter = HTMLExporter()
        exporter.export(results, output)
    elif output_format == "yaml":
        output = _as_text_writer(output)
        output.write(dump_minimal_yaml(results))
    elif output_format == "owl":
        output = _as_text_writer(output)
        exporter = OWLExporter()
        exporter.export(results, output, knowledge_engine.schemaview)
    else:
        output = _as_text_writer(output)
        output.write(dump_minimal_yaml(results))


template_option = click.option("-t", "--template", required=True, help="Template to use.")
target_class_option = click.option("-T", "--target-class", help="Target class (if not already root).")
engine_option = click.option("-e", "--engine", help="Engine to use, e.g. text-davinci-003.")
recurse_option = click.option(
    "--recurse/--no-recurse", default=True, show_default=True, help="Recursively parse structures."
)
output_option_wb = click.option(
    "-o", "--output", type=click.File(mode="wb"), default=sys.stdout, help="Output file."
)
output_option_txt = click.option(
    "-o", "--output", type=click.File(mode="w"), default=sys.stdout, help="Output file."
)
output_format_options = click.option(
    "-O",
    "--output-format",
    type=click.Choice(["json", "yaml", "pickle", "md", "html", "owl"]),
    default="yaml",
    help="Output format.",
)


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.option("--cache-db",
              help="Path to sqlite database to cache prompt-completion results")
@click.option("--skip-annotator",
              multiple=True,
              help="Skip annotator (e.g. --skip-annotator gilda)")
@click.version_option(__version__)
def main(verbose: int, quiet: bool, cache_db: str, skip_annotator):
    """CLI for oak-ai.

    :param verbose: Verbosity while running.
    :param quiet: Boolean to be quiet or verbose.
    """
    logger = logging.getLogger()
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    if quiet:
        logger.setLevel(level=logging.ERROR)
    logger.info(f"Logger {logger.name} set to level {logger.level}")
    if cache_db:
        settings.cache_db = cache_db
    if skip_annotator:
        settings.skip_annotators = list(skip_annotator)

@main.command()
@template_option
@target_class_option
@engine_option
@recurse_option
@output_option_wb
@click.option("--dictionary")
@output_format_options
@click.option("--auto-prefix",
              default="AUTO",
              help="Prefix to use for auto-generated classes.")
@click.argument("input")
def extract(template, target_class, dictionary, input, output, output_format, **kwargs):
    """Extract knowledge from text guided by schema, using SPIRES engine.

    Example:

        ontogpt extract -t gocam.GoCamAnnotations gocam-27929086.txt

    The input argument must be either a file path or a string. If the file path exists,
    it will be read. Otherwise, the input is assumed to be a string.

    You can also use fragments of existing schemas, use the --target-class option (-T) to
    specify an alternative Container/root class.

    Example:

        ontogpt -extract -t gocam.GoCamAnnotations -T GeneOrganismRelationship "the mouse Shh gene"

    """
    logging.info(f"Creating for {template}")
    ke = SPIRESEngine(template, **kwargs)
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.client.skip_annotators = settings.skip_annotators
    if dictionary:
        ke.load_dictionary(dictionary)
    if not input or input == "-":
        text = sys.stdin.read()
    else:
        if len(input) < 50 and Path(input).exists():
            text = open(input, "r").read()
        else:
            logging.info(f"Input {input} is not a file, assuming it is a string")
            text = input
    logging.info(f"Input text: {text}")
    if target_class:
        target_class_def = ke.schemaview.get_class(target_class)
    else:
        target_class_def = None
    results = ke.extract_from_text(text, target_class_def)
    write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@engine_option
@recurse_option
@output_option_wb
@output_format_options
@click.argument("pmid")
def pubmed_extract(pmid, template, output, output_format, **kwargs):
    """Extract knowledge from a pubmed ID."""
    logging.info(f"Creating for {template}")
    pmc = PubmedClient()
    text = pmc.text(pmid)
    ke = SPIRESEngine(template, **kwargs)
    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text)
    write_extraction(results, output, output_format)


@main.command()
@template_option
@engine_option
@recurse_option
@output_option_wb
@output_format_options
@click.option("--keyword",
              "-k",
              multiple=True,
              help="Keyword to search for (e.g. --keyword therapy). Also obtained from schema")
@click.argument("term_tokens", nargs=-1)
def search_and_extract(term_tokens, keyword, template, output, output_format, **kwargs):
    """Searches for relevant literature and extracts knowledge from it.
    """
    term = " ".join(term_tokens)
    logging.info(f"Creating for {template}; search={term} kw={keyword}")
    ke = SPIRESEngine(template, **kwargs)
    logging.info(f"Creating PubMed client for {template}; search={term}")
    pmc = PubmedClient()
    logging.info("Got client")
    keywords = list(keyword) if keyword else []
    logging.info(f"KW={keywords}")
    keywords.extend(ke.schemaview.schema.keywords)
    logging.info(f"Keywords={keywords}")
    if not keywords:
        raise ValueError("No keywords specified; use --keyword or annotate schema with keywords")
    pmids = list(pmc.search(term, keywords))
    logging.info(f"PMIDs={pmids}")
    pmid = pmids[0]
    logging.info(f"PMID={pmid}")
    text = pmc.text(pmid)
    logging.info(f"Input text: {text}")
    results = ke.extract_from_text(text)
    write_extraction(results, output, output_format)


@main.command()
@template_option
@engine_option
@recurse_option
@output_option_wb
@output_format_options
@click.argument("url")
def web_extract(template, url, output, output_format, **kwargs):
    """Extract knowledge from web page."""
    logging.info(f"Creating for {template}")
    web_client = SoupClient()
    text = web_client.text(url)
    print(f"## Text: \n\n{text}")
    ke = SPIRESEngine(template, **kwargs)
    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text)
    write_extraction(results, output, output_format)


@main.command()
@output_option_txt
@output_format_options
@click.option(
    "-C", "--context", required=True, help="domain e.g. anatomy, industry, health-related"
)
@click.argument("term")
def synonyms(term, context, output, output_format, **kwargs):
    """Extract synonyms."""
    logging.info(f"Creating for {term}")
    ke = SynonymEngine()
    out = str(ke.synonyms(term, context))
    output.write(out)


@main.command()
@engine_option
@recurse_option
@output_option_txt
@output_format_options
@click.option(
    "--num-tests",
    type=click.INT,
    default=5,
    show_default=True,
    help="number of iterations to cycle through.",
)
@click.argument("evaluator")
def eval(evaluator, num_tests, output, output_format, **kwargs):
    """Evaluate an extractor."""
    logging.info(f"Creating for {evaluator}")
    evaluator = create_evaluator(evaluator)
    evaluator.num_tests = num_tests
    eos = evaluator.eval()
    output.write(dump_minimal_yaml(eos, minimize=False))


@main.command()
@template_option
@engine_option
@click.option("-E", "--examples", type=click.File("r"), help="File of example objects.")
@recurse_option
@output_option_wb
@output_format_options
@click.argument("object")
def fill(template, object: str, examples, output, output_format, **kwargs):
    """Fills in missing values."""
    logging.info(f"Creating for {template}")
    ke = SPIRESEngine(template, **kwargs)
    object = yaml.safe_load(object)
    logging.info(f"Object to fill =  {object}")
    logging.info(f"Loading {examples}")
    examples = yaml.safe_load(examples)
    logging.debug(f"Input object: {object}")
    results = ke.generalize(object, examples)
    output.write(yaml.dump(results.dict()))


@main.command()
@template_option
@click.option("--input", "-i", type=click.File("r"), default=sys.stdin, help="Input file")
def parse(template, input):
    """Parse openai results."""
    logging.info(f"Creating for {template}")
    ke = SPIRESEngine(template)
    text = input.read()
    logging.debug(f"Input text: {text}")
    # ke.annotator = BioPortalImplementation()
    results = ke.parse_completion_payload(text)
    print(yaml.dump(results))


@main.command()
@click.option("-o", "--output", type=click.File(mode="w"), default=sys.stdout, help="Output file.")
@output_format_options
@engine_option
@click.option("-m", "match", help="Match string to use for filtering.")
@click.option("-D", "database", help="Path to sqlite database.")
def dump_completions(engine, match, database, output, output_format):
    """Dumps cached completions."""
    logging.info(f"Creating for {engine}")
    client = OpenAIClient()
    if database:
        client.cache_db_path = database
    if output_format == "jsonl":
        writer = jsonlines.Writer(output)
        for engine, prompt, completion in client.cached_completions(match):
            writer.write(dict(engine=engine, prompt=prompt, completion=completion))
    elif output_format == "yaml":
        for engine, prompt, completion in client.cached_completions(match):
            output.write(
                dump_minimal_yaml(dict(engine=engine, prompt=prompt, completion=completion))
            )
    else:
        output.write("# Cached Completions:\n")
        for engine, prompt, completion in client.cached_completions(match):
            output.write("## Entry\n")
            output.write(f"### Engine: {engine}\n")
            output.write(f"### Prompt:\n\n {prompt}\n\n")
            output.write(f"### Completion:\n\n {completion}\n\n")


@main.command()
@click.option("-o", "--output", type=click.File(mode="w"), default=sys.stdout, help="Output file.")
@click.argument("input", type=click.File("r"))
def convert_examples(input, output):
    """Converts training examples from YAML."""
    logging.info(f"Creating examples for {input}")
    example_doc = yaml.safe_load(input)
    writer = jsonlines.Writer(output)
    for example in example_doc["examples"]:
        prompt = example["prompt"]
        completion = yaml.dump(example["completion"], sort_keys=False)
        writer.write(dict(prompt=prompt, completion=completion))


@main.command()
@click.option("-o", "--output", type=click.File(mode="w"), default=sys.stdout, help="Output file.")
@click.option("-i", "--input", help="Input ontology.")
@click.option("-c", "--context", help="Context.")
@click.option(
    "--num-iterations",
    type=click.INT,
    default=5,
    show_default=True,
    help="number of iterations to cycle through.",
)
@click.argument("terms", nargs=-1)
def halo(input, context, terms, output, **kwargs):
    """Runs HALO over inputs."""
    engine = HALOEngine()
    engine.seed_from_file(input)
    if context is None:
        context = engine.ontology.elements[0].context
    engine.fixed_slot_values = {"context": context}
    engine.hallucinate(terms, **kwargs)
    output.write(dump_minimal_yaml(engine.ontology))


@main.command()
def list_templates():
    """Lists the templates."""
    print("TODO")


if __name__ == "__main__":
    main()
