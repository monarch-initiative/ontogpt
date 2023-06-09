"""Tools for loading and working with GPT4All models."""

import logging

from langchain import LLMChain, PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All


def set_up_gpt4all_model(modelpath):
    """Prepare a GGML-formatted GPT4All model for LLM interaction."""
    logging.info(f"Preparing {modelpath}...")
    local_path = str(modelpath)

    callbacks = [StreamingStdOutCallbackHandler()]
    if local_path.endswith("ggml-gpt4all-j-v1.3-groovy.bin"):
        backend = "gptj"
        llm = GPT4All(model=local_path, backend=backend, callbacks=callbacks, verbose=True)
    else:
        llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

    return llm


def chain_gpt4all_model(llm, prompt_text):
    """Interact with a GPT4All model."""
    template = """{prompt_text}"""

    prompt = PromptTemplate(template=template, input_variables=["prompt_text"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    raw_output = llm_chain.run({"prompt_text": prompt_text})

    return raw_output
