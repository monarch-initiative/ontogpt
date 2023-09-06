"""Utilities for handling gene sets."""
import csv
import glob
import json
import logging
from copy import deepcopy
from pathlib import Path
from random import sample
from typing import Dict, List, Optional, Tuple, Union

import requests_cache
import yaml
from oaklib import BasicOntologyInterface, get_adapter
from pydantic import BaseModel

ENTITY_ID = str
SYMBOL = str
DESCRIPTION = str
GENE_TUPLE = Tuple[ENTITY_ID, SYMBOL, DESCRIPTION]

GENE_REQUESTS_CACHE = ".gene_requests_cache"


logger = logging.getLogger(__name__)

session = requests_cache.CachedSession(GENE_REQUESTS_CACHE)


class Gene(BaseModel):
    id: str
    symbol: str = None
    ontological_synopsis: str = None
    narrative_synopsis: str = None


class GeneSet(BaseModel):
    """A set of genes."""

    name: str
    gene_symbols: Optional[List[str]] = None
    gene_ids: Optional[List[str]] = None
    genes: Optional[Dict[str, Gene]] = None
    taxon: str = "human"
    taxon_id: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None
    source_url: Optional[str] = None
    target_term_ids: Optional[List[str]] = None
    number_of_genes_dropped: Optional[int] = None
    original_name: Optional[str] = None
    lacks_descriptions: Optional[bool] = None


class GeneSetCollection(BaseModel):
    """A collection of gene sets."""

    gene_sets: List[GeneSet]


