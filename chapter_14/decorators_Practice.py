from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'You are calling {function.__name__} function')
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def addition(a,b):
    '''This function take two numbers as arguments and return their sum '''
    return a+b

print(addition(4,5))
# output
# you are calling add function
# This function take two number as parameters and return their sum
# 9