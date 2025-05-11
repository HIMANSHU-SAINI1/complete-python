#how to write a class for rectangle class for calculating its area and perimeter
class rectangle:
    count=0
    def __init__(self,length,breadth):
        self.set_length(length)
        self.set_breadth(breadth) 
        rectangle.count+=1

    def get_length(self):
        return self.length
    
    def set_length(self,length):
        if length>=0:
            self.length=length
        else:
            self.length=1

    def set_breadth(self,breadth):
        if breadth>=0:
            self.breadth=breadth
        else:
            self.breadth=1

    def get_breadth(self):
        return self.breadth
    def area(self):   #instance methods
        return self.length*self.breadth
    

    def perimeter(self):  #instance methods
        return 2*(self.length+self.breadth)
    

    @classmethod
    def countrect(cls):
        print(cls.count)


    @staticmethod
    def issquare(length,breadth):
        return length==breadth

    
length=int(input('enter the length of rectangle'))
breadth=int(input('enter breadth of the rectangle'))


r=rectangle(length,breadth)
print(r.issquare(length,breadth))
print(r.get_length())
print(r.get_breadth())
print('length',r.length)
print('breadth',r.breadth)
print('area',r.area())
print('perimeter',r.perimeter())


class cuboid(rectangle):
    def __init__(self,length,breadth,height):
        self.height=height
        super().__init__(length,breadth)
    
    def set_height(self,height):
        if height>=0:
            self.height=height
        else:
            self.height=1
    
    def get_height(self):
        return self.height
    
    def volume(self):
        return self.length*self.breadth*self.height
    
height=int(input("enter height of the object"))
r=cuboid(length,breadth,height)
print('height',r.height)
print('volume',r.volume())