import matplotlib.pyplot as plt
import numpy as np
import math 
a = 3.0
b = 1.0

def myPalette(x,y):
    return x**2+y**2
vcalc_z = np.vectorize(myPalette)
X = np.linspace(-5, 5, 1001)
Y = np.linspace(-5, 5, 1001)

def isInMS(x,y):
    count = 0
    xn = 0
    yn = 0
    for n in range(0,255):
        xn = xn**2 - yn**2 + x
        yn = 2*xn*yn + y
        length = math.sqrt(xn**2+yn**2)
        count += 1
        if (length  > 2):
            break
    if (count < 255):
        return xn+yn
    else:
        return 0
apply = np.vectorize(isInMS)

XX, YY = np.meshgrid(X, Y)

Z = np.sqrt((XX/a)**2+(YY/b)**2)
# temp = np.ones((X.size,Y.size))
# Z = apply(XX,YY)
plt.contour(XX,YY,Z)
plt.imshow(Z, extent=(X.min(), X.max(), Y.min(), Y.max()))
plt.title('Contour')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
