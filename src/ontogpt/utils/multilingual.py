"""Utility for running multilingual analysis."""

import codecs
import logging
import os
from io import TextIOWrapper


from ontogpt.clients import LLMClient
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.template_loader import get_template_details
from ontogpt.io.yaml_wrapper import dump_minimal_yaml


def multilingual_analysis(input_data_dir, output_directory, output, model):
    """Run the multilingual analysis."""
    # Set up the extraction template
    template = "all_disease_grounding"
    template_details = get_template_details(template=template)

    # make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Set up the writer object
    if not isinstance(output, TextIOWrapper):
        output = codecs.getwriter("utf-8")(output)

    ai = LLMClient()
    ai.model = model

    # Keep track of the predictions
    # Key is the filename, value is a list of predictions
    pred_ids = {}
    pred_names = {}

    # Log all errors, with prompt filename as key and error as value
    errors = {}

    for filename in os.listdir(input_data_dir):
        completed = False
        grounded = False
        if filename.endswith(".txt"):
            file_path = os.path.join(input_data_dir, filename)

            with open(file_path, mode="r", encoding="utf-8") as txt_file:
                prompt = txt_file.read()

            try:
                gpt_diagnosis = ai.complete(prompt)
                completed = True
            except Exception as e:
                errors[filename] = e
                logging.error(f"Error: {e}")

            # Call the extract function here
            # to ground the answer to OMIM (using MONDO, etc)
            # The KE is refreshed here to avoid retaining
            if completed:
                try:
                    ke = SPIRESEngine(
                        template_details=template_details,
                        model=model,
                    )
                    extraction = ke.extract_from_text(text=gpt_diagnosis)
                    predictions = extraction.named_entities
                    pred_ids[filename] = []
                    pred_names[filename] = []
                    for pred in predictions:
                        pred_ids[filename].append(pred.id)
                        pred_names[filename].append(pred.label)

                    # Log the result
                    logging.info(
                        "input file name" "\tpredicted diagnosis ids\tpredicted diagnosis names\n"
                    )
                    logging.info(
                        f"{filename}"
                        f'\t{"|".join(pred_ids[filename])}'
                        f'\t{"|".join(pred_names[filename])}\n'
                    )
                    grounded = True
                except Exception as e:
                    errors[filename] = e
                    logging.error(f"Error: {e}")

            # Retain the output as text
            # Create the output filename based on the input filename
            output_file_name = filename + ".result"
            output_file_path = os.path.join(output_directory, output_file_name)
            with open(output_file_path, "w", encoding="utf-8") as outfile:
                if completed and grounded:
                    outfile.write(gpt_diagnosis)

                    # Write the result
                    # Include the input filename for the prompt in the output
                    extraction.extracted_object.label = filename
                    output.write("---\n")
                    output.write(dump_minimal_yaml(extraction))

                else:
                    outfile.write(f"Error: {errors[filename]}")

            # If there were errors, log them to a file
            if len(errors) > 0:
                error_file_path = os.path.join(output_directory, "errors.txt")
                with open(error_file_path, "w", encoding="utf-8") as outfile:
                    for error in errors:
                        outfile.write(f"{error}\t{errors[error]}\n")
