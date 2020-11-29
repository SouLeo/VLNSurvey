import os
import complexity
# from nltk.tree import *
# import nltk
from nltk.util import ngrams
from nltk.util import pad_sequence
from collections import Counter
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse import *
from nltk.tokenize import word_tokenize
from nltk import pos_tag_sents
from nltk import FreqDist


def getVocabSize(sentences):
    word_counter = Counter()
    for sentence in sentences:
        tokenized_sentence = word_tokenize(sentence)
        if word_counter is not None:
            for word in tokenized_sentence:
                word_counter[word] += 1.0
    return len(word_counter)


def getMeanFrazier(server, sentences):
    with server:
        parser = CoreNLPParser()
        sentence_list = []
        for sentence in sentences:
            parse = next(parser.raw_parse(sentence))
            sentence_list.append(str(parse[0]))
    server.stop()
    return complexity.get_mean_frazier(sentence_list)


def getMeanYngve(server, sentences):
    with server:
        parser = CoreNLPParser()
        sentence_list = []
        for sentence in sentences:
            parse = next(parser.raw_parse(sentence))
            sentence_list.append(str(parse[0]))
    server.stop()
    return complexity.get_mean_yngve(sentence_list)


def getPoSDistribution(sentences):
    sentences_tokenized = [word_tokenize(i) for i in sentences]
    pos_tagged_sentences = pos_tag_sents(sentences_tokenized)
    pos_tags = []
    for sentence in pos_tagged_sentences:
        pos_tags += [pos_tag for _, pos_tag in sentence]
    fd = FreqDist(pos_tags)
    return fd.most_common(5)


def getAbstractRatio(sentences):
    raise NotImplementedError


def getAvgSentLen(sentences):
    sentence_length_list = []
    for sentence in sentences:
        num_words = len(word_tokenize(sentence))
        sentence_length_list.append(num_words)
    total_words = sum(sentence_length_list)
    num_sentences = len(sentence_length_list)
    return total_words/num_sentences


def getPerplexity(sentences):
    raise NotImplementedError


if __name__ == '__main__':
    working_directory = os.getcwd()
    core_nlp_directory = os.path.join(working_directory, 'stanford-corenlp-4.2.0')

    server = CoreNLPServer(
        os.path.join(core_nlp_directory, "stanford-corenlp-4.2.0.jar"),
        os.path.join(core_nlp_directory, "stanford-corenlp-4.2.0-models.jar"),
    )

    example = ['Mary had a little lamb',
               'Jack went up the hill',
               'Jill followed suit',
               'i woke up suddenly',
               'it was a really bad dream.']
