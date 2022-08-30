n=int(input("enter the number"))
str1=str(n)
str2=str1[::-1]
print(str2)
if str1==str2:
    print("palindrome")
else:
    print("not palindrome")