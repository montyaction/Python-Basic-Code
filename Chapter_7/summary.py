# summary dictionary
# what is dictionary
# unordered collection of data

d = {'name' : 'Mohit','age' : 24}

# or
d1 = dict(name ='Mohit', age = 24)

# or 
d2 = {
    'name' : 'Mohit',
    'age' : 27,
    'fav_movies' : []
}


# How to access data from dictionary
# you cannot do like
# d[0], beacuse there is no order inside dictionary
 

# syntax
# print(dictname[keyname])
# print(d['name'])


# add data inside empty dict
empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
#print(empty_dict)

# check existence of values inside dict
# use in keyword to check for keys
# if 'name' in d:

# how to iterate over dictionary
# most common method
# for key, value in d.items():
#     print(f'key is {key} and value is {value}')
 

# to print all keys
# for i in d:
#     print(i)


# to print all values
# for i in d.values():
#     print(i)


# most comman dict methods


# get method
# to access a key and check existance
# print(d.get('name'))

# Q - why we use get
# A - to get rid of error
# example
# print(d['names'])
# print(d.get('names'))


# to delete item
# pop ----> take one argument which is keyname

# popped = d.pop('name')
# print(popped)
# print(d)

# popitem
popped = d.popitem()
print(popped)
print(d)
