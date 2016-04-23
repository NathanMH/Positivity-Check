"""####################
Author: Nathan Mador-House
Title: PositivityCheck
####################"""

"""####################
Index:
    1. Imports and Readme
    2. Functions 
    3. Main
    4. Testing
####################"""


###################################################################
# 1. IMPORTS AND README
###################################################################

import checkr

###################################################################
# 2. FUNCTIONS
###################################################################

###################################################################
# 1. MAIN
###################################################################

###################################################################
# 1. TESTING
###################################################################

text = "Hello this is some sample text. It has some positive text as well as negative. This is to test if the program fucking works. It has a lot of great words like; love, adore, best, beautiful."
test = checkr.text_block(text)
print(test.print_stats())

