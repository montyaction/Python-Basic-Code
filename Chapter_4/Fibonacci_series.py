# Fibonacci series
# 0 1 1 2 3 5 8 13 21 34

for i in range(1,11):
    print(i, end = " ")

def fibonacci_seq(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)