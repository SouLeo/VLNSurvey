import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize


def load_REVERIE():
    cwd = pathlib.Path().absolute()
    base_REVERIE = Path('REVERIE')
    concat_path = cwd / base_REVERIE

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            exs_jsons.append(json.load(infile))

    instructions = []
    for ex in exs_jsons:
        for task in ex:
            for dialogue_entries in task['instructions']:
                sents = dialogue_entries.replace('%', '')
                sents = sents.replace('-', '')
                list_of_sentences = sent_tokenize(sents)
                instructions += list_of_sentences
    return instructions
