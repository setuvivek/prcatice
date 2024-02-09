a="shivam"                                #input for def 1, 2, 4 & 5
if len(a)>2:
    aa=(a[0]+a[1]+a[-2]+a[-1])
else:
    ""
b="test test"                               #input for def 3
# b="at bat bat"
d=list()
for i in range(len(b)):
    if i==0:
        d.append(b[i])
        continue
    if b[i]==b[0]:
        d.append("$")
    else:
        d.append(b[i])

a2=int(len(a)/2)
ae=len(a)
c=list()
for i in range(len(a)):
    if i in range(0,a2):
        a[i].lower()
        c.append(a[i])
    if i in range(a2,ae):
        c.append(a[i].upper())


x=list(a)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
x=("".join(x))


print("def : 1 ",len(a))
print("def : 2 ",aa)
print("def : 3 ","".join(d))
print("def : 4 ",x)
print("def : 5 ","".join(c))