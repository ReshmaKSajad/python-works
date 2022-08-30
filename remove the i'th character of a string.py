str=input("enter the string")
print("the original string =",str)
str1=""
for i in range(len(str)):
    if i!=2:
        str1=str1+str[i]
print("the string after the removal of i'th character =",str1)