n=int(input("enter the limit"))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print("sum of the digits=",sum)
