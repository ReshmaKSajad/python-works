#findall   	Returns a list containing all matches

import re
zipcode = "234-6478-6376 SDGRY 67"
new = re.findall("\d",zipcode)              #\d
print(new)

import re
zipcode = "234-6478-6376-SDGRY-67"
new = re.findall("\D",zipcode)
print(new)

import re
zipcode = "234-6478-6376-SDGRY-67"
new = re.findall("\S",zipcode)
print(new)