"""Command line interface for ontogpt."""
import codecs
import json
import logging
import pickle
import sys
from copy import copy, deepcopy
from dataclasses import dataclass
from io import BytesIO, TextIOWrapper
from pathlib import Path
from typing import List, Optional

import click
import jsonlines
import openai
import yaml
from oaklib import get_adapter
from oaklib.cli import query_terms_iterator
from oaklib.interfaces import OboGraphInterface
from oaklib.io.streaming_csv_writer import StreamingCsvWriter
from sssom.parsers import parse_sssom_table, to_mapping_set_document
from sssom.util import to_mapping_set_dataframe

import ontogpt.ontex.extractor as extractor
from ontogpt import MODELS, DEFAULT_MODEL, __version__
from ontogpt.clients import OpenAIClient
from ontogpt.clients.pubmed_client import PubmedClient
from ontogpt.clients.soup_client import SoupClient
from ontogpt.clients.wikipedia_client import WikipediaClient
from ontogpt.engines import create_engine
from ontogpt.engines.embedding_similarity_engine import SimilarityEngine
from ontogpt.engines.enrichment import EnrichmentEngine
from ontogpt.engines.ggml_engine import GGMLEngine
from ontogpt.engines.generic_engine import GenericEngine, QuestionCollection
from ontogpt.engines.halo_engine import HALOEngine
from ontogpt.engines.hfhub_engine import HFHubEngine
from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.engines.mapping_engine import MappingEngine
from ontogpt.engines.pheno_engine import PhenoEngine
from ontogpt.engines.reasoner_engine import ReasonerEngine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.engines.synonym_engine import SynonymEngine
from ontogpt.evaluation.enrichment.eval_enrichment import EvalEnrichment
from ontogpt.evaluation.resolver import create_evaluator
from ontogpt.io.csv_wrapper import write_obj_as_csv
from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.io.markdown_exporter import MarkdownExporter
from ontogpt.utils.gene_set_utils import (
    GeneSet,
    _is_human,
    fill_missing_gene_set_values,
    parse_gene_set,
)
from ontogpt.utils.model_utils import get_model

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
    output_format: str = None,
    knowledge_engine: KnowledgeEngine = None,
):
    """Write results of extraction to a given output stream."""
    # Check if this result contains anything writable first
    if results.extracted_object:
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
        elif output_format == "turtle":
            output = _as_text_writer(output)
            exporter = RDFExporter()
            exporter.export(results, output, knowledge_engine.schemaview)
        elif output_format == "owl":
            output = _as_text_writer(output)
            exporter = OWLExporter()
            exporter.export(results, output, knowledge_engine.schemaview)
        else:
            output = _as_text_writer(output)
            output.write(dump_minimal_yaml(results))


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
    help="Model name to use, e.g. openai-text-davinci-003."
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
@click.option(
    "--auto-prefix",
    default="AUTO",
    help="Prefix to use for auto-generated classes. Default is AUTO.",
)
@click.option(
    "--set-slot-value",
    "-S",
    multiple=True,
    help="Set slot value, e.g. --set-slot-value has_participant=protein",
)
@click.argument("input", required=False)
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
    **kwargs,
):
    """Extract knowledge from text guided by schema, using SPIRES engine.

    Example:

        ontogpt extract -t gocam.GoCamAnnotations -i gocam-27929086.txt

    The input argument must be either a file path or a string.
    Use the -i/--input-file option followed by the path to the input file if using the former.
    Otherwise, the input is assumed to be a string to be read as input.

    You can also use fragments of existing schemas, use the --target-class option (-T) to
    specify an alternative Container/root class.

    Example:

        ontogpt -extract -t gocam.GoCamAnnotations -T GeneOrganismRelationship "the mouse Shh gene"

    """
    logging.info(f"Creating for {template}")

    # Choose model based on input, or use the default
    model_source = "OpenAI"
    found = False
    for knownmodel in MODELS:
        if model in knownmodel["alternative_names"] or model == knownmodel["name"]:
            selectmodel = knownmodel
            model_source = selectmodel["provider"]
            found = True
            break
    if model and not found:
        logging.warning(
            f"""Model name not recognized or not supported yet. Using default, {DEFAULT_MODEL}.
            See all models with `ontogpt list-models`"""
        )

    if not inputfile or inputfile == "-":
        text = sys.stdin.read()
    if inputfile and Path(inputfile).exists():
        logging.info(f"Input file: {inputfile}")
        if use_textract:
            import textract

            text = textract.process(inputfile).decode("utf-8")
        else:
            text = open(inputfile, "r").read()
        logging.info(f"Input text: {text}")
    elif inputfile and not Path(inputfile).exists():
        raise FileNotFoundError(f"Cannot find input file {inputfile}")

    if model_source == "OpenAI":
        ke = SPIRESEngine(template, **kwargs)
        if settings.cache_db:
            ke.client.cache_db_path = settings.cache_db
        if settings.skip_annotators:
            ke.client.skip_annotators = settings.skip_annotators

    elif model_source == "GPT4All":
        model_path = get_model(selectmodel["url"])
        ke = GGMLEngine(template=template, local_model=model_path, **kwargs)

    elif model_source == "HuggingFace Hub":
        hf_repo_name = selectmodel["hf_repo_name"]
        ke = HFHubEngine(template=template, local_model=hf_repo_name, **kwargs)

    if dictionary:
        ke.load_dictionary(dictionary)
    if target_class:
        target_class_def = ke.schemaview.get_class(target_class)
    else:
        target_class_def = None
    results = ke.extract_from_text(text, target_class_def)
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
@click.argument("pmid")
def pubmed_extract(pmid, template, output, output_format, **kwargs):
    """Extract knowledge from a single PubMed ID."""
    logging.info(f"Creating for {template}")
    pmc = PubmedClient()
    text = pmc.text(pmid)
    ke = SPIRESEngine(template, **kwargs)
    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text)
    write_extraction(results, output, output_format)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@click.argument("search")
