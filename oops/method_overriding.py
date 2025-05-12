#method overriding
import math
class shape:
    def __init__(self,name):
        self.name=name
    
    def area(self):
        print('shape area')

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    

class circle(shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return math.pi*(self.radius**2)

r=rectangle(10,5)
print('area',r.area())