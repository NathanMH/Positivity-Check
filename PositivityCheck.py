"""####################
Author: Nathan Mador-House
Title: PositivityCheck
####################"""

"""####################
Index:
    1. Imports and Readme
    2. Functions
    3. Main
    4. Testing
####################"""


###################################################################
# 1. IMPORTS AND README
###################################################################

import math
import string

###################################################################
# 2. CLASSES & FUNCTIONS
###################################################################

# Setup a dictionary with AFINN
afinn_file = 'resources/AFINN-111.txt'
afinn = {}
with open(afinn_file) as f:
    for line in f:
        new_string = " ".join(line.split())
        # *rest is incase there are more than two arguments per line
        (w, s, *rest) = new_string.split()
        afinn[w] = s


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
        word_values = map(lambda word: afinn.get(word, 0), self.word_list)
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
        self.percent_neg = round((self.neg_count / self.word_total) * 100, 2)
        self.percent_pos = round((self.pos_count / self.word_total) * 100, 2)
        self.percent_neutral = round((self.neutral_count / self.word_total) * 100, 2)

    def eval_sentiment(self):
        self.sentiment = round((self.neg_total + self.pos_total) / math.sqrt(self.word_total), 3)

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

# test_text = "Hello this is some sample text. It has some positive text as well as negative. This is to test if the program fucking works. It has a lot of great words like; love, adore, best, beautiful."
# test_obj = text_block(test_text)
# test_obj.print_stats()


