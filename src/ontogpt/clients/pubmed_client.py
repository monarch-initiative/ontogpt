"""Pubmed Client."""
import logging
import time
from dataclasses import dataclass
from typing import List, Tuple, Union

import inflection
import requests
from bs4 import BeautifulSoup
from oaklib.utilities.apikey_manager import get_apikey_value

PMID = str
TITLE_WEIGHT = 5
MAX_PMIDS = 50

PUBMED = "pubmed"
EUTILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def _normalize(s: str) -> str:
    return inflection.singularize(s).lower()


def _score_paper(paper: str, keywords: List[str]) -> Tuple(PMID, int):
    """Assign a quality score to a PubMed entry.

    Input needs to be XML so it can be parsed by component.
    :param paper: string, the text of the paper, as XML
    :param keywords: list of keywords to use in scoring
    :return: tuple of article ID (PMID) and score
    """

    # Parse the paper by component first
    soup = BeautifulSoup(paper, "xml")
    for pa in soup.find_all("PubmedArticle"):  # This should be one exactly
        ti = pa.find("ArticleTitle").text
        pmid = pa.find("ArticleId", IdType="pubmed")
        if pa.find("Abstract"):  # Document may not have abstract
            ab = pa.find("Abstract").text
        else:
            ab = ""

    title_score = _score_text(ti, keywords)
    abstract_score = _score_text(ab, keywords)
    logging.info(f"Scored {pmid} {ti} with TS={title_score} AS={abstract_score} ")
    score = title_score * TITLE_WEIGHT + abstract_score
    return (pmid, score)


def _score_text(text: str, keywords: List[str]) -> int:
    """Assign a quality score to a text entry.

    A text entry not mentioning any of its keywords has a score of zero.
    Score increases by one for each keyword mentioned in the text.
    :param text: The text to assign the score to
    :param keywords: The keywords to use in scoring"""
    text = text.lower()
    if not text:
        return -100
    score = 0
    for kw in keywords:
        if kw in text:
            score += 1
    return score


def parse_pmxml(xml: str, raw: bool, autoformat: bool) -> List[str]:
    """Extract structured text from PubMed XML.

    :param xml: One or more xml entries, as string
    :param raw: if True, do not parse the xml beyond separating documents
    :param autoformat: if True include title and abstract concatenated
    :return: a list of strings, one per entry
    """

    docs = []

    soup = BeautifulSoup(xml, "xml")

    for pa in soup.find_all("PubmedArticle"):
        if autoformat and not raw:
            ti = pa.find("ArticleTitle").text
            if pa.find("Abstract"):  # Document may not have abstract
                ab = pa.find("Abstract").text
            if pa.find("KeywordList"):  # Document may not have MeSH terms or keywords
                kw = [tag.text for tag in pa.find_all("Keyword")]
            else:
                kw = ""
            txt = f"Title: {ti}\nAbstract: {ab}\nKeywords: {'; '.join(kw)}"
        elif raw:
            txt = str(pa)
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

        batch_size = 5000
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

    def text(
        self, ids: Union[list[PMID], PMID], raw=False, autoformat=True
    ) -> Union[list[str], str]:
        """Get the text of one or more papers from their PMIDs.

        :param ids: List of PubMed IDs, or string with single PMID
        :param raw: if True, do not parse the xml, just return the raw output with tags
        :param autoformat: if True include title and abstract concatenated
        :return: the text of a single entry, or a list of strings for text of multiple entries
        """

        # Check if the PMID(s) can be parsed
        # and remove prefix if present
        if isinstance(ids, PMID):  # If it's a single PMID
            ids = [ids]
            singledoc = True
        else:
            singledoc = False
        clean_ids = [id.replace("PMID:", "", 1) for id in ids]
        ids = clean_ids

        # Check if we have enough IDs to require epost
        use_post = False
        if len(ids) > 9999:
            use_post = True

        fetch_url = EUTILS_URL + "efetch.fcgi"

        if not use_post:
            if self.email and self.ncbi_key:
                params = {
                    "db": PUBMED,
                    "id": ",".join(ids),
                    "rettype": "xml",
                    "retmode": "xml",
                    "email": self.email,
                    "api_key": self.ncbi_key,
                }
            else:
                params = {"db": PUBMED, "id": ",".join(ids), "rettype": "xml", "retmode": "xml"}

            response = requests.get(fetch_url, params=params)

        else:
            # Do post request first
            post_url = EUTILS_URL + "epost.fcgi"
            if self.email and self.ncbi_key:
                params = {
                    "db": PUBMED,
                    "id": ",".join(ids),
                    "email": self.email,
                    "api_key": self.ncbi_key,
                }
            else:
                params = {"db": PUBMED, "id": ",".join(ids)}

            response = requests.post(post_url, params=params)

            webenv = response.text.split("<WebEnv>")[1].split("</WebEnv>")[0]
            querykey = response.text.split("<QueryKey>")[1].split("</QueryKey>")[0]

            # Not do the fetch
            params = {
                "db": PUBMED,
                "query_key": querykey,
                "WebEnv": webenv,
                "rettype": "xml",
            }

            response = requests.get(fetch_url, params=params)

        if response.status_code == 200:
            xml_data = response.text
        else:
            logging.error("Encountered error in fetching from PubMed:", response.status_code)

        # Parse that xml - this returns a list of strings
        # if raw is True, the tags are kept, but we still get a list of docs
        these_docs = parse_pmxml(xml_data, raw, autoformat)
        txt = []
        for doc in these_docs:
            if len(doc) > self.max_text_length:
                logging.warning(
                    f'Truncating entry beginning "{doc[:50]}" to {str(self.max_text_length)}...'
                )
                shortdoc = doc[0 : self.max_text_length]
                txt.append(shortdoc)
            else:
                txt.append(doc)
            if singledoc:
                return txt[0]

        return txt

    def search(self, term: str, keywords: List[str] = None) -> List[PMID]:
        """Get the quality-scored text of PubMed papers relating to a search term and keywords.

        This generator yields PMIDs. Note this uses the MAX_PMIDS value
        to determine how many documents to collect.
        :param term: search term, a string
        :param keywords: keywords, a list of strings
        :return: a list of PMIDs corresponding to the search term and keywords
        """

        if keywords:
            keywords = [_normalize(kw) for kw in keywords]
            term = f"({term}) AND ({' OR '.join(keywords)})"
        else:
            keywords = []

        logging.info(f"Searching for {term}...")

        esr = self.get_pmids(term=term)

        paset = self.text(id=esr[0:MAX_PMIDS], raw=True)

        scored_papers = [(_score_paper(paper, keywords), paper) for paper in paset]
        scored_papers.sort(key=lambda x: x[1][0], reverse=True)

        for id_and_score, paper in scored_papers:
            pmid = id_and_score[0]
            score = id_and_score[1]
            logging.debug(f"Yielding {pmid} with score {score} ")
            yield f"{pmid}"
