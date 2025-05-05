#create a dictionary for country names in alphabetically order

# countries={'a':['america','alaska','argentina'],
#            'b':['bhutan','brazil','bahrain'],
#            'c':['china','coasta rica','cuba']}


countries={}
for i in range(4):
    name=input('enter country name')
    if name[0].upper() not in countries:
        countries[name[0].upper()]=[name]
    else:
        countries[name[0].upper()].append(name)

print(countries)