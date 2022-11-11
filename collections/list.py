# #collections
# #list ->     heterogenous...elements seperated by commas..datas are enclosed in a square colon...mutable...can change
lst=[2,5,"reshma",5.8,0.6]
# #indexing
# #forward and backward
print(lst[2])        #forward indexing
print(lst[-5])    #backward indexing
print(lst[-2])
print(lst[0:5:1])    #slicing method
print(lst[::-1])     #reverse slicing
lst[2]="razik"       #for replacing the value at an index
print(lst)
lst[3]=6.7
print(lst)
lst.append("rinshad")     #adding values to the end...only one value can be added at a time
lst.append(1)
lst.extend([3,9,0.4])     #adding multiple values to the end
lst.insert(4,7)           #inserting additional values to the list..4 represent the index and 7 represent the new-
                            #value that added to the 4th index
lst.pop()                 #used to remove the last value from the list
lst.pop(5)                #if index is specified, that value will be removed
lst.remove(2)              #to remove a particular value,that value should be enclosed within the remove function
print(lst)

lst1=[34,67,12,37,89,10,4,23]
lst1.sort()              #to arrange the datas in the ascending order
lst1.sort(reverse=True)  #to arrange the datas in the descending order
lst1.reverse()            #to reverse the given data from right to left
print(lst1)
print(max(lst1))           #to get the largest or maximum value in a list
print(min(lst1))           #to get the smallest or minimum value in a list

#find the second largest element from lst1?
lst1.sort(reverse=True)
print(lst1)
print(lst1[1])

# find the sum of all numbers in the list?
lst=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in lst:
    sum=sum+i
print("sum=",sum)

lst=input("enter the list elements").split()
print(lst)
sum=0
for i in lst:
    sum=sum+int(i)
print("sum=",sum)


# print only even numbers in the list?
for i in lst:
    if int(i)%2==0:
        print(i)

lst=input("enter the list elements").split()
evenlist=[]
oddlist=[]
for i in lst:
    if int(i)%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("list of even numbers=",evenlist)
print("list of odd numbers=",oddlist)


lst=[1,2,3,5,[4,6],7]
print(len(lst))
# lst[0]=1
# lst[1]=2
# lst[2]=3
# lst[3]=5
# lst[4]=[4,6]
#      lst[4][0]=4
#      lst[4][1]=6
# lst[5]=7

lst=[1,3,5,4,[7,8,[9,0]],4,6]
print(lst[4][2][0])

