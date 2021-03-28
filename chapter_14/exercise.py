# Exercise decorator
import time

t1 = time.time()
print('This is line one ')
x = 5
if x == 5 :
    print( 'X is equal to 5')
print('this is line two')
t2 = time.time()
print(t2-t1)

# @calculate_time
# def func():
    # print('this is function')

# func()
# this function took 3 sec to run