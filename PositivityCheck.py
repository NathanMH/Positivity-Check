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

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

# Get file from the user - for future builds
def getFilenameFromUser():
    userFile = input("Which file would you like to analyze?: ")
    return userFile

def getContentFromRSS():
    ArticlePositivity.getLinks(ArticlePositivity.sources)
    content = ArticlePositivity.getArticleContent(ArticlePositivity.links[1])
    return content

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

# Make an array of words out of the content provided
def makeContentWordsArray(content):
    contentWordsArray = []

    for word in content.split():
        contentWordsArray.append(word.lower())

    return contentWordsArray

###################################################################
# 3. SETUP WITH FILES
###################################################################

negativeWordsDoc = open("wordList.txt", "r")
idiomListDoc = open("idiomList.txt", "r")

negWords = makeNegativeWordsArray(negativeWordsDoc)
idiomList = makeIdiomArray(idiomListDoc)

content = getContentFromRSS()
contentWords = makeContentWordsArray(content)
contentNegWords = []

###################################################################
# 4. GENERAL FUNCTIONS
###################################################################

# Go through each negative word and check if it matches any in the content word list
def getNegativeWordCount(negWordList, contentWordsArray):
    negativeWordCounter = 0
    for negativeWord in negWords:
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
