import csv
import pandas

finalsheet={

}
file = open('../statevise/hospital_directory.csv')
type(file)
# print(type(file))
File = csv.DictReader(file)
for column in File:
        # print("column")
        # print(column)
        if column['State'] not in finalsheet:
            finalsheet[column['State']] = []
        finalsheet[column['State']].append(column)

with pandas.ExcelWriter('Demo.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    # newDf = df[df['State'] == i]
    # newDf.to_excel(writer, sheet_name=i)

    for i in finalsheet:
        Data_Frame = pandas.DataFrame(finalsheet[i])
        Data_Frame.to_excel(writer,sheet_name=i)
        print(i)

















'''
import csv
import pandas
finalsheet={}

with open('hospital_directory.csv', mode='r') as file:
    # read_file = pd.read_csv('hospital_directory.csv')
    # read_file.to_excel('sta.xlsx', header=True)
    # df = pd.read_excel('sta.xlsx')
    # df.head()
    File = csv.DictReader(file)
    for column in File:
        # print("column")
        # print(column)
        if column['State'] not in finalsheet:
            finalsheet[column['State']] = []
        finalsheet[column['State']].append(column)

with pandas.ExcelWriter('Deo.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    # newDf = df[df['State'] == i]
    # newDf.to_excel(writer, sheet_name=i)

    for i in finalsheet:
        Data_Frame = pandas.DataFrame(finalsheet[i])
        Data_Frame.to_excel(writer,sheet_name=i)
        print(i)
        
'''