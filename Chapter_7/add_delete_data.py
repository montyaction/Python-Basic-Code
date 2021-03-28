# add and delete data
user_info = {
    'name' : 'Archana',
    'age' : 25,
    'fav_movies' : ['coco', 'kiwi no na wa'],
    'fav_tune' : ['awakening', 'fairy tale'],
}


# How to add data
user_info['fav_songs'] = ['song1','song2']
print(user_info)


# pop method
# popped_item = user_info.pop('fav_tune')     # .pop(isme ek argument pass karna jaruri h)
# print(f"Popped item is {popped_item}")
# print(type(popped_item))
# print(user_info)


# popitem method
# popped_item =user_info.popitem()
# print(user_info)
# print(type(popped_item))