import numpy as np

import matplotlib.pyplot as plt

import math


def fun(x):
    return math.e ** (-x) + x ** 2


print("Dani:")

x = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])

y = np.array([fun(0.1), fun(0.15), fun(0.2), fun(0.3), fun(0.4), fun(0.5), fun(0.6), fun(0.7), fun(0.47), fun(0.5)])

print("x=", x)

print("y=", y)

mean_x = np.mean(x)

mean_y = np.mean(y)

n = len(x)

number = 0

xy = 0

mean2_x = (x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2 + x[5] ** 2 + x[6] ** 2 + x[7] ** 2 + x[8] ** 2 +
           x[9] ** 2) / n

mean2_y = (y[0] ** 2 + y[1] ** 2 + y[2] ** 2 + y[3] ** 2 + y[4] ** 2 + y[5] ** 2 + y[6] ** 2 + y[7] ** 2 + y[8] ** 2 +
           y[9] ** 2) / n

for i in range(n):
    number += x[i] * y[i]

    xy = number / n

a1 = (xy - mean_x * mean_y) / (mean2_x - mean_x ** 2)

a0 = mean_y - a1 * mean_x

print("Nabluzhennia line:")

print("a1=", a1)

print("a0=", a0)

print("f(x)=", a0, "+", a1, "*x")

f = a0 + a1 * x

##parabola

m = 0

xy2 = 0

mean3_x = (x[0] ** 3 + x[1] ** 3 + x[2] ** 3 + x[3] ** 3 + x[4] ** 3 + x[5] ** 3 + x[6] ** 3 + x[7] ** 3 + x[8] ** 3 +
           x[9] ** 3) / n

mean4_x = (x[0] ** 4 + x[1] ** 4 + x[2] ** 4 + x[3] ** 4 + x[4] ** 4 + x[5] ** 4 + x[6] ** 4 + x[7] ** 4 + x[8] ** 4 +
           x[9] ** 4) / n

for i in range(n):
    m += y[i] * (x[i] ** 2)

    xy2 = m / n

A = np.matrix([[1, mean_x, mean2_x], [mean_x, mean2_x, mean3_x], [mean2_x, mean3_x, mean4_x]])

B = np.matrix([[mean_y], [xy], [xy2]])

jd = np.array(np.linalg.inv(A) * B)

print("Nabluzhennia paraboloy:")

print("a0=", jd[0])

print("a1=", jd[1])

print("a2=", jd[2])

print("f(x)=", jd[0], "+", jd[1], "*x + ", jd[2], "*x^2")

k = jd[0] + jd[1] * x + jd[2] * (x ** 2)

plt.plot(x, y, 'ro', label="експериментальні точки")

plt.plot(x, k, 'g-', label="наближення параболою")

plt.plot(x, f, 'b-', label="наближення прямою")

plt.title('Наближення прямою і параболою за допомогою МНК')

plt.xlabel('x')

plt.ylabel('y')

plt.legend()

plt.grid()

plt.show()