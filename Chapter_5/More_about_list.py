# Generate lists with range function

numbers = list(range(1,21))
# # print(numbers)

# # More about pop method

popped_item = numbers.pop()
print(numbers)
print(popped_item)

# Index method
number = [1,2,3,4,5,6,7,8,9,10,1,5,7,8,1]
print(number.index(1, 3))

# Pass list to a function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(number))
