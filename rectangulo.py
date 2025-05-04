import math

class Rectangle:
    def __init__(self,xmin,ymin,xmax,ymax):
        if xmin >= xmax:
            raise ValueError("Xmin debe ser menor que Xmax")
        if ymin >= ymax:
            raise ValueError("Ymin debe ser menor que Ymax")

        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
    
    def area(self):
        return (self.xmax - self.xmin)*(self.ymax - self.ymin)

    def perimetro(self):
        return (self.xmax-self.xmin)*2 + (self.ymax - self.ymin)*2

    def centro(self):
        xcentro = (self.xmax - self.xmin)/2
        ycentro = (self.ymax - self.ymin)/2
        return(xcentro, ycentro)
    
    def diagonal(self):
        return math.sqrt((self.xmax - self.xmin)**2 + (self.ymax - self.ymin)**2)




