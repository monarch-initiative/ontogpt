"""Pubmed Client."""
import logging
import time
from dataclasses import dataclass
from typing import List

import inflection
import requests
from bs4 import BeautifulSoup
from oaklib.utilities.apikey_manager import get_apikey_value

PMID = str
TITLE_WEIGHT = 5
MAX_PMIDS = 50

PUBMED = "pubmed"
EUTILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
DOCSEP = "\n------\n"


def _normalize(s: str) -> str:
    return inflection.singularize(s).lower()


# TODO: Add this back
# def _score_paper(paper: PubmedArticle, keywords: List[str]) -> int:
#     title_score = _score_text(paper.title, keywords)
#     abstract_score = _score_text(paper.abstract, keywords)
#     logging.info(f"Scored {paper.pmid} {paper.title} with TS={title_score} AS={abstract_score} ")
#     return title_score * TITLE_WEIGHT + abstract_score


# def _score_text(text: str, keywords: List[str]) -> int:
#     text = text.lower()
#     if not text:
#         return -100
#     score = 0
#     for kw in keywords:
#         if kw in text:
#             score += 1
#     return score


def parse_pmxml(xml: str, autoformat: bool) -> List[str]:
    """Extract structured text from  PubMed XML.

    :param xml: One or more xml entries, as string
    :param autoformat: if True include title and abstract concatenated
    :return: a list of strings, one per entry
    """

    docs = []

    soup = BeautifulSoup(xml, "xml")

    for pa in soup.find_all("PubmedArticle"):
        if autoformat:
            ti = pa.find("ArticleTitle").text
            if pa.find("Abstract"):  # Document may not have abstract
                ab = pa.find("Abstract").text
            if pa.find("KeywordList"):  # Document may not have MeSH terms or keywords
                kw = [tag.text for tag in pa.find_all("Keyword")]
            else:
                kw = ""
            txt = f"Title: {ti}\nAbstract: {ab}\nKeywords: {'; '.join(kw)}"
        else:
            txt = soup.get_text()
        docs.append(txt)

    return docs


@dataclass
class PubmedClient:
    """A client for the Pubmed API.

    This class is a wrapper around the Entrez API.
    """

    max_text_length = 3000

    try:
        email = get_apikey_value("ncbi-email")
    except ValueError:
        email = None
        logging.info(f"Email for NCBI API not found.")

    try:
        ncbi_key = get_apikey_value("ncbi-key")
    except ValueError:
        ncbi_key = None
        logging.info(f"NCBI API key not found. Will use no key.")

    def get_pmids(self, term: str) -> List[str]:
        """Search PubMed and retrieve a list of PMIDs matching the search term.

        :param term: The search term to query PubMed.
        :return: A list of PMIDs matching the search term.
        """

        pmids = []

        batch_size = 250

        retry_max = 2

        search_url = EUTILS_URL + "esearch.fcgi"

        # If retmax==0, we get only the size of the search result in count of PMIDs
        if self.email and self.ncbi_key:
            params = {
                "db": PUBMED,
                "term": term,
                "retmode": "json",
                "retmax": 0,
                "email": self.email,
                "api_key": self.ncbi_key,
            }
        else:
            params = {"db": PUBMED, "term": term, "retmode": "json", "retmax": 0}
        response = requests.get(search_url, params=params)

        if response.status_code == 200:
            data = response.json()
            resultcount = int(data["esearchresult"]["count"])
            logging.info(f"Search returned {resultcount} PMIDs matching search term {term}")
        else:
            logging.error("Encountered error in searching PubMed:", response.status_code)

        # Now we get the list of PMIDs, iterating as needed

        for retstart in range(0, resultcount, batch_size):
            params["retstart"] = retstart
            params["retmax"] = batch_size

            response = requests.get(search_url, params=params)

            trying = True
            try_count = 0
            while trying:
                if response.status_code == 200:
                    data = response.json()
                    pmids.extend(data["esearchresult"]["idlist"])
                    trying = False
                else:
                    logging.error(f"Encountered error in searching PubMed: {response.status_code}")
                    try_count = try_count + 1
                    if try_count < retry_max:
                        logging.info("Trying again...")
                        time.sleep(0.5)
                    else:
                        logging.info(f"Giving up - last status code {response.status_code}")
                        trying = False
            logging.info("Retrieved PMIDs.")

        return pmids

    # TODO: verify the text() function works as expected for both single and multiple entries
    # TODO: get multiple batches of records using history server
    # TODO: catch error 414 (URI too long)
    def text(self, id: list[PMID], autoformat=True) -> str:
        """Get the text of one or more papers from their PMIDs.

        :param ids: List of PubMed IDs
        :param autoformat: if True include title and abstract concatenated
        :return: the text of a single entry, or concatenated text of multiple entries
        """

        fetch_url = EUTILS_URL + "efetch.fcgi"
        if self.email and self.ncbi_key:
            params = {
                "db": PUBMED,
                "id": ",".join(id),
                "rettype": "xml",
                "retmode": "xml",
                "email": self.email,
                "api_key": self.ncbi_key,
            }
        else:
            params = {"db": PUBMED, "id": ",".join(id), "rettype": "xml", "retmode": "xml"}

        response = requests.get(fetch_url, params=params)

        if response.status_code == 200:
            xml_data = response.text
        else:
            print("Encountered error in fetching from PubMed:", response.status_code)

        # Parse that xml - this returns a list of strings so we concatenate
        these_docs = parse_pmxml(xml_data, autoformat)
        txt = ""
        for doc in these_docs:
            if len(doc) > self.max_text_length:
                logging.warning(
                    f'Truncating entry beginning "{doc[:50]}" to {str(self.max_text_length)}...'
                )
                shortdoc = doc[0 : self.max_text_length]
                txt = f"{txt}{DOCSEP}{shortdoc}"
            else:
                txt = f"{txt}{DOCSEP}{doc}"
        return txt

    # def search(self, term: str, keywords: List[str] = None) -> Iterator[PMID]:
    #     """Get the text of a paper from its PMID.

    #     :param term:
    #     :param keywords:
    #     :return:
    #     """
    #     print("Getting client")
    #     ec = self.entrez_client
    #     if keywords:
    #         keywords = [_normalize(kw) for kw in keywords]
    #         term = f"({term}) AND ({' OR '.join(keywords)})"
    #     logging.info(f"Searching for {term}...")
    #     esr = ec.esearch(db="pubmed", term=term)
    #     logging.info(f"Found {esr.count} papers for {term}.")
    #     paset = ec.efetch(db="pubmed", id=esr.ids[0:MAX_PMIDS])
    #     keywords = keywords or []
    #     keywords = [_normalize(kw) for kw in keywords]
    #     scored_papers = [(_score_paper(paper, keywords), paper) for paper in paset]
    #     scored_papers.sort(key=lambda x: x[0], reverse=True)
    #     for score, paper in scored_papers:
    #         logging.debug(f"Yielding {paper.pmid} {paper.title} with score {score} ")
    #         yield f"PMID:{paper.pmid}"
