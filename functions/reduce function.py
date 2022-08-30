# #reduce function- for combining the entire elements in a list and give a single value
# import functools
# lst=[1,2,3,4,5,6,7,8,9,10]
# result1=functools.reduce(lambda x,y:x+y,lst)
# result2=functools.reduce(lambda x,y:x*y,lst)
# print("sum:",result1)
# print("product:",result2)


#Return the largest number in a list using reduce?


import functools
lst=input("enter the list elements").split()
lst1 = list(map(int,lst))
lst1.sort()
print("sorted list =",lst1)
result=functools.reduce(max,lst1)
print(result,"is largest")


import functools
list=input("enter the list elements").split()
list1=map(int,list)
result=functools.reduce(lambda x,y:x if x>y else y, list1)
print("largest number in the list =",result)
















