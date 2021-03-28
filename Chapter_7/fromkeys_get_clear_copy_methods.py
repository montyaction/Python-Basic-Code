# fromkeys
# d = {'name' : 'Unknown', 'age' : 'Unknown'}
# d = dict.fromkeys(['name','age','height'],'Unknown')
# d = dict.fromkeys(('name','age','height'),'Unknown')
# d = dict.fromkeys("abc",'Unknown')
# d = dict.fromkeys(range(1,11),'Unknown')
# d = dict.fromkeys(['name','age'],['Unknown','unknown'])
# print(d)


# get method
d = {'name' : 'Unknown','age' : 'unknown'}
# print(d['name'])

# print(d.get('name'))
# print(d.get('names'))

# if 'name' in d:
#     print('present')
# else:
#     print('not present')

# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# if None ----> Fales, else ----> True


# Clear Method
# # d.clear()
# print(d)

# Copy Method
d1 = d.copy()
# d1 = d
# print(d1.popitem())
# print(d)


print(d1 == d )

