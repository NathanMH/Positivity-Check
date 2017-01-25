####################
# Author: Nathan Mador-House
# Title: PositivityCheck
####################

####################
# Index:
#     1. Imports and Readme
#     2. Functions
#     3. Main
#     4. Testing
####################


###################################################################
# 1. IMPORTS AND README
###################################################################

import math
import string
import os

###################################################################
# 2. CLASSES & FUNCTIONS
###################################################################

# Setup a dictionary with AFINN
AFINN_FILE = os.path.dirname(__file__) + '/resources/AFINN-111.txt'

AFINN = dict(line.split('\t') for line in open(AFINN_FILE))

class text_block:
    def __init__(self, text):
        # Set up variables
        self.text = "".join(l for l in text if l not in string.punctuation)
        self.word_list = self.text.split()
        self.word_total = len(self.word_list)
        self.neg_count = 0
        self.pos_count = 0
        self.neg_total = 0
        self.pos_total = 0
        self.neutral_count = 0
        self.percent_neg = 0
        self.percent_pos = 0
        self.percent_neutral = 0
        self.sentiment = 0

        # Run functions
        self.word_sort()
        self.eval_percentages()
        self.eval_sentiment()

    def word_sort(self):
        word_values = map(lambda word: AFINN.get(word, 0), self.word_list)
        for val in word_values:
            if int(val) < 0:
                self.neg_count += 1
                self.neg_total += int(val)
            elif int(val) > 0:
                self.pos_count += 1
                self.pos_total += int(val)
            else:
                self.neutral_count += 1

    def eval_percentages(self):
        try:
            self.percent_neg = round((self.neg_count / self.word_total) * 100, 2)
            self.percent_pos = round((self.pos_count / self.word_total) * 100, 2)
            self.percent_neutral = round((self.neutral_count / self.word_total) * 100, 2)
        except ZeroDivisionError:
            pass

    def eval_sentiment(self):
        try:
            self.sentiment = round((self.neg_total + self.pos_total) / math.sqrt(self.word_total), 3)
        except ZeroDivisionError:
            pass

    def print_stats(self):
        print("Total words: " + str(self.word_total))
        print("Negative words: " + str(self.neg_count))
        print("Negative sum: " + str(self.neg_total))
        print("Positive words: " + str(self.pos_count))
        print("Positive sum: " + str(self.pos_total))
        print("Percent Negative Words: " + str(self.percent_neg))
        print("Percent Positive Words: " + str(self.percent_pos))
        print("Normalized Sentiments: " + str(self.sentiment))

###################################################################
# 3. MAIN
###################################################################

###################################################################
# 4. TESTING
###################################################################


