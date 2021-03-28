# any, all function
numbers1 = [2,4,6,8,10]
print(all([num%2==0 for num in numbers1]))

numbers2 = [1,2,3,4,5,6]
print(any([num%2==0 for num in numbers2]))

# evens1 = []
# for num in numbers1:
    # evens1.append(num%2==0)

# print(evens1)

# print(all([True, True, True, True, True]))