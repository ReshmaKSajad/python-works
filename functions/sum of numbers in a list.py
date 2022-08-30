#find the sum of numbers in a list using function
def sum(lst):
    s=0
    for i in lst:
        s=s+i
    return s
lst=[1,2,3,4,5,6,7,8,9,10]
print("sum is",sum(lst))