#takes variable number of arguments and returns minimum value
def minimum(*val,low_limit=0):
    if low_limit is None:
        return min(val)
    else:
        l=[x for x in val if x>=low_limit]
        return min(l)
    
print(minimum(3,7,5,9,1,3,54))