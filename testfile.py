import os
import glob
import spacy as spacy
import gensim


import time

class MySentences(object):


    def __init__(self, dirname):
        self.dirname = dirname

    # make sure to go through ALL the directories
    # i.e. how to recursively get files from every directory
    # an iterative solution can also work here: go into every directory


    def getSize(self):
        count = 1647305 # as of June 27
        # for filename in glob.iglob(os.path.join(self.dirname, "**", "*.txt"), recursive=True):
        #     count+=1
        return count

    def __iter__(self):
        count = 0
        t0 = time.time()
        for filename in glob.iglob(os.path.join(self.dirname, "**", "*.txt"), recursive=True):
            with open(filename) as file:
                for line in file:
                    yield gensim.utils.simple_preprocess(line)

            if count %1000 == 0:

                t1 = time.time()
                print ("done %d docs" % count)
                print ("took %s time" % (t1 - t0))
                t0 = time.time()

            count+=1

            # print(filename)


        # for fname in os.listdir(self.dirname):
        #     for line in open(os.path.join(self.dirname, fname)):
        #         yield line.split()

def train_vectors():
    sentences = MySentences("../pubmed_data/unzipped/")

    print("size was %d" % sentences.getSize())

    model = gensim.models.Word2Vec(sentences, size=300, workers=8)
    model.save('./tmp/draft_model')
    return model
    # print(model.wv.index2word[0], model.wv.index2word[1], model.wv.index2word[2])
    # print (model.wv['the'])


def load_vectors():
    return gensim.models.Word2Vec.load("./tmp/draft_model")


if __name__ == "__main__":

    t0 = time.time()
    model = load_vectors()
    print("took %s time to load" % (time.time()-t0))
    similar_dict = model.most_similar("diabetes", topn=100)
    print(similar_dict)

    with open("topn_nicely.txt") as file:
        for key in similar_dict:
            file.write(key + "\n")
            # print key


    # model.train()

