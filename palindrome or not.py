#check a given string is palindrome or not?
str=input("enter the string")
str1=str[::-1]
print(str1)
if str==str1:
    print("palindrome")
else:
    print("not palindrome")
