"""Command line interface for ontogpt."""

import codecs
import json
import logging
import pickle
import sys
from copy import deepcopy
from dataclasses import dataclass
from io import BytesIO, TextIOWrapper
from pathlib import Path
from typing import List, Optional, Union

import click
import jsonlines

import yaml
from oaklib import get_adapter
from oaklib.cli import query_terms_iterator
from oaklib.interfaces import OboGraphInterface
from oaklib.io.streaming_csv_writer import StreamingCsvWriter
from sssom.parsers import parse_sssom_table, to_mapping_set_document
from sssom.util import to_mapping_set_dataframe

import ontogpt.ontex.extractor as extractor
from ontogpt import DEFAULT_MODEL, DEFAULT_MODEL_DETAILS, MODELS, __version__
from ontogpt.clients import OpenAIClient
from ontogpt.clients.pubmed_client import PubmedClient
from ontogpt.clients.soup_client import SoupClient
from ontogpt.clients.wikipedia_client import WikipediaClient
from ontogpt.engines.embedding_similarity_engine import SimilarityEngine
from ontogpt.engines.generic_engine import GenericEngine, QuestionCollection
from ontogpt.engines.halo_engine import HALOEngine  # type: ignore
from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.engines.mapping_engine import MappingEngine
from ontogpt.engines.pheno_engine import PhenoEngine
from ontogpt.engines.reasoner_engine import ReasonerEngine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.engines.synonym_engine import SynonymEngine
from ontogpt.evaluation.resolver import create_evaluator
from ontogpt.io.csv_wrapper import output_parser, write_obj_as_csv
from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.io.markdown_exporter import MarkdownExporter
from ontogpt.io.template_loader import get_template_details

__all__ = [
    "main",
]

from ontogpt.io.owl_exporter import OWLExporter
from ontogpt.io.rdf_exporter import RDFExporter
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.templates.core import ExtractionResult


@dataclass
class Settings:
    """Global command line settings."""

    cache_db: Optional[str] = None
    skip_annotators: Optional[List[str]] = None


settings = Settings()


def _as_text_writer(f):
    if isinstance(f, TextIOWrapper):
        return f
    else:
        return codecs.getwriter("utf-8")(f)


def write_extraction(
    results: ExtractionResult,
    output: BytesIO,
    output_format: str,
    knowledge_engine: KnowledgeEngine,
):
    """Write results of extraction to a given output stream."""
    # Check if this result contains anything writable first
    if results.extracted_object:
        exporter: Union[MarkdownExporter, HTMLExporter, RDFExporter, OWLExporter]

        if output_format not in ["pickle"]:
            output = _as_text_writer(output)

        if output_format == "pickle":
            output.write(pickle.dumps(results))
        elif output_format == "md":
            exporter = MarkdownExporter()
            exporter.export(results, output)
        elif output_format == "html":
            exporter = HTMLExporter(output=output)
            exporter.export(results, output)
        elif output_format == "yaml":
            output.write("---\n")  # type: ignore
            output.write(dump_minimal_yaml(results))  # type: ignore
        elif output_format == "turtle":
            exporter = RDFExporter()
            exporter.export(results, output, knowledge_engine.schemaview)
        elif output_format == "owl":
            exporter = OWLExporter()
            exporter.export(results, output, knowledge_engine.schemaview)
        elif output_format == "kgx":
            # output.write(write_obj_as_csv(results))
            output.write(dump_minimal_yaml(results))  # type: ignore
            with open("output.kgx.tsv") as secondoutput:
                for line in output_parser(obj=results, file=output):
                    secondoutput.write(line)
        else:
            output.write("---\n")  # type: ignore
            output.write(dump_minimal_yaml(results))  # type: ignore


# TODO: allow this to tolerate a local model
def get_model_by_name(modelname: str):
    """Retrieve a model name and metadata from those available.

    Returns a dict describing the selected model.
    """
    found = False
    for knownmodel in MODELS:
        these_knownmodel_names = [knownmodel["name"], knownmodel["canonical_name"]] + knownmodel[
            "alternative_names"
        ]
        if modelname in these_knownmodel_names:
            selectmodel = knownmodel
            found = True
            logging.info(
                f"Found model: {selectmodel['name']}, provided by {selectmodel['provider']}."
            )
            if "not_implemented" in selectmodel or "deprecated" in selectmodel:
                logging.error(f"Model {selectmodel['name']} not implemented or is deprecated.")
                raise NotImplementedError
            break
    if not found:
        logging.warning(
            f"""Model name not recognized or not supported yet. Using default, {DEFAULT_MODEL}.
            See all models with `ontogpt list-models`"""
        )
        selectmodel = DEFAULT_MODEL_DETAILS

    return selectmodel


