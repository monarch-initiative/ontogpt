"""Tools for loading and working with GPT4All models."""

import logging

import llm


def set_up_gpt4all_model(modelname):
    """Prepare a GPT4All model for LLM interaction."""
    logging.info(f"Preparing {modelname}...")

    model = llm.get_model(modelname)

    return model


def chain_gpt4all_model(model, prompt_text):
    """Interact with a GPT4All model."""
    raw_output = model.prompt(prompt_text)

    return raw_output.text()
