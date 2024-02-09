# ifelse

a = int(input('a enter number= '))
b = int(input('b enter number= '))
if a > b:
    print(True)
    print()
elif a == b:
    print('Same')
    print()
else:
    print(False)
    print()

if b > a: print(True)
print()
print(True) if b > a else print(False)
print()
print(True) if a == b and a >= b else print(False)
print()
print(True) if a == b or a > b else print(False)
print()
print(True) if not a > b else print(False)
print()
print(True) if not a > b else print(False)

if a > b:
    if a > 10:
        print('a is grater than b and a is grater than 10')
    else:
        print('a is grater than b but a is less than 10')

# if there no content in if then we can't write it empty
# we can use pass keyword
if a > b:
    pass
