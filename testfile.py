import os
import glob
import spacy as spacy
import gensim


if __name__ == "__main__":

    print("hello world")
    print("ok, it is working, sort of")
    # nlp = spacy.load('en_core_web_md')
    # hardcoded for now



    # exit()


    for filename in os.listdir("../pubmed_data/unzipped/AAPS_J"):
        with open(os.path.join("../pubmed_data/unzipped/AAPS_J", filename)) as file:
            print(filename)
            text = file.read()

            # we should try doing things with gensim simple preprocess

            tokens = gensim.utils.simple_preprocess(text)


            print(len(text))
            print(tokens)

        break

        model = gensim.models.Word2Vec()
        sentences = MySentences("./pubmed_data/unzipped/")

        model.train()



class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    # make sure to go through ALL the directories
    # i.e. how to recursively get files from every directory
    # an iterative solution can also work here: go into every directory
    def __iter__(self):

        for filename in glob.iglob('../pubmed_data/**/*.txt', recursive=True):
            with open(os.path.join("../pubmed_data/unzipped/AAPS_J", filename)) as file:
                for line in file:
                    yield gensim.utils.simple_preprocess(line)

            print(filename)


        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()