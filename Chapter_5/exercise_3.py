# define a function that take list of words as argument and
# return list with reverse ofevery element in that list

# example
# ['abc','mno','tuv','xyz'] ----> ['cba','vut','zyx]

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

words = ['abc','mno','tuv','xyz']
print(reverse_elements(words))
