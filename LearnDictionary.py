d1 = {1: 'Biren', 2: 'Chauhan', 3: 'setu', 4: 'consulting', 'h1': 'Yes'}
print(d1)
print(d1[3])
print(d1['h1'])

# if you set duplicate KEY then it will be ovverriden by last one
d1 = {1: 'Biren', 2: 'Chauhan', 3: 'setu', 4: 'consulting', 4: 'Yes'}
print(d1[4])

# Type Of value that we can set
# we can not set value in tuple
d1 = {1: 'Biren', 2: 'Chauhan', 3: False, 5: [32, 21, 321, 12], 4: 342}
print(d1)

d2 = dict(biren='Biren', yash='yash')
print(d2)
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

print(d2['yash'])
print(d2.get('bv', ''))
print(d2.get("Biren", ''))

print(d1.keys(), '\n', d2.keys())
print(d1.values(), '\n', d2.values())
# do change in dict
print()
d1["bvc"] = 'BVC'
print(d1.keys(), '\n', d2.keys())
print(d1.values(), '\n', d2.values())
print('item')
print(d1.items(), '\n', d2.items())

print(d1[4]) if 4 in d1 else print()
if 4 in d1:
    print(d1[4])

print('update')
d1[3] = True
print(d1)
d1.update({3: False})
print(d1)
d2 = {1: 11, 2: 22, 7: 33, 'abc': 32}
d1.update(d2)
d2.update(d1)
print(d2)

print('delete')
d1.pop(3)
print(d1)
d1.popitem()
print()
print()
print()
print()
print(d1)
del d1[4]
print(d1)
d1.clear()
print(d1)
del d1  # delete the dictionary

print('loops travers')
for d in d2:  # default it travers the key
    print(d, end=' ')
print()
for d in d2:  # values
    print(d2[d], end=' ')
print()
for d in d2.keys():  # default it travers the key
    print(d, end=' ')
print()
for d in d2.values():  # with this you can travers through values
    print(d, end=' ')
print()

for x, z in d2.items():
    print(x, '=', z, ',', end=' ')
print()

d3 = d2.copy()
print(d3)
d4 = dict(d3)
print(d4)

l1 = ['cricket', 'carom', 'chess', 'wally ball']
t1 = ('cricket', 'carom', 'wally ball', 'chess')
d5 = {'d1': d2, 'l1': l1, 't1': t1}

for x, z in d5.items():
    print(x, z)
print()

d6 = dict.fromkeys(t1, t1)
print(d6)

d6 = dict.fromkeys(t1)
print(d6)
print(type(d6))

s = d6.setdefault('yes', 'not present')
print(s)

print('yes' in d6)

print()
d0 = {'a': 231, 'b': 232, 'c': 234}

print()
