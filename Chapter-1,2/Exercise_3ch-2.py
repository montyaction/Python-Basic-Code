name,char=input('Enter comma sparated your name and single character ').split(',')
print(f'Lenght of your name is = {len(name)}')
print(f'Character count :{name.strip().lower().count(char.strip().lower())}')

# name.strip().lower().count()
# char.strip().lower()
# name.strip().lower().count(char.strip().lower())