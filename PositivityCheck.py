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
####################"""
#######################

###################################################################
###################################################################
# 1. IMPORTS AND README
###################################################################
###################################################################

import math
# Regex for finding idioms
import re

###################################################################
###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################
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
###################################################################
# 3. SETUP WITH FILES
###################################################################
###################################################################

negativeWordsDoc = open("wordList.txt", "r")
idiomListDoc = open("idiomList.txt", "r")
userFile = open("testFile2.txt")

negWords = makeNegativeWordsArray(negativeWordsDoc)
idiomList = makeIdiomArray(idiomListDoc)
userWords = makeUserWordsArray(userFile)

###################################################################
###################################################################
# 4. GENERAL FUNCTIONS
###################################################################
###################################################################

# Go through each negative word and check if it matches any in the user file word list
def getNegativeWordCount(negWordList, userWordsArray):
    negativeWordCount = 0
    for negativeWord in negWords:
        for userWord in userWords:
            if negativeWord == userWord:
                negativeWordCount += 1
    return negativeWordCount

def calcPercentNegWords(negNum, totNum):
    perc = negNum / len(totNum)
    return math.ceil(perc)

def getIdiomCount(idiomArray, userFile):
    idiomCount = 0
    for idiom in idiomArray:
        m = re.match(idiom, userFile.read())
    print(m.groups())


negWordCount = getNegativeWordCount(negWords, userWords)
print("Total words in file: " + str(len(userWords)))
print("Total negative words in file: ", negWordCount)

percentNegative = calcPercentNegWords(negWordCount, userWords)
print("This file is composed of ", percentNegative, "% negative words.")

print()
getIdiomCount(idiomList, userFile)

###################################################################
###################################################################
