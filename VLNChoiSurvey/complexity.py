"""
@AUTHOR: meyersbs
Source: https://github.com/andymeneely/sira-nlp/blob/b027a5d7407043b6541e2aa02704a7239f109485/app/lib/nlp/complexity.py
"""
from nltk.tree import *


def word_score(tree):
    """ Calculate the word score a tree. """
    if type(tree) == str:
        return 1
    else:
        score = 0
        for child in tree:
            score += word_score(child)
        return score


def is_sent(value):
    """ Determine if the given string is a sentence. """
    return len(value) > 0 and value[0] == "S"


def calc_yngve_score(tree, parent=0):
    """ Calculate the Yngve score for a given tree. """
    if type(tree) == str:
        return parent
    else:
        c = 0
        for i, child in enumerate(reversed(tree)):
            c += calc_yngve_score(child, parent + i)
        return c


def yngve_redux(treestring):
    """
    For the given treestring, return the word count and the Yngve score.
    """
#    print(treestring)
    tree = Tree.fromstring(treestring)
    total = float(calc_yngve_score(tree, 0))
    words = float(word_score(tree))

    return [total, words]


def get_mean_yngve(treestrings):
    """ Average all of the yngve scores for the given input. """
    c = 0
    total = 0
    if type(treestrings) != list:
        raise ValueError('Input to get_mean_yngve() must be a list of strings.')

    for treestring in treestrings:
        results = yngve_redux(treestring)
        total += results[0]
        c += results[1]

    try:
        score = float(total / c)
    except ZeroDivisionError:
        logger.warning('ZeroDivisionError for Yngve calculation.')
        score = 0.0

    return score


def calc_frazier_score(tree, parent, parent_label):
    """ Calculate the Frazier scores for the given input. """
    my_lab = ''
    if type(tree) == str:
        return parent-1
    else:
        c = 0
        for i, child in enumerate(tree):
            score = 0
            if i == 0:
                my_lab = tree.label()
                if is_sent(my_lab):
                    score = (0 if is_sent(parent_label) else parent + 1.5)
                elif my_lab != '' and my_lab != "ROOT" and my_lab != "TOP":
                    score = parent+1
            c += calc_frazier_score(child, score, my_lab)
        return c


def get_mean_frazier(treestrings):
    """ Average all of the Frazier scores for the given input. """
    sentences, total_frazier_score, total_word_count = 0, 0, 0
    if type(treestrings) != list:
        raise ValueError('Input to get_mean_frazier() must be a list of '
                         'strings.')
    for tree_line in treestrings:
        if tree_line.strip() == "":
            continue
        tree = Tree.fromstring(tree_line)
        sentences += 1
        raw_frazier_score = calc_frazier_score(tree, 0, "")

        total_word_count += word_score(tree)
        total_frazier_score += raw_frazier_score

    try:
        score = float(total_frazier_score) / float(total_word_count)
    except ZeroDivisionError:
        lg.warning('ZeroDivisionError for Frazier calculation.')
        score = 0.0

    return score
