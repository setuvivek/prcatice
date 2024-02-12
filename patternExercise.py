'''[1] Write a program to print the following number pattern using a loop.

	1
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5
'''
input = 5
# input = int(input('num = '))
for i in range(input + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

'''
[2] Write a program to print the following number pattern using a loop.

	2 
	2 4 
	2 4 6 
	2 4 6 8 
	2 4 6 8 10
'''
# input=int(input('num = '))
for i in range(input + 1):
    n = 2
    for j in range(1, i + 1):
        print(n, end=' ')
        n += 2
    print()
print()
'''
[3] Write a program to print the following number pattern using a loop.

	2 4 6 8 10
	2 4 6 8 
	2 4 6 
	2 4 
	2 
'''
# input=int(input('num = '))
for i in range(input + 1, 0, -1):
    n = 2
    for j in range(1, i):
        print(n, end=' ')
        n += 2
    print()

'''
[4] Write a program to print the following number pattern using a loop.

	2 4 6 8 10
	  2 4 6 8 
		2 4 6 
		  2 4 
		    2

'''
# input=int(input('num = '))
# input=6
for i in range(input, 0, -1):
    print(' ' * (input - i) * 2, end='')
    n = 2
    for j in range(1, i):
        print(n, end=' ')
        n += 2
    print()

# If anybody wants to know: Go to debug at PyCharm. There is a settings there. Look for variable loading policy.
# then click asynchronously. And debug again and it should be fixed.

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
# input=int(input('num = '))
for i in range(input):
    n = 1
    for j in range(i):
        print(n, end=' ')
        n += 2
    print()
for i in range(input):
    n = 1
    for j in range(input, i, -1):
        print(n, end=' ')
        n += 2
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
# input=int(input('num = '))
# input=5
for i in range(input):
    n = 1
    for j in range(i):
        print(n, end=' ')
        n += 2
    print('-' * ((input - i) * 2) * 2, end='')
    for j in range(i * 2 - 1, 0, -2):
        print(j, end=' ')
    print()
for i in range(input):
    n = 1
    for j in range(input, i, -1):
        print(n, end=' ')
        n += 2
    print('-' * (i * 2) * 2, end='')
    n -= 2
    for k in range(input, i, -1):
        print(n, end=' ')
        n -= 2
    print()
