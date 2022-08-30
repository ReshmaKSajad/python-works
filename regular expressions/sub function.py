#substitution function - 	Replaces one or many matches with a string
import re
zipcode = "366-355 saafd 56"
new = re.sub("\d","@",zipcode)
print(new)

import re
zipcode = "366-355 saafd 56"
new = re.sub("\D","@",zipcode)
print(new)

import re
zipcode = "366-355 saafd 56"
new = re.sub("\s","@",zipcode)
print(new)

import re
zipcode = "366-355 saafd 56"
new = re.sub("\S","@",zipcode)
print(new)