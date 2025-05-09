with open('my.data','rb') as f:
    print(f.read(5).decode())
    f.seek(-3,1)
    print(f.read(1).decode())