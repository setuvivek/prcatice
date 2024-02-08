'''
[1] Write a Python program to calculate the length of a string.
Sample String : 'w3school'
Output : 8
'''

text = "w3schools"
count = -1
for x in text:
    count = count+1;

print( count)
print()

'''
[2] Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3school'
Expected Result : 'w3ol'
'''

text = "jatin"
count = -1
for x in text:
    count = count+1

if(count<2):
    print(" . ")
else:
    print(text[:2] + text[count-1:])
print()

'''
[3] Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'test'
Expected Result : 'tes$'


text = str("test")
if(text[0]==text[1] or text[0]==text[2] or text[0]==text[2] or text[0]==text[3] or text[0]==text[4]):
    print(text.replace(text[0],"$"))
else:
    print("nn")
'''
text = "test tt"
k = text[0]
# d = ''
print(k)
for i in text[1:]:
    if(i != k):
     print(i)
    else:
     print("$")
print()
# print(text[0])
# if(text[0] == text[:d]):
#     print(text[i].replace("[i]","$"))

'''
[4] Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
Sample String : 'xyz'
Expected Result : 'zyx'
                             '''


String = "xyz"

# print(String[2:3])
# print(String[1:2])
# print(String[0:1])
# print(String[-3:])
print(String[::-1])

'''
[5] Write a Python program to perform uppercase of the later part of the string.
Input : 'w3school' 
Output : w3scHOOL
 '''

text = "w3school"
count = 0
ca = 0

for i in text:
    count+=1
print(count)
ca = count/2
a = int(ca)
print(text[:a]+text[a:].upper())




