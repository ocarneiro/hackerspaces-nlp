# coding: utf-8
from glob import glob  # finds files using wildcard
from pathlib import Path  # reads whole content of file
from nltk.tokenize import sent_tokenize
import sys
from pprint import pprint  # for use in the console

def find_term(term_searched = 'arduino'):
    text_files = glob('data/*.txt')
    sents_found = {}
    
    for filename in text_files:
        contents = Path(filename).read_text()
        contents = contents.replace('\n', '. ')
        sents = sent_tokenize(contents)
        sents_with_term = [a for a in sents if term_searched in a.lower()]
        if len(sents_with_term) > 0:
            sents_found[filename.replace('data/','')] = sents_with_term

    return sents_found

def find_two_terms(term1, term2):
    list1 = find_term(term1)
    list2 = find_term(term2)
    contains_both = [x for x in list1 if x in list2]
    details = {}
    for h in contains_both:
        details[h] = {}
        details[h][term1] = list1[h]
        details[h][term2] = list2[h]
        for b in details[h][term1]:
            if b in details[h][term2]:
                details[h]['**both**'] = b

    return details


if __name__ == '__main__':
    if len(sys.argv) == 2:
        s = find_term(sys.argv[1])
    elif len(sys.argv) == 3:
        b = find_two_terms(sys.argv[1], sys.argv[2])
