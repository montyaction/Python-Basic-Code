fruits1 = ['Grapes', 'Mango', 'Apple']
fruits1.sort()
print(fruits1)

fruits2 = ('Grapes', 'Mango', 'Apple')
print(sorted(fruits2))

fruits3 = {'Grapes', 'Mango', 'Apple'}
print(sorted(fruits3))



guitars = [
    {'model': 'yamaha f310', 'price' : 8400},
    {'model': 'faith naptune', 'price':50000},
    {'model': 'faith apollo venus', 'price':35000},
    {'model': 'taylor 814ce', 'price':450000}
]

print(sorted(guitars, key= lambda d:d['price']))
print(sorted(guitars, key= lambda d:d['price'], reverse=True))

sorted_guitars = sorted(guitars, key= lambda d:d['price'])
print(sorted_guitars)
