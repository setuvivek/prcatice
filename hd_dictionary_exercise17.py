dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
#check key present in dict
def fun(i):
	if i in dic1:
		print("yes")
	else:
		print("no")
fun(1)

#chcek value present in dictionary
if 60 in dic2.values():
    print("yes")
else:
    print("no")


#Merge dictionaries
dict4 = {**dic1, **dic2, **dic3}
print(dict4)

#iterate dictionary using loop
for j, k in dic1.items():
	print(j, '--^', k)

#Merge dictionary using loop
dic = {}
for a in (dic1, dic2, dic3):
	dic.update(a)
print(dic)

# Print Dictionary and the values are the square of keys
d = dict()
m = int(input("Enter number"))
for i in range(0,m+1):
	d[i] = i * i
print(d)

#Print the sum of dictionary values
n = sum(dic1.values())
print(n)

#Delete particular key of dictionary
# del dic1[1]
# print(dic1)

#sort dictionary based on key
color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
for key in sorted(color_dict):
	print(key, color_dict[key])

# list = []
# n = int(input("enter a number"))
# for i in range(n):
#     j = int(input("enter index "))
#     list.append(j)
#
# print(list)

#To get minimum and maximum values in the dictionary
my_dict = {'x': 500, 'y': 5874, 'z': 560}
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Minimum Value: ', my_dict[key_min])
print('Maximum Value: ', my_dict[key_max])

import  itertools
print(list(itertools.permutations([1, 2])))

#Initialize dictionary with default value
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
b = dict.fromkeys(employees,defaults)
print(b)
#print individual data
print(b["Kelly"])

#create a dictionary from extracting a key from given dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
key = ["name","salary"]
res = dict()
for k in key:
    res.update({k:sampleDict[k]})
print(res)


#change the key name
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict["location"] = sampleDict["city"]
sample_dict.pop("city")
print(sample_dict)

#Change the value of brad's salary in nested dictionary and set 8500
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)
