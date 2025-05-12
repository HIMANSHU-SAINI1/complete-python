import math

class polygon:
    def __init__(self,ns,*sides):
        self.no_of_sides=ns
        self.sides=sides[:ns]

class triangle(polygon):
    def __init__(self, ns, *sides):
        polygon.__init__(self,ns, *sides)    
    
    def area(self):
        a,b,c= self.sides
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
    
t1=triangle(3,10,15,9)
print('area is:', t1.area())