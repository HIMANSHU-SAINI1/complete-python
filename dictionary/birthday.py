birthdays={
    'sachin':'03/04/1989',
    'carl': '31/12/2002',
    'himannshu':'16/11/2003'}

name=input("enter name")

if name in birthdays:
    print(birthdays[name])
else:
    print("name is not found")