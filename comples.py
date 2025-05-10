class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")

c1 = Complex(2, 3)
c2 = Complex(1, 4)
c3 = c1 + c2
c4 = c1 * c2
print("Addition:")
c3.display()
print("Multiplication:")
c4.display()