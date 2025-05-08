# n=int(input("enter the number for factorial"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial is:",fact)




n=int(input("enter the number for factorial"))
def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))