# class Rectangle:
#     def get_data(self):
#         self.length=int(input("enter the length"))
#         self.breadth=int(input("enter the breadth"))
#         self.area=self.length*self.breadth
#         self.perimeter=2*(self.length+self.breadth)
#     def display(self):
#         print("Length =",self.length)
#         print("Breadth =",self.breadth)
#         print("Area =",self.area)
#         print("Perimeter =",self.perimeter)
# r1=Rectangle()
# r1.get_data()
# r1.display()
# r2=Rectangle()
# r2.get_data()
# r2.display()
# r3=Rectangle()
# r3.get_data()
# r3.display()

class Rectangle:
    def get_data(self,l,b):
        self.length=l
        self.breadth=b
        self.area=self.length*self.breadth
        self.perimeter=2*(self.length+self.breadth)
    def display(self):
        print("Length =",self.length)
        print("Breadth =",self.breadth)
        print("Area =",self.area)
        print("Perimeter =",self.perimeter)
r1=Rectangle()
r1.get_data(3,5)
r1.display()
r2=Rectangle()
r2.get_data(6,7)
r2.display()
r3=Rectangle()
r3.get_data(4,5)
r3.display()