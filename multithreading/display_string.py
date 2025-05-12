#mutex
from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()

l=Lock()

t1=Thread(target=display,args=('hello world',))
t2=Thread(target=display,args=('you are welcome',))

t1.start()
t2.start()

t1.join()
t2.join()


#semaphore
from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()

l=Semaphore(1)

t1=Thread(target=display,args=('hello world',))
t2=Thread(target=display,args=('you are welcome',))

t1.start()
t2.start()

t1.join()
t2.join()