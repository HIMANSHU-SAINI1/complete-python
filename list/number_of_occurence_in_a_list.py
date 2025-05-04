l1=['a','b','c','d','e','a','c','b','a','e']
result=[]

for x in l1:
    if x not in result:
        result.append(x)
        count=l1.count(x)
        result.append(count)
print(result)