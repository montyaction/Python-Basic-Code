# LIST COMPREHENSION summary
# square = []
# for i in range(1,11):
#     square.append(i**2)

# print(square)

# square = [i**2 for i in range(1,11)]
# print(square)

# even_num = [i for i in range(1,11)if i%2 == 0]
# print(even_num)

#  if else

# mixed = [i*2 if (i%2==0) else -i for i in range(1,11)]
# print(mixed)

nl = [[1,2,3],[1,2,3],[1,2,3]]
new_list = [[i for i in range(1,5)]for j in range(4)]
print(new_list)

new_list2 = []
for j in range(3):
    new_list2.append([1,2,3,4])