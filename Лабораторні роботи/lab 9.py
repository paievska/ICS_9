import numpy as np
import matplotlib.pyplot as plt
import math

mas_x = np.array([0,0.2,0.4,0.6,0.8,1])
mas_y = np.array([1.2715,2.4652,3.6443,4.8095,5.9614,7.1005])
h=mas_x[1]-mas_x[0]
x1=0.1
x2= 0.9
g1=((x1-mas_x[0])/h)
g2=((x2-mas_x[5])/h)
def  y(mas_y,j):
   mas=[]
   for i in range(1,len(mas_y)):
      mas.append(mas_y[i]-mas_y[i-1])
   if j==1:
      return mas
   else:
      j-=1
   return y(mas,j)
y1=(mas_y[0]+(g1*(y(mas_y,1)[0]))+(((g1*(g1-1))/math.factorial(2))*(y(mas_y,2)[0]))+(((g1*(g1-1)*(g1-2))/math.factorial(3))*(y(mas_y,3)[0]))+(((g1*(g1-1)*(g1-2)*(g1-3))/math.factorial(4))*(y(mas_y,4)[0]))+(((g1*(g1-1)*(g1-2)*(g1-3)*(g1-4))/math.factorial(5))*(y(mas_y,5)[0])))
y2=(mas_y[5]+(g2*(y(mas_y,1)[4]))+(((g2*(g2+1))/math.factorial(2))*(y(mas_y,2)[3]))+(((g2*(g2+1)*(g1+2))/math.factorial(3))*(y(mas_y,3)[2]))+(((g2*(g2+1)*(g2+2)*(g2+3))/math.factorial(4))*(y(mas_y,4)[1]))+(((g2*(g2-1)*(g2-2)*(g2-3)*(g2-4))/math.factorial(5))*(y(mas_y,5)[0])))

print("f(0.1)= ", y1)
print("f(0.9)= ", y2)
plt.plot(mas_x,mas_y, "g--")
plt.show()