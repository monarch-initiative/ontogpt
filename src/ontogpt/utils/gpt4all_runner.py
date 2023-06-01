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


def chain_gpt4all_model(llm):
    """Interact with a GPT4All model."""

    # TODO: pass prompt text to this function

    template = """Question: {question}
    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "How can we find the nouns in the following sentence: 'The car jumped over the wall.'"

    llm_chain.run(question)

