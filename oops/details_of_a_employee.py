class employee:
    employee_count=101
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        self.employee_id='e'+str(employee.employee_count)
        employee.employee_count+=1


    def show_details(self):
        print('name: ',self.name)
        print('employee_id: ',self.employee_id)
        print('designation: ', self.designation)
        print('salary:',self.salary)


    @classmethod
    def total_employee(cls):
        return cls.employee_count-101


n=int(input("enter number of employees"))
employee_data=[]

for i in range(n):
    print(f'\n enter details for employees{i+1}:')
    name=input('name')
    designation=input('designation')
    salary=input('salary')
    employee_data.append((name,designation,salary))

employees=[]

for data in employee_data:
    emp=employee(*data)
    employees.append(emp)
    emp.show_details()
print(f'\n total employees created:{employee.total_employee()}')