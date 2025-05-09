#zero division error handling
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# try:
#     c=a//b 
#     print(c)
# except:
#     print('zero division error,b should not be 0')

# print('end')


#index error handling
# l=input("enter elements of list separated by spaces").split()
# try:    
#     index=input("enter index value")
#     print(l[index])
# except:
#     print('invalid index or index error')
# print('end of program')

#multiple exception handling
# l=[10,20,30,40,50]

# try:
#     index=int(input("enter index number"))
#     print(l[index])
# except IndexError:
#     print('invalid index')
# except TypeError:
#     print('index should be integar')
# except:
#     print('some error')

# print('end of program')

#else block 
# a=10
# b=5
# try:
#     c=a//b
#     print(c)
# except:
#     print('b should not be 0')
# else:
#     print(c) #dependent statements in try block are written in else


#finally block
# def fun():
#     try:
#         x=int('246')
#         return x
#     except Exception as e:
#         raise e 
#     finally:
#         print('end of function')

# res=fun()
# print(res)


#user-defined exceptions
# class NegativeError(Exception):
#     def __init__(self):
#         self.msg='-ve dimensions'
#     def __str__(self):
#         return self.msg

# def area(length,breadth):
#     if length>=0 and breadth>=0:
#         a=length*breadth
#         return a
#     else:
#         raise NegativeError()
    
# print(area(-5,3))


#nested try except
L=[10,20,30,40,50]
try:
    try:
        index=int(input('enter index'))
    except ValueError as e:
        print(e)
    print(L[index])
except IndexError as e:
    print(e)
except Exception as e:
    print(e)