import student,pickle

studs=[student.student(10,'john','cs'),student.student(20,'ajay','ec'),student.student(25,'himanshu','ds')]

with open('students.data','ab') as f:
    for s in studs:
        pickle.dump(s,f)
        