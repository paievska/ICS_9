from scipy import integrate

from numpy import *


def f1(x):
    return 1 / sqrt(0.5 * x + 1)


def left_rec(f1, a, b, n):
    h = (b - a) / n

    sum = 0

    for i in range(0, n):
        sum += f1(a + i * h)

    return sum * h


v, err = integrate.quad(f1, 3.2, 4)  # Перевірка

print("left rectangle:", left_rec(f1, 3.2, 4, 10))


def right_rec(f1, a, b, n):
    h = (b - a) / n

    sum = 0

    for i in range(1, n + 1):
        sum += f1(a + i * h)

    return sum * h


print("right rectangle:", right_rec(f1, 3.2, 4, 10))


def aver_rec(f1, a, b, n):
    h = 0.08

    sum = 0

    for i in range(0, n):
        sum += f1(a + i * h)

    return sum * h


print("average rectangle:", aver_rec(f1, 3.24, 3.96, 10))

print("Check for the rectangle method= ", v) 