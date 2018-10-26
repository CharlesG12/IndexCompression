import os
import Token
from xml.dom import minidom


class ProcessDoc:
    def __init__(self, path, lemma, stem):
        self.collection_dic = {}
        self.doc_info = []
        self.lemma = lemma
        self.stem = stem
        self.path = path

    def run(self):
        for filename in os.listdir(self.path):
            token = self.load_file(os.path.join(self.path, filename))

            if self.lemma == 1:
                token.apply_lemma()
            elif self.stem == 1:
                token.apply_stemming()

            doc_dic = token.tokenize()

            for key, value in doc_dic.items():

                # add token to dictionary if not exist
                if key not in self.collection_dic:
                    self.collection_dic[key] = [value]
                # increase the frequency by one if exist in the dictionary
                else:
                    self.collection_dic[key].append(value)

    def load_file(self, url):
        doc_dic = []

        # parse xml doc from the url
        mydoc = minidom.parse(url)

        # read doc NO
        doc = mydoc.getElementsByTagName('DOCNO')[0]
        doc_no = int(doc.firstChild.data)

        # read doc text file
        text = mydoc.getElementsByTagName('TEXT')[0]
        data = text.firstChild.data

        return Token.Token(data, doc_no)


