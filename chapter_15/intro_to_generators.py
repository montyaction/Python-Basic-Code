# Genrators
# Genrators are iterators

# iterator, iterable

l = [1,2,3]     # iterable

# for i in l:
    # print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

for num in map(lambda a :a**2, l):      #iterator
    print(num)


# l - [1,4,9,16]
# memory --->[.....................................], list
# memory --->[4]