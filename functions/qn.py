lst = input("enter the list elements").split()
lst1 = list(map(int,lst))
print("original list =",lst1)

evenlist = list(filter(lambda x:x%2==0,lst1))
oddlist = list(filter(lambda x:x%2!=0,lst1))
print("even list =",evenlist)
print("odd list =",oddlist)

import functools
sum1 = functools.reduce(lambda x,y:x+y,evenlist )
sum2 = functools.reduce(lambda x,y:x+y,oddlist)
print("sum of even list =",sum1)
print("sum of odd list =",sum2)

