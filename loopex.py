'''[1] Write a program to print the following number pattern using a loop.

	1
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5
'''
o=1
n=7

for x in range(o,n):
    for j in range(o,x):
        print(j,end=' ')
    print()


'''
[2] Write a program to print the following number pattern using a loop.

	2 
	2 4 
	2 4 6 
	2 4 6 8 
	2 4 6 8 10

'''
o=1
n=7

for x in range(o,n):
    for j in range(o,x):
        print(j*2,end=' ')
    print()

'''
[3] Write a program to print the following number pattern using a loop.

	2 4 6 8 10
	2 4 6 8 
	2 4 6 
	2 4 
	2 
'''
print()
o=1
m=7
for i in range(o,m):
    for j in range(i+1,m):
        print((j*2)-2*i,end=' ')
    print()

'''
[4] Write a program to print the following number pattern using a loop.

	2 4 6 8 10
	  2 4 6 8 
		2 4 6 
		  2 4 
		    2
		    '''
print()
o=1
m=7
for i in range(o,m):
    for k in range(o,i):
        print(" ",end=' ')
    for j in range(i+1,m):
        print((j*2)-2*i,'',end='')
    print()
'''
[5] Write a program to print the following number pattern using a loop.

	1 
	1 3 
	1 3 5 
	1 3 5 7 
	1 3 5 7 9
	1 3 5 7 
	1 3 5 
	1 3 
	1
	 '''

o=0
n=5

for x in range(o,n):
    for j in range(o,x):
        print(j*2+1,end=' ')

    print()
for x in range(o, n):
    for j in range(x,n):
        # print(j*2, end=' ')
        print((j-1*x)*2+1, end=' ')
    print()


'''
[6] Write a program to print the following number pattern using a loop.

	1               1
	1 3           3 1
	1 3 5 	    5 3 1
	1 3 5 7   7 5 3 1
	1 3 5 7 9 7 5 3 1
	1 3 5 7   7 5 3 1
	1 3 5 	    5 3 1
	1 3 		  3 1
	1 			    1
'''




o=0
n=6

for i in range(o,n):
    for j in range(o,i):
        print(j*2+1,end=' ')
    for k in range(i,n):
        print("   ",end=' ')

    for l in range(o+1, i+1):
        # print(int(((((l*2)-2*i)*-1)/2))*2+1, end=' ')  # print(i,end='')#print((j*2)-2*i ,end=' ')
        print((o + i - l) * 2 + 1, end=' ')
    print()
for x in range(o, n):
    for j in range(x,n):
        # print(j*2, end=' ')
        print((j-1*x)*2+1, end=' ')
    for j in range(o+1,x+1):
       print("   " ,end= ' ')

    for m in range(x+2,n+1):
        # print(j*2, end=' ')
        print((n-m)*2+1, end=' ')
    print()


# 1                     1
# 1 3                 3 1
# 1 3 5             5 3 1
# 1 3 5 7         7 5 3 1
# 1 3 5 7 9     9 7 5 3 1
# 1 3 5 7         7 5 3 1
# 1 3 5             5 3 1
# 1 3                 3 1
# 1                     1

o=0
n=6
for i in range(o,n):
    for j in range(o,i):
        print(j*2+1,end=' ')
    for k in range(i,n):
        print("   ",end=' ')
    for l in range(o+1, i+1):
        print((o+i-l)*2+1, end=' ')  # print(i,end='')#print((j*2)-2*i ,end=' ')
    print()
for x in range(o+2, n):
    for j in range(x,n):
        # print(j*2, end=' ')
        print((j-1*x)*2+1 , end=' ')

    for j in range(o+1,x+1):
       print("   " ,end= ' ')

    for m in range(x+1,n+1):
        # print(j*2, end=' ')
        print((n-m)*2+1, end=' ')
    print()
