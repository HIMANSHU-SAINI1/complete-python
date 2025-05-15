# import sqlite3

# con=sqlite3.connect('uni.db')

# cur = con.cursor()
# for i in range(1,16):
#     roll=int(input('enter rollno'))
#     name=input("enter name")
#     city=input("enter city")
#     dno=int(input('enter deptno'))


#     cur.execute(f"insert into students values({roll},'{name}','{city}',{dno})")



# con.commit()
# cur.close()
# con.close()


import sqlite3

con=sqlite3.connect('uni.db')

cur = con.cursor()

rows= cur.execute('select * from dept')
# print(rows.fetchone())

print(rows.fetchmany(3))
cur.close()
con.close()
