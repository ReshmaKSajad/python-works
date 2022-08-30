# import re
# f1 = open("file_1","r")
# text = f1.readlines()
# for line in text:
#     result = re.search(r"\bs.e\b", line)   #r stands for regular expression pattern . \b operates for blank spaces
#     if result:
#         print(line)

import re
f1 = open("file_1","r")
text = f1.readlines()
for line in text:
    result = re.search(r"\bs\w*e\b", line)   #\w 
    if result:
        print(line)