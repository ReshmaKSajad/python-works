import re
p = input("enter the password")
if len(p)<=6 or len(p)>=16:
    print("INVALID PASSWORD")
elif not re.search("[a-z]",p):
    print("INVALID PASSWORD")
elif not re.search("[A-Z]",p):
    print("INVALID PASSWORD")
elif not re.search("[0-9]",p):
    print("INVALID PASSWORD")
elif not re.search("[@#$&]",p):
    print("INVALID PASSWORD")
else:
    print("VALID PASSWORD")

