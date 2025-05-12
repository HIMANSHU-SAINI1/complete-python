# #INTER-PROCESS COMMUNICATION
# from threading import *
# from time import *
# class mydata:
#     def __init__(self):
#         self.data=0
#         self.flag=False
#         self.lock=Lock()

#     def put(self,d):
#         while self.flag!=False:
#             pass
#         self.lock.acquire()
#         self.data=d
#         self.flag=True
#         self.lock.release()

#     def get(self):
#         while self.flag!=True:
#             pass
#         self.lock.acquire()
#         x=self.data
#         self.flag=False
#         self.lock.release()
#         return x
    
# def producer(data):
#     i=1
#     while True:
#         data.put(i)
#         print('producer:', i)
#         i+=1

# def consumer(data):
#     while True:
#         x=data.get()
#         print('consumer:', x)

# data=mydata()
# t1=Thread(target=lambda:producer(data))
# t2=Thread(target=lambda:consumer(data))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# int-proc comm using condition


# from threading import *
# from time import *
# class mydata:
#     def __init__(self):
#         self.data=0
#         self.cv=Condition()

#     def put(self,d):
#         self.cv.acquire()
#         self.cv.wait()
#         self.data=d
#         self.cv.notify()
#         self.cv.release()

#     def get(self):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         x=self.data
#         self.cv.notify()
#         self.cv.release()
#         return x
    
# def producer(data):
#     i=1
#     while True:
#         data.put(i)
#         print('producer:', i)
#         i+=1

# def consumer(data):
#     while True:
#         x=data.get()
#         print('consumer:', x)

# data=mydata()
# t1=Thread(target=lambda:producer(data))
# t2=Thread(target=lambda:consumer(data))

# t1.start()
# t2.start()

# t1.join()
# t2.join()



#int-proc comm using queue
from threading import *
from time import *
from queue import *

q=Queue()

def producer(data):
    i=1
    while True:
        q.put(i)
        print('producer:', i)
        sleep(1)
        i+=1

def consumer(data):
    while True:
        x=q.get()
        print('consumer:', x)
        sleep(1)
t1=Thread(target=lambda:producer(q))
t2=Thread(target=lambda:consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()