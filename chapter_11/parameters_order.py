# functions with all parameters
# very important to understand

# PACK

# parameters
# args
# default parameters
# **kwargs

# def func (name = 'Unknown', age = 25):
    # print(name)
    # print(age)

# func('Archana', 26)

def func(name,*args,last_name = 'Unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Archana', 1,2,3, a = 1, b =2)

def func2(name, last_name =)