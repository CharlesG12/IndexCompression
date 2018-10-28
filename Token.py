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
                # add new key to dictionary
                if self.applyLemma == 1:
                    processed_word = Lemmatizer.lemmatizing(processed_word)
                if processed_word not in book_dict:
                    book_dict[processed_word] = 1
                # increment value by 1 if key exist
                else:
                    book_dict[processed_word] += 1
            max_tf = self.add_doc_info(book_dict)
        return doc_no, doclen, max_tf, book_dict

    # return max_tf value, and list of term
    def add_doc_info(self, dictionary):
        max_value = 1
        max_tf = [max_value]
        for key, value in dictionary.items():
            if value == max_value:
                max_tf.append(key)
            elif value > max_value:
                max_value = value
                max_tf = [value, key]
        return max_value

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

