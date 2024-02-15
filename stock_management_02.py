import tabulate
from tabulate import tabulate

import xlsxwriter
workbook = xlsxwriter.Workbook('/home/setu/Documents/csv/feb0724.xlsx')
worksheet1 = workbook.add_worksheet("customer")
worksheet2 = workbook.add_worksheet("product")
worksheet3 = workbook.add_worksheet("stock")

import pandas as pd
df1 = pd.read_excel(io='/home/setu/Documents/csv/feb0724.xlsx', sheet_name="customer")
df2 = pd.read_excel(io='/home/setu/Documents/csv/feb0724.xlsx', sheet_name="product")
df3 = pd.read_excel(io='/home/setu/Documents/csv/feb0724.xlsx', sheet_name="stock")
list1 = df1.values.tolist()
list2 = df2.values.tolist()
list3 = df3.values.tolist()
# print(list1)
# print(list2)
# print(list3)
def fun():

    class Dbms():
        import xlsxwriter
        workbook = xlsxwriter.Workbook('/home/setu/Documents/csv/feb0724.xlsx')
        worksheet1 = workbook.add_worksheet("customer")
        row = 0
        col = 0
        l = ["id", "name", "type", "pan"]
        for i in l:
            worksheet1.write(row, col, i)
            col += 1
        row = 1
        col = 0
        for i in list1:
            for j in i:
                worksheet1.write(row, col, j)
                col += 1
            col = 0
            row += 1
        worksheet2 = workbook.add_worksheet("product")
        row = 0
        col = 0
        l = ["id", "name", "incoming", "outgoing", "onhand"]
        for i in l:
            worksheet2.write(row, col, i)
            col += 1
        row = 1
        col = 0
        for i in list2:
            for j in i:
                worksheet2.write(row, col, j)
                col += 1
            col = 0
            row += 1
        worksheet3 = workbook.add_worksheet("stock")
        row = 0
        col = 0
        l = ["id", "product_id ", "customer_id", "qty", "type"]
        for i in l:
            worksheet3.write(row, col, i)
            col += 1
        row = 1
        col = 0
        for i in list3:
            for j in i:
                worksheet3.write(row, col, j)
                col += 1
            col = 0
            row += 1
        workbook.close()

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
                k = int(cid)
                filtered = [print("customer already exist") for i in list1 if i[0] == k ]
                if filtered: return fun()
                cname = input("Enter Customer Name :")
                ctype1 = str(input("Enter Customer Type :"))
                cpan = str(input("Enter Customer Pan :"))
                f = [print("customer already exist") for i in list1 if i[3] == cpan]
                if f: return fun()
                list1.append([cid,cname,ctype1,cpan])
                obc = Dbms()
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
                    r = int(pid)
                    p = [print("product already exist") for i in list2 if i[0] == r]
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
                    b = int(incoming)
                    while True:
                        outgoing= input("Enter Outgoing :")
                        try:
                            int(outgoing)
                            break
                        except ValueError:
                            print("please enter integer")
                    o = int(outgoing)
                    if o > b:
                        print("outgoing is grater than incoming ")
                        return fun()
                    else:
                        onhand = b - o

                    list2.append([pid,pname,incoming,outgoing,onhand])
                    obp = Dbms()
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
                n = int(sid)
                s = [print("stock already exist") for i in list3 if i[0] == n]
                if s: return fun()

                while True:
                    spid = input("Enter Product Id:")
                    try:
                        int(spid)
                        break
                    except ValueError:
                        print("please enter integer")
                k = int(spid)
                if list2 == []:
                    print("product master table is empty")
                    return fun()
                for i in list2:
                    if i[0] == k:
                        pass
                c = any(e[0] == k for e in list2)
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
                a = int(scid)
                if list1 == []:
                    print("customer master table is empty.")
                    return fun()
                for i in list1:
                    if i[0] == a:
                        pass
                c = any(e[0] == a for e in list1)
                if c == False:
                    print("This customer is not defined in customer master table.")
                    return fun()

                while True:
                    sqty = input("Enter qty:")
                    try:
                        int(sqty)
                        break
                    except ValueError:
                        print("please enter integer")
                p = int(sqty)
                stype2 = str(input("Enter Type:"))
                if stype2 == "incoming":
                    for i in list2:
                        for j in list1:
                            if i[0] == k and j[0] == a:
                                    #a = int(i[2])
                                    i[2] += p
                                    #a += int(sqty)
                                    i[4] = i[2]-i[3]

                if stype2 == "outgoing":
                    for i in list2:
                        for j in list1:
                            if i[0] == k and j[0] == a:
                                    if p > i[4]:
                                        print("not available enough stock")
                                        return fun()
                                    else:
                                        i[3] += p
                                        i[4] = i[2]-i[3]
                list3.append([sid,spid,scid,sqty,stype2])
                obs = Dbms()

    c = input("enter which data you want to add or exit :")
    if c =="customer":
        obj1= Customer_master.customer()
        return fun()
    if c =="product":
        obj2 = Product_master.product()
        return fun()
    if c == "stock":
        obj3 = Stock_move_master.stock()
        return fun()
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
ob = fun()