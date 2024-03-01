import pandas as pd

df = pd.read_csv('hospital_directory.csv')


write = pd.ExcelWriter('hospital_statewise.xlsx', engine='xlsxwriter')
for option in df['State'].unique():
    df1 = df[df['State'] == option]
    df1.to_excel(write, sheet_name=option, index=False)

write._save()

print('operation success')
