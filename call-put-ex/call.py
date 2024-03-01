import xlsxwriter
import csv

with open('ans.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)
#print(data)

workbook = xlsxwriter.Workbook('output_xlsxwriter.xlsx')


opetion = {}


for x in data[1:]:
    option_type = x[5]
    if option_type not in opetion:
        if option_type == 'Jigna':
            continue
        opetion[option_type] = [data[0]]
    opetion[option_type].append(x)


for option_type, option_data in opetion.items():
    worksheet = workbook.add_worksheet(option_type)
    for r, row_data in enumerate(option_data):
        for c, value in enumerate(row_data):
            worksheet.write(r, c, value)

workbook.close()

print("operation success")