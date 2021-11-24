import math


def f(x):
    return 4 * x * x * x * x - 4 * x * x * x + 2 * x * x - 3 * x - 9


def f1(x):
    return 48 * x * x - 24 * x + 4


def mt(a, b, e):
    while (abs(a - b) > e):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    x = (a + b) / 2
    return x



print("mtofhalf-division x1= ", mt(-1, 3 / 4, 0.001))
print("mtofhalf-division x2= ", mt(-3 / 4, 5, 0.001))