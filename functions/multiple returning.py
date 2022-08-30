def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    expo=a**b
    mod=a%b
    return sum,sub,mul,div,expo,mod
m,n,o,p,q,r=calc(6,3)
print("sum is",m)
print("difference is",n)
print("product is",o)
print("quotient is",p)
print("power is",q)
print("reminder is",r)