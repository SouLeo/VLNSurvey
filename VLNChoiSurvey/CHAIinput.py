import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize


def load_CHAI():
    cwd = pathlib.Path().absolute()
    base_CHAI_path = Path('CHAI')
    concat_path = cwd / base_CHAI_path

    filenames = list(concat_path.glob('*.txt'))
    contents = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            contents.append(infile.read())

    sentences = []
    for instructions in contents:
        instructions = instructions.replace('%', '')
        instructions = instructions.replace('-', '')
        sentences += sent_tokenize(instructions)
    return sentences