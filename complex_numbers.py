import math
from math import sqrt


class Complex:
    def __init__(self, real, imag=0.0j):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        divisor = (other.real ** 2 + other.imag ** 2)
        return Complex(((self.real * other.real) +
                       (self.imag * other.imag)) / divisor,
                       ((self.imag * other.real) - (self.real * other.imag)) / divisor)
    def __abs__(self):

        new = (self.real ** 2 + (self.imag ** 2) * -1)
        return Complex(sqrt(new.real))

# liczba = Complex(20, 2j)
# liczba_2 = Complex(30, 3j)
#
# print(f'{liczba + liczba_2}')
