# def reverse_list(l):
#     l.reverse()
#     return l

# def reverse_list(l):
#     return l[::-1]    

def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

number = list(range(1,11))
print(reverse_list(number))