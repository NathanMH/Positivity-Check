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

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

# Get filee from the user
def getFilenameFromUser():
    userFile = input("Which file would you like to analyze?: ")
    return userFile

# Make the array of negative words
def makeNegativeWordsArray(negWordList):
    negativeWordsArray = []
    for word in negWordList:
        negativeWordsArray.append(word.rstrip('\n'))
    return negativeWordsArray

def makeIdiomArray(idiomList):
    idiomArray = []
    for line in idiomList:
        idiomArray.append(line.rstrip('\n'))
    return idiomArray

# Make an array of words out of the user provided file
def makeUserWordsArray(usrFile):
    userWordsArray = []
    for lines in open(usrFile, 'r'):
        for word in lines.split(" "):
            userWordsArray.append(word.lower())
    return userWordsArray

###################################################################
# 3. SETUP WITH FILES
###################################################################

negativeWordsDoc = open("wordList.txt", "r")
idiomListDoc = open("idiomList.txt", "r")
userFilename = getFilenameFromUser()

negWords = makeNegativeWordsArray(negativeWordsDoc)
idiomList = makeIdiomArray(idiomListDoc)
userWords = makeUserWordsArray(userFilename)
userNegWords = []

###################################################################
# 4. GENERAL FUNCTIONS
###################################################################


# Go through each negative word and check if it matches any in the user file word list
def getNegativeWordCount(negWordList, userWordsArray):
    negativeWordCounter = 0
    for negativeWord in negWords:
        for userWord in userWords:
            if negativeWord == userWord:
                negativeWordCounter += 1
                userNegWords.append(negativeWord)
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
        for word in userNegWords:
            print(word)
    else:
        print("Goodbye!")

###################################################################
# 5. MAIN
###################################################################

# Individual words
negWordCount = getNegativeWordCount(negWords, userWords)
percentNegative = calcPercentNegWords(negWordCount, userWords)

# Idioms
sentenceNumber = getSentenceCount(userFilename)
idiomCount = getIdiomCount(idiomList, userFilename)
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
showNegWords()
print()
