a = { "a": 10 , "b": 20 , "c" : 40}
b = {"a": 5 ,"d":15 , "c":10}
for x in a.keys():
    for y in b.keys():
       if(x==y):
            b[y] = b[y] + a[x]
b.update({"b":20})
print(b)

# 2 nd method
from collections import Counter
a = { "a": 10 , "b": 20 , "c" : 30}
b = {"a": 5 ,"d":15 , "c":10}
c = Counter(a) + Counter(b)
print(c)

# 3rd method
a = { "a": 10 , "b": 20 , "c" : 40}
b = {"a": 5 ,"d":15 , "c":10}
final = map(lambda x,y: b[y]==b[y]+a[x] if a.keys()==b.keys() else print(a) ,a,b)
print(final)
