import pandas as pd
import xlsxwriter

file_path = '/home/setu51/Desktop/pythonProject1/Names.csv'

df = pd.read_csv(file_path)  # read csv file into data frame

Put_data = df[df["optionType"] == "Put"]  # separate push and call
Call_data = df[df["optionType"] == "Call"]
# Create an Excel
# excel_writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as excel_writer: #with means if option type is put, all put data in put sheet else call data in call sheet
    Put_data.to_excel(excel_writer, sheet_name='Put', index=False)

    Call_data.to_excel(excel_writer, sheet_name='Call', index=False)
