import math

def fun(x):
    return 4 * x * x * x * x - 4 * x * x * x + 2 * x * x - 3 * x - 9


def fun1(x):
    return 16 * x * x * x - 12 * x * x + 4 * x - 3


def fun2(x):
    return 48 * x * x - 24 * x + 4


def NewtonMethod(a, b, e):
    condition = True
    f = fun1(b)
    f2 = fun2(b)
    if f * f2 > 0:
        x = b
    else:
        x = a
    while condition:
        f1 = fun1(x)
        f1_2 = fun2(x)
        h = f1 / f1_2
        x = x - h
        condition = abs(h) <= e
    print("x= ", x, "f(x)= ", fun(x))


def comb(a, b, e):
    if fun(a) * fun2(a) < 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    xp1 = a0
    xp2 = b0

    xn2 = xp2 - fun(xp2) * (xp2 - xp1) / (fun(xp2) - fun(xp1))
    xn1 = xp1 - fun(xp1) / fun1(xp1) if fun1(xp1) != 0 else 0
    xp2 = xn1
    xp1 = xn2

    while abs(xp2 - xp1) > e:
        xn2 = xp2 - fun(xp2) * (xp2 - xp1) / (fun(xp2) - fun(xp1))
        xn1 = xp1 - fun(xp1) / fun1(xp1) if fun1(xp1) != 0 else 0
        xp2 = xn1
        xp1 = xn2
    x = (xp1 + xp2) / 2
    print("comb=", x)



NewtonMethod(-1, 3 / 4, 0.001)
NewtonMethod(3 / 4, 5, 0.001)
comb(-1, 3 / 4, 0.001)
comb(3 / 4, 5, 0.001)