class Student:
    def __init__(self,r,n):
        self.rollno =r
        self.name =n
    def printdata(self):
        print("ROLL NO :",self.rollno)
        print("NAME :",self.name)

class Mark(Student):
    def __init__(self,r,n,m):
        Student.__init__(self,r,n)
        self.mark=m
    def printmark(self):
        print("MARK :",self.mark)

class Grade(Mark):
    def __init__(self,r,n,m):
        Mark.__init__(self,r,n,m)
    def calculategrade(self):
        p=(self.mark/500)*100
        if p>= 90:
            print("grade A+")
        elif p>=80:
            print("grade A")
        elif p>=70:
            print("grade B+")
        elif p>=60:
            print("grade B")
        elif p>=50:
            print("grade C+")
        elif p>=40:
            print("grade C")
        elif p>=30:
            print("grade D+")
        else:
            print("failed")

s1=Grade(23,"RESHMA",435)
s1.printdata()
s1.printmark()
s1.calculategrade()
print("----------------------------")
s2=Grade(24,"BENNA",456)
s2.printdata()
s2.printmark()
s2.calculategrade()
print("----------------------------")
s3=Grade(25,"RAZIK",453)
s3.printdata()
s3.printmark()
s3.calculategrade()
print("----------------------------")
s4=Grade(26,"RINSHAD",437)
s4.printdata()
s4.printmark()
s4.calculategrade()
