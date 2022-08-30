#filter function
#syntax:
#filter(function,sequence)

lst=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x:x%2==0,lst)
print(list(result))

lst=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x:x%2!=0,lst)
print(list(result))

lst=input("enter the elements").split()
lst1=map(int,lst)
result=filter(lambda x:x%2==0,lst1)
print(list(result))

# lst=input("enter the elements").split()
# lst1=map(int,lst)
# mul=filter(lambda x:x%5==0,lst1)
# print(list(mul))
#
# lst=input("enter the elements").split()
# lst1=map(int,lst)
# greater=filter(lambda x:x>5,lst1)
# print(list(greater))

lst=[15,2,4,6,8]
nwlist=filter(lambda x:x>5,lst)
print(tuple(nwlist))

