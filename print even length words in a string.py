#print the even length words in a string?
str=input("enter the string")
s=str.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)