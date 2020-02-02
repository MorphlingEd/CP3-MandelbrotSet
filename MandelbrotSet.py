import matplotlib.pyplot as plt
import numpy as np
import math 

class mandelbrot(object):
    
    def __init__(self,width = 800, height = 600,maxIter = 255):
        """Initialize the picture's width,height and max times of iteration"""
        xmin = -2.025
        xmax = 0.6
        ymin = -1.125
        ymax = 1.125
        self.width = 800
        self.height = 600
        self.maxIter = 255
        self.X = np.linspace(xmin,xmax,self.width)
        self.Y = np.linspace(ymin,ymax,self.height)


    def mandelbrot_point(self,c):
        """ method used to determine whether this point belongs to mandelbrot set
        If so returns 0, otherwise return the iteration times"""
        z = 0
        for n in range(self.maxIter):
            if (abs(z) > 2) :
                return n/self.maxIter
            z = z*z + c
        return 0
    
    
    def mandelbrot_set(self):
        """method to determine each point's value in the picture applying
        mandelbrot_point to each point and creates a new 2D array"""
        Z = np.empty((self.width,self.height))
        for i in range(self.width):
            for j in range(self.height):
                Z[i,j] = self.mandelbrot_point(self.X[i] + 1j * self.Y[j])
        return Z
    
    def run(self):
        """method to generate the pciture"""
        X = self.X
        Y = self.Y
        Z = self.mandelbrot_set()

        """Using imshow method to color each pixel depending on this point's value returned
        from mandelbrot_point method"""
        plt.imshow(Z.T,extent = (X.min(),X.max(),Y.min(),Y.max()))
        plt.title('Mandelbrot Set')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    

def main():
    m = mandelbrot()
    m.run()


main()
    
    

