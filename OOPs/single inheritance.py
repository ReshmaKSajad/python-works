#single inheritance - used for single parent and single child
class Person:                #parent class
    def __init__(self):
        self.voter_id=input("enter the id")
        self.name=input("enter the name")
    def print_data(self):
        print("voter ID :",self.voter_id)
        print("name :",self.name)

class Employee(Person):       #child class
    def __init__(self):
        super().__init__()
        self.salary=int(input("enter the salary"))
    def print_data(self):
        super().print_data()
        print("salary :",self.salary)

emp1=Employee()
emp1.print_data()
print("----------------------")

emp2=Employee()
emp2.print_data()