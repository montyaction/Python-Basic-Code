# replance method
string=('She is beautiful and she is good dancer')
# print(string.replace(' ','_'))
# print(string.replace('is','was'))
# print(string.replace('is','was',1))
# print(string.replace('is','was',2))

# Find methods
# print(string.find('is'))
# print(string.find('is',1))
is_pos1=string.find('is')
is_pos2=string.find('is',is_pos1+1)
print(is_pos2)