# advance min and max

def func(item):
    return len(item)

names=['saras', 'saket', 'ankit']
print(min(names, key=func))

students={
    'saras' : {'score':90, 'age':17},
    'saket' : {'score':80, 'age':18}

}

print(max(students, key=lambda item:item.get('score'))['name'])