def pubmed_annotate(search, template, output, output_format, **kwargs):
    """Retrieve a collection of PubMed IDs for a search term; annotate them using a template."""
    logging.info(f"Creating for {template}")
    pubmed_annotate_limit = 20 # TODO: make this a CLI argument
    pmc = PubmedClient()
    pmids = pmc.get_pmids(search)
    textlist = pmc.text(pmids[:pubmed_annotate_limit + 1])
    for text in textlist:
        ke = SPIRESEngine(template, **kwargs)
        logging.debug(f"Input text: {text}")
        results = ke.extract_from_text(text)
        write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@click.option("--auto-prefix", default="AUTO", help="Prefix to use for auto-generated classes.")
@click.argument("article")
def wikipedia_extract(article, template, output, output_format, **kwargs):
    """Extract knowledge from a Wikipedia page."""
    logging.info(f"Creating for {template} => {article}")
    client = WikipediaClient()
    text = client.text(article)
    ke = SPIRESEngine(template, **kwargs)
    logging.debug(f"Input text: {text}")
    results = ke.extract_from_text(text)
    write_extraction(results, output, output_format, ke)


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@click.option(
    "--keyword",
    "-k",
    multiple=True,
    help="Keyword to search for (e.g. --keyword therapy). Also obtained from schema",
)
@click.argument("topic")
def wikipedia_search(topic, keyword, template, output, output_format, **kwargs):
    """Extract knowledge from a Wikipedia page."""
    logging.info(f"Creating for {template} => {topic}")
    client = WikipediaClient()
    keywords = list(keyword) if keyword else []
    logging.info(f"KW={keywords}")
    ke = SPIRESEngine(template, **kwargs)
    keywords.extend(ke.schemaview.schema.keywords)
    search_term = f"{topic + ' ' + ' '.join(keywords)}"
    print(f"Searching for {search_term}")
    search_results = client.search_wikipedia_articles(search_term)
    for _index, result in enumerate(search_results, start=1):
        title = result["title"]
        text = client.text(title)
        logging.debug(f"Input text: {text}")
        if len(text) > 4000:
            # TODO
            text = text[:4000]
        results = ke.extract_from_text(text)
        write_extraction(results, output, output_format)
        break


@main.command()
@template_option
@model_option
@recurse_option
@output_option_txt
@output_format_options
@click.argument("pmcid")
def pmc_extract(pmcid, template, output, output_format, **kwargs):
    """Extract knowledge from PubMed Central texts (TODO)."""
    logging.info(f"Creating for {template}")
    pmc = PubmedClient()
    ec = pmc.entrez_client
    paset = ec.efetch(db="pmc", id=pmcid)
    from lxml import etree  # noqa

    for pa in paset:
        pa._xml_root
        print(etree.tostring(pa._xml_root, pretty_print=True))


