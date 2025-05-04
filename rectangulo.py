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
