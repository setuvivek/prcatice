#1.calculate length of a string
#do not use length, any inbuilt function
my_string = "w3school"
print("---Length of a string without inbuilt function---")
# print(f"The length of a string {my_string} is :: ",len(my_string))
count = 0
for i in my_string:
    count += 1
print(count)
print(end="\n")

#2.First two character and last two character
my_string = "w3school"
print("---Print first two and last two characters---")
print("Original string :: ",my_string)
first = my_string[:3]
last = my_string[-3:]
new_string = first+last
print(f"The first two and last two characters of a string {my_string} are :: ",new_string)
print(end="\n")

#3.all occurences of first character changed to '$',except first character
sample = "test"
print("---all occurences of first character changed to '$',except first character---")
print("Original String :: ",sample)
first = sample[0]
change = first + sample[1:].replace(first,"$")
print("Changed string is :: ",change)
# print(sample.replace("t","$",1))
print(end="\n")

#4.first and last character exchanged
str = 'ushma'
print("---first and last character exchanged---")
temp = str[0]    #x
first = str[-1]    #z
print("Original String :: ",str)
print("First and Last character exchanged :: ",first+str[1:-1]+temp)
print(end="\n")

#5.Convert to uppercase of the later part of the string
first = (my_string[:4])
print("---Convert to uppercase of the later part of the string---")
print("Original String :: ",my_string)
new = my_string[4:].upper()
print(first+new)
print(end="\n")
