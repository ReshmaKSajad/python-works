# #tuple - immutable...enclosed in simple brackets
tuple=(1,2,6.7,'rechu')
print(tuple)    #the tuple object does not support item assignment....we cannot replace or change the elements in it
print(len(tuple))
print(tuple.count("rechu"))    #refers to number of times the element present in the tuple
print(tuple.index(1))    #refers to index number
print(tuple.index("rechu"))
#in tuple,functions such as append,extend,insert,pop,remove,replace does not work

tuple1=(1,9,6,5,3,5)
print(max(tuple1))
print(min(tuple1))

tuple2=(2,8,7,9,4,3)
sum=0
for i in tuple2:
    sum=sum+i
print("sum=",sum)
#print(sum(tuple2))

tuple3=(3,4,5,7,1,3,9,7)
n=int(input("enter the item to be searched"))
for i in tuple3:
    if i==n:
        print("item found")
        break
else:
    print("item not found")

item=input("enter the tuple items").split()
print(item)
tuple4 = tuple(item)
print(tuple4)










