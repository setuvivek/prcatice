user1 = int(input("Enter number-1 : "))
user2 = int(input("Enter number-2 : "))
print(user1, user2)
eqaul_num = (user1 == user2)
not_equal_num = (user1 != user2)
print("Which operation you want to perform :: \n\"==\" or \"!=\"")
ask = input("Which operation :: ")
if ask == "==":
    print(eqaul_num)
elif ask == "!=":
    print(not_equal_num)