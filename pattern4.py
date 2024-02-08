rows = 6
def pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(rows-i):
            print(" ", end=" ")
        for j in range(2, i*2, 2):
            print(j, end=" ")
        print()
pattern(rows)