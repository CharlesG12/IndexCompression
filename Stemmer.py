from nltk.stem import PorterStemmer

ps = PorterStemmer()


def stemming(word):
    return ps.stem(word)


