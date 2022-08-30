#find the factorial of a number?
n=int(input("enter the limit"))
fact=1
for i in range(1,n+1,1):
    fact = fact * i
print("factorial is",fact)