class Student:
    def __init__(self):
        self.rollno =int(input("enter the roll number"))
        self.name =input("enter the name")
    def printdata(self):
        print("ROLL NO :",self.rollno)
        print("NAME :",self.name)

class Mark(Student):
    def __init__(self):
        Student.__init__(self)
        self.mark=int(input("enter the mark"))
    def printmark(self):
        Student.printdata(self)
        print("MARK :",self.mark)

class Grade(Mark):
    def __init__(self):
        Mark.__init__(self)
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

s1=Grade()

s1.printdata()
s1.printmark()
s1.calculategrade()