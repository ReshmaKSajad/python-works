# class Person:                #parent class
#     def get_data(self):
#         self.voter_id=input("enter the id")
#         self.name=input("enter the name")
#     def print_data(self):
#         print("voter ID :",self.voter_id)
#         print("name :",self.name)
#
# class Employee(Person):       #child class
#     def get_data(self):
#         self.salary=int(input("enter the salary"))
#     def print_data(self):
#         print("salary :",self.salary)
#
# emp1=Employee()
# emp1.get_data()
# emp1.print_data()
# print("----------------------")
#
# emp2=Employee()
# emp2.get_data()
# emp2.print_data()

#over riding - if parent class and child class contain same member function, function of child class will over ride
# the parent class

class Person:                #parent class
    def get_data(self):
        self.voter_id=input("enter the id")
        self.name=input("enter the name")
    def print_data(self):
        print("voter ID :",self.voter_id)
        print("name :",self.name)

class Employee(Person):       #child class
    def get_data(self):
        super().get_data()
        self.salary=int(input("enter the salary"))
    def print_data(self):
        super().print_data()
        print("salary :",self.salary)

emp1=Employee()
emp1.get_data()
emp1.print_data()
print("----------------------")

emp2=Employee()
emp2.get_data()
emp2.print_data()