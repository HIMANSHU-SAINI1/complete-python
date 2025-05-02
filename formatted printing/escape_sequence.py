print("hello\nworld")  #new line
print("hello\rworld")   #carriage return
print("hello\fworld")   #line feed
print("hello\tworld")   #tab
print("hello\vworld")    #vertical tab
print("hello\bworld")     #backspace
print("hello\a")        #alert



print("line1" \
"line2")     #ignore newline

print("c:\\")     #backslash

print("himanshu\'s")    #quote

print("\101\102")   #octal

print("\x41")     #hexadecimal



print("\x41")    #2 digit hexa
print("\u0041")  #4 digit hexa
print("\U00000041")  #8 digit hexa
print("\N{dollar sign}")    #name in unicode database
print("\N{dollar sign}")    #name in unicode database
print("\N{grinning face}")  #name in unicode database


#print arguments
print('hello',5,12.75)    #print can take multiple objects as input
print('hello',5,12.54,sep='*',end='\t')   #the separator and end statement of print can be changed
print("world")
print(object,sep='',end='\n',file=SystemError,flush=True) #dispaly and forcefully we can flush something in print