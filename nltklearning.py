#! /usr/bin/python

import nltk

sentence = "AD Services provide services that range from vocational / developmental skills training, social and recreational activities, home-based care to residential care services for persons with disabilities."

tokens = nltk.word_tokenize(sentence)

print(tokens)
