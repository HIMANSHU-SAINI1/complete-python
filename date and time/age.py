#calculate age of a person
from datetime import date

def age(dob):
    today=date.today()
    years=today.year-dob.year
    
    if(today.month,today.day)<(dob.month,dob.day):
        years-=1
        return years
    
print('age:',age(date(2003,11,16)))