inputfile_option = click.option("-i", "--inputfile", help="Path to a file containing input text.")
template_option = click.option("-t", "--template", required=True, help="Template to use.")
target_class_option = click.option(
    "-T", "--target-class", help="Target class (if not already root)."
)
interactive_option = click.option(
    "--interactive/--no-interactive",
    default=False,
    show_default=True,
    help="Interactive mode - rather than call the LLM API it will prompt you do this.",
)
model_option = click.option(
    "-m",
    "--model",
    help="Model name to use, e.g. orca-mini-7b or gpt-4."
    " See all model names with ontogpt list-models.",
)
prompt_template_option = click.option(
    "--prompt-template", help="Path to a file containing the prompt."
)
recurse_option = click.option(
    "--recurse/--no-recurse", default=True, show_default=True, help="Recursively parse structures."
)
use_textract_options = click.option(
    "--use-textract/--no-use-textract",
    default=False,
    show_default=True,
    help="Use textract to extract text.",
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
    type=click.Choice(["json", "yaml", "pickle", "md", "html", "owl", "turtle", "jsonl"]),
    default="yaml",
    help="Output format.",
)
auto_prefix_option = click.option(
    "--auto-prefix",
    default="AUTO",
    help="Prefix to use for auto-generated classes. Default is AUTO.",
)
show_prompt_option = click.option(
    "--show-prompt/--no-show-prompt",
    default=False,
    show_default=True,
    help="If set, show all prompts passed to model through an API. Use with verbose setting.",
)
azure_select_option = click.option(
    "--azure-select/--no-azure-select",
    default=False,
    show_default=True,
    help="Use OpenAI model through Azure.",
)


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.option("--cache-db", help="Path to sqlite database to cache prompt-completion results")
@click.option(
    "--skip-annotator",
    multiple=True,
    help="Skip one or more annotators (e.g. --skip-annotator gilda)",
)
@click.version_option(__version__)
def main(verbose: int, quiet: bool, cache_db: str, skip_annotator):
    """CLI for ontogpt.

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
@inputfile_option
@template_option
@target_class_option
@model_option
@recurse_option
@output_option_wb
@click.option("--dictionary")
@output_format_options
@use_textract_options
@auto_prefix_option
@show_prompt_option
@click.option(
    "--set-slot-value",
    "-S",
    multiple=True,
    help="Set slot value, e.g. --set-slot-value has_participant=protein",
)
@click.argument("input", required=False)
@azure_select_option
def extract(
    inputfile,
    template,
    target_class,
    dictionary,
    input,
    output,
    output_format,
    set_slot_value,
    use_textract,
    model,
    show_prompt,
    azure_select,
    **kwargs,
):
    """Extract knowledge from text guided by schema, using SPIRES engine.

    Example:

        ontogpt extract -t gocam.GoCamAnnotations -i gocam-27929086.txt

    The input argument may be:
        A file path,
        A directory,
        or a string.
    Use the -i/--input-file option followed by the path to the input file
    or directory.
    If the input is a directory, all files with the .txt extension will be read.
    This is not recursive.
    Otherwise, the input is assumed to be a string to be read as input.

    You can also use fragments of existing schemas, use the --target-class option (-T) to
    specify an alternative Container/root class.

    Example:

        ontogpt extract -t gocam.GoCamAnnotations -T GeneOrganismRelationship "the mouse Shh gene"

    """
    # Choose model based on input, or use the default
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    inputlist = []

    if not inputfile or inputfile == "-":
        text = sys.stdin.read()
        inputlist.append(text)
    elif inputfile and Path(inputfile).is_dir():
        logging.info(f"Input file directory: {inputfile}")
        inputfiles = Path(inputfile).glob("*.txt")
        inputlist = [open(f, "r").read() for f in inputfiles if f.is_file()]
        logging.info(f"Found {len(inputlist)} input files here.")
    elif inputfile and Path(inputfile).exists():
        logging.info(f"Input file: {inputfile}")
        if use_textract:
            import textract

            text = textract.process(inputfile).decode("utf-8")
        else:
            text = open(inputfile, "r").read()
        logging.info(f"Input text: {text}")
        inputlist.append(text)
    elif inputfile and not Path(inputfile).exists():
        raise FileNotFoundError(f"Cannot find input file {inputfile}")

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        use_azure=azure_select,
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.client.skip_annotators = settings.skip_annotators

    if dictionary:
        ke.load_dictionary(dictionary)
    if target_class:
        schemaview = template_details[3]
        target_class_def = schemaview.get_class(target_class)
    else:
        target_class_def = None

    i = 0
    for input_entry in inputlist:
        if len(inputlist) > 1:
            i = i + 1
            logging.info(f"Now extracting from file {i} of {len(inputlist)}")
        results = ke.extract_from_text(
            text=input_entry, cls=target_class_def, show_prompt=show_prompt
        )
        if set_slot_value:
            for slot_value in set_slot_value:
                slot, value = slot_value.split("=")
                setattr(results.extracted_object, slot, value)
        write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@auto_prefix_option
@show_prompt_option
@click.argument("entity")
def generate_extract(model, entity, template, output, output_format, show_prompt, **kwargs):
    """Generate text and then extract knowledge from it."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    logging.debug(f"Input entity: {entity}")
    results = ke.generate_and_extract(
        entity=entity, prompt_template=template, show_prompt=show_prompt
    )
    write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@auto_prefix_option
