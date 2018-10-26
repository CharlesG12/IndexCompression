import TokenRules
import Stemmer
import Lemmatizer


class Token:
    def __init__(self, data, doc_no):
        # the frequency of the most frequent term or stem in the document
        self.max_tf = []
        # the total number of word occurrences in the document
        self.docLen = []
        self.applyStemming = 0
        self.applyLemma = 0
        self.data = data
        self.doc_no = doc_no

    def apply_stemming(self):
        self.applyStemming = 1

    def no_stemming(self):
        self.applyStemming = 0

    def apply_lemma(self):
        self.applyLemma = 1

    def no_lemma(self):
        self.applyLemma = 0

    def tokenize(self):
        # create token dictionary for the book
        book_dict = {}

        # split the data string by space
        words = self.data.split()
        for w in words:
            # return processed word, 0 is not qualified
            processed_word = TokenRules.apply(w)
            # filter empty word after tokenization
            if processed_word != 0:
                # apply stemming
                if self.applyStemming == 1:
                    processed_word = Stemmer.stemming(processed_word)
                # apply lemmatization
                if self.applyLemma == 1:
                    processed_word = Lemmatizer.lemmatizing(processed_word)
                # add new key to dictionary
                if processed_word not in book_dict:
                    book_dict[processed_word] = [self.doc_no, 1]
                # increment value by 1 if key exist
                else:
                    book_dict[processed_word] = [self.doc_no, book_dict[processed_word][1] + 1]
        return book_dict

