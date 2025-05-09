#to read a file
file= open('C:\\Users\\hp\\OneDrive\\Desktop\\python\\file handling\\file.txt','r') # to open and read the file
str1=file.read()
print(str1)
file.close()


#to write a file
file=open('demo.txt','w')
file.write('hello\n')
file.write('how are you\n')
file.close()


#to append a file
file=open('demo.txt','a')
file.write('i am learning python')
file.close()


#to read and write
file=open('demo.txt','r+')
str1=file.read(10)
print(str1)

file.write('practising file handling')
file.close()


#to write and read
file=open('demo.txt','w+')
file.write('good bye')

str1=file.read(15)
print(str1)
file.close()


#to append and read
file=open('demo.txt','a')
file.write('done')

file.close()