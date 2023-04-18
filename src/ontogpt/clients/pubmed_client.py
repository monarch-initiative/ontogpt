"""Pubmed Client."""
import logging
from dataclasses import dataclass, field
from typing import Iterator, List

import inflection
from eutils import Client
from eutils._internal.xmlfacades.pubmedarticle import PubmedArticle

PMID = str
TITLE_WEIGHT = 5
MAX_PMIDS = 50


def _normalize(s: str) -> str:
    return inflection.singularize(s).lower()


def _score_paper(paper: PubmedArticle, keywords: List[str]) -> int:
    title_score = _score_text(paper.title, keywords)
    abstract_score = _score_text(paper.abstract, keywords)
    logging.info(f"Scored {paper.pmid} {paper.title} with TS={title_score} AS={abstract_score} ")
    return title_score * TITLE_WEIGHT + abstract_score


def _score_text(text: str, keywords: List[str]) -> int:
    text = text.lower()
    if not text:
        return -100
    score = 0
    for kw in keywords:
        if kw in text:
            score += 1
    return score


@dataclass
class PubmedClient:
    """A client for the Pubmed API.

    This class is a wrapper around the Entrez API.
    """

    entrez_client: Client = field(default_factory=lambda: Client())
    max_text_length = 3000

    def text(self, id: PMID, autoformat=True) -> str:
        """Get the text of a paper from its PMID.

        :param id:
        :param autoformat: if True include title and abstract concatenated
        :return:
        """
        ec = self.entrez_client
        id = id.replace("PMID:", "")
        paset = ec.efetch(db="pubmed", id=id)
        for pa in paset:
            if autoformat:
                txt = f"Title: {pa.title}\nAbstract: {pa.abstract}\nKeywords: {'; '.join(pa.mesh_headings)}"  # noqa
            else:
                txt = pa.full_text
        if len(txt) > self.max_text_length:
            logging.warning(f"Truncating text: {txt[:self.max_text_length]}...")
            txt = txt[0 : self.max_text_length]
        return txt

    def search(self, term: str, keywords: List[str] = None) -> Iterator[PMID]:
        """Get the text of a paper from its PMID.

        :param term:
        :param keywords:
        :return:
        """
        print("Getting client")
        ec = self.entrez_client
        if keywords:
            keywords = [_normalize(kw) for kw in keywords]
            term = f"({term}) AND ({' OR '.join(keywords)})"
        logging.info(f"Searching for {term}...")
        esr = ec.esearch(db="pubmed", term=term)
        logging.info(f"Found {esr.count} papers for {term}.")
        paset = ec.efetch(db="pubmed", id=esr.ids[0:MAX_PMIDS])
        keywords = keywords or []
        keywords = [_normalize(kw) for kw in keywords]
        scored_papers = [(_score_paper(paper, keywords), paper) for paper in paset]
        scored_papers.sort(key=lambda x: x[0], reverse=True)
        for score, paper in scored_papers:
            logging.debug(f"Yielding {paper.pmid} {paper.title} with score {score} ")
            yield f"PMID:{paper.pmid}"
