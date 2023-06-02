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

    template = """From the text below, extract the following entities in the following format: {entities}
    {input_text}"""

    prompt = PromptTemplate(template=template, input_variables=["entities", "input_text"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    entities = """  name: <the name of the disease>
  description: <a description of the disease>
  synonyms: <semicolon-separated list of synonymss>
  subclass_of: <semicolon-separated list of subclass_ofs>
  symptoms: <semicolon-separated list of symptomss>
  inheritance: <the value for inheritance>
  genes: <semicolon separated list of gene symbols; for example: PEX1; PEX2; PEX3>
  disease_onsets: <semi-colon separated list of onsets at which the disease occurs, for example: adult; juvenile; first decade>
  label: <The label (name) of the named thing>"""

    input_text = """Text:
  Sly syndrome, also called mucopolysaccharidosis type VII (MPS-VII), is an autosomal recessive lysosomal storage disease caused by a deficiency of the enzyme β-glucuronidase. This enzyme is responsible for breaking down large sugar molecules called glycosaminoglycans (AKA GAGs, or mucopolysaccharides). The inability to break down GAGs leads to a buildup in many tissues and organs of the body. The severity of the disease can vary widely."
"""

    llm_chain.run({"entities":entities, "input_text":input_text})

