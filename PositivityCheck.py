"""####################
Author: Nathan Mador-House
Title: PositivityCheck
####################"""

negativeWordsDoc = open("wordList.txt", "r")
negativeWordsArray = []
userWordsArray = []
negativeWordCount = 0

# User file actually from the user... Commented for testing
# userFile = open(input("Which file would you like to analyze?: "))

# Make the array of negative words
for word in negativeWordsDoc:
    negativeWordsArray.append(word.rstrip('\n'))


# Make an array of words out of the user provided file
userFile = open("testFile.txt")
for lines in userFile:
    for word in lines.split(" "):
        userWordsArray.append(word.lower())


# Go through each negative word and check if it matches any in the user file word list
for negativeWord in negativeWordsArray:
    for userWord in userWordsArray:
        if negativeWord == userWord:
            negativeWordCount += 1
            print(negativeWord)


print(negativeWordCount)
