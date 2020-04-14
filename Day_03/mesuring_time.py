import time
import random

start_time=time.clock()

ys=[]
for rep in range(100000):
    y=0
    for k in range(10):
        x= random.choice([1,2,3,4,5,6])
        y=y+x
    ys.append(y)

end_time=time.clock()
value=end_time-start_time
print(value)