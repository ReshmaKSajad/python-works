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

str = input("enter the string")
count = 0
for letter in str:
    if letter in "aeiouAEIOU":
        count += 1
print("no.of vowels =",count)
str1 = str.lower()
print("count of a=",str1.count("a"))
print("count of e=",str1.count("e"))
print("count of i=",str1.count("i"))
print("count of o=",str1.count("o"))
print("count of u=",str1.count("u"))