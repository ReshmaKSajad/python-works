class Person:
    def __init__(self,v,n):
        self.voterid=v
        self.name=n
    def printdata(self):
        print("Voter ID :",self.voterid)
        print("Name :",self.name)

class Employee(Person):
    def __init__(self,v,n,s):
        super().__init__(v,n)
        self.salary=s
    def printdata(self):
        super().printdata()
        print("Salary :",self.salary)

e1=Employee("KL2347657","RESHMA K SAJAD",5000000)
e1.printdata()

