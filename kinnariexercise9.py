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
    dict1.update({"name": self.name, "email": self.email , "line": list})
  def display(self):
    print(dict1)
for i in range(2):
  obj = Sales_order()
  obj.display()
