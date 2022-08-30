#count the number of vowels in a string?
str1="i like grapes"
count=0
for i in str1:
    if i in "aeiouAEIOU":
        count=count+1
print("number of vowels=",count)
str2=str1.lower()
print("count of a=",str2.count("a"))
print("count of e=",str2.count("e"))
print("count of i=",str2.count("i"))
print("count of o=",str2.count("o"))

