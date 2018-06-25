import os

import spacy as spacy

print("hello world")
print("ok, it is working, sort of")
nlp = spacy.load('en_core_web_md')
# hardcoded for now
for filename in os.listdir("./pubmed_data/unzipped/AAPS_J"):
    with open(os.path.join("./pubmed_data/unzipped/AAPS_J", filename)) as file:
        print(filename)
        text = file.read()
        print(len(text))

        doc = nlp(text)
        for sent in doc.sents:

            print(sent)
        # print(file.readlines())
    break

