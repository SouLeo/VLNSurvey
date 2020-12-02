import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize


def load_asknav():
    cwd = pathlib.Path().absolute()
    base_asknav = Path('asknav')
    concat_path = cwd / base_asknav

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            exs_jsons.append(json.load(infile))

    instructions = []
    for ex in exs_jsons:
        for task in ex:
            instructions += task['instructions']
    return instructions
