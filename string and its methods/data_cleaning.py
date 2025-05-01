scan=input("enter data to clean")
clean=''
for x in scan:
    if x.isalpha() or x.isspace():
        clean=clean+x
    else:
        clean=clean+' '
print(clean)