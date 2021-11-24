import numpy as np
A = np.matrix([[1, 2, 1], [3, -5, 3], [2, 7, -1]])
B = np.matrix([[4], [1], [8]])

d = np.linalg.solve(A, B)


def gauss(A, B):
    n = len(B)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A[i, k] != 0.0:
                rat = A[i, k] / A[k, k]
                A[i, k + 1:n] = A[i, k + 1:n] - rat * A[k, k + 1:n]
                B[i] = B[i] - rat * B[k]

    for k in range(n - 1, -1, -1):
        B[k] = (B[k] - np.dot(A[k, k + 1:n], B[k + 1:n])) / A[k, k]
    return B


def jordgas():
    jd = np.linalg.inv(A) * B
    return jd


print("Perevirka", d)
print("Print jordgauss", jordgas())
print("Print gauss", gauss(A, B))