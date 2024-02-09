'''
[5] Write a Python program to remove duplicate number from a list.

Input: [10,12,20,22,10]

Output: [10,12,20,22]
'''

list1 = [10,12,20,22,10]
list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)

print(list2)