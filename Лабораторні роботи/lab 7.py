from numpy import *
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-4, -2, 0, 3])
y = np.array([-18, 8, -6, 3])


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1;
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


t = float(input("enter x:"))
print("x= ", t)
print("L=", lagranz(x, y, t))

xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagranz(x, y, i) for i in xnew]
plt.xlabel('x')  # позначення вісі абсцис
plt.ylabel('f(x)')  # позначення е вісі ординат
plt.plot(x, y, 'o', xnew, ynew)
plt.grid()
plt.legend(['f(x)', 'x^3+x^2-9*x-6'])
plt.show()