from student_details import *

LuminarStudentDetails.display_welcome()

x=LuminarStudentDetails("Reshma",21,"Edappally")
y=LuminarStudentDetails("Arunima",21,"Trissur")
z=LuminarStudentDetails("Nihana",21,"Guruvayoor")

x.display()
y.display()
z.display()

print("-----------------------------------")
LuminarStudentDetails.year=LuminarStudentDetails.year+1
x.add_age()
y.add_age()
z.add_age()

x.display()
y.display()
z.display()

print("-----------------------------------")
LuminarStudentDetails.add_year()

x.add_age()
y.add_age()
z.add_age()
x.relocate("London")
y.relocate("Australia")
z.relocate("Dubai")

x.display()
y.display()
z.display()
