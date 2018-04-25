####################
# Author: Nathan Mador-House
####################

#######################
# Index:
# 1. Imports and Readme
# 2. Functions
# 3. Main
# 4. Testing
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

# Use csv file of tv/movie scripts for sentiment analysis

import csv
import operator
import os
import re

from positive_graph import make_characters_graph
from positive_graph import make_seasons_graph
from positive_graph import make_episodes_graph
from positivity_check import UserText

###################################################################
# 2. FUNCTIONS
###################################################################

main_characters = ["Michael", "Jim", "Pam", "Dwight", "Ryan", "Andy", "Robert"]
recurring_characters = ["Jan", "Roy", "Stanley", "Kevin", "Meredith", "Angela", "Oscar", "Phyllis", "Kelly", "Toby", "Creed", "Gabe", "Holly", "Nellie", "Clark", "Pete", "Erin"]
other_characters = ["Todd", "David", "Karen", "Charles", "Jo", "Deangelo", "Val", "Cathy"]

characters = {}
seasons = {}
episodes = {}
scenes = {}

class Show:
    def __init__(self):
        self.total_text = ""

    def add_text(self, line):
        self.total_text += line + " "

    def print_stats(self):
        print(self.total_text)

class Character:
    def __init__(self, name):
        self.name = name
        self.total_text = ""
        self.seasons = {}
        self.episodes = {}

    def add_text(self, season, episode, line):
        self.total_text += line + " "
        if season in self.seasons:
            self.seasons[season].add_text(line)
        else:
            self.seasons[season] = Season(season)
            self.seasons[season].add_text(line)
        if episode in self.episodes:
            self.episodes[episode].total_text += line
        else:
            self.episodes[episode] = Episode(episode)
            self.episodes[episode].add_text(line)
 
class Season(Show):
    def __init__(self, season):
        self.season = season
        self.total_text = ""

class Episode(Show):
    def __init__(self, episode):
        self.episode = episode
        self.total_text = ""

class Scene(Show):
    def __init__(self, scene):
        self.scene = scene
        self.total_text = ""

def load_csv(loc):
    # Load csv and add one item to each dictionary so it's not empty
    with open(loc) as csvfile:
        csvfile.readline()
        reader = csv.reader(csvfile, delimiter=',')

        # Setup dictionaries with first row (excluding the column names)
        row1 = next(reader)
        line = remove_stage_directions_and_punctuation(row1[4])
        character = row1[5]
        season = row1[1]
        epi_season = str(row1[1] + format(int(row1[2]), '02d'))

        # Init dictionaries
        characters[character] = Character(character)
        characters[character].add_text(season, epi_season, line)
        seasons[season] = Season(season)
        seasons[season].add_text(line)
        episodes[epi_season] = Episode(epi_season)
        episodes[epi_season].add_text(line)

        analyze_csv(reader)

def analyze_csv(reader):
    for row in reader:
        character = row[5]
        season = row[1]
        # epi_season = str(row[1]) + str(row[2])
        epi_season = str(row[1] + format(int(row[2]), '02d'))
        line = remove_stage_directions_and_punctuation(row[4])

        # Characters
        if character in characters:
            characters[character].total_text += " " + line
            if season in characters[character].seasons:
                characters[character].seasons[season].add_text(line)
            else:
                characters[character].seasons[season] = Season(season)
                characters[character].seasons[season].add_text(line)
            if epi_season in characters[character].episodes:
                characters[character].episodes[epi_season].add_text(line)
            else:
                characters[character].episodes[epi_season] = Episode(epi_season)
                characters[character].episodes[epi_season].add_text(line)
        else:
            characters[character] = Character(character)
            characters[character].add_text(season, epi_season, line)

        # Season
        if season in seasons:
            seasons[season].add_text(line)
        else:
            seasons[season] = Season(season)
            seasons[season].add_text(line)
 
        # Episode
        if epi_season in episodes:
            episodes[epi_season].add_text(line)
        else:
            episodes[epi_season] = Episode(epi_season)
            episodes[epi_season].add_text(line)
            
        # Scene - TODO

def remove_stage_directions_and_punctuation(text):
    without_directions = re.sub("[\(\[].*?[\)\]]", "", text)
    result = re.sub('[^A-Za-z0-9 ]+', '', without_directions)
    return result

def graph_seasons():
    seasons_analysis = {}
    for s in seasons:
        sentiment = UserText(seasons[s].total_text)
        seasons_analysis[seasons[s].season] = sentiment
    make_seasons_graph(seasons_analysis)

def graph_episodes():
    episodes_analysis = {}
    for e in episodes:
        sentiment = UserText(episodes[e].total_text)
        episodes_analysis[episodes[e]] = sentiment
    make_episodes_graph(episodes_analysis)

def graph_characters():
    characters_analysis = {}
    main_characters = ["Michael", "Jim", "Pam", "Dwight", "Ryan", "Andy", "Robert"]
    recurring_characters = ["Jan", "Roy", "Stanley", "Kevin", "Meredith", "Angela", "Oscar", "Phyllis", "Kelly", "Toby", "Creed", "Gabe", "Holly", "Nellie", "Clark", "Pete", "Erin"]
    other_characters = ["Todd", "David", "Karen", "Charles", "Jo", "Deangelo", "Val", "Cathy"]

    for c in main_characters:
        sentiment = UserText(characters[c].total_text)
        characters_analysis[characters[c].name] = sentiment
    make_characters_graph(characters_analysis)


###################################################################
# 3. MAIN
###################################################################

if __name__ == "__main__":

    text = input("Test or Real: ").lower()
    if text == "real" or text == "r":
        office_file = os.getcwd() + "\\positivity_check\\resources\\the-office-lines-scripts.csv"
    else:
        office_file = os.getcwd() + "\\positivity_check\\test\\the-office-lines-scripts-test.csv"
    
    load_csv(office_file)

    graph = input("What variable would you like to graph? Characters, Seasons, or Episodes: ").lower()

    if graph == "characters" or graph == "c":
        graph_characters()
    elif graph == "seasons" or graph == "s":
        graph_seasons()
    elif graph == "episodes" or graph == "e":
        graph_episodes()
    else:
        print("Sorry, didn't catch that.")



    # most_positive = max(sentiments.items(), key=operator.itemgetter(1))[0]
    # most_negative = min(sentiments.items(), key=operator.itemgetter(1))[0]
    # print("Most Positive = " + most_positive + " : " + str(sentiments[most_positive]))
    # print("Most Negative = " + most_negative + " : " + str(sentiments[most_negative]))


    # Episodes
    # for e in episodes:
    #     sentiment = UserText(episodes[e].total_text)
    #     sentiments[episodes[e]] = sentiment.sentiment

    # most_positive = max(sentiments.items(), key=operator.itemgetter(1))[0]
    # most_negative = min(sentiments.items(), key=operator.itemgetter(1))[0]
    # print("Episode " + most_positive.episode + " : " + str(sentiments[most_positive]))
    # print("Episode " + most_negative.episode + " : " + str(sentiments[most_negative]))
