import cmath
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = (b ** 2) - (4 * a * c)

x1 = (-b - cmath.sqrt(d)) / (2 * a)
x2 = (-b + cmath.sqrt(d)) / (2 * a)


print('X1 ={0}\r\nX2 ={1}'.format(x1, x2))
