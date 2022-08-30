class Student:
    def __init__(self,n,r):
        self.name=n
        self.rollno=r
    def printdata(self):
        print("NAME :",self.name)
        print("ROLL NUMBER :",self.rollno)
class Mark:
    def __init__(self,n,r,m):
        Student.__init__(self,n,r)
        self.mark=m
    def printmark(self):
        print("TE MARK :",self.mark)
class Gracemark:
    def __init__(self,n,r,m,g):
        Mark.__init__(self,n,r,m)
        self.gracemark=g
    def printgmark(self):
        print("CE MARK :",self.gracemark)
class Grade(Student,Mark,Gracemark):
    def __init__(self,n,r,m,g):
        Gracemark.__init__(self,n,r,m,g)
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
s1=Grade("RESHMA K SAJJAD",21,385,95)
s1.printdata()
s1.printmark()
s1.printgmark()
s1.calculate()
print("------------------------")
s2=Grade("HASANUL BENNA",65,378,94)
s2.printdata()
s2.printmark()
s2.printgmark()
s2.calculate()
print("--------------------------")
s3=Grade("RAZIK K SAJJAD",34,245,78)
s3.printdata()
s3.printmark()
s3.printgmark()
s3.calculate()
print("---------------------------")
s4=Grade("RINSHAD K S",45,267,89)
s4.printdata()
s4.printmark()
s4.printgmark()
s4.calculate()




