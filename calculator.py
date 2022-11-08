import complex_numbers as cplx
import cmath


class Calculator():
    def __init__(self):
        self.result = 0

    def add(self, element_1: cplx.Complex, element_2: cplx.Complex) -> float:
        self.result = element_1 + element_2
        return self.result

    def sub(self, element_1: cplx.Complex, element_2: cplx.Complex) -> float:
        self.result = element_1 - element_2
        return self.result

    def mul(self, element_1: cplx.Complex, element_2: cplx.Complex) -> float:
        self.result = element_1 * element_2
        return self.result

    def div(self, element_1: cplx.Complex, element_2: cplx.Complex) -> float:
        self.result = element_1 / element_2
        return self.result

    def abs(self, element_1: cplx.Complex) -> float:
        self.result = abs(element_1)
        return self.result

    def solve_equation(self, coef1: cplx.Complex, coef2: cplx.Complex, coef3: cplx.Complex):
        d = (coef2 * coef2) - (cplx.Complex(4, 0j) * coef1 * coef3)
        temp = (cmath.sqrt(d.real))
        sqrt_d = cplx.Complex(temp.real, complex(0, temp.imag))
        x1 = ((cplx.Complex(-1) * coef2 - sqrt_d) / (cplx.Complex(2) * coef1))
        x2 = ((cplx.Complex(-1) * coef2 + sqrt_d) / (cplx.Complex(2) * coef1))
        return x1, x2


if __name__ == '__main__':
    calc = Calculator()
    calc.abs(cplx.Complex(2, 3j))
    x1, x2 = calc.solve_equation("w", -11, 12)
    print(x1)
    print(x2)
