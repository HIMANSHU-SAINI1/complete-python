f=open("C:\\Users\\hp\\OneDrive\\Desktop\\python\\file handling\\p.jpeg",'rb')
data=f.read()

cp=open('p.jpeg','wb')
cp.write(data)
f.close()
cp.close()