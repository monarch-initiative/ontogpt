"""Utilities for processing PDF files using PyMuPDF."""

from operator import itemgetter


def headers_para(doc, size_tag):
    """Scrapes headers & paragraphs from PDF and return texts with element tags.

    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param size_tag: textual element tags for each size
    :type size_tag: dict
    :rtype: list
    :return: texts with pre-prended element tags
    """
    header_para = []  # list with headers and paragraphs
    first = True  # boolean operator for first header
    previous_s = {}  # previous span

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b["type"] == 0:  # this block contains text

                # REMEMBER: multiple fonts and sizes are possible IN one block

                block_string = ""  # text found in block
                for line in b["lines"]:  # iterate through the text lines
                    for span in line["spans"]:  # iterate through the text spans
                        if span["text"].strip():  # removing whitespaces:
                            if first:
                                previous_s = span
                                first = False
                                block_string = size_tag[span["size"]] + span["text"]
                            else:
                                if span["size"] == previous_s["size"]:

                                    if block_string and all((c == "|") for c in block_string):
                                        # block_string only contains pipes
                                        block_string = size_tag[span["size"]] + span["text"]
                                    if block_string == "":
                                        # new block has started, so append size tag
                                        block_string = size_tag[span["size"]] + span["text"]
                                    else:  # in the same block, so concatenate strings
                                        block_string += " " + span["text"]

                                else:
                                    header_para.append(block_string)
                                    block_string = size_tag[span["size"]] + span["text"]

                                previous_s = span

                    # new block started, indicating with a pipe
                    block_string += "|"

                header_para.append(block_string)

    return header_para


def fonts(doc, granularity=False):
    """Extract fonts and their usage in PDF documents.

    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param granularity: also use 'font', 'flags' and 'color' to discriminate text
    :type granularity: bool
    :rtype: [(font_size, count), (font_size, count}], dict
    :return: most used fonts sorted by count, font style information
    """
    styles = {}
    font_counts = {}

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b["type"] == 0:  # block contains text
                for line in b["lines"]:  # iterate through the text lines
                    for span in line["spans"]:  # iterate through the text spans
                        if granularity:
                            identifier = "{0}_{1}_{2}_{3}".format(
                                span["size"], span["flags"], span["font"], span["color"]
                            )
                            styles[identifier] = {
                                "size": span["size"],
                                "flags": span["flags"],
                                "font": span["font"],
                                "color": span["color"],
                            }
                        else:
                            identifier = "{0}".format(span["size"])
                            styles[identifier] = {"size": span["size"], "font": span["font"]}

                        font_counts[identifier] = (
                            font_counts.get(identifier, 0) + 1
                        )  # count the fonts usage

    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)

    if len(font_counts) < 1:
        raise ValueError("Zero discriminating fonts found!")

    return font_counts, styles


def font_tags(font_counts, styles):
    """Return dictionary with font sizes as keys and tags as value.

    :param font_counts: (font_size, count) for all fonts occuring in document
    :type font_counts: list
    :param styles: all styles found in the document
    :type styles: dict

    :rtype: dict
    :return: all element tags based on font-sizes
    """
    p_style = styles[font_counts[0][0]]  # get style for most used font by count (paragraph)
    p_size = p_style["size"]  # get the paragraph's size

    # sorting the font sizes high to low, so that we can append the right integer to each tag
    font_sizes = []
    for font_size, _count in font_counts:
        font_sizes.append(float(font_size))
    font_sizes.sort(reverse=True)

    # aggregating the tags for each font size
    idx = 0
    size_tag = {}
    for size in font_sizes:
        idx += 1
        if size == p_size:
            idx = 0
            size_tag[size] = "<p>"
        if size > p_size:
            size_tag[size] = "<h{0}>".format(idx)
        elif size < p_size:
            size_tag[size] = "<s{0}>".format(idx)

    return size_tag
