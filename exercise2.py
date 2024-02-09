
print("def 1 : ")
for i in range(1,6):                                          #def : 1 done
    for j in range(1,i+1):
        print(j, end=" ")
    print("")

print("\ndef 2 : ")
for i in range(2,11,2):                                       #def : 2 done
    for j in range(2,i+1,2):
        print(j, end=" ")
    print("")

print("\ndef 3 : ")
for i in range(0,5):                                          #def : 3 done
    a = 2
    for j in range(i,5):
        if a == 5 : a+=2
        print(a, end=" ")
        a+=2
    print("")

print("\ndef 4 : ")
for i in range(0,5):                                            #def : 4 done
    a = 2
    for k in range(1, i+1):
        print("  ", end="")
    for j in range(i,5):
        print(a, end=" ")
        a+=2
    print("")

print("\ndef 5 : ")
for i in range(1,9,2):                                          #def : 5 done
    for j in range(1,i+1,2):
        # if j >=5 : j+=2
        print(j, end=" ")
    print("")
for i in range(0,5):
    a = 1
    for j in range(i,5):
        print(a, end=" ")
        a+=2
    print("")

print("\ndef 6 : ")
a=8
for i in range(1,10,2):
    for j in range(1,i+1,2):
        print(j,end="")
    for i1 in range(a):
        print(" ",end="")
    for k in range(j,0,-2):
        print(k,end="")
    print("")
    a-=2
a=2                                                #def 6 : done
for i in range(8,1,-2):
    for j in range(1,i+1,2):
        print(j,end="")
    for i1 in range(a):
        print(" ",end="")
    for k in range(j,0,-2):
        print(k, end="")
    print("")
    a += 2
