import pandas as pd

df = pd.read_csv('ans.csv')


write = pd.ExcelWriter('main_call_put.xlsx', engine='xlsxwriter')
for option in df['optionType'].unique():
    if option == 'Jigna':
        continue
    df1 = df[df['optionType'] == option]
    df1.to_excel(write, sheet_name=option, index=False)

write._save()

print('operation success')
