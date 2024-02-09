# for loop
print('list')
fruits = ['apple', 'banana', 'cherry', 'mengo']
for x in fruits:
    print(x)
    for i in x:
        print(i)

print('tuple')
fruits = ('apple', 'banana', 'cherry', 'mengo')
for x in fruits:
    print(x)
    for i in x:
        print(i)

print('set')
fruits = {'apple', 'banana', 'cherry', 'mengo'}
for x in fruits:
    print(x)
    for i in x:
        print(i)

print('dictionary')
fruits = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'mengo'}
for x in fruits:
    print(fruits[x], x)
    for i in fruits[x]:
        print(i)

print()
for i in "Chauhan":
    print(i)

print()
for x in fruits:
    print(x)
    if x == 'banana':
        break

print()
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# range in for
# use of start range(Start,Stop)
# defaul range(stop)
# range(Start,Stop,Step)

print()
for x in range(6):
    print(x)

print()
for x in range(3, 6):
    print(x)

print()
n = 1
for x in range(4, 41, 4):
    print(n, ' * ', 4, ' ', x)
    n += 1
else:
    print('always work when for loop done')

for x in range(4, 41, 4):
    n += 1
    if x == 20:
        continue
    print(n, ' * ', 4, ' ', x)
else:
    print('it will work if we use continue keyword')

for x in range(4, 41, 4):
    print(n, ' * ', 4, ' ', x)
    n += 1
    if x == 20:
        break
else:
    print('it will not work if we use break keyword')
