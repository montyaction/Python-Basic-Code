# dictionaries intro
# Q - why we use dictionaries?
# A - Because of limitations of lists, lists are not enough to represent
# real data


# Example
user = ['Archana',24,['coco', 'kiwi no na wa'],['awakening', 'fairy tale']]
# this list contain user name, age, fav movies, fav tunes
# you can do this is not a good way to do this.


# Q - what are dictionaries
# A - unordered collections of data in key : value pair.


# How to create dictionaries
user = {'name': 'Archana' , 'age' : 25}
#print(user)
#print(type(user))


# Second method to create dictionary
user1 = dict(name = 'Archana' , age = 25)
#print(user1)


# How to access data from dictionary
# NOTE - there is no indexing because of unordered collections of data.
print(user['name'])
print(user['age'])


# which type of data a dictionary can store ?
# anything
# number, string, lists, dictionry

user_info = {
    'name' : 'Archana',
    'age' : 25,
    'fav_movies' : ['coco', 'kiwi no na wa'],
    'fav_tune' : ['awakening', 'fairy tale'],
}
# print(user_info['fav_movies'])

# How to add data empty dictionary
user_info_2 = {}
user_info_2['name'] = 'Mohit'
user_info_2['age'] = 27

print(user_info_2)