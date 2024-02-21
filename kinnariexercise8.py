dict1 = {}
list = []
class Sales_order:
    def __init__(self):
        self.name = input("enter name : ")
        self.email = input("enter email : ")
        while (True):
            self.product = input("enter product: ")
            self.quantity = (input("enter quantity : "))
            self.price = (input("enter price : "))
            list.append({"product": self.product, "quantity": self.quantity, "price": self.price})
            count = input("Want to add another? (Y/N)")
            if count == "N":
                break;
        dict1.update({"name": self.name, "email": self.email, "line": list})
    def display(self):
        print(dict1)
s1 = Sales_order()
s1.display()
#
# for i in range(2):
#   obj = Sales_order()
#   obj.display()

# mydict = {}
# mydict[self.name] = dict(name= self.name, email=self.email)
# print(mydict)

# class_list = dict()
# data = input('Enter name & score separated by ":" ')
# temp = data.split(':')
# class_list[temp[0]] = int(temp[1])
#
# # Displaying the dictionary
# for key, value in class_list.items():
#   print('Name: {}, Score: {}'.format(key, value))
# cancel = False
# dict = ()
# class_list = []
# list2 = []
# while (True):
#     name = input("Enter Name: ")
#     email = input("Enter email: ")
#     product = input("Enter product: ")
#     quantity = [int(i) for i in input("Enter quantity (seperated by spaces): ").split(" ")]
#     price = [int(i) for i in input("Enter price (seperated by spaces): ").split(" ")]
#     class_list.append( {"name": name ,"email": email })
#     class_list.append("lines")
#     list2.append( {"product": product,"quantity": quantity,"price": price })
#
#     # for item in range(len(class_list)):
#     #     for items in range(len(list2)):
#     #         key = class_list[item]
#     #         value = list2[items]
#     #         dict[class_list[item]] = list2[items]
#
#
#     #dict[class_list] =[list2]
#     cont = input("Want to add another? (Y/N)")
#     if cont == "N":
#         break;
# print(class_list)
# print(list2)
# merge_list = class_list + list2
# print(merge_list)
# print(dict)
