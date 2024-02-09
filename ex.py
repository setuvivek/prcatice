'''
[1] Write a Python program to calculate the length of a string.not using len
Sample String : 'w3school'
Output : 8
'''
a = 'w3school'
#print(len(a))
count=0
for x in a:
    count+=1
print(count)
'''[2] Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3school'
Expected Result : 'w3ol'
'''
a = 'w3school'
x=a[:3]
y=a[-3:]

print(x+y)

'''
[3] Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'test'
Expected Result : 'tes$'
alternate logic
'''
a = 'test is importent'
'''
x=a.capitalize()
y=x.replace('t','$')
z=y.casefold()
print(z)
'''
x=a[0]
y=a[1:]

z=y.replace("t","$")

print(x+z)
'''[4] Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
Sample String : 'xyz'
Expected Result : 'zyx'
'''
a="xyz"
x=list(a)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))


'''[5] Write a Python program to perform uppercase of the later part of the string.
Input : 'w3school'
Output : w3scHOOL
'''
a="w3school"
x=a[:4]
y=a[4:]
z=y.upper()
print(x+z)


