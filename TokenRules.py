import re


# apply token rules on word
def apply(word):
    # remove possessives
    np_word = remove_possessive(word)
    # remove mark
    clean_word = remove_mark(np_word)
    # remove digits
    clean_word = remove_digits(clean_word)
    if is_short(clean_word) == 1:
        return 0
    return clean_word.lower()


# remove marks ['.', '?', '!', ',', '-']
def remove_mark(word):
    marks = ['.', '?', '!', ',', '-']
    for m in marks:
        word = word.replace(m, '')
    return word


# remove digits
def remove_digits(word):
    return re.sub("[^a-zA-Z]", "", word)


# remove words that are too short
def is_short(word):
    if len(word) <= 1:
        return 1
    return 0


# remove Possessives
# example: university's -> university
def remove_possessive(word):
    if word[-2:] is "'s":
        print(word[-2:])
        return word[:-2]
    return word
