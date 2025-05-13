#find time taken for a code to execute
import datetime

start_time=datetime.datetime.now()

for i in range(1000000):
    pass
end_time=datetime.datetime.now()

print('execution time: ', end_time-start_time)