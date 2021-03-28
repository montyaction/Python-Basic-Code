# We use enumerate function with for loop to track position of our
# item in iterable


# How we can do this without enumerate function
names = ['abc', 'abcdef', 'archana']
# 0 -- 'abc'
# 1 -- 'abcdef'
# pos = 0
# for name in names:
#     print(f"{pos} ----> {name} ")
#     pos += 1


# with enumerate function
for pos, name in enumerate(names):
    print(f"{pos} ----> {name}")
 