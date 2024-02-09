'''
    1
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5

'''
row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j,end=" ")
    print()
print(end="\n")

'''
    2 
	2 4 
	2 4 6 
	2 4 6 8 
	2 4 6 8 10
'''
row = 5
for i in range(1,row+1):
    for j in range(1,i+1):
        print(2*j,end=" ")
    print()
print(end="\n")

'''
	2 4 6 8 10
	2 4 6 8 
	2 4 6 
	2 4 
	2 
'''
row = 5
for i in range(row, 0, -1):
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()
print(end="\n")

'''
	2 4 6 8 10
	  2 4 6 8 
		2 4 6 
		  2 4 
		    2

'''
row = 5
for i in range(row, 0, -1):
    for k in range(row-i):
        print(" ",end=" ")
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()
print(end="\n")

'''
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

row = 6
for i in range(1,row):
    for j in range(1,i*2,2):
        print(j,end=" ")
    print()

row = 4
for i in range(row,0,-1):
    for j in range(1,i*2,2):
        print(j,end=" ")
    print()

print(end="\n")

'''
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
row = 6
num = 1
ncol = row*2-7
lst = []

#   UP SIDE   #
for i in range(1, row):

    # for a in lst:
    #     print(a,end=" ")
    for z in range(1, i*2, 2):      #left upper
        print(z, end=" ")

    for k in range(ncol-i):         #space
        count = " "
        print(count," ",end=" ")

    for j in range(1,2):        #right upper
    #     lst.append(j)
    # lst.reverse()
        num = list(map(str, range(1,i*2,2)))
        num.reverse()
        if i == 5:
            num.remove('9')
            # num.insert(0," ")
        print(" ".join(num),end=" ")
    print()

#   DOWN SIDE
row = 4
num = range(1,i*2,2)
for i in range(row,0,-1):

    for z in range(1,i*2,2):    #left down
        print(z,end=" ")

    for k in range(ncol-i):         #space
        count = " "
        print(count," ",end=" ")

    for j in range(1,2):        #right down
        num = list(map(str, range(1,i*2,2)))
        num.reverse()
        print(" ".join(num),end=" ")
    print()
print(end="\n\n")




# row = 4
# for i in range(row,0,-1):   #right down
#     for k in range(ncol-i):         #space
#         count = " "
#         print(count," ",end=" ")
#
#     for j in range(1,i*2,2):
#         print(j,end=" ")
#     print()


# l = []
# for i in range(0,6):
#
#     l.append(i)
#     print(i,end=" ")
# print(l)
# l.reverse()
# print(l)
# for j in l:
#     print(j,end=" ")

'''
                    1
                3   1
            5   3   1
        7   5   3   1
    9   7   5   3   1
'''

row = 5
# lst = []
# for i in range(1,11,2):
#     lst.append(i)
#     # print(i,end=" ")
# # lst.reverse()
# print(lst)
# for j in (lst[::-1]):
#         # print(j,end=" ")
#         # lst.append(j)
#         # i = lst.reverse()
#     print(j,end=" ")

for i in range(1,row + 1):
    num = list(map(str,range(1,i*2,2)))
    num.reverse()
    # print(" ".join((str(num))))
    print(" ".join(num))
#
# lst = ['1','2','3','4','5','6']
# print(lst)
# lst.remove('2')
# print(lst)
