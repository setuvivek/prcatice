#exercise of list of list
#remove empty list from a list
list13 = [1,7,[],4,[],3,2,9,1,10,[]]
for i in list13:
    if i == []:
        list13.remove(i)
print(list13)


#convert list to dictionary(same length of two list)
list14 = [1,2,3,4]
list15 = ['a','b','c','d']
a = zip(list14,list15)
print(dict(a))


#different length
from itertools import zip_longest
list16 = [1,2,3,4,5,6,7]
list17 = ['a','b','c','d']
b = zip_longest(list16,list17)
print(dict(b))


#convert list of dictionary into one dictionary
l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
c = {}
for c1 in l1:
    c.update(c1)
print(c)


#convert list of list into dictionary
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
res = dict()
for n in test_list:
    res[tuple(n[:2])] = [tuple(n[2:])]
print(res)


#21-sort the list of tuple
list_of_tuples = [(1, "USA"), (3, "United Kingdom"), (2, "Brazil")]
list_of_tuples.sort()
print(list_of_tuples)
#sort key wise
a = sorted(list_of_tuples, key = lambda x:x[1])
print(a)
