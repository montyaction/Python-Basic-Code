# Define a function that take two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

names = ['abc', 'abcdef', 'archana']

def find_pos(l,taget):
    for pos, name in enumerate(l):
        if name == taget:
            return pos
    return -1

print(find_pos(names,"archana"))