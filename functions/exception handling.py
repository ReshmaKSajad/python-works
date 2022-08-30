#exception handling - they are method for handling the abnormal errors/run time errors/conditions occurs during
# execution of programmes...not a syntax or logical error


a=int(input("enter the first number"))
b=int(input("enter the second number"))
try:      #suspected code
    div=a/b
    print("result =",div)
except:   #handling code
    print("not give 0 as second number")


