# Filter function

numbers = [3,4,6,9,8,5,4,2,13,1,10,15,17,20]
def is_even(a):
    return a%2 == 0

evens = tuple(filter(is_even, numbers))
print(evens)

# With lambda
evens1 = list(filter(lambda a:a%2==0, numbers ))
print(evens1)

for i in evens1:
    print(i)

# With list comprehenion
new_evens = [i for i in numbers if i%2==0]
print(new_evens)