fruits=['grapes', 'mango', 'apple']
# sort
fruits.sort()
print(fruits)

fruits2=('grapes', 'mango', 'apple')
print(sorted(fruits2))


fruits3={'grapes', 'mango', 'apple'}
print(sorted(fruits3))
guitars=[
    {'model' : 'yamaha f310', 'price' : 8400},
    {'model' : 'faith naptune', 'price': 50000},
    {'model' : 'faith apollo venus', 'price' : 35000},
    {'model' : 'taylor 814ce', 'price' : 450000}
]

print(sorted(guitars, key = lambda d:d['price'], reverse = True))