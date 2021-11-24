import matplotlib.pyplot as plt

import math

from numpy import *

from sympy import Symbol

print("Variant 17")


def f(x):
    return math.e ** (-2 * x) + x ** 2


print('f(0)=e^(-2*x)+x^2= ', f(0))


def f1(x):
    return -2 * math.e ** (-2 * x) + 2 * x


print('f1(0)=-2*e^(-2x)+2x= ', f1(0))


def f2(x):
    return -4 * math.e ** (-2 * x) + 2


print('f2(0)=-4*e^(-2*x)+2= ', f2(0))


def f3(x):
    return -8 * math.e ** (-2 * x)


print('f3(0)=-8*e^(-2*x)= ', f3(0))

x = Symbol('x')

s = f(0) + f1(0) * (x - 0) + f2(0) * (((x - 0) ** 2) / 2) + f3(0) * (((x - 0) ** 3) / 6)

print("tailor=", s)


def Tailor(x):
    y = 0

    y += f(0) + f1(0) * (x - 0) + f2(0) * (((x - 0) ** 2) / 2) + f3(0) * (((x - 0) ** 3) / 6)

    return y


x = linspace(-5, 5, 1000)

yx = f(x)

xs = Tailor(x)

plt.plot(x, yx, 'r-')

plt.plot(x, xs, 'b-')

plt.title('Наближення Тейлора')

plt.legend(["e^(-2*x)+x^2", "1-2*x-x^2-(4*x^3)/3"], loc="upper right")

plt.grid()

plt.show()