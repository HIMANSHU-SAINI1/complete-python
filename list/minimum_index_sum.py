l1=['pizza','burger','chowmein','dosa','sweets']
l2=['dosa','burger','pizza','sweets','chowmein']

index1=len(l1)+1
index2=len(l2)+1

for i in range(len(l1)):
    i1=l2.index(l1[i])
    
    if i+i1 < index1 + index2:
        index1=i
        index2=i1
print(l1[index1],index1+index2)