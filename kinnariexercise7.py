import xlsxwriter
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('/home/setu/Documents/csv/Puttt.xlsx')
#worksheet = workbook.add_worksheet()
sheetOne = workbook.add_worksheet("PUT")
sheetTwo = workbook.add_worksheet("CALL")
#worksheet.write(0,0,'abc')

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/kinnaricsv.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict = {}
       for rows in csvFile:
             if rows['optionType'] == "Put":
                 dict.update(rows)
                 for key in dict.keys():
                 #for i in rows:
                     row = 0
                     sheetOne.write(row,col,key)
                     col += 1
                 break;
       dict3 ={}


       dict2 = {}
       row = 1
       for data in csvFile:
           if data['optionType'] == "Put":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   sheetOne.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv

with open('/home/setu/Documents/csv/kinnaricsv.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    dict = {}
    for rows in csvFile:
        if rows['optionType'] == "Call":
            dict.update(rows)
            for key in dict.keys():
                # for i in rows:
                row = 0
                sheetTwo.write(row, col, key)
                col += 1
            break;
    dict3 = {}

    dict2 = {}
    row = 1
    for data in csvFile:
        if data['optionType'] == "Call":
            dict2.update(data)
            # row = 1
            col = 0
            for item in dict2.values():
                sheetTwo.write(row, col, item)
                col += 1
            row += 1

workbook.close()
















# import openpyxl
# wb = openpyxl.load_workbook('Put.xlsx')
# ws = wb.active







# from openpyxl import load_workbook
#
# wb_col = load_workbook('test_sheet.xlsx')
#
# sheet = wb_col.active
#
# # Adding three adjacent columns
#
# sheet.insert_cols(idx=4, amount=3)
#
# wb_col.save('test_sheet.xlsx')



              #print(rows)

              # if rows['optionType'] == "Put":
                     #print(rows)
                     # worksheet.write_row

# import openpyxl  # so we import the necessary lib to handle the excel, others you can use like pandas
#
# try:
#        # loading and opening the excel workbook,
#        workbook = openpyxl.load_workbook('Put.xlsx')  # esnsure this script is in the same directory as your excel file
#
#        workbook_sheetName = workbook['Put.xlsx']  # the sheetname containing your data
# except FileNotFoundError as error:
#        print(f'{error} file not found, check the name or path of the file')


       # for rows in csvFile:
       #     print(rows)
           #print(rows['optionType'])
           # if rows['optionType']=="Put":
           #    # workbook = openpyxl.Workbook()
              #   worksheet= workbook.active
              #      for row in csv_data:
              #          if row['optionType']=="Put":
              #              worksheet.append(row)
              #              workbook.save('Put.xlsx')



#
# import xlsxwriter
# # Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('Put.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# col = 0
# for row in csvFile:
#     print(row['optionType'])
# for item in csvFile:
#     worksheet.write(row, data, item)
#     row += 1
#import pandas
# csvFile = pandas.read_csv("/home/setu/Documents/csv/kinnari (4).csv")
# print(csvFile)
# import pandas as pd
# read_file = pd.read_csv(r'/home/setu/Documents/csv/kinnari (4).csv')
# read_file.to_excel(r'/home/setu/Documents/csv/forexercise.xlsx', index = None, header=True)
# import xlsxwriter
# # Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('Put.xlsx')
# worksheet = workbook.add_worksheet()
#
# workbook2 = xlsxwriter.Workbook('Call.xlsx')
# worksheet = workbook2.add_worksheet()


# row = 0
# col = 0
# writer=csv.DictWriter(open("/home/setu/Documents/csv/kinnari (4).csv","w"),fieldnames='optionType',extrasaction='Put')
# writer.writerows(allrows)
#
# import csv
# import openpyxl
# def csv_to_excel(csv_file, excel_file):
#     csv_data = []
#     with open(csv_file) as file_obj:
#         reader = csv.reader(file_obj)
#         for row in reader:
#             csv_data.append(row)
#
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     for row in csv_data:
#         sheet.append(row)
#     workbook.save(excel_file)
# if __name__ == "__main__":
#     csv_to_excel("/home/setu/Documents/csv/kinnari (4).csv", "/home/setu/Documents/csv/forexercise.xlsx")
