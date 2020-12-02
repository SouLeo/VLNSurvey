import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize


def load_Alfred():
    cwd = pathlib.Path().absolute()
    base_alfred = Path('Alfred')
    alfred_data_dir = cwd / base_alfred

    split_list = [x for x in alfred_data_dir.iterdir() if x.is_dir()]
    trial_list = []
    for split in split_list:
        trial_list += [x for x in split.iterdir() if x.is_dir()]

    examples = []
    for trial in trial_list:
        filenames = list(trial.glob('*.json'))
        for file in filenames:
            with open(file) as infile:
                examples.append(json.load(infile))

    annotation_list = []
    for example in examples:
        annotation_list += example['turk_annotations']['anns']

    sentences = []
    for annotation in annotation_list:
        sentences.append(annotation['task_desc'])
        high_descs = annotation['high_descs']
        for desc in high_descs:
            sentences.append(desc)

    sentences_tokenized = []
    for sentence in sentences:
        sentences_tokenized += sent_tokenize(sentence)

    return sentences_tokenized
    #
    # filenames = list(concat_path.glob('*.json'))
    # exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    # for filename in filenames:
    #     with open(filename) as infile:
    #         contents = exs_jsons.append(json.load(infile))
    #
    # instruction_list = []
    # for instructions in exs_jsons:  # gather list of json objects from single training data
    #     for instruction in instructions:
    #         instruction_list.append(instruction['instructions'])
    #
    # sentences = []
    # for ex in instruction_list:
    #     for user_response in ex:
    #         sentences += sent_tokenize(user_response)
    #
    # return sentences
