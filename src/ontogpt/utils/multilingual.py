"""Utility for running multilingual analysis."""

import codecs
import logging
import os
from io import TextIOWrapper

import openai

from ontogpt.clients import OpenAIClient
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.template_loader import get_template_details
from ontogpt.io.yaml_wrapper import dump_minimal_yaml

def multilingual_analysis(
    input_data_dir, output_directory, output, model="gpt-4-turbo"
):
    """Run the multilingual analysis."""
    # Set up the extraction template
    template = "all_disease_grounding"
    template_details = get_template_details(template=template)

    # make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Set up the writer object
    if not isinstance(output, TextIOWrapper):
        output = codecs.getwriter("utf-8")(output)

    # TODO (maybe) - handle non-OpenAI models
    ai = OpenAIClient()
    ai.model = model

    # Keep track of the predictions
    # Key is the filename, value is a list of predictions
    pred_ids = {}
    pred_names = {}

    for filename in os.listdir(input_data_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_data_dir, filename)

            with open(file_path, mode="r", encoding="utf-8") as txt_file:
                prompt = txt_file.read()

            try:
                gpt_diagnosis = ai.complete(prompt)
            except openai.error.InvalidRequestError as e:
                gpt_diagnosis = "OPENAI API CALL FAILED"

            # Call the extract function here
            # to ground the answer to OMIM (using MONDO, etc)
            # The KE is refreshed here to avoid retaining
            ke = SPIRESEngine(
                template_details=template_details,
                model=model,
                model_source="openai",
            )
            extraction = ke.extract_from_text(text=gpt_diagnosis)
            predictions = extraction.named_entities
            pred_ids[filename] = []
            pred_names[filename] = []
            for pred in predictions:
                pred_ids[filename].append(pred.id)
                pred_names[filename].append(pred.label)

            # Retain the output as text
            # Create the output filename based on the input filename
            output_file_name = filename + ".result"
            output_file_path = os.path.join(output_directory, output_file_name)
            with open(output_file_path, "w", encoding="utf-8") as outfile:
                outfile.write(gpt_diagnosis)

            # Log the result
            logging.info(
                "input file name"
                "\tpredicted diagnosis ids\tpredicted diagnosis names\n"
            )
            logging.info(
                f'{filename}'
                f'\t{"|".join(pred_ids[filename])}'
                f'\t{"|".join(pred_names[filename])}\n'
            )

            # Write the result
            # Include the input filename for the prompt in the output
            extraction.extracted_object.label = filename
            output.write("---\n")
            output.write(dump_minimal_yaml(extraction))
