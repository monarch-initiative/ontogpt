"""Utility for running multilingual analysis."""

import logging
import os
from typing import Tuple

from ontogpt.clients import LLMClient
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.template_loader import get_template_details
from ontogpt.templates.core import ExtractionResult


def multilingual_analysis(
    prompt,
    filename,
    output_directory,
    model,
    temperature,
    api_base,
    api_version,
    model_provider,
    system_message,
) -> Tuple[ExtractionResult, str, SPIRESEngine]:
    """Run the multilingual analysis."""
    # Set up the extraction template
    template = "all_disease_grounding"
    template_details = get_template_details(template=template)

    ai = LLMClient()
    ai.model = model

    # Keep track of the predictions
    # Key is the filename, value is a list of predictions
    pred_ids: dict[str, list[str]] = {}
    pred_names: dict[str, list[str]] = {}

    try:
        gpt_diagnosis = ai.complete(prompt)
        print(gpt_diagnosis)
    except Exception as e:
        raise Exception(f"Error in completion: {e}")

    # Call the extract function here
    # to ground the answer to OMIM (using MONDO, etc)
    # The KE is refreshed here to avoid retaining
    ke = SPIRESEngine(
        template_details=template_details,
        model=model,
        temperature=temperature,
        api_base=api_base,
        api_version=api_version,
        model_provider=model_provider,
        system_message=system_message,
    )
    extraction = ke.extract_from_text(text=gpt_diagnosis)
    predictions = extraction.named_entities
    pred_ids[filename] = []
    pred_names[filename] = []
    for pred in predictions:
        pred_ids[filename].append(pred.id)
        pred_names[filename].append(pred.label)

    if len(pred_ids[filename]) == 0:
        raise Exception(f"No grounded IDs found for {filename}")

    # Log the result
    logging.info("input file name" "\tpredicted diagnosis ids\tpredicted diagnosis names\n")
    logging.info(
        f"{filename}" f'\t{"|".join(pred_ids[filename])}' f'\t{"|".join(pred_names[filename])}\n'
    )

    # Retain the output as an ExtractionResult object
    # Create the output filename based on the input filename
    output_file_name = filename + ".result"
    output_file_path = os.path.join(output_directory, output_file_name)
    extraction.extracted_object.label = filename

    return (extraction, output_file_path, ke)
