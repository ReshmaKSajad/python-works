#regualar expressions    - search , match , findall , sub
#search	 -  Returns a Match object if there is a match anywhere in the string

import re
str = "My Name is Reshma K Sajjad"
result = re.search("Reshma",str)      #syntax: re.search("pattern",string_name)
if result:
    print("pattern exists")
else:
    print("pattern not exist")