@main.command()
@template_option
@model_option
@recurse_option
@output_option_wb
@output_format_options
@click.option(
    "--keyword",
    "-k",
    multiple=True,
    help="Keyword to search for (e.g. --keyword therapy). Also obtained from schema",
)
@click.argument("term_tokens", nargs=-1)
def search_and_extract(term_tokens, keyword, template, output, output_format, **kwargs):
    """Search for relevant literature and extract knowledge from it."""
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
@model_option
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
@click.argument("url")
def recipe_extract(url, recipes_urls_file, dictionary, output, output_format, **kwargs):
    """Extract from recipe on the web."""
    from recipe_scrapers import scrape_me

    if recipes_urls_file:
        with open(recipes_urls_file, "r") as f:
            urls = [line.strip() for line in f.readlines() if url in line]
            if len(urls) != 1:
                raise ValueError(f"Found {len(urls)} URLs in {recipes_urls_file}")
            url = urls[0]
    scraper = scrape_me(url)
    template = "recipe"
    logging.info(f"Creating for {template}")
    ke = SPIRESEngine(template, **kwargs)
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if settings.skip_annotators:
        ke.skip_annotators = settings.skip_annotators
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
    results = ke.extract_from_text(text)
    logging.debug(f"Results: {results}")
    results.extracted_object.url = url
    write_extraction(results, output, output_format, ke)


@main.command()
@output_option_wb
@output_format_options
@click.argument("input")
def convert(input, output, output_format, **kwargs):
    """Convert output format."""
    template = "recipe"
    logging.info(f"Creating for {template}")
    ke = SPIRESEngine(template, **kwargs)
    cls = ke.template_pyclass
    with open(input, "r") as f:
        data = yaml.safe_load(f)
    obj = cls(**data["extracted_object"])
    results = ExtractionResult(extracted_object=obj)
    write_extraction(results, output, output_format, ke)


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
@output_option_txt
@output_format_options
@click.option(
    "--annotation-path",
    "-A",
    required=True,
)
@click.argument("term")
def create_gene_set(term, output, output_format, annotation_path, **kwargs):
    """Create a gene set."""
    logging.info(f"Creating for {term}")
    evaluator = EvalEnrichment()
    evaluator.load_annotations(annotation_path)
    gene_set = evaluator.create_gene_set_from_term(term)
    print(yaml.dump(gene_set.dict(), sort_keys=False))


@main.command()
@output_option_txt
@output_format_options
@click.option("--fill/--no-fill", default=False)
@click.option(
    "--input-file",
    "-U",
    help="File with gene IDs to enrich (if not passed as arguments)",
)
def convert_geneset(input_file, output, output_format, fill, **kwargs):
    """Convert gene set to YAML."""
    gene_set = parse_gene_set(input_file)
    if fill:
        fill_missing_gene_set_values(gene_set)
    output.write(dump_minimal_yaml(gene_set.dict()))


