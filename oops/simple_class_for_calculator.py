class calculator:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b 
    
    @staticmethod
    def mul(a,b):
        return a*b 
    
    @staticmethod
    def div(a,b):
        return a/b 
    
x=int(input("enter first number"))
y=int(input("enter second number"))

print(calculator.add(x,y))
print(calculator.sub(x,y))
print(calculator.mul(x,y))
print(calculator.div(x,y))