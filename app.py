import csv
import os
import random

from flask import Flask
from flask import render_template

app = Flask(__name__)

with open(os.path.join('data', 'nouns.csv'), newline='') as f:
    reader = csv.reader(f)
    nouns = [n[0] for n in list(reader)]

with open(os.path.join('data', 'verbs.csv'), newline='') as f:
    reader = csv.reader(f)
    verbs = [v[0] for v in list(reader)]


@app.route("/")
def hello_world():

    subject_1 = random.choice(nouns)
    subject_2 = random.choice(nouns)
    verb_1 = random.choice(verbs)
    verb_2 = random.choice(verbs)

    s = f'The {subject_1} {verb_1}s and the {subject_2} {verb_2}s.'
    return s
    return render_template("index.html")
