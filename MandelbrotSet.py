import matplotlib.pyplot as plt
import numpy as np
import math 
a = 3.0
b = 1.0

def myPalette(x,y):
    return x**2+y**2
vcalc_z = np.vectorize(myPalette)
pointNum = 500
X = np.linspace(-2.025, 0.6, pointNum+1)
Y = np.linspace(-1.125, 1.125, pointNum+1)
maxDis = math.sqrt((X.max() - X.min())**2 + (Y.max()-Y.min())**2)

def isInMS(x,y):
    count = 0
    xn = 0
    yn = 0
    N = 2000
    for n in range(0,N):
        xn = xn**2 - yn**2 + x
        yn = 2*xn*yn + y
        length = math.sqrt(xn**2+yn**2)
        count += 1
        if (length  > 2):
            break
    if (count < N):
        return length / maxDis
    else:
        return 0
apply = np.vectorize(isInMS)

XX, YY = np.meshgrid(X, Y)
Z = apply(XX,YY)
plt.imshow(Z, extent=(X.min(), X.max(), Y.min(), Y.max()))
plt.title('Mandelbrot Set')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
