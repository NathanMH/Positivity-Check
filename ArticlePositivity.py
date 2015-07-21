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

import newspaper
from bs4 import BeautifulSoup
import urllib
import os # Comment this out to stop program from running

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

sources = ["http://www.nytimes.com/services/xml/rss/index.html", "http://feeds.gawker.com/lifehacker/full", "http://feeds.feedburner.com/techcrunch", "http://www.cbc.ca/cmlink/rss-arts", "http://www.cbc.ca/cmlink/rss-world", "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml", "http://www.npr.org/rss/rss.php?id=1008", "http://feeds.reuters.com/news/artsculture"]

# Step one, Loop through each 'source'
def getArticleLinks(sources):
    links = []
    for site in sources:
        print(site)
        soup = BeautifulSoup(urllib.request.urlopen(site))
        links.append(soup.find_all('a'))
    print()
    return links 

def getLinksFromLifehacker(rssSource):



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

# currentLinks = getArticleLinks(sources)

# os.system("PositivityCheck.py")

###################################################################
