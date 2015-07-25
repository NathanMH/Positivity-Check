"""####################
Author: Nathan Mador-House
Title: ArticlePositivity
####################"""

######################
"""###################
Index:
    1. Imports and Readme
    2. Initialization Functions
    3. Setup with supplied files
    4. General Functions
    5. Main
    6. Testing
###################"""
######################


###################################################################
# 1. IMPORTS AND README
###################################################################

from newspaper import Article
from bs4 import BeautifulSoup
import urllib
import os 
import sys, io # Needed for proper encoding for windows powershell("cp437")
import string

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

sources = ["http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml", "http://feeds.gawker.com/lifehacker/full", "http://feeds.feedburner.com/techcrunch", "http://www.cbc.ca/cmlink/rss-arts", "http://www.cbc.ca/cmlink/rss-world", "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml", "http://www.npr.org/rss/rss.php?id=1008", "http://feeds.reuters.com/news/artsculture"]

links = []

# Get the links from LifeHacker RSS 
def getLinks(rssSources):
    for site in rssSources:
        # Open RSS feed in xml format
        soup = BeautifulSoup(urllib.request.urlopen(site), 'xml')
        # Get the links into string format and place into list
        for i in soup.find_all('link')[3:]:
            if i.string != None:
                links.append(i.string)

    return links

def getArticleContent(url):
    content = Article(url, fetch_images=False)
    content.download()
    content.parse()
    articleString = content.text.encode('utf-8')

    print(articleString)
    return articleString

###################################################################
# 3. SETUP WITH SUPPLIED FILES
###################################################################



###################################################################
# 4. GENERAL FUNCTIONS
###################################################################



###################################################################
# 5. MAIN
###################################################################



###################################################################
# 6. TESTING
###################################################################

'''
getLinks(sources)

print(links[1])

testContent = getArticleContent(links[1])
'''

###################################################################
