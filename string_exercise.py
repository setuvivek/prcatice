string = "w3school"
print(len(string))
#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'test'
#Expected Result : 'tes$'
string1 = "enter the string:"
x = list(string1)
x[-1] = "$"
def fun (s):
    str = ""
    for ele in s:
        str += ele
    return str
s = x
print(fun)
#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
#Sample String : 'w3school'
#Expected Result : 'w3ol'
str3 = "w3school"
def func(str3):
    if len(str) < 2:
        return ''
    else:
        return str3[0:2] + str3[-2:]
    print(func(str3))
#[4] Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
#Sample String : 'xyz'
#Expected Result : 'zyx'
str1 = input("enter the string:")
print(str1[::-1])
#w3school
#w3scHOOL
A= 'w3school'
print(A[:4] + A[4:].upper())












