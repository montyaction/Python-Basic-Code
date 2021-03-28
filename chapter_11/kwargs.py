# kwargs (keyword arguments)
# **kwargs (double star operator)

# wkargs as a parameter
# def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
# func(first_name = 'Mohit', last_name = 'Kanwar')

def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func(first_name = 'Mohit', last_name = 'Kanwar')

# dictionary unpacking
d = {'name' : 'archana', 'age' : 25}
func(**d)