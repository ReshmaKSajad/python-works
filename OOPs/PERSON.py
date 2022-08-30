#write a python program to implement the following.Create a base class called Person consisting of name
# and code.Create 2 child classes.
#a) Account with member_pay
#b) Admin with experience and inherit the base class.
#Create a class Employee with name, code, experience and pay by inheriting the above classes.
class Person:
    def getData(self):
        self.name = input("enter the name :")
        self.code = int(input("enter the code :"))

class Account(Person):
    def getMemberPay(self):
        self.memberpay = float(input("enter the amount :"))

class Admin(Person):
    def getExperience(self):
        self.experience = input("enter your experience :")

class Employee(Account, Admin):
    def getEmployeeDetails(self):
        self.getData()
        self.getMemberPay()
        self.getExperience()
    def printEmployeeDetails(self):
         print("NAME OF EMPLOYEE :",self.name)
         print("CODE OF EMPLOYEE :",self.code)
         print("MEMBER PAY :",self.memberpay)
         print("YEAR OF EXPERIENCE :",self.experience)

emp = Employee()
emp.getEmployeeDetails()
print("-------------------")
print("DETAILS OF EMPLOYEE")
print("-------------------")
emp.printEmployeeDetails()