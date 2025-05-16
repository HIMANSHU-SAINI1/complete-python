#find a pair of integars with highest product from any array
import array

def max_product(arr):
    x=arr[0]
    y=arr[1]

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j]>x*y:
                x=arr[i]
                y=arr[j]
    return x,y

arr=array.array('i',[2,3,4,5,6,7,9,8])

print('max product is: ', max_product(arr))