# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import stanza
import os
import complexity
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse import *

Dataset = list[str]


def getVocabSize(dataset: Dataset):
    raise NotImplementedError


def getMeanFrazier(dataset: Dataset):
    # TODO: Use helper functions in complexity.py
    raise NotImplementedError


def getMeanYngve(dataset: Dataset):
    # TODO: Use helper functions in complexity.py
    raise NotImplementedError


def getPoSDistribution(dataset: Dataset):
    raise NotImplementedError


def getAbstractRatio(dataset: Dataset):
    raise NotImplementedError


def getAvgSentLen(dataset: Dataset):
    raise NotImplementedError


def getPerplexity(dataset: Dataset):
    raise NotImplementedError


if __name__ == '__main__':
    #
    # TODO: FOR HANDLING EXCEPTIONS
    #
    # https://bbengfort.github.io/snippets/2018/06/22/corenlp-nltk-parses.html
    #
    # jars = (
    #     "stanford-corenlp-3.9.1.jar",
    #     "stanford-corenlp-3.9.1-models.jar"
    # )
    #
    # with CoreNLPServer(*jars):
    #     parser = CoreNLPParser()
    #
    #     text = "The runner scored from second on a base hit"
    #     parse = next(parser.parse_text(text))

    working_directory = os.getcwd()
    core_nlp_directory = os.path.join(working_directory, 'stanford-corenlp-4.2.0')

    server = CoreNLPServer(
        os.path.join(core_nlp_directory, "stanford-corenlp-4.2.0.jar"),
        os.path.join(core_nlp_directory, "stanford-corenlp-4.2.0-models.jar"),
    )

    server.start()

    parser = CoreNLPParser()
    parse = next(parser.raw_parse("I put the book in the box on the table."))

    pee = complexity.word_score(parse)
    server.stop()
    print(pee)

# TODO:
# Download Lingual Aspects of Datasets and convert their lingual components into a list of strings.
# Feed list of strings into each function
