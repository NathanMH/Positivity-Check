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

# Setup a dictionary with AFINN
afinn_file = 'AFINN-111.txt'
afinn = {}
with open(afinn_file) as f:
    for line in f:
        new_string = " ".join(line.split())
        #print(new_string)
        (w, s, *rest) = new_string.split()
        afinn[w] = s

###################################################################
# 2. FUNCTIONS
###################################################################

# Make a word list from text
def get_word_list(text):
    words = text.split()
    return words
    
def word_sort(word_list):
    neg_counter = 0
    pos_counter = 0 
    neg_total = 0
    pos_total = 0
    neutral_counter = 0

    word_values = map(lambda word: afinn.get(word, 0) , word_list)
    for val in word_values:
        if int(val) < 0:
            neg_counter += 1
            neg_total += int(val)
        elif int(val) > 0:
            pos_counter += 1
            pos_total += int(val)
        else:
            neutral_counter += 1
    print("There are " + str(neg_counter) + " negative words in the text.")
    print("There are " + str(pos_counter) + " positive words in the text.")
    print("Total negative sentiment is " + str(neg_total))
    print("Total positive sentiment is " + str(pos_total))
    print("There are also " + str(neutral_counter) + " neutral words in the text.")
    return neg_counter, pos_counter, neg_total, pos_total

###################################################################
# 3. MAIN
###################################################################

###################################################################
# 4. TESTING
###################################################################

#counter = 0
#for w, s, *rest in afinn.items():
#    if counter <= 20:
#        print(w + " : " + afinn[w])
#        counter += 1


test_list = ["bad", "good", "help", "hinder", "hate", "destroy", "remorse", "deny", "love"]
word_sort(test_list)
