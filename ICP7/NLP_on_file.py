# import libraries

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import word_tokenize, pos_tag, ne_chunk

# read the input.text file created in previous questions
def read_file():
    sentence = open('input.txt', encoding="utf8").read()
    return sentence

def tokenization(sent):
    print("************************************ ")
    print("*********TOKENIZATION************ ")
    print("************************************ ")
# Tokenization: breaking a stream of text into tokens.
    stokens = nltk.sent_tokenize(sentence)
    wtokens = nltk.word_tokenize(sentence)

    stoken_count = 0
    for s in stokens:
        stoken_count += 1
        if stoken_count < 6:
            print("+++sent_token+++:", s)

    wtoken_count = 0
    for w in wtokens:
        wtoken_count += 1
        if wtoken_count < 6:
            print("token word:", w)

    return stokens, wtokens


def stemming(wtokens):
    print("************************************ ")
    print("*********STEMMING************ ")
    print("************************************ ")

    p_stemmer = PorterStemmer()
    l_stemmer = LancasterStemmer()
    s_stemmer = SnowballStemmer('english')

    wtoken_count = 0
    for w in wtokens:
        wtoken_count += 1
        if wtoken_count < 6:
            print(p_stemmer.stem(w), l_stemmer.stem(w), s_stemmer.stem(w))


def lemmatization(wtokens):
    print("************************************ ")
    print("*********LEMMATIZATION************ ")
    print("************************************ ")

    lemmatizer = WordNetLemmatizer()

    wtoken_count = 0
    for w in wtokens:
        wtoken_count += 1
        if wtoken_count < 6:
          print("Lemmatizer:", lemmatizer.lemmatize(w), ",    With POS=a:",
                  lemmatizer.lemmatize(w, pos="a"))


def trigram(sentence, stokens):
    print("************************************ ")
    print("*********TRIGRAM************ ")
    print("************************************ ")

    stoken_count = 0
    for s in stokens:
        stoken_count += 1
        if stoken_count < 2:
            token = nltk.word_tokenize(s)
            bigrams = list(ngrams(token, 2))
            trigrams = list(ngrams(token, 3))
            print("The TRIGRAM:", sentence[:100], "\nword_tokenize:", token, "\nbigrams:", bigrams, "\ntrigrams", trigrams)

# by categories
def ner(stokens):
    print("************************************ ")
    print("*********NAMED ENTITY RECOGNITION************ ")
    print("************************************ ")

    stoken_count = 0
    for s in stokens:
        stoken_count += 1
        if stoken_count < 3:
            print(ne_chunk(pos_tag(word_tokenize(s))))


if __name__ == '__main__':
    sentence = read_file()
    stokens, wtokens = tokenization(sentence)
    stemming(wtokens)
    lemmatization(wtokens)
    trigram(sentence, stokens)
    ner(stokens)