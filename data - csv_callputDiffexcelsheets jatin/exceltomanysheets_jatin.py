import pandas as pd
df = pd.read_excel('books.xlsx')
df.head()
df['optionType'].unique()

for oType in df['optionType'].unique():
    print(oType)

writer = pd.ExcelWriter('book.xlsx', engine='xlsxwriter')
for oType in df['optionType'].unique():
    if oType!='Jigna':
        newDf = df[df['optionType'] == oType]
        newDf.to_excel(writer, sheet_name=oType ,index=False)

writer._save()