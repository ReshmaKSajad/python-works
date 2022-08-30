#OOPs  - object oriented programming
# class
# object
# abstraction -act of representing essential features without showing background details
# encapsulation - wrapping up of data and methods
# inheritance -inherit the properties from parent class
# polymorphism - ability to exist in more than one form
#eg : 2+3=5    hai+students = haistudents

# class Students:
#     def read(self):    #member function
#         self.rollno=int(input("enter the roll number"))   #data member
#         self.name=input("enter the name")                 #data member
#     def display(self):
#         print("Roll number :",self.rollno)
#         print("Name :",self.name)
# #objectname=classname()
# s1=Students()                        #s1,s2,s3,.....objects
# s1.read()
# s1.display()
# s2=Students()
# s2.read()
# s2.display()
# s3=Students()
# s3.read()
# s3.display()
class Person:
    def read(self,name,age):
        self.name = name
        self.age = age


sachu = Person()
sachu.read("Sachu", 23)


reshma = Person()
reshma.read("reshma",21)

print(reshma.name)
print(reshma.age)

aachi = Person()
aachi = reshma

aachi.age = 16
print(reshma.age)

print(reshma is aachi)
print(reshma is sachu)

print(reshma == aachi)

