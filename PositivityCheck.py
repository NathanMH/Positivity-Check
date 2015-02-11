"""####################
Author: Nathan Mador-House
Title: PositivityCheck
####################"""

doc = open("wordList.txt", "r")
words = []
instances = []

for line in doc:
    words.append(line)

userFile = open(input("Which file would you like to analyze?: "))

