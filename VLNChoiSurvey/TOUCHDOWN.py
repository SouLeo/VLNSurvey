import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize


def load_TOUCHDOWN():
    cwd = pathlib.Path().absolute()
    base_TOUCHDOWN = Path('TOUCHDOWN')
    concat_path = cwd / base_TOUCHDOWN

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            for jsonObj in infile:
                jsonDict = json.loads(jsonObj)
                exs_jsons.append(jsonDict)

    instructions = []
    for ex in exs_jsons:
        sents = ex['full_text']
        sents = sents.replace('%', '')
        sents = sents.replace('-', '')
        list_of_sentences = sent_tokenize(sents)
        instructions += list_of_sentences
    return instructions
