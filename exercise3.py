a="Complete sentence Complete exercise"
print(a.count("Complete"),a.count("sentence"),a.count("exercise"))

b=[10,12,20,22]
sum=0
for i in b:
    sum+=i
print(sum)

c=[10,12,20,22,2]
print(min(c))

d=['abc', 'xyz', 'aba',"abcba", '1221']
z=0
z1=-1
c=0

for i in range(0,len(d)):
    if d[i][z]==d[i][z1]:
        c+=1
    # print(d[i][z],d[i][z1])
print(c)
# print(d[0][0]==d[0][-1])
# print(d[1][0]==d[1][-1])
# print(d[2][0]==d[2][-1])
# print(d[3][0]==d[3][-1])


e=[10,12,20,22,10]
print(sorted(set(e)))