#file - collection of data    eg: jpg,ppt,doc,pdf
#to open a file:
#fileobject = open(file_name,mode)
#mode
#r - read ....read content from the file
#r+ - read,write,append
#w - write
#w+ - read,write
#a - append
f1 = open("file_1","r")
print("first location :",f1.tell())   #to find the present location of file pointer
print(f1.read(3)) #if no.of characters is not specified,whole file will read
print("second location :",f1.tell())
print(f1.read(3))
print("third location :",f1.seek(0))   #to move the position of file pointer
print(f1.read(3))
f1.close()
#after each line ends, /n is referred as the next character.


