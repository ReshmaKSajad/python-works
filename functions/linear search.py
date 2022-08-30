#linear search
def linear_search(lst,key):
    for i in lst:
        if i==key:
            print("key found at the position",lst.index(i)+1)
            break
    else:
        print("key not found")
lst=[1,3,4,6,7,8,9,3,0]
print("list=",lst)
key=1
print("key=",key)
linear_search(lst,key)