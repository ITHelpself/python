from __future__ import division  # can run in python 2
import operator
import math
import cmath
# print number


def printNumber(number):
    print(number)
# check type


def checkType(number, type):
    return isinstance(number, type) and number == 3
a, b, c, d, e, f = 3.0, -2, 5, 6, 7, -7
print(a, "/", b, "=", a/b)
print(c, "/", d, "=", c//d)
# using div in operator library
g = operator.__truediv__(3, 4)
print(g)
# operator return int number
h = operator.pow(3, 4)
print(h)
# math return float number
h = math.pow(3, 4)
print(h)
# pow 3 argument
h = pow(3, 2, 3)
print(h)
# pow 2 argument
h = pow(3, 2)
print(h)
# complex math
h = cmath.sqrt(complex(3, 4))
print(h)
# exp
h = math.exp(3)
print(h)
a = 6
if 3 <= a <= 7:
    print("3<= a <= 7")
