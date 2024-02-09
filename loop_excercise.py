# Prg_1
for i in range(1,6):
    for j in range(1,6):
        if i >= j:
            print(j,end=" ")
        else:
            print(' ',end=" ")
    print()

# # Prg_2

for i in range(2,11,2):
    for j in range(2,11,2):
        if i >= j:
            print(j,end=" ")
        else:
            print(' ',end=" ")
    print()

# Prg_3
for i in range(2,11,2):
     for j in range(2,11,2):
         if j<=13-i:
             print(j,end=" ")
         else:
             print(' ',end=" ")
     print()




# Prg_4

rows=5
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=' ')
    for k in range(i):
        print(2*k+2,end=' ')
    print()


# #prg_5

for i in range(1,11,2):
    for j in range(1,11,2):

        if i >= j:
            print(j,end=" ")
        else:
            print(' ',end=" ")
    print()

for i in range(1,9,2):
    for j in range(1,9,2):
        if j<=9-i:
              print(j,end=" ")
        else:
              print(' ',end=" ")
    print()

#prg_6

row=5
for i in range(row):
    n = 1
    for j in range(i):
        print(n,end=' ')
        n+=2
    print(' '*((row-i)*2)*2,end='')
    for k in range(i*2-1,0,-2):
        print(k,end=' ')
    print()
for i in range(row):
    n=1
    for j in range(row,i,-1):
        print(n,end=' ')
        n+=2
    print(' ' *(i*2)*2, end='')
    n-=2
    for k in range(row,i,-1):
        if n==9:
            print(" ",end=' ')
        else:
            print(n,end=' ')
        n-=2
    print()