@show_prompt_option
@click.option("--ontology", "-r", help="Ontology to use; use oaklib selector path")
@click.option("--max-iterations", "-M", default=10, type=click.INT)
@click.option("--iteration-slot", "-I", multiple=True, help="Slots to iterate over")
@click.option("--db", "-D", help="Where the resulting yaml database is stored")
@click.option(
    "--clear/--no-clear", default=False, show_default=True, help="Clear the db before starting"
)
@click.argument("entity")
def iteratively_generate_extract(
    model,
    entity,
    template,
    output,
    output_format,
    db,
    iteration_slot,
    max_iterations,
    clear,
    ontology,
    show_prompt,
    **kwargs,
):
    """Iterate through generate-extract."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    logging.debug(f"Input entity: {entity}")
    adapter = get_adapter(ontology)
    for results in ke.iteratively_generate_and_extract(
        entity,
        db,
        show_prompt=show_prompt,
        iteration_slots=list(iteration_slot),
        max_iterations=max_iterations,
        adapter=adapter,
        clear=clear,
    ):
        write_extraction(results, output, output_format, ke)


# TODO: combine this command with pubmed_annotate - they are converging
@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.option(
    "--get-pmc/--no-get-pmc",
    default=False,
    help="Attempt to parse PubMed Central full text(s) instead of abstract(s) alone.",
)
@click.argument("pmid")
def pubmed_extract(model, pmid, template, output, output_format, get_pmc, show_prompt, **kwargs):
    """Extract knowledge from a single PubMed ID."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    pmc = PubmedClient()
    if get_pmc:
        logging.info(f"Will try to retrieve PubMed Central text for {pmid}.")
        textlist = pmc.text(pmid, pubmedcental=True)
    else:
        textlist = pmc.text(pmid)
    for text in textlist:
        logging.debug(f"Input text: {text}")
        results = ke.extract_from_text(text=text, show_prompt=show_prompt)
        write_extraction(results, output, output_format)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.option(
    "--limit",
    default=20,
    help="Total number of citation records to return.",
)
@click.option(
    "--get-pmc/--no-get-pmc",
    default=False,
    help="Attempt to parse PubMed Central full text(s) instead of abstract(s) alone.",
)
@click.argument("search")
def pubmed_annotate(
    model, search, template, output, output_format, limit, get_pmc, show_prompt, **kwargs
):
    """Retrieve a collection of PubMed IDs for a search term; annotate them using a template.

    Example:
    ontogpt pubmed-annotate -t phenotype "Takotsubo Cardiomyopathy: A Brief Review"
        --get-pmc --model gpt-3.5-turbo-16k --limit 3
    """
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    pubmed_annotate_limit = limit
    pmc = PubmedClient()
    pmids = pmc.get_pmids(search)
    if get_pmc:
        logging.info("Will try to retrieve PubMed Central texts.")
        textlist = pmc.text(pmids[: pubmed_annotate_limit + 1], pubmedcental=True)
    else:
        textlist = pmc.text(pmids[: pubmed_annotate_limit + 1])
    for text in textlist:
        logging.debug(f"Input text: {text}")
        results = ke.extract_from_text(text=text, show_prompt=show_prompt)
        write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.option("--auto-prefix", default="AUTO", help="Prefix to use for auto-generated classes.")
