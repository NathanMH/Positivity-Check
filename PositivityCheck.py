"""####################
Author: Nathan Mador-House
Title: PositivityCheck
####################"""

#######################
"""####################
Index:
1. Imports and Readme
2. Initialization Functions 
3. Setup using supplied files and user input
4. General Functions
5. Main
6. Testing
####################"""
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

import math
# Get regex for finding idioms
import re

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

# Get file from the user // NOT IN USE YET, DELETE THIS WHEN USED
def getFileFromUser():
    userFile = open(input("Which file would you like to analyze?: "))
    return userFile

# Make the array of negative words
def makeNegativeWordsArray(list):
    negativeWordsArray = []
    for word in list:
        negativeWordsArray.append(word.rstrip('\n'))
    return negativeWordsArray

def makeIdiomArray(list):
    idiomArray = []
    for line in list:
        idiomArray.append(line.rstrip('\n'))
    return idiomArray

# Make an array of words out of the user provided file
def makeUserWordsArray(file):
    userWordsArray = []
    for lines in file:
        for word in lines.split(" "):
            userWordsArray.append(word.lower())
    return userWordsArray

###################################################################
# 3. SETUP WITH FILES
###################################################################

negativeWordsDoc = open("wordList.txt", "r")
idiomListDoc = open("idiomList.txt", "r")
userFile = "testFile2.txt"

negWords = makeNegativeWordsArray(negativeWordsDoc)
idiomList = makeIdiomArray(idiomListDoc)
userWords = makeUserWordsArray(userFile)

###################################################################
# 4. GENERAL FUNCTIONS
###################################################################

# Get text source from user
def getTextSource():
    userInput = raw_input("What file would you like to analyze?: ")
    return userInput

# Go through each negative word and check if it matches any in the user file word list
def getNegativeWordCount(negWordList, userWordsArray):
    negativeWordCounter = 0
    for negativeWord in negWords:
        for userWord in userWords:
            if negativeWord == userWord:
                negativeWordCounter += 1
    return negativeWordCounter

def calcPercentNegWords(negNum, totNum):
    perc = negNum / len(totNum)
    return math.ceil(perc)

def getSentenceCount(doc):
    sentenceCounter = open(doc).read().count(".")
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

###################################################################
# 5. MAIN
###################################################################

# Individual words
negWordCount = getNegativeWordCount(negWords, userWords)
percentNegative = calcPercentNegWords(negWordCount, userWords)

# Idioms
sentenceNumber = getSentenceCount(userFile)
idiomCount = getIdiomCount(idiomList, userFile)
percentIdiom = calcPercentIdioms(idiomCount, sentenceNumber)

###################################################################
# 6. TESTING
###################################################################

print()

print("Total words in file: " + str(len(userWords)))
print("Total negative words in file: ", negWordCount)
print("This file is composed of ", percentNegative, "% negative words.")

print("Total sentences in file:", sentenceNumber)
print("Total idioms used:", idiomCount)
print("This file is composed of ", percentIdiom, "% idioms")

print()