@main.command()
@output_option_txt
@output_format_options
@model_option
@click.option(
    "--resolver", "-r", help="OAK selector for the gene ID resolver. E.g. sqlite:obo:hgnc"
)
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.option(
    "--strict/--no-strict",
    default=True,
    show_default=True,
    help="If set, there must be a unique mappings from labels to IDs",
)
@click.option(
    "--show-prompt/--no-show-prompt",
    default=True,
    show_default=True,
    help="If set, show prompt passed to model",
)
@click.option(
    "--input-file",
    "-U",
    help="File with gene IDs to enrich (if not passed as arguments)",
)
@click.option(
    "--randomize-gene-descriptions-using-file",
    help="FOR EVALUATION ONLY. Swap out gene descriptions with genes from this gene set filefile",
)
@click.option(
    "--ontological-synopsis/--no-ontological-synopsis",
    default=True,
    show_default=True,
    help="If set, use automated rather than manual gene descriptions",
)
@click.option(
    "--combined-synopsis/--no-combined-synopsis",
    default=False,
    show_default=True,
    help="If set, both gene descriptions",
)
@click.option(
    "--end-marker",
    help="For testing minor variants of prompts",
)
@click.option(
    "--annotations/--no-annotations",
    default=True,
    show_default=True,
    help="If set, include annotations in the prompt",
)
@prompt_template_option
@interactive_option
@click.argument("genes", nargs=-1)
def enrichment(
    genes,
    context,
    input_file,
    resolver,
    output,
    model,
    show_prompt,
    interactive,
    end_marker,
    output_format,
    randomize_gene_descriptions_using_file,
    **kwargs,
):
    """Gene class summary enriching (SPINDOCTOR).

    Algorithm:

    1. Map gene symbols to IDs using the resolver (unless IDs specified)
    2. Fetch gene descriptions using Alliance API
    3. Create a prompt using descriptions

    Limitations:

    It is very easy to exceed the max token length with GPT-3 models.

    Usage:

        ontogpt enrichment -r sqlite:obo:hgnc -U tests/input/genesets/dopamine.yaml

    Usage:

        ontogpt enrichment -r sqlite:obo:hgnc -U tests/input/genesets/dopamine.yaml

    """
    if not genes and not input_file:
        raise ValueError("Either genes or input file must be passed")
    if genes:
        gene_set = GeneSet(name="TEMP", gene_symbols=genes)
    if input_file:
        if genes:
            raise ValueError("Either genes or input file must be passed")
        gene_set = parse_gene_set(input_file)
    if not gene_set:
        raise ValueError("No genes passed")
    ke = create_engine(None, EnrichmentEngine, model=model)
    if end_marker:
        ke.end_marker = end_marker
    if interactive:
        ke.client.interactive = True
    if settings.cache_db:
        ke.client.cache_db_path = settings.cache_db
    if not isinstance(ke, EnrichmentEngine):
        raise ValueError(f"Expected EnrichmentEngine, got {type(ke)}")
    if resolver:
        ke.add_resolver(resolver)
    if randomize_gene_descriptions_using_file:
        print("WARNING!! Randomly spiking gene descriptions")
        spike_gene_set = parse_gene_set(randomize_gene_descriptions_using_file)
        aliases = {}
        if not spike_gene_set.gene_symbols:
            raise ValueError("No gene symbols for spike set")
        syms = copy(gene_set.gene_symbols)
        if len(spike_gene_set.gene_symbols) < len(gene_set.gene_symbols):
            raise ValueError("Not enough genes in spike set")
        for sym in spike_gene_set.gene_symbols:
            if not syms:
                break
            aliases[sym] = syms.pop()
        results = ke.summarize(
            spike_gene_set, normalize=resolver is not None, gene_aliases=aliases, **kwargs
        )
    else:
        results = ke.summarize(gene_set, normalize=resolver is not None, **kwargs)
    if results.truncation_factor is not None and results.truncation_factor < 1.0:
        logging.warning(f"Text was truncated; factor = {results.truncation_factor}")
    output = _as_text_writer(output)
    if show_prompt:
        print(results.prompt)
    output.write(dump_minimal_yaml(results))


@main.command()
@output_option_txt
@output_format_options
@model_option
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.argument("text", nargs=-1)
def embed(text, context, output, model, output_format, **kwargs):
    """Embed text."""
    if not text:
        raise ValueError("Text must be passed")
    if model is None:
        model = "text-embedding-ada-002"
    client = OpenAIClient(model=model)
    resp = client.embeddings(text)
    print(resp)


@main.command()
@output_option_txt
@output_format_options
@model_option
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.argument("text", nargs=-1)
def text_similarity(text, context, output, model, output_format, **kwargs):
    """Embed text."""
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
    if model is None:
        model = "text-embedding-ada-002"
    client = OpenAIClient(model=model)
    sim = client.similarity(text1, text2, model=model)
    print(sim)


