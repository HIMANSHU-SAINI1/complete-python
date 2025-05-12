class customer:
    def __init__(self,name,phoneno):
        self.name=name 
        self.phoneno=phoneno


    def set_phoneno(self,ph):
        self.phoneno=ph

    def get_phoneno(self):
        return self.phoneno
    
    def get_name(self):
        return self.name
    
    
    


c1=customer('john',7650941234)

print('name:',c1.get_name())
print('phone no: ',c1.get_phoneno())

c1.set_phoneno(9876543219)
print(' ')
print('name: ',c1.get_name())
print('phone no:', c1.get_phoneno())