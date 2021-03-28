import time
# list vs generator
# memory usage , time
# when to use list, when to use generator

# t1 = time.time()
# l = [ i**2 for i in range(10000000)]    # 10 million
# t2 = time.time()
# print(t2-t1)

t1 = time.time()
g = ( i**2 for i in range(10000000))    # 10 million
t2 = time.time()
print(t2-t1)