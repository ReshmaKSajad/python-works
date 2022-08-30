str1=input("enter the string")
sub=input("enter the substring")
r=str1.find(sub)
if r!=-1:
    print("the substring is present in the string,and the location=",r)
else:
    print("not present in the string")

