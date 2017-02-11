# coding: utf-8
from glob import glob  # finds files using wildcard
from pathlib import Path  # reads whole content of file
from nltk.tokenize import sent_tokenize

text_files = glob('data/*.txt')
term_searched = 'arduino'
sents_found = {}

for filename in text_files:
    contents = Path(filename).read_text()
    contents = contents.replace('\n', '. ')
    sents = sent_tokenize(contents)
    sents_with_term = [a for a in sents if term_searched in a.lower()]
    if len(sents_with_term) > 0:
        sents_found[filename.replace('data/','')] = sents_with_term
