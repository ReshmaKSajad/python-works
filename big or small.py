#read the number
#number>10 -> big
#number<10  -> small
#number=10  -> expected number

n=int(input("enter the number"))
if n>10:
    print("big")
elif n<10:
    print("small")
else:
    print("expected number")