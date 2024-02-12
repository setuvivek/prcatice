#day2
'''
num1=int(input())
operator=input()
num2=int(input())

if operator =="==" or operator =="!=":
    if num1 == num2:
        print("num1 is equal to num 2")
    else:
        print("num1 is not equal to num2")
else:
    print("enter valid operator")
'''

'''
[1] Write a program to print the following number pattern using a loop.

	1 
	1 2 
	1 2 3 
	1 2 3 4 
	1 2 3 4 5
'''
'''
n= 5
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print(j, end=" ")
  print()
'''
'''
[2] Write a program to print the following number pattern using a loop.

	2 
	2 4 
	2 4 6 
	2 4 6 8 
	2 4 6 8 10
'''
'''
for i in range(2,11,2):
  for j in range(2, i + 2,2):
    print(j, end=" ")
  print()
'''
'''
[3] Write a program to print the following number pattern using a loop.

	2 4 6 8 10
	2 4 6 8 
	2 4 6 
	2 4 
	2
'''
'''
n = 10
for i in range(n, 0, -2):
  for j in range(2, i + 2, 2):
    print(j, end=" ")
  print()
'''
'''
[4] Write a program to print the following number pattern using a loop.

	2 4 6 8 10
	  2 4 6 8 
		2 4 6 
		  2 4 
		    2
'''
'''
n = 5
for i in range(n, 0, -1):
	print("  "*(n-i),end="")

	for j in range(2, i*2+2, 2):
    		print(j,end=" ")
	print()
'''
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

for i in range(1,10,2):
  for j in range(1, i + 2,2):
    print(j, end=" ")
  print()


for i in range(4, 0, -1):
	print(""*(4-i),end="")

	for j in range(1, i*2+1, 2):
    		print(j,end=" ")
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
'''
n=5
for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")

    for k in range(2 * n - 2 * i):
        print(" ", end=" ")

    for l in range(i, 0, -1):
        if l != n:
            print(2 * l - 1, end=" ")
    print()

for i in range(n - 1, 0, -1):

    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")

    for k in range(2 * n - 2 * i):
        print(" ",end=" ")

    for l in range(i, 0, -1):
        print(2 * l - 1, end=" ")
    print()



'''