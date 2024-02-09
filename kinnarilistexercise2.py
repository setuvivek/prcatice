s = 'Complete Sentence Complete Exercise'
c = s.count('Complete')
d= s.count('Sentence')
f = s.count('Exercise')
print('Complete-', c, 'Sentence-' , d , 'Exercise-', f)

list1 = [10,12,20,22]
print(sum(list1))

list2 = [10,12,20,22,2]
print(min(list2))

list3 = [10,12,20,22,10]
my_set = {s for s in list3}
s = list(my_set)
print(s)

list4 = ['abc', 'xyz', 'aba', '1221']
list5= []
for i in list4:
    if len(i) >= 2:
        if i[0] == i[-1]:
            list5.append(i)
print(len(list5))


