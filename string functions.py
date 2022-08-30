str1="i like programming"
print(str1.title())              #CAPITALIZE FIRST LETTER IN EACH WORD
print(str1.capitalize())         #CAPITALIZE FIRST LETTER OF THE STRING
print(str1.upper())
str2="HELLO WORLD"
print(str2.lower())
str3="hai,How Are You?"
print(str3.swapcase())
print(len(str1))                  #LENGTH STARTS WITH 1
print(len(str2))
print(len(str3))
print(str2.isupper())
print(str3.isupper())
print(str1.islower())
print(str3.islower())
str4="@@hello@@"
print(str4.rstrip("@"))
print(str4.lstrip("@"))
print(str4.strip("@"))
print(str2.count("L"))
print(str2.count("O",0,8))
str5="i like python"
print(str5.find("like"))
print(str5.find("python"))
str6="python programming"
print(str6.replace("python","C"))
print(str6.replace("p","t"))

