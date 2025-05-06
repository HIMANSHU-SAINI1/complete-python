"""function to define cuboid"""
# def volume(length,breadth,height):
#     vol=length*breadth*height
#     return vol

# v=volume(10,5,3)
# print(v)


# def volume(l,b=1,h=1):
#     v=l*b*h
#     return v

# print(10)


# variable length positional arguments
# def fun(*args):
#     print(args)
# fun(10,30,29)

# iterators:
# l1=[5,6,7]
# it=iter(l1)
# print(next(it))


# generators:
# def myrange(n): #range like function
#     i=0
#     while i<n:
#         yield i  
#         i+=1
# m=myrange(4)
# print(next(m))  
# print(next(m))  
# print(next(m))  
# print(next(m))  


#generator for days of the week.
# def days():
#     d=['sun','mon','tue','wed','thu','fri','sat']
#     i=0
#     while True:
#         yield d[i]
#         i=(i+1)%7