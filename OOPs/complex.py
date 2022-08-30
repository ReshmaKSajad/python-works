class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    def __sub__(self, other):
        newreal = self.real - other.real
        newimaginary = self.imaginary - other.imaginary
        return Complex(newreal,newimaginary)
    def __str__(self):
        return "{0}+{1}j".format(self.real,self.imaginary)
c1 = Complex(6,8)
c2 = Complex(2,6)
print("difference : ",c1-c2)

