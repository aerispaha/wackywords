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

#
# with open(os.path.join('data', 'verbs.csv'), newline='') as f:
#     reader = csv.reader(f)
#     verbs = [v[0] for v in list(reader)]
#
# with open(os.path.join('data', 'adjectives.csv'), newline='') as f:
#     reader = csv.reader(f)
#     verbs = [v[0] for v in list(reader)]


@app.route("/")
def hello_world():

    subject_1 = random.choice(nouns)
    subject_2 = random.choice(nouns)
    verb_1 = random.choice(verbs)
    verb_2 = random.choice(verbs)
    pronoun_1 = random.choice(['they', 'I', 'you', 'we'])
    pronoun_2 = random.choice(['he', 'she'])

    sentences = [
        f'The {subject_1} {verb_1}s and the {subject_2} {verb_2}s.',
        f'Why does the {subject_1} {verb_1} while the {subject_2} {verb_2}s?',
        f'Can a {subject_1} {verb_1}?',
        f'Is {verb_1}ing possible when {pronoun_1} {verb_2}?',
        f'Is {verb_1}ing possible when {pronoun_2} {verb_2}s?',
        f'A {random.choice(adjectives)} {subject_1} is {verb_1}ing when the {subject_2} {verb_2}s.',
        f'Is it {random.choice(adjectives)} to {verb_1}?'
    ]

    return render_template("index.html", sentence=random.choice(sentences))
