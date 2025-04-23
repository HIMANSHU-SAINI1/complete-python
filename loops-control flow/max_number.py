n=int(input("enter number"))
print("enter",n,"numbers")
i=0
maximum=float("-inf")
minimum=float("inf")
while i<n:
    x=int(input(""))
    if x>maximum:
        maximum=x
    if x<minimum:
        minimum=x
    i+=1
print("max",maximum)
print("min",minimum)