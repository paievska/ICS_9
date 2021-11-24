from scipy import integrate

from numpy import *


def f1(x):
    return 1 / sqrt(0.5 * x + 1)


def simpson(a, b, n):
    h = (b - a) / n

    integration = f1(a) + f1(b)

    for i in range(1, n):

        k = a + i * h

        if i % 2 == 0:

            integration = integration + 2 * f1(k)

        else:

            integration = integration + 4 * f1(k)

    integration = integration * h / 3

    return integration


print("Simpsone method:", simpson(3.2, 4.0, 8))

v, err = integrate.quad(f1, 3.2, 4)  # Перевірка

print("Check for the simpsone method= ", v) 