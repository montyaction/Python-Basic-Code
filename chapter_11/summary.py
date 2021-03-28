def add(a,b):
    return a + b

def new_add(*args):
    total = 0
    for num in args:
        total += num
    return total

# print(new_add(1,2,3))

# l = [1,2,3,4]
# print(new_add(*l))

# kwargs keyword arguments , **
# def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))

# func(name = 'Archana', age = 25)

# *args , **kwargs , normal parameter , default parameter
# PADK - parameter , args , default , kwargs

def func2(name,*args,last_name = 'Unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func2('Archana', 1,2,3,4,a = 1, b =2)
