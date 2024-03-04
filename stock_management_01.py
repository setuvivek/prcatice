import tabulate
from tabulate import tabulate
list1 = []
list2 = []
list3 = []
def fun():
    class Customer_master():
        def __init__(self, cid, cname, ctype1, cpan):
            self.id = cid
            self.name = cname
            self.type1 = ctype1
            self.pan = cpan
        def customer():
                while True:
                    cid = input("Enter Customer Id:")
                    try :
                        int(cid)
                        break
                    except ValueError:
                        print("please enter integer")
                filtered = [print("customer already exist") for i in list1 if i[0] == cid ]
                if filtered: return fun()
                cname = input("Enter Customer Name :")
                ctype1 = str(input("Enter Customer Type :"))
                cpan = str(input("Enter Customer Pan :"))
                f = [print("customer already exist") for i in list1 if i[3] == cpan]
                if f: return fun()
                list1.append([cid,cname,ctype1,cpan])
    class Product_master:
        def __init__(self,pid, pname, incoming, outgoing,onhand):
            self.id = pid
            self.name = pname
            self.incoming = incoming
            self.outgoing = outgoing
            self.onhand = onhand
        def product():
                    while True:
                        pid = input("Enter Product Id:")
                        try :
                            int(pid)
                            break
                        except ValueError:
                            print("please enter integer")
                    p = [print("product already exist") for i in list2 if i[0] == pid]
                    if p : return fun()
                    pname = str(input("Enter Product Name :"))
                    pn = [print("product already exist") for i in list2 if i[1] == pname]
                    if pn: return fun()
                    while True:
                        incoming = input("Enter Incoming :")
                        try:
                            int(incoming)
                            break
                        except ValueError:
                            print("please enter integer")
                    while True:
                        outgoing= input("Enter Outgoing :")
                        try:
                            int(outgoing)
                            break
                        except ValueError:
                            print("please enter integer")
                    if int(outgoing) > int(incoming):
                        print("outgoing is grater than incoming ")
                        return fun()
                    else:
                        onhand = int(incoming) - int(outgoing)
                    list2.append([pid,pname,incoming,outgoing,onhand])
    class Stock_move_master():
            def __init__(self,sid,spid,scid,sqty,stype2):
                self.id = sid
                self.product_id = spid
                self.customer_id = scid
                self.qty = sqty
                self.type2= stype2
            def stock():
                while True:
                    sid = input("Enter Id:")
                    try:
                        int(sid)
                        break
                    except ValueError:
                        print("please enter integer")
                s = [print("stock already exist") for i in list3 if i[0] == sid]
                if s: return fun()

                while True:
                    spid = input("Enter Product Id:")
                    try:
                        int(spid)
                        break
                    except ValueError:
                        print("please enter integer")
                if list2 == []:
                    print("product master table is empty")
                    return fun()
                for i in list2:
                    if i[0] == str(spid):
                        pass
                c = any(e[0] == str(spid) for e in list2)
                if c == False:
                    print("This product is not defined in product master table.")
                    return fun()
                while True:
                    scid = input("Enter Customer Id:")
                    try:
                        int(scid)
                        break
                    except ValueError:
                        print("please enter integer")
                if list1 == []:
                    print("customer master table is empty.")
                    return fun()
                for i in list1:
                    if i[0] == str(scid):
                        pass
                c = any(e[0] == str(scid) for e in list1)
                if c == False:
                    print("This customer is not defined in customer master table.")
                    return fun()

                while True:
                    sqty = (input("Enter qty:"))
                    try:
                        int(sqty)
                        break
                    except ValueError:
                        print("please enter integer")
                stype2 = str(input("Enter Type:"))
                if stype2 == "incoming":
                    for i in list2:
                        for j in list1:
                            if i[0] == str(spid) and j[0] == str(scid):
                                    a = int(i[2])
                                    a += int(sqty)
                                    i[2] = a
                                    i[4] = int(i[2])-int(i[3])
                if stype2 == "outgoing":
                    for i in list2:
                        for j in list1:
                            if i[0] == str(spid) and j[0] == str(scid):
                                    c = int(i[4])
                                    if int(sqty) > c:
                                        print("not available enough stock")
                                        return fun()
                                    else:
                                        b = int(i[3])
                                        b += int(sqty)
                                        i[3] = b
                                        i[4] = int(i[2])-int(i[3])
                list3.append([sid,spid,scid,sqty,stype2])
    c = input("enter which data you want to add or exit :")
    if c =="exit":
        print("data of customer: ")
        col = ["id","name","type","pan"]
        print(tabulate(list1, headers=col))
        print("data of product : ")
        colm = ["id", "name", "incoming", "outgoing", "onhand"]
        print(tabulate(list2, headers=colm))
        print("data of stock : ")
        colmu = ["id", "product_id ", "customer_id", "qty", "type"]
        print(tabulate(list3, headers=colmu))
        exit()
    if c =="customer":
        obj1= Customer_master.customer()
    if c =="product":
        obj2 = Product_master.product()
    if c == "stock":
        obj3 = Stock_move_master.stock()
    return fun()

ob = fun()
