s1 = {54.532, 342, 432, 432, 342, 42345, 2, 4, 32}

s2 = {"apple", "banana", "cherry", 'banana', True, 1, 12, True}
s3 = s2.copy()
print(s2)
print(len(s2))
print(type(s2))

print('loops')
for i in s2:
    print(i, end=' ')
print()
print('yes' in s2)

print('delete')
print(s2)
s2.remove(True)
print(s2, 'remove')
s2.discard(False)
print(s2, 'discard')
print(s2.pop())  # random value will be deleted
print(s2, 'pop')
s2.clear()
print(s2, 'clear')
del s2

s4 = s1.union(s3)
print(s4)
s4.update({1, 2, 3, 4, 5, 6, 7, 89})
print(s4)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x, 'intersection_update')
z = x.intersection(y)
print(z, 'x.intersection')

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z, 'symmetric_difference')

d1 = {1: 'a', 2: 'b'}
l1 = [1, 2, 3, 4]
