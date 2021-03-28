# You have to have a complete understanding of functions,
# first class function / closures
# then finally we will learn about decorators

def square(a):
    return a**2

s = square
print(s(5))

print(s.__name__)
print(square.__name__)
print(s)
print(square)