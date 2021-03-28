# five = 5
def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('OOPs you are passing wrong data type to faction')
print(add(4, 3))