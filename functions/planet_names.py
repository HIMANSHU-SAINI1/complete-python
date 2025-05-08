#find planet name by id
def planet(id):
    planets={1:'mercury',2:'venus',3:'earth',4:'mars',5:'jupiter',6:'saturn',7:'uranus',8:'neptune',9:'pluto'}
    return planets[id]
id=int(input('enter planet ID'))
if id<10:
    if id>0:
        p=planet(id)
        print('planet name is:',p)
else:
    print("please enter the id between 0-9")