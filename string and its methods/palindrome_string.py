s1=input("enter the string")
s2=s1.replace(' ','')
rev=s2[::-1]
if s2.casefold()==rev.casefold():
    print(s1)
else:
    palindrome=s2.casefold()+rev.casefold()
    print(palindrome)                                       