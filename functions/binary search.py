#binary search
def BinarySearch(lst,key):
    mid=0
    low=0
    high=len(lst)-1
    while(low<=high):
        mid=(low+high)//2
        if lst[mid]<key:
            low=mid+1
        elif lst[mid]>key:
            high=mid-1
        else:
            return mid
    return -1
lst1=input("enter the elements").split()
lst1.sort()
print(lst1)
key=input("enter the key")
f=BinarySearch(lst1,key)
if f==-1:
    print("key not found")
else:
    print("key found at",f+1)