@click.argument("article")
def wikipedia_extract(model, article, template, output, output_format, show_prompt, **kwargs):
    """Extract knowledge from a Wikipedia page."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    logging.info(f"Creating for {template} => {article}")
    client = WikipediaClient()
    text = client.text(article)

    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text=text, show_prompt=show_prompt)
    write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.option(
    "--keyword",
    "-k",
    multiple=True,
    help="Keyword to search for (e.g. --keyword therapy). Also obtained from schema",
)
@click.argument("topic")
def wikipedia_search(model, topic, keyword, template, output, output_format, show_prompt, **kwargs):
    """Extract knowledge from a Wikipedia page."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )

    logging.info(f"Creating for {template} => {topic}")
    client = WikipediaClient()
    keywords = list(keyword) if keyword else []
    logging.info(f"KW={keywords}")

    keywords.extend(ke.schemaview.schema.keywords)
    search_term = f"{topic + ' ' + ' '.join(keywords)}"
    print(f"Searching for {search_term}")
    search_results = client.search_wikipedia_articles(search_term)
    for _index, result in enumerate(search_results, start=1):
        title = result["title"]
        text = client.text(title)
        logging.debug(f"Input text: {text}")
        if len(text) > 4000:
            # TODO - expand this to fit context limits better
            # or add as cli option
            text = text[:4000]
        results = ke.extract_from_text(text=text, show_prompt=show_prompt)
        write_extraction(results, output, output_format, ke)
        break


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.option(
    "--keyword",
    "-k",
    multiple=True,
    help="Keyword to search for (e.g. --keyword therapy). Also obtained from schema",
)
@click.argument("term_tokens", nargs=-1)
def search_and_extract(
    model, term_tokens, keyword, template, output, output_format, show_prompt, **kwargs
):
    """Search for relevant literature and extract knowledge from it."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )

    term = " ".join(term_tokens)
    logging.info(f"Creating for {template}; search={term} kw={keyword}")

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
    results = ke.extract_from_text(text=text, show_prompt=show_prompt)
    write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.argument("url")
def web_extract(model, template, url, output, output_format, show_prompt, **kwargs):
    """Extract knowledge from web page."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    web_client = SoupClient()
    text = web_client.text(url)

    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text=text, show_prompt=show_prompt)
    write_extraction(results, output, output_format, ke)


@main.command()
@output_option_wb
@click.option("--dictionary")
@output_format_options
@click.option(
    "--recipes-urls-file",
    "-R",
    help="File with URLs to recipes to use for extraction",
)
@click.option("--auto-prefix", default="AUTO", help="Prefix to use for auto-generated classes.")
@model_option
@show_prompt_option
@click.argument("url")
def recipe_extract(
    model, url, recipes_urls_file, dictionary, output, output_format, show_prompt, **kwargs
):
    """Extract from recipe on the web."""
    try:
        from recipe_scrapers import scrape_me
    except ModuleNotFoundError as e:
        logging.error(
            f"Did not find recipe_scrapers. Try: poetry install extras=recipes. Error: {e}"
        )

    template = "recipe"

    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators

    if recipes_urls_file:
        with open(recipes_urls_file, "r") as f:
            urls = [line.strip() for line in f.readlines() if url in line]
            if len(urls) != 1:
                raise ValueError(f"Found {len(urls)} URLs in {recipes_urls_file}")
            url = urls[0]
    scraper = scrape_me(url)

    if dictionary:
        ke.load_dictionary(dictionary)
    ingredients = "\n".join(scraper.ingredients())
    instructions = "\n".join(scraper.instructions_list())
    text = f"""
    Recipe: {scraper.title()}
    Ingredients:\n{ingredients}
    Instructions:\n{instructions}
    """
    logging.info(f"Input text: {text}")
    results = ke.extract_from_text(text=text, show_prompt=show_prompt)
    logging.debug(f"Results: {results}")
    results.extracted_object.url = url
    write_extraction(results, output, output_format, ke)


