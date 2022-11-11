#input a number
#check the number is divisible by 5 and 7
#check the number is divisible by 5 only
#check the number is divisible by 7 only
#check the number is  not divisible by 5 and 7
n=int(input("enter the number"))
if n%5==0 and n%7==0:
    print("number is divisible by 5 and 7")
elif n%5==0:
    print("number is divisible by 5 only")
elif n%7==0:
    print("number is divisible by 7 only")
else:
    print("number is not divisible by 5 and 7")