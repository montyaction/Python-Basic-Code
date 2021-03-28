# Define two list l1, l2
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]

# for this list 
l = [ (1,2), (3,4), (5,6), (7,8)]

# * operator with zip

print(list(zip(*l)))

l1, l2 =list(zip(*l))
print(f'Tuple list1 is = {l1}')
print(f'Tuple list2 is = {l2}')

# convert to list
list1 = list(l1)
print(f'list1 is = {list1}')

list2 = list(l2)
print(f"list2 is = {list2}")

l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)
