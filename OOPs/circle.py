class Circle:
    def read(self):
        self.radius=int(input("enter the radius"))
        self.area=3.14*self.radius*self.radius
    def display(self):
        #print("Radius =",self.radius)
        print("Area of the circle =",self.area)
c1=Circle()
c1.read()
c1.display()
c2=Circle()
c2.read()
c2.display()
c3=Circle()
c3.read()
c3.display()











