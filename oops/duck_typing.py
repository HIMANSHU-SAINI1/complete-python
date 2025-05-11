class duck:
    def talk(self):
        print('duck talking')
    
    def walk(self):
        print('duck talking')

class dog:
    def talk(self):
        print('dog talking')
    
    def walk(self):
        print('dog walking')

def person(pet):
    pet.talk()
    pet.walk()
duck=duck() 
person(duck)