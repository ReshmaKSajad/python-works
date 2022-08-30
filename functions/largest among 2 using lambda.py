#largest among 2 using lambda
largest=lambda x,y:x if x>y else y
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("largest number is",largest(a,b))