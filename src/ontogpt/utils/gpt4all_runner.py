"""Tools for loading and working with GPT4All models."""

import logging

from langchain import LLMChain, PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All


def set_up_gpt4all_model(modelpath, backend="gptj"):
    """Prepare a GGML-formatted GPT4All model for LLM interaction."""
    # TODO: change backend as needed
    # see https://docs.gpt4all.io/gpt4all_python.html

    logging.info(f"Preparing {modelpath}...")
    local_path = str(modelpath)

    callbacks = [StreamingStdOutCallbackHandler()]
    llm = GPT4All(model=local_path, backend=backend, callbacks=callbacks, verbose=True)

    return llm


def chain_gpt4all_model(llm, prompt_text):
    """Interact with a GPT4All model."""
    template = """{prompt_text}"""

    prompt = PromptTemplate(template=template, input_variables=["prompt_text"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    raw_output = llm_chain.run({"prompt_text": prompt_text})

    return raw_output
