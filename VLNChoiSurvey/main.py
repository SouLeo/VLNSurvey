# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import stanza
import os
import complexity
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse import *

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
#     parse.draw()


def getVocabSize():
    raise NotImplementedError


def getFrazier():
    raise NotImplementedError


def getYgnve():
    raise NotImplementedError


def getPoSDistribution():
    raise NotImplementedError


def getAbstractRatio():
    raise NotImplementedError


def getAvgSentLen():
    raise NotImplementedError


def getPerplexity():
    raise NotImplementedError


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
