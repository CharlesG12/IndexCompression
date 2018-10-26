from nltk.stem import WordNetLemmatizer


def lemmatizing(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word)
