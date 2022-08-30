
# f1 = open("file_1","r+")
# f1.write("my name is reshma")
# f1.seek(0)
# print(f1.read(3))
# f1.close()

#
# f1 = open("file_1","w")
# f1.write("hello\n")
# f1.close()

# f1 = open("file_1","w")
# lst = ["hello\n","how are you?\n","where are you?\n"]
# f1.writelines(lst)
# f1.close()

# f1 = open("file_1","a")
# lst = ["hello\n","how are you?\n","where are you?\n"]
# f1.writelines(lst)
# f1.close()

#
# f1 = open("file_1","r")
# f2 = open("file_2","w")
# lst = f1.readlines()
# print(lst)
# f2.writelines(lst)
# f1.close()
# f2.close()


#read the words
# f1 = open("file_2","r")
# r = f1.read()
# words = r.split()
# print(words)
# c=0
# for i in words:
#     c=c+1
# print("no of words :",c)


#unique words
# f1 = open("file_2","r")
# r = f1.read()
# words = set(r.split())
# print(words)
# c=0
# for i in words:
#     c=c+1
# print("no of words :",c)



# dict = {}
# dict["hello"] = 1
# print(dict)
# dict["are"] = 3
# print(dict)
# dict["hello"] = dict["hello"]+1
# print(dict)

#word count:
# def Wordcount(lst):
#     dict = {}
#     for word in lst:
#         if word in dict:
#             dict[word] = dict[word]+1
#         else:
#             dict[word] = 1
#     print(dict)
#
# f1 = open("file_2","r")
# r = f1.read()
# words = r.split()
# Wordcount(words)


def Wordcount(lst):
    dict = {}
    for word in lst:
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] = 1
    for k,v in dict.items():
        print(k,":",v)

f1 = open("file_2","r")
r = f1.read()
words = r.split()
Wordcount(words)





















