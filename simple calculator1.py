#simple calculator
#enter 2 numbers
#1.addition
#2.subtraction
#3.multiplication
#4.division
#enter your choice
#print result

a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("enter your choice"))
if ch==1:
    print(a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
elif ch==4:
    print(a/b)
else:
    print("wrong choice")
