maths=int(input("enter maths marks"))
chem=int(input("enter chem marks"))
phy=int(input("enter phy marks"))

if(maths>=35 and maths<=100) and (chem>=35 and chem<=100) and (phy>=35 and phy<=100):
    print("passed")
else:
    print("failed")