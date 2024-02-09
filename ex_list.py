'''
[1] Write a Python program to count the occurrences of each word in a given sentence.

Input: "Complete sentence Complete exercise"

Output: Complete - 2
		sentence - 1
		exercise - 1
'''

list1  ="Complete sentence Complete exercise"
x = list1.split()

a = x.count("Complete")
b = x.count("sentence")
c = x.count("exercise")

com = "complete - {}"
print(com.format(a))

sen = "sentence - {}"
print(sen.format(b))

ex = "exersise - {}"
print(ex.format(c))