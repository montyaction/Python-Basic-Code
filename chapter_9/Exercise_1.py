# define a function that take list of strings
# list containing reverse of every string

# NOTE - USE LIST COMPREHENSION because we already did this exercise
# using normal method

# example
# l = ['abc', 'vut', 'zyx']
# reverse_string(l) ----> ['cba', 'tuv', 'zyx']


def reverse_strings(l):
    return[name[::-1]for name in l] 
print(reverse_strings(['abc', 'vut', 'zyx']))

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list

print(reverse_str(['abc', 'vut', 'zyx']))