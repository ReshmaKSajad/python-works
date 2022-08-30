#match function - match function searches only the beginning word

import re
str = "Python Programming is very fun"
result = re.match("Python",str)
if result:
    print("pattern exist")
else:
    print("pattern not exist")

import re
str = "Python Programming is very fun"
result = re.match("fun",str)
if result:
    print("pattern exist")
else:
    print("pattern not exist")