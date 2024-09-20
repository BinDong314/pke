#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/Users/dbin/work/SciSearch/pke')

# this example uses TopicRank
from pke.unsupervised import TopicRank

# create a TopicRank extractor
extractor = TopicRank()

# load the content of the document, here in raw text format
# the input language is set to English (used for the stoplist)
# normalization is set to stemming (computed with Porter's stemming algorithm)
with open('2.txt') as f:
    doc = f.read()
extractor.load_document(
    doc,
    language='en',
    normalization='stemming')

def read_txt_to_dict(filename):
    dictionary = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(', ')
            dictionary[key] = float(value)
    return dictionary

feedback=read_txt_to_dict('feedback.txt')
print(feedback)

extractor.load_user_feedback(feedback)
# select the keyphrase candidates, for TopicRank the longest sequences of 
# nouns and adjectives
extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ'})

# weight the candidates using a random walk. The threshold parameter sets the
# minimum similarity for clustering, and the method parameter defines the 
# linkage method
extractor.candidate_weighting(threshold=0.74,
                              method='average')

# print the n-highest (10) scored candidates
for (keyphrase, score) in extractor.get_n_best(n=10, stemming=True):
    print(keyphrase, score)


print("\n\n")
# this example uses TopicRank
from pke.unsupervised import YAKE

# create a TopicRank extractor
yake_extractor = YAKE()
yake_extractor.load_document(doc, language='en', normalization='stemming')
yake_extractor.load_user_feedback(feedback)
yake_extractor.candidate_selection()
yake_extractor.candidate_weighting()

# print the n-highest (10) scored candidates
for (keyphrase, score) in yake_extractor.get_n_best(n=10, stemming=True):
    print(keyphrase, score)