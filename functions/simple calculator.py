def sum(n1,n2):
    c=n1+n2
    print("sum is",c)
def sub(n1,n2):
    c=n1-n2
    print("difference is",c)
def mul(n1,n2):
    c=n1*n2
    print("product is",c)
def div(n1,n2):
    c=n1/n2
    print("quotient is",c)
while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    a = int(input("enter the first number"))
    b = int(input("enter the second number"))
    ch=int(input("enter your choice"))
    if ch==1:
        sum(a,b)
    elif ch==2:
        sub(a,b)
    elif ch==3:
        mul(a,b)
    elif ch==4:
        div(a,b)
    else:
        print('wrong choice')
        break
