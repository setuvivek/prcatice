'''
a = {‘a’ : 10 , ‘b’ : 20 , ‘c’: 30}
b = {‘a’:5 , ‘d‘: 15 , ‘c’ : 10 }

'''
a= {'a' : 10 , 'b' : 20 , 'c': 30}
b = {'a':5 , 'd': 15 ,'c' : 10 }
c = {}
for key, value in a.items():
    if key in b:
        c[key] = value + b[key]

    else:
        c[key] = value

for key, value in b.items():
    if key not in c:
        c[key] = value

print(c)