@main.command()
@output_option_txt
@output_format_options
@model_option
@click.option(
    "-C",
    "--context",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.argument("text", nargs=-1)
def text_distance(text, context, output, model, output_format, **kwargs):
    """Embed text, calculate euclidian distance between embeddings."""
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
    if model is None:
        model = "text-embedding-ada-002"
    client = OpenAIClient(model=model)
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

    Uses the OpenAI ada embedding model by default, currently: $0.0004 / 1K tokens
    """
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
    """Diagnose."""
    phenopackets = [json.load(open(f)) for f in phenopacket_files]
    engine = PhenoEngine(model=model)
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
@output_option_txt
@click.option(
    "--strict/--no-strict",
    default=True,
    show_default=True,
    help="If set, there must be a unique mappings from labels to IDs",
)
@click.option(
    "--input-file",
    "-U",
    help="File with gene IDs to enrich (if not passed as arguments)",
)
@click.option(
    "--ontological-synopsis/--no-ontological-synopsis",
    default=True,
    show_default=True,
    help="If set, use automated rather than manual gene descriptions",
)
@click.option(
    "--combined-synopsis/--no-combined-synopsis",
    default=False,
    show_default=True,
    help="If set, both gene descriptions",
)
@click.option(
    "--annotations/--no-annotations",
    default=True,
    show_default=True,
    help="If set, include annotations in the prompt",
)
@click.option(
    "--number-to-drop",
    "-n",
    type=click.types.INT,
    default=1,
    help="Max number of genes to drop",
)
# @click.option(
#    "--randomize-gene-descriptions/--no-randomize-gene-descriptions",
#    help="DO NOT USE EXCEPT FOR EVALUATION PUPOSES."
# )
@click.option(
    "--annotations-path",
    "-A",
    help="Path to annotations",
)
@model_option
@click.argument("genes", nargs=-1)
def eval_enrichment(genes, input_file, number_to_drop, annotations_path, model, output, **kwargs):
    """Run enrichment using multiple methods."""
    if not genes and not input_file:
        raise ValueError("Either genes or input file must be passed")
    if genes:
        gene_set = GeneSet(name="TEMP", gene_symbols=genes)
    if input_file:
        if genes:
            raise ValueError("Either genes or input file must be passed")
        gene_set = parse_gene_set(input_file)
    if not gene_set:
        raise ValueError("No genes passed")
    fill_missing_gene_set_values(gene_set)
    if not annotations_path:
        if not _is_human(gene_set):
            raise ValueError("No annotations path passed")
        annotations_path = "tests/input/genes2go.tsv.gz"
    eval_engine = EvalEnrichment(model=model)
    eval_engine.load_annotations(annotations_path)
    comps = eval_engine.evaluate_methods_on_gene_set(gene_set, n=number_to_drop, **kwargs)
    output.write(dump_minimal_yaml(comps))


@main.command()
@model_option
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
@model_option
@click.option("-E", "--examples", type=click.File("r"), help="File of example objects.")
@recurse_option
@output_option_wb
@output_format_options
@click.argument("object")
def fill(template, object: str, examples, output, output_format, **kwargs):
    """Fill in missing values."""
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
def openai_models(**kwargs):
    """List OpenAI models for prompt completion."""
    ai = OpenAIClient()
    for model in openai.Model.list():
        print(model)


@main.command()
@model_option
@output_option_txt
@output_format_options
@click.argument("input")
def complete(input, output, output_format, **kwargs):
    """Prompt completion."""
    ai = OpenAIClient()
    text = open(input).read()
    payload = ai.complete(text)
    print(payload)


@main.command()
@template_option
@click.option("--input", "-i", type=click.File("r"), default=sys.stdin, help="Input file")
def parse(template, input):
    """Parse OpenAI results."""
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
@model_option
@click.option("-m", "match", help="Match string to use for filtering.")
@click.option("-D", "database", help="Path to sqlite database.")
def dump_completions(model, match, database, output, output_format):
    """Dump cached completions."""
    client = OpenAIClient()
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
    """Run HALO over inputs."""
    engine = HALOEngine()
    engine.seed_from_file(input)
    if context is None:
        context = engine.ontology.elements[0].context
    engine.fixed_slot_values = {"context": context}
    engine.hallucinate(terms, **kwargs)
    output.write(dump_minimal_yaml(engine.ontology))


@main.command()
@output_option_wb
@output_format_options
@click.option(
    "-d",
    "--description",
    help="domain e.g. anatomy, industry, health-related (NOT IMPLEMENTED - currently gene only)",
)
@click.option(
    "--sections", multiple=True, help="sections to include e.g. medications, vital signs, etc."
)
def clinical_notes(
    description,
    sections,
    output,
    output_format,
    **kwargs,
):
    """Create mock clinical notes.

    Example:

        ontogpt clinical-notes -d "middle-aged female patient with diabetes"
        ontogpt clinical-notes --description "middle-aged female patient with diabetes"\
         --sections medications --sections "vital signs"

    """
    c = OpenAIClient()
    prompt = "create mock clinical notes for a patient like this: " + description
    if sections:
        prompt += " including sections: " + ", ".join(sections)
    results = c.complete(prompt)
    print(results)
    output.write(results)


@main.command()
def list_templates():
    """List the templates."""
    print("TODO")


@main.command()
def list_models():
    """List all available models."""
    print("Model Name\tProvider\tAlternative Names\tStatus")
    for model in MODELS:
        primary_name = model["name"]
        provider = model["provider"]
        alternative_names = (
            " ".join(model["alternative_names"]) if model["alternative_names"] else ""
        )
        if "not_implemented" in model:
            status = "Not Implemented"
        else:
            status = "Implemented"

        print(f"{primary_name}\t{provider}\t{alternative_names}\t{status}")




if __name__ == "__main__":
    main()
