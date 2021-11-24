from scipy import integrate

from numpy import *


def f1(x):
    return 1 / sqrt(0.5 * x + 1)


def trap(f1, a, b, n):
    h = (b - a) / n

    sum = 0.5 * (f1(a) + f1(b))

    for i in range(1, n):
        sum += f1(a + i * h)

    return sum * h


v, err = integrate.quad(f1, 3.2, 4)  # Перевірка

print("Trapetzia method:", trap(f1, 3.2, 4, 20))

print("Check for the trapetzia method= ", v)