'''
[4] Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

Input : ['abc', 'xyz', 'aba', '1221']

Output : 2
'''

count = 0
list1 = ['abc', 'xyz', 'aba', '1221', 'xszx']
for x in list1:
    if len(x) >= 2 and x[0] == x[-1]:
        count +=1
print(count)
