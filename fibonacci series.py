#fibonacci series:
       #it is the series of numbers in which the third value will get by adding the first and second values
#  0,1,1,2,3,5,8,13,21,........

n=int(input("enter the limit"))
f=0
s=1
t=0
print(f,s,end=" ")
for i in range(2,n):
    t=f+s
    f=s
    s=t
    print(t,end=" ")