class Rectangle:
    def read(self,l,b):
        self.length=l           #public data member  - can be access at anywhere
        self.__breadth=b        #private data member  - access only within the class
    def display(self):
        print("length =",self.length)
        print("breadth =",self.__breadth)
r1=Rectangle()
r1.read(10,5)
r1.display()
print(r1.length)
print(r1.__breadth)