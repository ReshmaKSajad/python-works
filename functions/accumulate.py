#accumulate function
import itertools
lst=[1,3,2,4,5,6,7,8]
result=list(itertools.accumulate(lst,lambda x,y:x*y))  #if function is not specified,then by default,addition occurs
print(result)
