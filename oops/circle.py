from math import *
class circle:
    def __init__(self,r):
        self.radius=radius
    
    def area(self):
        return pi*self.radius*self.radius

    def perimeter(self):
        return 2*pi*self.radius

radius=int(input('enter radius of circle'))
c=circle(radius)

print('area',c.area())
print('perimeter',c.perimeter())

