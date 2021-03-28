# *args with normal parameter

def multipy_nums(num1, num2 , *args):
    multiply = 1
    # print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multipy_nums(1,4,3,4))
