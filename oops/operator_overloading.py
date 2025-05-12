#operator overloading
class angle:
    def __init__(self,deg):
        self.degree=deg
    
    def __add__(self,ang):
        sum=angle(self.degree+ang.degree)
        return sum
    
    def __str__(self):
        return 'degree' + str(self.degree)
    
a1=angle(30)
a2=angle(45)

a3=a1+a2
print(a3)