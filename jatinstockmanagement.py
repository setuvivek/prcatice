listpan = []
list1 = []
list1id = []

list2 = []
list2id = []
list2name = []

list3 = []

class customer:
    def __init__(self, id, name, type, pan):
        self.id = id
        self.name = name
        self.type = type
        self.pan = pan

    def cust(self):
        # list1 = []
        a = int(self.id)
        b = str(self.name)
        c = list(self.type)
        d = str(self.pan)
        # list1.append(a,b,c,d)

    def calcc(self):
        s = self.id, self.name, self.type, self.pan
        # print(s)

class product():
    def __init__(self, id, name, incoming, outgoing, onhand):
        self.id = id
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
        self.onhand = onhand
    def calp(self):
        s = self.id, self.name, self.incoming, self.outgoing, self.onhand
        # print(s)
class stockoMove(product, customer):
    def __init__(self, id, product_id, customer_id, qty, typeIO):
        self.id = id
        self.product_id = product_id
        self.customer_id = customer_id
        self.qty = qty
        self.typeIO = typeIO

    def sm(self):
        a = int(self.id)
        b = int(self.product_id)
        c = int(self.customer_id)
        d = float(self.qty)

    def typpe(self):
        print(self.id, self.product_id, self.customer_id, self.qty, self.typeIO)




for i in range(0, 1000):
    Flag = 1
    inputt = input("enter you master class name:-")

    if inputt == "c":
        id = input("enter id :- ")
        nam = input("enter name:-")
        type = input('enter type:-')
        pan = input("enter pan No. :- ")

        customerInput = customer(id, nam, type, pan)

        if pan in listpan:
            print("this pan is already exist in another user so pls enter your original pan number")
        if id in list1id:
            print("this id is already taken")
        else:
            list1.append(id)
            list1id.append(id)
            list1.append(nam)

            list1.append(type)
            # if pan in listpan:
            #     raise ("duplicate pan no")  // this raise will give error and rpogram end so it cant use ni it
            list1.append(pan)
            listpan.append(pan)


    elif inputt == "p":
        try:
            customerInput.cust()
        except:
            ("enter product data")

        id = int(input("enter id :- "))
        nam = input("enter name:-")
        incoming = int(input('enter incoming:-'))
        outgoing = int(input("enter outgoing. :- "))
        onhand = int((incoming - outgoing))

        ProductInput = product(id, nam, incoming, outgoing, onhand)
        if onhand < 0:
            print("Nagative value is not vALID for on hand")
        if nam in list2name:
            print("this name is already exist pls enter your name again")
        if id in list2id:
            print("this id is already taken")

        else:
            list2.append([id,nam,incoming,outgoing,onhand])
            list2id.append(id)
            list2name.append(nam)
        # ProductInput = product(input("enter id :- "), input("enter name:-"), input('enter incoming:-'),
        #                           input("enter outgoing :- "), "on")

    elif inputt == "s":
        try:
            customerInput.cust()
            Flag = 0
        except:
            print("pls first enter costomer value")
            exit()
        try:
            ProductInput.calp()
            Flag = 0
        except:
            print("pls first enter Product value")
            exit()
        id = input("enter id")
        pro_id = int(input("Enter product id"))
        cust_id = input("Enter customer id")
        qty = int(input("Enter qty which you want to update"))
        typeio = input("enter type incoming or outgoing")

        stockoMovInput = stockoMove(id, pro_id, cust_id, qty, typeio)


        if pro_id not in list2id:
            print("this product id isnt exist")

        if cust_id not in list1id:
            print("this customer id isnt exist")

        else:
            list3.append([id,pro_id,cust_id,qty,typeio])
            if typeio == 'outgoing':

                if list3[pro_id-1][1] == list2[pro_id-1][0]:
                    if list2[pro_id - 1][3] >= list3[pro_id-1][3]:
                        list2[pro_id-1][3] -= list3[pro_id-1][3]
                        outgoing = list2[pro_id - 1][3]

                        list2[pro_id-1][4] -= list3[pro_id-1][3]
                        onhand = list2[pro_id - 1][4]

            elif typeio == 'incoming':
                if list3[pro_id - 1][1] == list2[pro_id - 1][0]:
                        list2[pro_id-1][2] += list3[pro_id-1][3]
                        incoming = list2[pro_id-1][2]
                        list2[pro_id-1][4] += list3[pro_id-1][3]
                        onhand = list2[pro_id-1][4]
            else:print("please enter valid input (incoming  /  outgoing")

    elif inputt == "ex":
        print(list1)
        print(list2)
        print(list3)
        exit()
    else:
        print("please enter any valid master class name")
    Flag = 0
