# f1 = open(r"C:\Users\Hp\OneDrive\Desktop\hello.txt","r")  #first r stands for relative path
# print(f1.read(22))
# f1.close()
#
#
# f1 = open("file_1","r")
# print(f1.readline())
# f1.close()
#
#
# f1 = open("file_1","r")
# print(f1.readlines())
# f1.close()
#
#
#
f1 = open("file_1","r")
lst = f1.readlines()
for i in lst:
    print(i.strip())












