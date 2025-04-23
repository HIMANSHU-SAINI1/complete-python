amount=int(input("enter your amount"))

if(amount<1000):
    total=amount-amount*0.1
elif(amount>=1000 and amount<5000):
    total=amount-amount*0.15
elif(amount>=5000 and amount<10000):
    total=amount-amount*0.15
else:
    total=amount-amount*0.25
print("your total bill after discount is",total)