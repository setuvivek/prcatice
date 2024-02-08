x = ["complete", "sentence", "complete", "exercise"]
print(x.count("complete"))
print(x.count("sentence"))
print(x.count("exercise"))

#exercise2
input = [10, 12, 20, 22]

print(sum(input))

# #exercise3
input = [10, 12, 20, 22, 2]
print(min(input))
#
#exercise5
input = [10, 12, 20, 22, 10]
set1 = set(input)
list1 = list(set1)
print(list1)
#exercise5
input = [10, 12,20,22,10]
input.pop()
print(input)

#exercise4
# Input : ['abc', 'xyz', 'aba', '1221']
#Output : 2
string = ['abc', 'xyz', 'aba', '1221']
count = 0
for x in string:
        if (len(x) >=2 and x[0] == x[-1]):
            count +=1
print(count)






