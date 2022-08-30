class Person:                #parent class
    def get_data(self):
        self.voter_id=input("enter the id")
        self.name=input("enter the name")
    def print_data(self):
        print("voter ID :",self.voter_id)
        print("name :",self.name)

class Employee(Person):       #child class
    def get_salary(self):
        self.salary=int(input("enter the salary"))
    def print_salary(self):
        print("salary :",self.salary)

emp1=Employee()
emp1.get_data()
emp1.print_data()
emp1.get_salary()
emp1.print_salary()
print("----------------------")

emp2=Employee()
emp2.get_data()
emp2.print_data()
emp2.get_salary()
emp2.print_salary()

