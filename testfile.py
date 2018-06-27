import os
import glob
import spacy as spacy
import gensim




class MySentences(object):


    def __init__(self, dirname):
        self.dirname = dirname

    # make sure to go through ALL the directories
    # i.e. how to recursively get files from every directory
    # an iterative solution can also work here: go into every directory



    def __iter__(self):
        count = 0
        for filename in glob.iglob(os.path.join(self.dirname, "**", "*.txt"), recursive=True):

            with open(filename) as file:
                for line in file:
                    yield gensim.utils.simple_preprocess(line)

            if count %1000 == 0:
                print ("done %d docs" % count)

            count+=1

            # print(filename)


        # for fname in os.listdir(self.dirname):
        #     for line in open(os.path.join(self.dirname, fname)):
        #         yield line.split()

if __name__ == "__main__":


    sentences = MySentences("../pubmed_data/unzipped/")

    model = gensim.models.Word2Vec(sentences, size=300, workers=16)
    print(model.wv.index2word[0], model.wv.index2word[1], model.wv.index2word[2])
    print (model.wv['the'])
    # model.train()

    model.save('./tmp/draft_model')