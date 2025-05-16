'''canteen queue
students queue os based on roll number
rotate the queue in every meal'''

from collections import deque

students=deque([1,2,3,4,5,6,7,8,9,10])

def serve_food():
    print('students are served in order:', students)
    students.rotate(-1)

print('breakfast')
serve_food()
print('lunch')
serve_food()
print('dinner')
serve_food()