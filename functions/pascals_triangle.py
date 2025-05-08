#print n rows of pascals triangle
def pascal(n):
    r=[1]
    for i in range(n):
        print(r)
        tr=[0]+r
        r=r+[0]
        r=[x+y for x,y in zip(r,tr)]
n=int(input("enter number of rows required"))
pascal(n)
