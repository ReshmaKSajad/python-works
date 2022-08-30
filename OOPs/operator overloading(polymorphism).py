#operator overloading
#2 types - 1)function overloading - not supporting in python
#           2)operator overloading - mathematical operations between objects of a class
class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self, other):
        newa = self.a + other.a
        newb = self.b + other.b
        return Point(newa,newb)
    def __str__(self):
        return "({1},{0})".format(self.a,self.b)

p1 = Point(2,4)
p2 = Point(5,6)
p3 = Point("RESHMA ","HASANUL ")
p4 = Point("K SAJJAD","BENNA A.E")
print("sum of points :",p1+p2)
print("names :",p3+p4)