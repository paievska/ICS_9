from numpy import *
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x=[1.1,1.4,1.9,2.4,2.7]
y=[2.91,3.64,4.55,2.47,0.24]

spl=UnivariateSpline(x,y)
xs=linspace(0,4.6,1000)
plt.plot(x,y,"ro",xs,spl(xs),'g',lw=3)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Графік кубічного слайну")
plt.grid()
plt.legend(["вузли","інтерполяція"],loc="lower right")
plt.show()