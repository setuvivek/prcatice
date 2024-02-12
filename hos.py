
import xlsxwriter
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('/home/setu/Documents/csv/exercise1.xlsx')
#worksheet = workbook.add_worksheet()
sheetOne = workbook.add_worksheet("Andhra Pradesh")
two = workbook.add_worksheet("Assam")
three =workbook.add_worksheet("Bihar")
four = workbook.add_worksheet("Chandigarh")
five = workbook.add_worksheet("Chhattisgarh")
six = workbook.add_worksheet("Dadra and Nagar Haveli")
seven = workbook.add_worksheet("Daman and Diu")
ei = workbook.add_worksheet("Goa")
ni = workbook.add_worksheet("Gujarat")
ten = workbook.add_worksheet("Haryana")
ele = workbook.add_worksheet("Himachal Pradesh")
twe = workbook.add_worksheet("Jammu and Kashmir")
thir = workbook.add_worksheet("Jharkhand")
fort = workbook.add_worksheet("Karnataka")
fif = workbook.add_worksheet("Kerala")
sixten = workbook.add_worksheet("Madhya Pradesh")
sevten = workbook.add_worksheet("Maharashtra")
eig = workbook.add_worksheet("Manipur")
nit = workbook.add_worksheet("Meghalaya")
twenty = workbook.add_worksheet("Mizoram")
#sheetTwo = workbook.add_worksheet("CALL")
#worksheet.write(0,0,'abc')

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Andhra Pradesh":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   sheetOne.write(row,col,item)
                   col += 1
               row += 1

#workbook.close()
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Assam":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   two.write(row,col,item)
                   col += 1
               row += 1
#workbook.close()

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Bihar":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   three.write(row,col,item)
                   col += 1
               row += 1
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict6 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Chandigarh":
               dict6.update(data)
               # row = 1
               col = 0
               for item in dict6.values():
                   four.write(row, col, item)
                   col += 1
               row += 1



row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict5 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Chhattisgarh":
               dict5.update(data)
               # row = 1
               col = 0
               for item in dict5.values():
                   five.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Dadra and Nagar Haveli":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   six.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Daman and Diu":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   seven.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Goa":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   ei.write(row,col,item)
                   col += 1
               row += 1
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Gujarat":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   ni.write(row,col,item)
                   col += 1
               row += 1
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Haryana":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   ten.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Himachal Pradesh":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   ele.write(row,col,item)
                   col += 1
               row += 1
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Jammu and Kashmir":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   twe.write(row,col,item)
                   col += 1
               row += 1
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Jharkhand":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   thir.write(row,col,item)
                   col += 1
               row += 1
row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Karnataka":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   fort.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Kerala":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   fif.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Madhya Pradesh":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   sixten.write(row,col,item)
                   col += 1
               row += 1


row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Maharashtra":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   sevten.write(row,col,item)
                   col += 1
               row += 1

row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Manipur":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   eig.write(row,col,item)
                   col += 1
               row += 1


row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Meghalaya":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   nit.write(row,col,item)
                   col += 1
               row += 1


row = 0
col = 0
import csv
with open('/home/setu/Documents/csv/hospital_directory.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       dict2 = {}
       row = 1
       for data in csvFile:
           if data['State'] == "Mizoram":
               dict2.update(data)
               # row = 1
               col = 0
               for item in dict2.values():
                   twenty.write(row,col,item)
                   col += 1
               row += 1
workbook.close()

# f = open("/home/setu/Documents/csv/data.txt", "r")
# print(f.read())
# with open('/home/setu/Documents/csv/data.txt') as f:
#     lines = f.readlines()
#
# print(lines)
# with open('/home/setu/Documents/csv/data.txt') as f:
#     contents = f.read()
#     print(contents)
# #
# import csv
#
# with open('/home/setu/Documents/csv/hos.csv', 'w') as file:
#     csv_file = csv.writer(file)
#     csv_file.writerow(["Sr_No","Location_Coordinates","Location","Hospital_Name","Hospital_Care_Type","Discipline_Systems_of_Medicine","Address_Original_First_Line",
#                        "State","District","Subdistrict","Pincode","Telephone","Mobile_Number","Ambulance_Phone_No","Foreign_pcare","Helpline","Hospital_Fax"
#                        ,"Hospital_Primary_Email_Id","Website","Specialties","Facilities","Accreditation","Hospital_Regis_Number","Nodal_Person_Info",
#                        "Town","Subtown","Village","Establised_Year","Miscellaneous_Facilities","Num_Mediconsultant_or_Expert","Num_Bed_for_Eco_Weaker_Sec",
#                        "Tariff_Range","State_ID","District_ID"])

    # writer = csv.writer(csv_file)
    # writer.writerow(('colum1', 'colum2', 'colum3'))
    # for l_name in f:
    #     for dictionary in l_name:
    #         for key, value in dictionary.items():
    #             csv_file.writerow([key, value[0], value[1]])


# import openpyxl
#
# wb = openpyxl.Workbook()
# sheet_counter = 1
#
# # You should consider adopting better conventions such as these ones:
# SHEET_SEPARATOR = "==="
# COLUMN_SEPARATOR = '|'
#
# with open('/home/setu/Documents/csv/data.txt', 'r+') as raw_text:
#     lines = raw_text.read().split(SHEET_SEPARATOR)
#
#     for line in lines:
#         rows = line.split('\n')
#         ws = wb.create_sheet(f'Sheet{sheet_counter}')
#
#         for row in rows:
#             ws.append(row.split(COLUMN_SEPARATOR))
#             wb.save('/home/setu/Documents/csv/result.xlsx')
#
#         sheet_counter += 1
#
#     wb.save('/home/setu/Documents/csv/result.xlsx')