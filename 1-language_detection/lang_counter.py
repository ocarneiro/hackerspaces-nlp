# coding: utf-8
import json
f = open('1-language_detection/languages.json')
langs = f.read()
f.close()
l = json.loads(langs)
from collections import Counter
c = Counter(l.values())

e = [f for f in l if l[f] == 'english']

from shutil import copy

for filename in e:
    copy('data/' + filename, 'data-en/')
