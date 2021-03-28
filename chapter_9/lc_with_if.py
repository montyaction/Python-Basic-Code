# list comprehendion with if statement

numbers = list(range(1,11))
# print(numbers)

nums = []
for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)

even_nums = [i for i in numbers if i%2 == 0]
even_nums2 = [i for i in range(1,11)if i %2 == 0]
odd_nums = [i for i in range(1,11) if i%2 != 0]

print(even_nums)
print(even_nums2)
print(odd_nums)