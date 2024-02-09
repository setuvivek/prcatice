# [1] Write a Python program to calculate the length of a string.
# Sample String : 'w3school'
# Output : 8

txt=input("Enter a value: ")
x = len(txt)
print(x)


#[2] Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3school'
# Expected Result : 'w3ol'
txt=input("Enter a value: ")
if len(txt) < 2:
    print('empty string')
else:
    x=txt[0:2]
    y=txt[-2:]
    print(x+y)

# # [3] Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# # Sample String : 'test'
# # Expected Result : 'tes$

# txt='test'
# txt1=txt[1:]
# x = txt1.replace('t','$')
# print(txt[0]+x)

txt = input("Enter a value: ")
str = txt[0]
print(str)
for i in txt[1:]:
    if i != str:
        print(i)
    else:
        print('$')

# [4] Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# Sample String : 'xyz'
# Expected Result : 'zyx'

txt1 = input("Enter a value: ")
txt=list(txt1)
x=txt[0]
txt[0]=txt[-1]
txt[-1]=x
print("".join(txt))

# 5] Write a Python program to perform uppercase of the later part of the string.
#  Input : 'w3school'
#  Output : w3scHOOL

txt = input("Enter a value: ")
temp = len(txt)/2
char = len(txt)

for i in range(len(txt)):
    if i >= temp:
        print(txt[i].upper(),end='')
    else:
        print(txt[i],end='')
