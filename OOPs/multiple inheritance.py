#multiple inheritance
#a -> c <- b

class Student:
    def getdata(self):
        self.name=input("enter the name")
        self.rollno=int(input("enter the roll number"))
    def printdata(self):
        print("NAME :",self.name)
        print("ROLL NO :",self.rollno)
class Mark:
    def getmark(self):
        self.mark=int(input("enter the theory mark"))
    def printmark(self):
        print("TE MARK :",self.mark)
class Gracemark:
    def getgmark(self):
        self.gracemark=int(input("enter the grace mark"))
    def printgmark(self):
        print("CE MARK :",self.gracemark)
class Grade(Student,Mark,Gracemark):
    def calculate(self):
        if self.mark>400 or self.gracemark>100:
            print("WRONG CALCULATION")
        else:
            total=self.mark+self.gracemark
            p=(total/500)*100
            if p>=90:
                print("GRADE A+")
            elif p>=80:
                print("GRADE A")
            elif p>=70:
                print("GRADE B+")
            elif p>=60:
                print("GRADE B")
            elif p>=50:
                print("GRADE C+")
            elif p>=40:
                print("GRADE C")
            elif p>=30:
                print("GRADE D+")
            else:
                print("FAILED")
s1=Grade()
s1.getdata()
s1.printdata()
s1.getmark()
s1.printmark()
s1.getgmark()
s1.printgmark()
s1.calculate()