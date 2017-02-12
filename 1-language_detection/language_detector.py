# coding: utf-8
from glob import glob  # finds files using wildcard
from pathlib import Path  # reads whole content of file
import langdetector
import json

def detect_file_languages():
    text_files = glob('../data/*.txt')
    languages = {}

    for filename in text_files:
        contents = Path(filename).read_text()
        contents = contents.replace('\n', '. ')
        language = langdetector.detect_language(contents)
        languages[filename.replace('../data/','')] = language

    return languages

if __name__ == '__main__':
    languages = detect_file_languages()
    with open('languages.json', 'w') as f:
        print(json.dumps(languages), file=f)

