# join split
# convert string to list

user_info = 'Archana','25'.split()
print(user_info)

name, age = 'Archana','25'.split()
print(name)
print(age)

name, age = input("Enter your name and age : ").split(',')
print(name)
print(age)


# Join method
# convert list to string

user_info = ['Archana','25']
print('&'.join(user_info))