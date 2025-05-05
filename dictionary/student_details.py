#create dictionary with student details

students={}

for i in range(3):
    name=input('enter name')
    roll=int(input('enter roll'))
    dept=input('enter dept')

students[name]={'roll':roll,'name':name,'dept':dept}

print(students)