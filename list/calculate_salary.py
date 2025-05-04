work_hours=[int(x) for x in input("enter work hours and give space after every work day").split()]
per_hour_salary=int(input("enter hourly salary"))

total=sum(work_hours)
salary=total*per_hour_salary

print("salary is: ",salary)

