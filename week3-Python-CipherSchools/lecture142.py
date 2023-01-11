# sets comprehension
s={k**2 for k in range(1,11)}
print(s)

names=['saras', 'ankit', 'ayush']
first={name[0] for name in names}
print(first)