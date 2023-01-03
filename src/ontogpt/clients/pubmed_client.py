import logging
from dataclasses import dataclass, field

import yaml
from eutils import Client

PMID = str


@dataclass
class PubmedClient:
    """
    A client for the Pubmed API.

    This class is a wrapper around the Entrez API.
    """

    entrez_client: Client = field(default_factory=lambda: Client())
    max_text_length = 3000

    def text(self, id: PMID, autoformat=True) -> str:
        """
        Get the text of a paper from its PMID

        :param id:
        :param autoformat: if True include title and abstract concatenated
        :return:
        """
        ec = self.entrez_client
        id = id.replace("PMID:", "")
        paset = ec.efetch(db="pubmed", id=id)
        for pa in paset:
            if autoformat:
                txt = f"Title: {pa.title}\nAbstract: {pa.abstract}\nKeywords: {'; '.join(pa.mesh_headings)}"
            else:
                txt = pa.full_text
        if len(txt) > self.max_text_length:
            logging.warning(f"Truncating text: {txt[:self.max_text_length]}...")
            txt = txt[0 : self.max_text_length]
        return txt
