# strings
name = 'archana'

# Srring Indexing
# print(name[1])
# print(name[-1])

# String slicing
# print(name[0:5])
# print(name[0:-2])
# print(name[0:])
# print(name[-4:])
# print(name[:-2])
# print(name[0:5:2])
# print(name[-1:0:-1])

# # Take user input
# age = int(input('Enter your age : '))
# print(age)

# # Take two user input
# user_name, age = input('Enter your name and age : ').split(',')
# print(user_name)
# print(age)

# # Len function
# print(len(name))

# # Lower, apper, title methods
print(name.lower())
print(name.upper())
print(name.title())

# # find, replace, center methods
print(name.find('r'))
print(name.find('a',1))
a_pos = name.find('a')
a_pos2 = name.find('a',a_pos + 1)
print(a_pos2)

print(name.replace('n','N'))

print(name.center(11,'*'))

# # 
print(name)