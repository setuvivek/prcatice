import pandas as pd
import openpyxl
xpath='rr.xlsx'
workbook=openpyxl.Workbook()
workbook.save(xpath)

list1=[]
list2=[]
list3=[]
def input_id(message):
    while True:
        try:
            return input(message)
        except ValueError:
            print("Please enter an integer")

def check_duplicate(data_list, index, value):
    return any(i[index] == value for i in data_list)

class Customer:
    def __init__(self, cid, cname, ctype1, cpan):
        self.id = cid
        self.name = cname
        self.type1 = ctype1
        self.pan = cpan

    @staticmethod
    def customer():
        while True:
            cid = input_id("Enter Customer Id:")
            if check_duplicate(list1, 0, cid):
                print("Customer already exists")
                return Customer.customer()

            cname = input("Enter Customer Name: ")
            ctype1 = str(input("Enter Customer Type customer/vendor "))
            cpan = str(input("Enter Customer Pan: "))
            if check_duplicate(list1, 3, cpan):
                print("Customer pan number must be unique.")
                return Customer.customer()

            list1.append([cid, cname, ctype1, cpan])

            main()

class Product:
    def __init__(self, pid, pname, incoming, outgoing, onhand):
        self.id = pid
        self.name = pname
        self.incoming = incoming
        self.outgoing = outgoing
        self.onhand = onhand

    @staticmethod
    def product():
        while True:
            pid = input_id("Enter Product Id:")
            if check_duplicate(list2, 0, pid):
                print("Product already exists")
                return Product.product()

            pname = str(input("Enter Product Name: "))
            if check_duplicate(list2, 1, pname):
                print("Product with the same name already exists")
                return Product.product()

            incoming = int(input("Enter Incoming: "))
            outgoing = int(input("Enter Outgoing: "))
            if outgoing > incoming:
                print("Not valid")
                return Product.product()

            onhand = incoming - outgoing
            print(onhand)
            list2.append([pid, pname, incoming, outgoing, onhand])

            main()

class Stock:
    def __init__(self, sid, spid, scid, sqty, stype2):
        self.id = sid
        self.product_id = spid
        self.customer_id = scid
        self.qty = sqty
        self.type2 = stype2

    @staticmethod
    def stock():
        while True:
            sid = input_id("Enter Stock Id:")
            if check_duplicate(list3, 0, sid):
                print("Stock entry already exists")
                return Stock.stock()

            spid = input("Enter Product Id:")
            if not check_duplicate(list2, 0, spid):
                print("This product does not exist.")
                return Stock.stock()

            scid = input("Enter Customer Id:")
            if not check_duplicate(list1, 0, scid):
                print("Customer does not exist.")
                return Stock.stock()

            sqty = int(input("Enter qty:"))
            stype2 = str(input("Enter Type incoming/outgoing:"))

            if stype2 == "incoming":
                for i in list2:
                    for j in list1:
                        if i[0] == spid and j[0] == scid:
                            i[2] += sqty
                            i[4] = i[2] - i[3]

            if stype2 == "outgoing":
                for i in list2:
                    for j in list1:
                        if i[0] == spid and j[0] == scid:
                            if sqty > i[4]:
                                print("Not enough available stock")
                                return Stock.stock()
                            else:
                                i[3] += sqty
                                i[4] = i[2] - i[3]

            list3.append([sid, spid, scid, sqty, stype2])

            main()
# import pandas as pd
#
# df1 = pd.DataFrame(list1)
# df2 = pd.DataFrame(list2)
# df3 = pd.DataFrame(list3)
#
# writer = pd.ExcelWriter('/home/setu/workspace/python/pythonProject/Riken/riken_stock.xlsx', engine='xlsxwriter')
#
# df1.to_excel(writer, sheet_name='Customer')
# df2.to_excel(writer, sheet_name='Product')
# df3.to_excel(writer, sheet_name='Stock')
#
# writer.close()

def main():
    c = input("Enter which data you want to add customer, product or stock or exit: ")

    if c == "exit":
        print("Data of customer: ")
        for item in list1:
            # print(item)
            df1 = pd.DataFrame(list1, columns=['cid', 'cname', 'ctype1', 'cpan'])
            df1.to_csv()
            print(df1)
            if not df1.empty:
                with pd.ExcelWriter('rr.xlsx',engine='openpyxl',mode='a', if_sheet_exists='replace') as writer:
                    df1.to_excel(writer,index=False, sheet_name='Customer')


        print("Data of product: ")
        for item in list2:
            #print(item)
            df2 = pd.DataFrame(list2, columns=['pid', 'pname', 'incoming', 'outgoing', 'onhand'])
            df2.to_csv()
            print(df2)
            if not df2.empty:
                with pd.ExcelWriter('rr.xlsx',engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    df2.to_excel(writer,index=False, sheet_name='product')

        print("Data of stock: ")
        for item in list3:
            #print(item)
            df3 = pd.DataFrame(list3, columns=['sid','spid', 'scid', 'sqty', 'stype2'])
            df3.to_csv()
            print(df3)
            if not df3.empty:
                with pd.ExcelWriter('rr.xlsx',engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    df3.to_excel(writer,index=False, sheet_name='stock')


        exit()

    if c == "customer":
        Customer.customer()

    elif c == "product":
        Product.product()

    elif c == "stock":
        Stock.stock()

    return main()

# df1 = pd.DataFrame(list1, columns= ['cid', 'cname', 'ctype1', 'cpan'])
# df2 = pd.DataFrame(list2, columns=[' pid', 'pname', 'incoming', 'outgoing', 'onhand'])
# df3 = pd.DataFrame(list3, columns=[' sid', 'spid', 'scid', 'sqty', 'stype2'])
#
#
#
# writer = pd.ExcelWriter('rr.xlsx', engine='xlsxwriter')
#
# df1.to_excel(writer, sheet_name='Customer')
# df2.to_excel(writer, sheet_name='Product')
# df3.to_excel(writer, sheet_name='Stock')
#
# writer.close()


if __name__ == "__main__":
    main()






