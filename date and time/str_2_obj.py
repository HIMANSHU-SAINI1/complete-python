#string date to date object
import datetime

str_date=input('ener date in DD-MM-YYYY format')
d,m,y=str_date.split('-')
d1=datetime.date(int(y),int(m),int(d))
print('date: ', d1)