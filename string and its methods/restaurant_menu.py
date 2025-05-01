

    # item1=input("enter name of item")
    # price1=input("enter price of items")
    # dots=20-len(item1)-len(price1)



    # item2=input("enter name of item")
    # price2=input("enter price of items")
    # dash=20-len(item2)-len(price2)



    # item3=input("enter name of item")
    # price3=input("enter price of items")
    # dash=20-len(item3)-len(price3)



    # item4=input("enter name of item")
    # price4=input("enter price of items")
    # dash=20-len(item4)-len(price4)
    # print(item1+('-'*30)+price1)
    # print(item2+('-'*30)+price2)
    # print(item3+('-'*30)+price3)
    # print(item4+('-'*30)+price4)





menu=[]

for i in range(4):
    item=input("enter name of item")
    price=input("enter price of item")
    menu.append((item,price))
print("\nmenu")
for item,price in menu:
    dots="."*(20-len(item)-len(price))
    print(item + dots + price)