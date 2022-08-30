n=int(input("enter the number"))
sum=0
while n>0:
    d=n%10
    sum=sum*10+d
    n=n//10
print("reverse of the number=",sum)

#           OR

n=int(input("enter the number"))
sum=0
while n>0:
    d=n%10
    n=n//10
    print(d,end="")


