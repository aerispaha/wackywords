import csv
import os
import random

from flask import Flask
from flask import render_template

app = Flask(__name__)


def word_list_from_file(filepath) -> list:

    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        words = [w[0] for w in list(reader)]
    return words


nouns = word_list_from_file(os.path.join('data', 'nouns.csv'))
verbs = word_list_from_file(os.path.join('data', 'verbs.csv'))
adjectives = word_list_from_file(os.path.join('data', 'adjectives.csv'))
adverbs = word_list_from_file(os.path.join('data', 'adverbs.csv'))


@app.route("/")
def hello_world():

    subject_1 = random.choice(nouns)
    subject_2 = random.choice(nouns)
    verb_1 = random.choice(verbs)
    verb_2 = random.choice(verbs)
    pronoun_1 = random.choice(['they', 'I', 'you', 'we'])
    pronoun_2 = random.choice(['he', 'she'])
    conjunction = random.choice(['when', 'while', 'but', 'and', 'or'])
    preposition = random.choice(['a', 'the', 'our', 'their'])
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)

    sentences = [
        f'{preposition.capitalize()} {subject_1} {verb_1}s {conjunction} the {subject_2} {verb_2}s.',
        f'Why does {preposition} {subject_1} {verb_1} {conjunction} the {subject_2} {verb_2}s?',
        f'Can {preposition} {subject_1} {verb_1}?',
        f'Is {verb_1}ing {adjective} when {pronoun_1} {verb_2}?',
        f'Is {verb_1}ing {adjective} when {pronoun_2} {verb_2}s?',
        f'{preposition.capitalize()} {adjective} {subject_1} is {verb_1}ing {conjunction} the {subject_2} {verb_2}s.',
        f'Is it {adjective} to {verb_1}?',
        f'{pronoun_1.capitalize()} {verb_1} {adverb}.'
    ]

    # grammar hacks
    words = random.choice(sentences).split()
    words = [w.replace('sss', 'sses') if w.endswith('sss') else w for w in words]
    words = [w.replace('chs', 'ches') if w.endswith('chs') else w for w in words]
    words = [w.replace('eing', 'ing') if w.endswith('eing') else w for w in words]

    sentence = ' '.join(words)

    return render_template("index.html", sentence=sentence)
