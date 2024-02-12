list1 = [1, 5, 2, 7, 9]
list2 = [0, -2, 3, 1]

def list(list1, list2):
    index = int(input("Enter an index"))
    list2 = list2[index:] + list2[:index]
    for i in range(len(list2)):
        list1[i] = list1[i] + list2[i]
    return list1



print(list(list1, list2))


