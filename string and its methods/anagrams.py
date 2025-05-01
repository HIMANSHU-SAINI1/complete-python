phrase1=input("enter phrase1")
phrase2=input("enter phrase2")
s1=phrase1.lower()
s2=phrase2.lower()

if len(s1)!=len(s2):
    print("not anagram")
else:
    for x in s1:
        if x not in s2:
            print("not anagram")
            break;
        else:
            print("anagram")    
    
