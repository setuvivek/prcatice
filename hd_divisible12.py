# divisible=[2,5,7]
# non divisible = [3,4]

divisible = list(map(int, input("Enter divisible number : ").split()))
not_divisible = list(map(int, input("Enter non divisible number: ").split()))

start = int(input("Enter start : "))
end= int(input("Enter  end : "))

list = []

for x in range(start, end + 1):
    if all(x % i == 0 for i in divisible) and all(x % i != 0 for i in not_divisible):
        list.append(x)

# Print the result
print("Numbers :", list)



# start = int(input("enter start"))
# end = int(input("enter end"))
#
# x1 = int(input("Enter a divisible number"))
# x2 = int(input("Enter second divisible number"))
# x3 = int(input("Enter third divisible number"))
# y1 = int(input("Enter non divisible number"))
# y2 = int(input("Enter second non divisible number"))
#
# for i in range(start, end+1):
#     if i % x1 == 0 and i % x2 == 0 and i % x3 == 0 and i % y1 != 0 and i % y2 != 0:
#         print(i)

    # if i % 2 == 0 and i%5==0 and i%7==0 and i%3!=0 and i%4!=0:
        # print(i)




