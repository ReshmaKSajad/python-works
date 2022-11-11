#removing the space in a string and count the number of characters
str1 = "reshma is a good girl"
print("The original string is : ",str1)
c=0
for i in str1:
    if i!=" ":
        c+=1
print("The Characters Frequency avoiding spaces : ",c)