@main.command()
@model_option
@template_option
@output_option_wb
@output_format_options
@click.argument("input")
def convert(model, template, input, output, output_format, **kwargs):
    """Convert output format."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )

    cls = ke.template_pyclass
    with open(input, "r") as f:
        data = yaml.safe_load(f)
    obj = cls(**data["extracted_object"])
    results = ExtractionResult(extracted_object=obj)
    write_extraction(results, output, output_format, ke)


@main.command()
@model_option
@output_option_txt
@output_format_options
@click.option(
    "-C", "--context", required=True, help="domain e.g. anatomy, industry, health-related"
)
@click.argument("term")
def synonyms(model, term, context, output, output_format, **kwargs):
    """Extract synonyms."""
    logging.info(f"Creating for {term}")

    if not model:
        model = DEFAULT_MODEL

    selectmodel = get_model_by_name(model)
    model_name = selectmodel["canonical_name"]
    model_source = selectmodel["provider"]

    if model_source != "OpenAI":
        raise NotImplementedError("Model not yet supported for this function.")

    ke = SynonymEngine(model=model_name, model_source=model_source.lower())
    out = ke.synonyms(term, context)
    for line in out:
        output.write(f"{line}\n")


@main.command()
@output_option_txt
@output_format_options
@model_option
@azure_select_option
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.argument("text", nargs=-1)
def embed(text, context, output, model, output_format, azure_select, **kwargs):
    """Embed text.

    Not currently supported for open models.
    """
    if model:
        selectmodel = get_model_by_name(model)
        model_source = selectmodel["provider"]

        if model_source != "OpenAI":
            raise NotImplementedError("Model not yet supported for embeddings.")
    else:
        model = "text-embedding-ada-002"

    if not text:
        raise ValueError("Text must be passed")

    client = OpenAIClient(model=model, use_azure=azure_select)
    resp = client.embeddings(text)
    print(resp)


@main.command()
@output_option_txt
@output_format_options
@model_option
@azure_select_option
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.argument("text", nargs=-1)
def text_similarity(text, context, output, model, output_format, azure_select, **kwargs):
    """Embed text.

    Not currently supported for open models.
    """
    if model:
        selectmodel = get_model_by_name(model)
        model_source = selectmodel["provider"]

        if model_source != "OpenAI":
            raise NotImplementedError("Model not yet supported for embeddings.")
    else:
        model = "text-embedding-ada-002"

    if not text:
        raise ValueError("Text must be passed")
    text = list(text)
    if "@" not in text:
        raise ValueError("Text must contain @")
    ix = text.index("@")
    text1 = " ".join(text[:ix])
    text2 = " ".join(text[ix + 1 :])
    print(text1)
    print(text2)

    client = OpenAIClient(model=model, use_azure=azure_select)
    sim = client.similarity(text1, text2, model=model)
    print(sim)


@main.command()
@output_option_txt
@output_format_options
@model_option
@azure_select_option
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.argument("text", nargs=-1)
def text_distance(text, context, output, model, output_format, azure_select, **kwargs):
    """Embed text and calculate euclidian distance between embeddings.

    Not currently supported for open models.
    """
    if model:
        selectmodel = get_model_by_name(model)
        model_source = selectmodel["provider"]

        if model_source != "OpenAI":
            raise NotImplementedError("Model not yet supported for embeddings.")
    else:
        model = "text-embedding-ada-002"

    if not text:
        raise ValueError("Text must be passed")
    text = list(text)
    if "@" not in text:
        raise ValueError("Text must contain @")
    ix = text.index("@")
    text1 = " ".join(text[:ix])
    text2 = " ".join(text[ix + 1 :])
    print(text1)
    print(text2)

    client = OpenAIClient(model=model, use_azure=azure_select)
    sim = client.euclidian_distance(text1, text2, model=model)
    print(sim)


@main.command()
@output_option_txt
@output_format_options
@model_option
@click.option("--ontology", "-r", help="Ontology to use")
@click.option(
    "--definitions/--no-definitions",
    default=True,
    show_default=True,
    help="Include text definitions in the text to embed",
)
@click.option(
    "--parents/--no-parents",
    default=True,
    show_default=True,
    help="Include is-a parent terms in the text to embed",
)
@click.option(
    "--ancestors/--no-ancestors",
    default=True,
    show_default=True,
    help="Include all ancestors in the text to embed",
)
@click.option(
    "--logical-definitions/--no-logical-definitions",
    default=True,
    show_default=True,
    help="Include logical definitions in the text to embed",
)
@click.option(
    "--autolabel/--no-autolabel",
    default=True,
    show_default=True,
    help="Add subj/obj labels to report objects",
)
@click.option(
    "--synonyms/--no-synonyms",
    default=True,
    show_default=True,
    help="Include synonyms in the text to embed",
)
@click.argument("terms", nargs=-1)
def entity_similarity(terms, ontology, output, model, output_format, **kwargs):
    """Embed text.

    Not currently supported for open models.
    """
    if model:
        selectmodel = get_model_by_name(model)
        model_source = selectmodel["provider"]

        if model_source != "OpenAI":
            raise NotImplementedError("Model not yet supported for embeddings.")

    if not terms:
        raise ValueError("terms must be passed")
    terms = list(terms)
    if "@" not in terms:
        logging.info("No @ found, assuming all by all")
        terms1 = list(terms)
        terms2 = list(terms)
    else:
        ix = terms.index("@")
        terms1 = terms[:ix]
        terms2 = terms[ix + 1 :]
    adapter = get_adapter(ontology)
    entities1 = list(query_terms_iterator(terms1, adapter))
    entities2 = list(query_terms_iterator(terms2, adapter))

    engine = SimilarityEngine(model=model, adapter=adapter, **kwargs)
    writer = StreamingCsvWriter(output, heterogeneous_keys=False)

    for e1 in entities1:
        sims = engine.search(e1, entities2)
        for sim in sims:
            writer.emit(sim)


@main.command()
@inputfile_option
@output_option_txt
@model_option
@click.option("--task-file")
@click.option("--task-type")
@click.option("--tsv-output")
@click.option("--all-methods/--no-all-methods", default=False)
@click.option("--explain/--no-explain", default=False)
@click.option("--evaluate/--no-evaluate", default=False)
@click.argument("terms", nargs=-1)
def reason(
    terms,
    inputfile,
    model,
    task_file,
    explain,
    task_type,
    output,
    tsv_output,
    all_methods,
    evaluate,
    **kwargs,
):
    """Reason."""
    reasoner = ReasonerEngine(model=model)
    if task_file:
        tc = extractor.TaskCollection.load(task_file)
    else:
        adapter = get_adapter(inputfile)
        if not isinstance(adapter, OboGraphInterface):
            raise ValueError("Only OBO graphs supported")
        ex = extractor.OntologyExtractor(adapter=adapter)
        # ex.use_identifiers = True
        task = ex.create_task(task_type=task_type, parameters=list(terms))
        tc = extractor.TaskCollection(tasks=[task])
    if all_methods:
        tasks = []
        print(f"Cloning {len(tc.tasks)} tasks")
        for core_task in tc.tasks:
            for m in extractor.GPTReasonMethodType:
                print(f"Cloning {m}")
                task = deepcopy(core_task)
                task.method = m
                task.init_method()
                tasks.append(task)
        tc.tasks = tasks
        print(f"New {len(tc.tasks)} tasks")
    else:
        for task in tc.tasks:
            task.include_explanations = explain
    resultset = reasoner.reason_multiple(tc, evaluate=evaluate)
    dump_minimal_yaml(resultset.dict(), file=output)
    if tsv_output:
        write_obj_as_csv(resultset.results, tsv_output)


@main.command()
@output_option_txt
@model_option
@click.argument("phenopacket_files", nargs=-1)
def diagnose(
    phenopacket_files,
    model,
    output,
    **kwargs,
):
    """Diagnose a clinical case represented as one or more Phenopackets."""
    if not phenopacket_files:
        raise ValueError("No phenopacket files specified. Please provide one or more files.")

    if not model:
        model = DEFAULT_MODEL

    selectmodel = get_model_by_name(model)
    model_name = selectmodel["canonical_name"]
    model_source = selectmodel["provider"]

    phenopackets = [json.load(open(f)) for f in phenopacket_files]
    engine = PhenoEngine(model=model_name, model_source=model_source.lower())
    results = engine.evaluate(phenopackets)
    print(dump_minimal_yaml(results))
    write_obj_as_csv(results, output)


@main.command()
@inputfile_option
@output_option_txt
@model_option
@click.option("--tsv-output")
@click.option("--template-path")
def answer(
    inputfile,
    model,
    template_path,
    output,
    tsv_output,
    **kwargs,
):
    """Answer a set of questions defined in YAML."""
    qc = QuestionCollection(**yaml.safe_load(open(inputfile)))
    engine = GenericEngine(model=model)
    qs = []
    for q in engine.run(qc, template_path=template_path):
        print(dump_minimal_yaml(q))
        qs.append(q)
    qc.questions = qs
    output.write(dump_minimal_yaml(qs))
    if tsv_output:
        write_obj_as_csv(qs, tsv_output)


@main.command()
@inputfile_option
@output_option_txt
@model_option
@click.option("--task-file")
@click.option("--task-type")
@click.option("--tsv-output")
@click.option("--yaml-output")
@click.option("--all-methods/--no-all-methods", default=False)
@click.option("--explain/--no-explain", default=False)
@click.option("--evaluate/--no-evaluate", default=False)
def categorize_mappings(
    inputfile,
    model,
    task_file,
    explain,
    task_type,
    output,
    tsv_output,
    yaml_output,
    all_methods,
    evaluate,
    **kwargs,
):
    """Categorize a collection of SSSOM mappings."""
    mapper = MappingEngine(model=model)
    if tsv_output:
        tc = mapper.from_sssom(inputfile)
        for cm in mapper.run_tasks(tc, evaluate=evaluate):
            print(dump_minimal_yaml(cm.dict()))
            # dump_minimal_yaml(cm.dict(), file=output)
        # write_obj_as_csv(resultset.results, tsv_output)
    else:
        import sssom.writers as sssom_writers

        msdf = parse_sssom_table(inputfile)
        msd = to_mapping_set_document(msdf)
        mappings = []
        cms = []
        done = []
        for mapping in msd.mapping_set.mappings:
            pair = mapping.subject_id, mapping.object_id
            if pair in done:
                continue
            mapping, cm = mapper.categorize_sssom_mapping(mapping)
            mappings.append(mapping)
            cms.append(cm.dict())
            done.append(pair)
        msd.mapping_set.mappings = mappings
        msdf = to_mapping_set_dataframe(msd)
        sssom_writers.write_table(msdf, output)
        if yaml_output:
            with open(yaml_output, "w") as file:
                dump_minimal_yaml(cms, file=file)


@main.command()
@recurse_option
@model_option
@output_option_txt
@click.option(
    "--num-tests",
    type=click.INT,
    default=5,
    show_default=True,
    help="number of iterations to cycle through.",
)
@click.option(
    "--chunking/--no-chunking",
    default=False,
    show_default=True,
    help="If set, chunk input text, then prepare a separate prompt for each chunk."
    " Otherwise the full input text is passed.",
)
@click.argument("evaluator")
def eval(evaluator, num_tests, output, chunking, model, **kwargs):
    """Evaluate an extractor."""
    logging.info(f"Creating for {evaluator}")

    if model:
        selectmodel = get_model_by_name(model)
        modelname = selectmodel["canonical_name"]
    else:
        modelname = DEFAULT_MODEL

    evaluator = create_evaluator(
        name=evaluator, num_tests=num_tests, chunking=chunking, model=modelname
    )
    eos = evaluator.eval()
    output.write(dump_minimal_yaml(eos, minimize=False))


@main.command()
@template_option
@model_option
@click.option("-E", "--examples", type=click.File("r"), help="File of example objects.")
@recurse_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.argument("object")
def fill(model, template, object: str, examples, output, output_format, show_prompt, **kwargs):
    """Fill in missing values."""
    ke: KnowledgeEngine

    # Choose model based on input, or use the default
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)

    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(
        template_details=template_details,
        model=selectmodel["canonical_name"],
        model_source=selectmodel["provider"].lower(),
        **kwargs,
    )

    object = yaml.safe_load(object)
    logging.info(f"Object to fill =  {object}")
    logging.info(f"Loading {examples}")
    examples = yaml.safe_load(examples)
    logging.debug(f"Input object: {object}")
    results = ke.generalize(object=object, examples=examples, show_prompt=show_prompt)

    output.write(yaml.dump(results.dict()))


@main.command()
def openai_models(**kwargs):
    """List OpenAI models for prompt completion."""
    ai = OpenAIClient()
    for model in client.models.list():
        print(model)


@main.command()
@model_option
@output_option_txt
@output_format_options
@show_prompt_option
@azure_select_option
@click.argument("input")
def complete(model, input, output, output_format, show_prompt, azure_select, **kwargs):
    """Prompt completion."""
    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)
    model_source = selectmodel["provider"]
    model_name = selectmodel["canonical_name"]

    text = open(input).read()

    # TODO: add support for other models
    if model_source == "OpenAI":
        c = OpenAIClient(model=model, use_azure=azure_select)
        results = c.complete(prompt=text, show_prompt=show_prompt)

    output.write(results)


@main.command()
@template_option
@click.option("--input", "-i", type=click.File("r"), default=sys.stdin, help="Input file")
def parse(template, input):
    """Parse OpenAI results."""
    if template:
        template_details = get_template_details(template=template)
    else:
        raise ValueError("No template specified. Use -t/--template option.")

    ke = SPIRESEngine(template_details=template_details)
    text = input.read()
    logging.debug(f"Input text: {text}")
    # ke.annotator = BioPortalImplementation()
    results = ke.parse_completion_payload(text)
    print(yaml.dump(results))


@main.command()
@click.option("-o", "--output", type=click.File(mode="w"), default=sys.stdout, help="Output file.")
@output_format_options
@model_option
@click.option("-m", "match", help="Match string to use for filtering.")
@click.option("-D", "database", help="Path to sqlite database.")
@azure_select_option
def dump_completions(model, match, database, output, output_format, azure_select):
    """Dump cached completions."""
    if model:
        raise NotImplementedError("Caching not currently enabled for this model.")
    else:
        client = OpenAIClient(model=model, use_azure=azure_select)

    if database:
        client.cache_db_path = database
    if output_format == "jsonl":
        writer = jsonlines.Writer(output)
        for _engine, prompt, completion in client.cached_completions(match):
            writer.write(dict(engine=model, prompt=prompt, completion=completion))
    elif output_format == "yaml":
        for _engine, prompt, completion in client.cached_completions(match):
            output.write(
                dump_minimal_yaml(dict(engine=model, prompt=prompt, completion=completion))
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
    """Convert training examples from YAML."""
    logging.info(f"Creating examples for {input}")
    example_doc = yaml.safe_load(input)
    writer = jsonlines.Writer(output)
    for example in example_doc["examples"]:
        prompt = example["prompt"]
        completion = yaml.dump(example["completion"], sort_keys=False)
        writer.write(dict(prompt=prompt, completion=completion))


@main.command()
@model_option
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
def halo(model, input, context, terms, output, **kwargs):
    """Run HALO over inputs."""
    if model:
        raise NotImplementedError("HALO not currently supported for this model.")

    engine = HALOEngine()
    engine.seed_from_file(input)
    if context is None:
        context = engine.ontology.elements[0].context
    engine.fixed_slot_values = {"context": context}
    engine.hallucinate(terms, **kwargs)
    output.write(dump_minimal_yaml(engine.ontology))


@main.command()
@model_option
@output_option_wb
@output_format_options
@show_prompt_option
@click.option(
    "-d",
    "--description",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.option(
    "--sections", multiple=True, help="sections to include e.g. medications, vital signs, etc."
)
@azure_select_option
def clinical_notes(
    description,
    sections,
    output,
    model,
    show_prompt,
    output_format,
    azure_select,
    **kwargs,
):
    """Create mock clinical notes.

    Example:

        ontogpt clinical-notes -d "middle-aged female patient with diabetes"
        ontogpt clinical-notes --description "middle-aged female patient with diabetes"\
         --sections medications --sections "vital signs"

    """
    prompt = "create mock clinical notes for a patient like this: " + description
    if sections:
        prompt += " including sections: " + ", ".join(sections)

    if not model:
        model = DEFAULT_MODEL
    selectmodel = get_model_by_name(model)
    model_source = selectmodel["provider"]
    model_name = selectmodel["canonical_name"]

    # TODO: add support for other models
    if model_source == "OpenAI":
        c = OpenAIClient(model=model, use_azure=azure_select)
        results = c.complete(prompt=prompt, show_prompt=show_prompt)

    output.write(results)


@main.command()
def list_templates():
    """List the available extraction templates."""
    http_prefixes = ("http", "https")

    # Get the list of yaml files in the templates directory
    # and populate a dict
    all_templates = {}
    template_dir = Path(__file__).parent / "templates"
    template_paths = [f for f in template_dir.glob("*.yaml")]
    for template_path in template_paths:
        with open(template_path, "r") as template_file:
            data = yaml.safe_load(template_file)
            if data["id"].startswith(http_prefixes):
                identifier = data["id"].split("/")[-1]
            else:
                identifier = data["id"]
            all_templates[identifier] = (data["name"], data["description"])

    # Sort that dict by id
    all_templates = dict(sorted(all_templates.items()))

    # Write it out
    print("ID\tName\tDescription")
    for template_id, (name, description) in all_templates.items():
        print(f"{template_id}\t{name}\t{description}")


@main.command()
def list_models():
    """List all available models.

    The following values are provided:

    Model Name: OntoGPT's name for the model. Use this with the -m/--model option.

    Provider: The service provider for the model.

    Canonical Name: The name of the model as provided by the service provider.

    Alternative Names: Other names for the model.

    Status: Whether the model is currently implemented or deprecated.

    Disk Space: The space required for the model to be stored on your local disk.
    "N/A" means the model is not stored locally.

    System Memory: The memory required for the model to run on your system.
    "N/A" means the model is not stored locally.
    """
    print(
        "Model Name\tProvider\tCanonical Name\tAlternative Names\tStatus\tDisk Space\tSystem Memory"
    )
    for model in MODELS:
        primary_name = model["name"]
        provider = model["provider"]
        canonical = model["canonical_name"]
        alternative_names = (
            " ".join(model["alternative_names"]) if model["alternative_names"] else ""
        )
        if "not_implemented" in model or "deprecated" in model:
            status = "Not Implemented"
        else:
            status = "Implemented"
        disk = model["requirements"]["diskspace"]
        memory = model["requirements"]["memory"]

        print(
            f"{primary_name}\t{provider}\t{canonical}\t{alternative_names}\t"
            f"{status}\t{disk}\t{memory}"
        )


if __name__ == "__main__":
    main()
