#implement heap sort

import heapq

def heap_sort(elements):
    heapq.heapify(elements)
    sorted_list=[]
    
    for i in range(len(elements)):
        x=heapq.heappop(elements)
        sorted_list.append(x)

    return sorted_list


elements=[12,14,8,7,3,-5,6,2]
sorted_list=heap_sort(elements)
print('sorted list is:', sorted_list)