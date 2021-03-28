# lambda expression practice
# def is_even(a):
    # if a %2 == 0:
        # return True
    # else:
        # return False

# def is_even(a):
    # if a %2 == 0:
        # return True
    
    # return False

def is_even(a):
    return a %2 == 0

print(is_even(5))

lambda2 = lambda a : a%2==0
print(lambda2(6))

# def last_char(s):
    # return s[-1]

last_char2 = lambda s : s[-1]
print(last_char2('Archana'))


# lambda with if , else
def func(s):
    if len(s) > 5:
        return True
    return False

func2 = lambda s : True if len(s) > 5 else False
func3 = lambda s : len(s) > 5
print(func2('abcd'))
print(func3('Archana'))