list1=[1,2,2,3,1,4,5,6,7,8,3,6,1]
list2=[]

for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)


