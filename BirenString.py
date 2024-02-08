print('Biren')
print("Bv")
a='Chauhan 252 222 Biren '
print(a)
print(a[0])
#str length
print(len(a))
#check
print('Biren' in a)
if 'Biren' in a:
    print('yes')

print('V' not in a)
if 'V' not in a:
    print('yes')

#multipleline
a1='''i am biren today is my first day at setu 
consulting the date is 15/01/2024.'''
print(a1)
for x in "SetuConsulting":
    print(x)

#slice
print(a[:3])
print(a[3:])
#negative
print(a[:-7:-1])
print(a[-5:-2])
print(a[::-1])

#Escape Characters
strings='''i am \'biren today \\is my first \nday at setu 
\rconsulting\tthe\bdate is 15/01/2024.'''
print(strings)
#Octal value
na='\102\111\122\105\116'
print(na)

#Methods
print(strings.count('a'))
print(a.encode())
print(a.find('B'))
print(a.index('B'))
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('Biren','VK'))
print(a.split(' '))

tuplee=('32','3','2','1','22')
print("**".join(tuplee))

x,y='setu','counsulting'
z=x+" "+y
j=x+y
print(z,' ',j)

#Format
age=23
txt ='My name is Biren, i am {} old'
print(txt.format(age))
name='BV'
txt ='My name is {}, i am {} old'
print(txt.format(name,age))
txt ='My name is {1}, i am {0} old'
print(txt.format(name,age))

a=' '
if a:
    print(True)
else:
    print(False)