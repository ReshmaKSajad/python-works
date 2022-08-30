#constructor - used to initialize the data members  ,it is a member function..init function operates when
# an object of the class is formed

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        self.area=self.length*self.breadth
        self.perimeter=2*(self.length+self.breadth)
    def display(self):
        print("length =",self.length)
        print("breadth =",self.breadth)
        print("area =",self.area)
        print("perimeter =",self.perimeter)
r1=Rectangle(10,5)
r1.display()

r2=Rectangle(20,10)
r2.display()
