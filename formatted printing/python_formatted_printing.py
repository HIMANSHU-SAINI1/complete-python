item='memory'
size=32
price=11.75

print("{0}GB {1} in ${2}".format(size,item,price))
#or there is another method for formatting in python
print(f"{size}GB {item:^10} in ${price}")




data=100
print("start {0:<15b} end".format(data))


#flags
# :<     :^      :>     :+     :-  for alignment

#conversion
# d=decimal   b=binary  o=octal x=hexa    f=float   f=float    g=general float  e=scientific exponent   ,=separated by comma    _=same as comma        %= for percentage sign