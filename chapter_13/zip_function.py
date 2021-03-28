 # zip function
user_id = ['user1', 'user2', 'user3', 'user4']
names = ['Monty', 'Archana', 'Sallu', 'Bably']
last_names = ['Sharma', 'kanwar', 'Paikra', 'Toppo']

 # output ('user1', 'Monty'), ('user2', 'Archana')
print(list(zip(user_id, names)))

print(list(zip(user_id, names, last_names)))

# Example = [('a',1),('b',2)]

print(dict(zip(user_id, names)))