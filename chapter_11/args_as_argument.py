def multipy_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

nums = [1,2,3,4]

print(multipy_nums(*nums))  # unpack