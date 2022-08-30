#find the product of numbers in a list using function
def product(lst):
    mul=1
    for i in lst:
        mul=mul*i
    return mul
lst=[1,2,3,4,5,6,7,8,9,10]
print("product is",product(lst))