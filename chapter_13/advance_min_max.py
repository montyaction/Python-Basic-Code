# advance min() and max()

numbers = [1,2,4,5,7,9,10]
print(min(numbers))
print(max(numbers))

def func(item):
    return len(item)

names = ['Archana', 'Monty', 'Bhuneshwar', 'Sonu']
print(max(names, key = func ))
print(min(names, key = func ))

# wiht lambda
print(min(names, key = lambda item: len(item)))
print(max(names, key = lambda item: len(item)))

students = {
    'Archana':{'score':90, 'age':26},
    'Mohit':{'score':80, 'age':27},
    'Sallu':{'score':85, 'age':28}
}

print(min(students, key = lambda item: students[item]['score']))


students2 = [
    {'name':'Archana','score':90, 'age':26},
    {'name':'Mohit','score':80, 'age':27},
    {'name':'Sallu','score':85, 'age':28}
]

print(max(students2, key = lambda item:item.get('score'))['name'])
print(max(students2, key = lambda item:item.get('score')))
print(max(students2, key = lambda item:item.get('age'))['name'])
print(max(students2, key = lambda item:item.get('age')))