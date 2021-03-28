# iterator vs iterables

numbers = [1,2,3,4,5]   # Tuples, string, list ---- iterables
squares = map(lambda a:a**2, numbers)   # iterator

print(next(squares))
print(next(squares))
print(next(squares))

# for i in numbers:
    # print(i)

# number_iter = iter(numbers)
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter)) 