# coding: utf-8
from glob import glob  # finds files using wildcard
from pathlib import Path  # reads whole content of file
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
import re

def word_filter(raw_list):
    stopwords_set = set(stopwords.words('english'))
    # removes stopwords from nltk
    filtered = [w for w in raw_list if w.lower() not in stopwords_set]
    # removes numbers (words without alphanumeric characters)
    filtered = [w for w in filtered if re.match('.*[a-zA-Z]+.*', w)]

    return filtered

def extract_words():
    text_files = glob('../data-en/*.txt')
    words = []

    for filename in text_files:
        contents = Path(filename).read_text()
        contents = contents.replace('\n', '. ')
        tokenizer = RegexpTokenizer(r'\w+')
        extracted_words = tokenizer.tokenize(contents)
        clean_words = word_filter(extracted_words)
        words.extend(clean_words)

    return words

if __name__ == '__main__':
    words = extract_words()
    c = Counter(words)