def save_gene_set(gene_set: GeneSet, path: Union[str, Path]):
    """
    Save a gene set to a file.

    :param gene_set:
    :param path:
    :return:
    """
    if isinstance(path, Path):
        path = str(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(yaml.dump(gene_set.dict(exclude_unset=True), sort_keys=False))


def parse_gene_set(input_path: Union[str, Path], format: str = None) -> GeneSet:
    """
    Parse a gene set from a file.

    Accepts:

    - yaml (native gene set format; recommended)
    - json (msigdb format)
    - txt (one gene symbol per line)

    This does no normalization of gene symbols or ids.
    """
    if isinstance(input_path, Path):
        input_path = str(input_path)
    if format is None:
        if "gene_export_geneset" in input_path:
            format = "geneweaver"
        else:
            format = input_path.split(".")[-1]
    if format == "yaml":
        with open(input_path, "r") as f:
            gene_set = GeneSet(**yaml.safe_load(f))
    elif format == "json" or format == "msigdb":
        with open(input_path, "r") as f:
            name, msig = list(json.load(f).items())[0]
            gene_set = GeneSet(name=name, gene_symbols=msig["geneSymbols"])
    elif format == "geneweaver":
        gene_set = parse_geneweaver(input_path)
    elif format == "txt":
        with open(input_path, "r") as f:
            gene_symbols = [line.strip() for line in f.readlines()]
            gene_set = GeneSet(name=input_path, gene_symbols=gene_symbols)
    else:
        raise ValueError(f"Unknown format {format}")
    return gene_set


def parse_geneweaver(path: str) -> GeneSet:
    gene_set = GeneSet(name=Path(path).stem, source="geneweaver", gene_ids=[], gene_symbols=[])
    col2sp = {
        "Wormbase": "C elegans",
        "ZFIN": "Danio rerio",
    }
    fix = {
        "Wormbase": "WB",
    }
    with open(path, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")
        col = None
        sp = None
        for row in reader:
            sym = row["Gene Symbol"]
            if not col:
                for k, v in col2sp.items():
                    if row.get(k, None):
                        col = k
                        db = col
                        gene_set.taxon = v
                        if col in fix:
                            db = fix[col]
                        break
            if not col:
                raise ValueError("Unknown column")

            id = f"{db}:{row[col]}"
            gene = Gene(id=id, symbol=sym)
            gene_set.gene_ids.append(id)
            gene_set.gene_symbols.append(sym)
            gene_set.gene_ids.append(id)
    return gene_set


def load_gene_sets(
    path: str,
    ontology_adapter: BasicOntologyInterface = None,
    strict=False,
    fill_missing=True,
) -> GeneSetCollection:
    """Load collection of gene sets from a folder.

    If ontology_adapter is provided, gene symbols will be converted to gene ids and vice versa.
    """
    gene_sets = []
    for input_path in glob.glob(f"{path}/*.yaml"):
        gene_set = parse_gene_set(input_path)
        gene_sets.append(gene_set)
        if not gene_set.gene_ids and not gene_set.gene_symbols:
            raise ValueError(f"Gene set {gene_set.name} has no gene symbols or ids")
        if fill_missing:
            fill_missing_gene_set_values(gene_set, ontology_adapter, strict)
    return GeneSetCollection(gene_sets=gene_sets)


def _is_human(gene_set: GeneSet) -> bool:
    """
    Check if a gene set is human.

    Note we need to handle this as a special case due to the need to
    depend on sqlite:obo:hgnc

    :param gene_set:
    :return:
    """
    if gene_set.gene_ids:
        if all([id.startswith("HGNC:") for id in gene_set.gene_ids]):
            return True
        if any([id.startswith("HGNC:") for id in gene_set.gene_ids]):
            raise ValueError("Gene set contains mixed taxons. Please use a different gene set.")
        return False
    return gene_set.taxon.lower() == "human" or gene_set.taxon_id == "NCBITaxon:9606"


def fill_missing_gene_set_values(
    gene_set: GeneSet,
    ontology_adapter: BasicOntologyInterface = None,
    strict=False,
):
    if not gene_set.gene_ids:
        # special purpose code to fill in HGNC symbols
        if not ontology_adapter:
            if not _is_human(gene_set):
                raise ValueError("Gene set is not human and no ontology adapter was provided")
            ontology_adapter = get_adapter("sqlite:obo:hgnc")
            logger.info(f"Fetching ids for {len(gene_set.gene_symbols)} genes")
            gene_set.gene_ids = []
            for sym in gene_set.gene_symbols:
                ids = ontology_adapter.curies_by_label(sym)
                if strict and len(ids) != 1:
                    raise ValueError(f"Could not find a single id for symbol {sym}")
                # hack! normalize casing
                gene_set.gene_ids.extend([id.upper() for id in ids])
    for gene_id in gene_set.gene_ids:
        # fill each gene using alliance API
        if not gene_set.genes:
            gene_set.genes = {}
        if gene_id not in gene_set.genes:
            gene_set.genes[gene_id] = Gene(id=gene_id)
        gene = gene_set.genes[gene_id]
        if gene_set.lacks_descriptions and gene.symbol:
            continue
        if not gene.symbol or gene.ontological_synopsis is None or gene.narrative_synopsis is None:
            symbol, narrative_synopsis, ontological_synopsis = gene_info(gene_id)
            if not gene.symbol:
                gene.symbol = symbol
            if not gene.ontological_synopsis:
                gene.ontological_synopsis = ontological_synopsis
            if not gene.narrative_synopsis:
                gene.narrative_synopsis = narrative_synopsis
    if not gene_set.gene_symbols:
        gene_set.gene_symbols = [gene.symbol for gene in gene_set.genes.values()]


def drop_genes_from_gene_set(gene_set: GeneSet, percent_to_drop: int) -> GeneSet:
    """
    Drop genes from a gene set.

    :param gene_set:
    :param percent_to_drop:
    :return:
    """
    gene_set = deepcopy(gene_set)
    if percent_to_drop < 0 or percent_to_drop > 100:
        raise ValueError("Percent to drop must be between 0 and 100")
    if percent_to_drop == 0:
        return gene_set
    num_genes = len(gene_set.genes)
    if not num_genes:
        raise ValueError("Gene set has no genes")
    num_to_drop = int(num_genes * percent_to_drop / 100)
    if num_to_drop == 0:
        num_to_drop = 1
    logger.info(f"Dropping {num_to_drop} genes from {gene_set.name}")
    gene_set.genes = dict(sample(gene_set.genes.items(), num_genes - num_to_drop))
    gene_set.gene_ids = list(gene_set.genes.keys())
    gene_set.gene_symbols = [gene.symbol for gene in gene_set.genes.values()]
    gene_set.number_of_genes_dropped = num_to_drop
    gene_set.original_name = gene_set.name
    return gene_set


def gene_info(id: ENTITY_ID) -> Tuple[SYMBOL, DESCRIPTION, DESCRIPTION]:
    url = f"https://www.alliancegenome.org/api/gene/{id}"
    logger.info(f"Fetching gene summary from {url}")
    response = session.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching issues: {response.status_code} // {response.text}")
    obj = response.json()
    symbol = obj["symbol"]
    return symbol, obj["geneSynopsis"], obj["automatedGeneSynopsis"]
