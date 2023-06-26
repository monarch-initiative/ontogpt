"""HuggingFace Hub Client."""
import logging

from dataclasses import dataclass
from oaklib.utilities.apikey_manager import get_apikey_value
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

# Note: See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
# for all relevant models

@dataclass
class HFHubClient:
    """A client for the HuggingFace Hub API."""

    try:
        api_key = get_apikey_value("hfhub-key")
    except ValueError:
        logging.error("HuggingFace Hub API key not found. See README.")

    def get_model(self, modelname: str) -> HuggingFaceHub:
        """Retreive a model from the Hub, given its repository name.

        Returns a model object of type
        langchain.llms.huggingface_hub.HuggingFaceHub
        """
        model = HuggingFaceHub(repo_id=modelname,
                               verbose=True,
                               model_kwargs={"temperature": 0.2, "max_length": 500},
                               huggingfacehub_api_token=self.api_key,
                               task="text-generation"
                               )

        return model
    
    def query_hf_model(self, llm, prompt_text):
        """Interact with a GPT4All model."""
        logging.info(f"Complete: prompt[{len(prompt_text)}]={prompt_text[0:100]}...")

        template = """{prompt_text}"""

        prompt = PromptTemplate(template=template, input_variables=["prompt_text"])

        llm_chain = LLMChain(prompt=prompt, llm=llm)

        try:
            raw_output = llm_chain.run({"prompt_text": prompt_text})
        except ValueError as e:
            logging.error(e)
            raw_output = ""

        return raw_output
