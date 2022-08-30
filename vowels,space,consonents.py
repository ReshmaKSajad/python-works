str1=input("enter the string")
str2=str1.lower()
vowels=0
space=0
digit=0
consonents=0
for i in str2:
    if i in "aeiou":
        vowels=vowels+1
    elif i==" ":
        space=space+1
    elif i in "0123456789":
        digit=digit+1
    else:
        consonents=consonents+1
print("number of vowels=",vowels)
print("number of space=",space)
print("number of digits=",digit)
print("number of consonents=",consonents)
