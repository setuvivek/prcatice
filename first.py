for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


val1=  20
val2=  11
print(val1/val2)
print(val1//val2)

a=10
b=1
# Subtract and assign value
b-=a
print("Subtract and assign value :", b)

g=3
h=6
k=g-h
print(k)

a = 3
b = 5

# a = a ** b
a **= b

# Output
print(a)

k=20
j=50
print(k>j)

s=50
d=60
print(s and d )
print(s or d)
print(not d)