#insert items in a list in sorted order
import bisect

def insertion_sort(ele):
    sorted_list=[]

    for e in ele:
        bisect.insort(sorted_list,e)

    return sorted_list

ele=[2,4,6,8,10,1,3,5,7,9]
s_list=insertion_sort(ele)

print('sorted list is:', s_list)
