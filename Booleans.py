print(10 > 9)
print(10 == 9)
print(10 < 9)

a, b = 2020, 3222
if a > b:
    print('a is grater')
else:
    print('a is not grater')
# if value are available then it will print True otherwise False
# True
print(bool('abc'))
print(bool(123))
print(bool(['abc', 'def', 'ghi']))
print(bool({1, 23, 4, 3}))
print(bool({1: 'fds', 3: 'czz'}))
print(bool((1, 2, 3, 4)))
print()
# False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))


class c1():
    def __len__(self):
        return False


obj = c1()
print(bool(obj))


def Fun():
    return False


print(Fun())

if Fun():
    print('Right')
else:
    print('Wrong')

x = 2222
print(isinstance(x, int))
