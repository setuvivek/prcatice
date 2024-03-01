import pandas as pd
df = pd.read_csv('hospital_directory.csv')

x = df['State'].str.lower()
write = pd.ExcelWriter('hospital_statewise1.xlsx', engine='xlsxwriter')
for option in x.unique():
    df1 = df[x == option]
    df1.to_excel(write, sheet_name=option, index=False)

write._save()
