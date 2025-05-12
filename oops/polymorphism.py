class cat:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def info(self):
        print('my name is'+self.name+'. my age is'+str(self.age))  

    def make_sound(self):
        print('mew mew')

class dog:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def info(self):
        print('my name is' +self.name+'. my age is'+str(self.age))  

    def make_sound(self):
        print('bow wow')


def my_pet(pet):
    pet.info()
    pet.make_sound()
c=cat('kitty',2)
d=dog('dog',3)
my_pet(d)