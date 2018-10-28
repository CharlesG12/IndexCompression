import TokenRules
import Stemmer
import Lemmatizer
import operator

# return a dictionary
# {term: [doc_no, tf]}
# @param data
# string need to be processed
# @doc_no
# document number


class Token:
    def __init__(self):
        # the frequency of the most frequent term or stem in the document
        self.max_tf = []
        # the total number of word occurrences in the document
        self.docLen = []
        self.applyStemming = 0
        self.applyLemma = 0
        self.build_stop_word_dic()

    def apply_stemming(self):
        self.applyStemming = 1

    def build_stop_word_dic(self):
        TokenRules.construct_stop_word_dict()

    def no_stemming(self):
        self.applyStemming = 0

    def apply_lemma(self):
        self.applyLemma = 1

    def no_lemma(self):
        self.applyLemma = 0

    # return a dictionary of the document
    # [term: [doc_no, tf]]
    def tokenize(self, data, doc_no):
        # create token dictionary for the book
        book_dict = {}

        # split the data string by space
        words = data.split()
        doclen = len(words)
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
                    book_dict[processed_word] = [doc_no, 1, doclen]
                # increment value by 1 if key exist
                else:
                    book_dict[processed_word] = [doc_no, book_dict[processed_word][1] + 1, doclen]

        return book_dict

    # def add_doc_info(self, dictionary):
    #     # max_entry structure: [df, [doc_no, tf, doclen]], "term"]
    #     max_entry = max(zip(dictionary.values(), dictionary.keys()))
    #     max_value = max_entry[0][1][1]
    #     maxtf = [max_value, max_entry[1]]
    #
    #     for key, value in dictionary:
    #         if value[1][1] == max_value:
    #             maxtf.append(key)
    #     for key, value in dictionary:



    # return a list of processed word
    # [doc_no, term1, term2 ...]
    def token_list_stemming(self, words):
        final_words = []
        for w in words:
            # return processed word, 0 is not qualified
            processed_word = TokenRules.apply(w)
            # filter empty word after tokenization
            if processed_word != 0:
                # apply stemming
                processed_word = Stemmer.stemming(processed_word)
                final_words.append(processed_word)
        return final_words

    # return a list of processed word
    # [doc_no, term1, term2 ...]
    def token_list_lemma(self, words):
        final_words = []
        for w in words:
            # return processed word, 0 is not qualified
            processed_word = TokenRules.apply(w)
            # filter empty word after tokenization
            if processed_word != 0:
                # apply stemming
                processed_word = Lemmatizer.lemmatizing(processed_word)
                final_words.append(processed_word)
        return final_words

