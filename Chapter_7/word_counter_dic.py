# word counter
# Archana 
d = {'a':1, 'a':2, 'r':1, 'c':1, 'h':1, 'n':1}
print(d)


def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

name = input('Enter your name : ')
print(word_counter(name))