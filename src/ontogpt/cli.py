"""Command line interface for oak-ai."""
import codecs
import logging
import pickle
import sys
from io import BytesIO

import click
import jsonlines
import yaml

from ontogpt import __version__
from ontogpt.clients import OpenAIClient
from ontogpt.clients.pubmed_client import PubmedClient
from ontogpt.clients.soup_client import SoupClient
from ontogpt.engines.halo_engine import HALOEngine
from ontogpt.engines.synonym_engine import SynonymEngine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.evaluation.resolver import create_evaluator
from ontogpt.io.markdown_exporter import MarkdownExporter

__all__ = [
    "main",
]

from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.templates.core import ExtractionResult
from ontogpt.templates.halo import Ontology


def write_extraction(results: ExtractionResult, output: BytesIO, output_format: str = None):
    if output_format == "pickle":
        output.write(pickle.dumps(results))
    elif output_format == "md":
        output = codecs.getwriter("utf-8")(output)
        exporter = MarkdownExporter()
        exporter.export(results, output)
    else:
        output = codecs.getwriter("utf-8")(output)
        output.write(dump_minimal_yaml(results))


template_option = click.option("-t", "--template", required=True, help="Template to use.")
engine_option = click.option("-e", "--engine", help="Engine to use, e.g. text-davinci-003.")
recurse_option = click.option(
    "--recurse/--no-recurse", default=True, show_default=True, help="Recursively parse structyres."
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
    type=click.Choice(["json", "yaml", "pickle", "md"]),
    default="yaml",
    help="Output format.",
)


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.version_option(__version__)
def main(verbose: int, quiet: bool):
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


@main.command()
@template_option
@engine_option
@recurse_option
@output_option_wb
@click.option("--dictionary")
@output_format_options
@click.argument("input")
def extract(template, dictionary, input, output, output_format, **kwargs):
    """Extract knowledge from text."""
    logging.info(f"Creating for {template}")
    ke = SPIRESEngine(template, **kwargs)
    if dictionary:
        ke.load_dictionary(dictionary)
    if not input or input == "-":
        input = sys.stdin
    else:
        input = open(input, "r")
    text = input.read()
    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text)
    write_extraction(results, output, output_format)


@main.command()
@template_option
@engine_option
@recurse_option
@output_option_wb
@output_format_options
@click.argument("input")
def pubmed_extract(template, input, output, output_format, **kwargs):
    """Extract knowledge from text."""
    logging.info(f"Creating for {template}")
    pmc = PubmedClient()
    text = pmc.text(input)
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
def list():
    """Lists the templates."""
    print("TODO")


if __name__ == "__main__":
    main()
