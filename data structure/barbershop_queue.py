#barbershop queue
from collections import deque

customers = deque()

def walk_in(customer):
    customers.append(customer)

def serviced():
    cust=customers.popleft()
    print(cust,'leaves the shop')

walk_in('john')
walk_in('himanshu')
walk_in('ankit')

serviced()
serviced()
print(customers)