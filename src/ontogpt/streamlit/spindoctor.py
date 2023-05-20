"""Streamlist web app for spindoctor."""
# Import necessary libraries
import re

import streamlit as st
from oaklib import get_adapter

from ontogpt.engines import create_engine
from ontogpt.engines.enrichment import EnrichmentEngine, GeneDescriptionSource
from ontogpt.engines.knowledge_engine import (
    MODEL_GPT_3_5_TURBO,
    MODEL_GPT_4,
    MODEL_TEXT_DAVINCI_003,
)
from ontogpt.utils.gene_set_utils import GeneSet

go = get_adapter("sqlite:obo:go")

# Title of the app
st.title("SPINDOCTOR")
st.caption("A tool for summarizing gene sets using GPT")

col1, col2 = st.columns(2)

# Text area for name input
gene_symbols = col1.text_area("Enter a list of human gene symbols")

model = col1.selectbox(
    "Select the model:", (MODEL_GPT_3_5_TURBO, MODEL_TEXT_DAVINCI_003, MODEL_GPT_4)
)

source = col1.selectbox(
    "Select the gene description source:",
    (
        GeneDescriptionSource.ONTOLOGICAL_SYNOPSIS.value,
        GeneDescriptionSource.NARRATIVE_SYNOPSIS.value,
        GeneDescriptionSource.NONE.value,
    ),
)

openai_api_key = col1.text_input(
    "OpenAI API Key:",
    placeholder="(sk-...) Press [Enter] to submit.",
)

# Button for parsing and displaying the names
if col1.button("Summarize genes"):
    gene_symbols = [symbol.strip() for symbol in re.split(r"[\-,;\s]+", gene_symbols)]
    gene_set = GeneSet(name="TEMP", gene_symbols=gene_symbols)
    ke = create_engine(None, EnrichmentEngine, model=model)
    if openai_api_key:
        ke.set_api_key(openai_api_key)
    if not isinstance(ke, EnrichmentEngine):
        raise ValueError(f"Expected EnrichmentEngine, got {type(ke)}")
    source_pv = GeneDescriptionSource(source)
    col1.write("Analyzing, please wait...")
    results = ke.summarize(gene_set, gene_description_source=source_pv)
    col1.header("Genes")
    for gene_id in gene_set.gene_ids:
        col1.write(f" * {gene_id}")
    # st.write("## Term Strings")
    # for term_string in results.term_strings:
    #    st.write(f" * {term_string}")
    col2.write("## Terms")
    for term_id in results.term_ids:
        if term_id.startswith("GO:"):
            lbl = go.label(term_id)
            col2.markdown(f" * [{term_id}](https://bioregistry.io/{term_id}) - _{lbl}_")
        else:
            col2.markdown(f" * UNPARSED {term_id}")
    col2.header("Summary")
    col2.caption(results.summary)
