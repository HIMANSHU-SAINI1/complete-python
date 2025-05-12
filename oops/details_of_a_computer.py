#inner class
class computer:
    def __init__(self,name,make,os):
        self.name=name
        self.cpu=self.cpu(make)
        self.os=self.os(os)
    def __str__(self):
        return 'name:'+self.name +'\nmake:'+self.cpu.get_make()+'\nOSname:'+self.os.get_name()
    
    class cpu:
        def __init__(self,make):
            self.make=make

        def get_make(self):
            return self.make
    class os:
        def __init__(self,os):
            self.name=os
        def get_name(self):
            return self.name
        
c1=computer('pc101','intel','windows')
print(c1)