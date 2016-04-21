"""####################
Author: Nathan Mador-House
Title: PositivityCheck
####################"""

#######################
"""####################
Index:
    1. Imports and Readme
    2. Initialization Functions 
    3. Setup using supplied files and content input
    4. General Functions
    5. Main
    6. Testing
####################"""
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

import math
import ArticlePositivity
import checkr

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

# Get file from the user - for future builds
def return_filename():
    userFile = input("Which file would you like to analyze?: ")
    return userFile

# Make an array of words out of the content provided
def content_words_array(content):
    content_words_array = []
    for word in content.split():
        content_words_array.append(word.lower())
    return contentWordsArray

###################################################################
# 3. SETUP WITH FILES
###################################################################

###################################################################
# 4. GENERAL FUNCTIONS
###################################################################

# Go through each negative word and check if it matches any in the content word list
def negative_word_count(afinn_list, content_words):
    counter = 0
    for word in :
        for contentWord in contentWords:
            if negativeWord == contentWord:
                negativeWordCounter += 1
                contentNegWords.append(negativeWord)
    return negativeWordCounter

def calcPercentNegWords(negNum, totNum):
    perc = negNum / len(totNum)
    return math.ceil(perc)

def getSentenceCount(doc):
    periods = open(doc).read().count(".")
    exclamPoints = open(doc).read().count("!")
    questMarks = open(doc).read().count("?")
    sentenceCounter = periods + exclamPoints + questMarks
    return sentenceCounter

def getIdiomCount(idiomArray, doc):
    idiomCounter = 0
    for idiom in idiomArray:
        if idiom in open(doc).read():
            idiomCounter += 1
    return idiomCounter

def calcPercentIdioms(idioms, totSentences):
    perc = idioms / totSentences
    return math.ceil(perc)

def showNegWords():
    q = input("Would you like to see the negative words in this text?").lower()
    if q == "yes" or q == "y":
        for word in contentNegWords:
            print(word)
    else:
        print("Goodbye!")

###################################################################
# 5. MAIN
###################################################################

# Individual words
negWordCount = getNegativeWordCount(negWords, contentWords)
percentNegative = calcPercentNegWords(negWordCount, contentWords)

# Idioms
# sentenceNumber = getSentenceCount(content)
# idiomCount = getIdiomCount(idiomList, content)
# percentIdiom = calcPercentIdioms(idiomCount, sentenceNumber)

###################################################################
# 6. TESTING
###################################################################

print()

print("Total words in file: " + str(len(contentWords)))
print("Total negative words in file: ", negWordCount)
print("This file is composed of ", percentNegative, "% negative words.")

print("Total sentences in file:", sentenceNumber)
print("Total idioms used:", idiomCount)
print("This file is composed of ", percentIdiom, "% idioms")

print()
showNegWords()
print()
