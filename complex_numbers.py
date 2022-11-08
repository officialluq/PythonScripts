import math
from math import sqrt


class Complex:
    def __init__(self, real, imag=0.0j):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        if isinstance(other, int) or isinstance(other, int):
            return Complex(self.real + other, self.imag)
        raise TypeError('Bad input type')

    def __radd__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        if isinstance(other, int) or isinstance(other, int):
            return Complex(self.real + other, self.imag)
        raise TypeError('Bad input type')
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        if isinstance(other, int) or isinstance(other, int):
            return Complex(self.real - other, self.imag)
        raise TypeError('Bad input type')

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        if isinstance(other, (int, float)):
            return Complex( other-self.real, self.imag)
        raise TypeError('Bad input type')

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)
        if isinstance(other, int) or isinstance(other, int):
            return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real)
        raise TypeError('Bad input type')

    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)
        if isinstance(other, int) or isinstance(other, int):
            return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real)
        raise TypeError('Bad input type')

    def __truediv__(self, other):
        divisor = (other.real ** 2 + other.imag ** 2)
        return Complex(((self.real * other.real) +
                        (self.imag * other.imag)) / divisor,
                       ((self.imag * other.real) - (self.real * other.imag)) / divisor)

    def __abs__(self):
        new = (self.real ** 2 + (self.imag ** 2) * -1)
        return Complex(sqrt(new.real))

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        return f'Complex({self.real}, {self.imag})'

# liczba = Complex(20, 2j)
# liczba_2 = Complex(30, 3j)
#
# print(f'{liczba + liczba_2}')
if __name__ == '__main__':
    a = Complex(2, 3)
    print(a)