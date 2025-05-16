#find kth largest element

import heapq

def kth_largest(ele,k):
    sorted_list=[]

    for e in ele:
        heapq.heappush(sorted_list,-e)

    for i in range(k-1):
        heapq.heappop(sorted_list)

    return -heapq.heappop(sorted_list)

element=[10,20,30,40,90,64,89,70,6]

print('kth largest number is:', kth_largest(element,1))