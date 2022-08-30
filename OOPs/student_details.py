class LuminarStudentDetails:
    year=2022
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("Year :",str(LuminarStudentDetails.year))
        print("Name :",self.name)
        print("Age :",str(self.age))
        print("Place :",self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def display_welcome():
        print("WELCOME")
#
# LuminarStudentDetails.display_welcome()
#
# x=LuminarStudentDetails("Reshma",21,"Edappally")
# y=LuminarStudentDetails("Arunima",21,"Trissur")
# z=LuminarStudentDetails("Nihana",21,"Guruvayoor")
#
# x.display()
# y.display()
# z.display()
#
# print("-----------------------------------")
# LuminarStudentDetails.year=LuminarStudentDetails.year+1
# x.add_age()
# y.add_age()
# z.add_age()
#
# x.display()
# y.display()
# z.display()
#
# print("-----------------------------------")
# LuminarStudentDetails.add_year()
#
# x.add_age()
# y.add_age()
# z.add_age()
# x.relocate("London")
# y.relocate("Australia")
# z.relocate("Dubai")
#
# x.display()
# y.display()
# z.display()