# Map function

numbers = [1,2,3,4,5]

def square(a):
    return a**2

squares = list(map(square, numbers))
print(squares)

# with lambda
squares = list(map(lambda a:a**2, numbers))
print(squares)

# list comphenion
squares_new = [i**2 for i in numbers]
print(squares)


# other method
new_list = []
for num in numbers:
    new_list.append(square(num))

print(new_list)


names = ['abc', 'abcd', 'abcde']
length = map(len, names)
for i in length:
    print(i)

length = list(map(len,names))
print(length)