from numpy import *
import numpy as np
import matplotlib.pyplot as plt

h = 0.2
x = np.array([2.4, 2.6, 2.8, 3.0, 3.2, 3.4])
y = np.array([3.526, 3.782, 3.945, 4.043, 4.104, 4.155])
delta1_y = []
delta1_y = np.diff(y)
print("delta1_y=", delta1_y)
delta2_y = []
delta2_y = np.diff(delta1_y)
print("delta2_y=", delta2_y)
delta3_y = []
delta3_y = np.diff(delta2_y)
print("delta3_y=", delta3_y)
delta4_y = []
delta4_y = np.diff(delta3_y)
print("delta4_y=", delta4_y)

y1 = (1 / h) * (delta1_y[1] - ((delta2_y[1]) / 2) + ((delta3_y[1]) / 3) - ((delta4_y[1]) / 4))

y2 = (1 / h ** 2) * (delta2_y[1] - delta3_y[1] + (11 / 12) * delta4_y[1])

print("y'= ", y1)
print("y''= ", y2)