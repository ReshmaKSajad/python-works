#find the words that contain 3 or more letters from a string?
str1=input("enter the string").split()
print(str1)
for i in str1:
    if len(i)>=3:
        print(i)
