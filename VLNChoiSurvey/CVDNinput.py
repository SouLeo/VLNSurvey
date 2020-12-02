import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize


def load_CVDN():
    cwd = pathlib.Path().absolute()
    base_CVDN = Path('CVDN')
    concat_path = cwd / base_CVDN

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            exs_jsons.append(json.load(infile))

    instructions = []
    for ex in exs_jsons:
        for task in ex:
            for dialogue_entry in task['dialog_history']:
                dialogue_entry['message'] = dialogue_entry['message'].replace('%', '')
                dialogue_entry['message'] = dialogue_entry['message'].replace('-', '')
                list_of_sentences = sent_tokenize(dialogue_entry['message'])
                instructions += list_of_sentences
    return instructions
