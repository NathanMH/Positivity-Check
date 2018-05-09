#%%

import pandas as pd
import collections
import matplotlib.pyplot as plt
import os
import sys
import pprint
import re
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from positivity_check.positivity_check import UserText

office_file = os.getcwd() + "\\positivity_check\\resources\\the-office-lines-scripts.csv"
columns = pd.read_csv(office_file, nrows=1).columns
print(columns)
data = pd.read_csv(office_file)

def count_lines():
    df = pd.DataFrame(data=data, columns=columns)
    char_count = collections.Counter(df['speaker'])
    epi_count = collections.Counter(df['episode'])
    season_count = collections.Counter(df['season'])
    counts = {}
    counts["char_count"] = collections.OrderedDict(char_count.most_common(10))
    counts["season_count"] = dict(season_count)
    counts["epi_count"] = dict(epi_count)
    return counts

def lines_per():
    df = pd.DataFrame(data=data, columns=columns)
    jim_lines = df[(df['season'] == 1) & (df['episode'] == 1) & (df['speaker'] == 'Jim')]['line_text']
    return jim_lines

def remove_stage_directions_and_punctuation(text):
    without_directions = re.sub("[\(\[].*?[\)\]]", "", text)
    result = re.sub('[^A-Za-z0-9 ]+', '', without_directions)
    return result

# Make Season[Episode][Character] data structure
main_characters = ["Michael", "Jim", "Pam", "Dwight", "Ryan", "Andy", "Robert"]
recurring_characters = ["Jan", "Roy", "Stanley", "Kevin", "Meredith", "Angela", "Oscar", "Phyllis", "Kelly", "Toby", "Creed", "Gabe", "Holly", "Nellie", "Clark", "Pete", "Erin"]
other_characters = ["Todd", "David", "Karen", "Charles", "Jo", "Deangelo", "Val", "Cathy"]

df = pd.DataFrame(data=data, columns=columns)

# seasons = dict.fromkeys(set(data['season']))
seasons = {1:None}

for season in seasons:
    episodes = df[ (df['season']) == season]
    seasons[season] = dict.fromkeys(set(episodes['episode']))
    for episode in seasons[season]:
        seasons[season][episode] = dict.fromkeys(main_characters)
        for char in seasons[season][episode]:
            seasons[season][episode][char] = {'total_text': "", 'text_value_counts': []}
            for line in df[ (df['season'] == season) & (df['episode'] == episode) & (df['speaker'] == char)]['line_text']:
                # print(line)
                seasons[season][episode][char]['total_text'] += " " + remove_stage_directions_and_punctuation(line)

analyzed_chars = {}
for char in seasons[1][1]:
    analyzed_chars[char] = UserText(seasons[1][1][char]['total_text'])

# pprint.pprint(seasons[1][1]['Jim']['total_text'])
# analyzed_text = UserText(seasons[1][1]['Jim']['total_text'])
analyzed_chars['Jim'].print_stats()

# Line counting, season counting results
# counts = count_lines()
# counts = pd.Series(count_lines()['char_count'])
# counts.plot(kind='bar', rot=-45)
# counts = pd.Series(count_lines()['season_count'])
# counts.plot(kind='bar', rot=0)

counts = pd.Series(analyzed_chars['Jim'].word_values_count)
counts.plot(kind='bar', rot=0, logy=True, figsize=(12, 8), title="Distribution of Positive and Negative Words")
plt.xlabel('Word Values')
plt.ylabel('Occurance Rate')
