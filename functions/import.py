#math is a buitin module

#first method
import math
help(math)
print(math.factorial(7))
print(math.sqrt(64))
print(math.floor(5.7865))

#another method
from math import sqrt   #here only one operation is possible
print(sqrt(100))

#another method
from math import *
print(cos(45))
print(sin(30))
print(tan(45))