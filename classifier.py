import random
import nltk
from nltk.corpus import webtext

with open("input.txt", "r") as fh:
    input_document = fh.read()

all_words = nltk.FreqDist(w.lower() for w in webtext.words())
word_features = list(all_words)[:2500]
