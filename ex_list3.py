'''
[3] Write a Python program to get the smallest number from a list.

Input: [10,12,20,22,2]

Output: 2
'''

list1 = [10,12,20,22,2]

min = list1[0]

for x in list1:
    if x < min:
        min =x
print(min)