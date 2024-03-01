import json
import csv

# Open the JSON file & load its data
with open('/home/setu/Documents/csv/nse_data_prac.json',) as dat_file:
    data = json.load(dat_file)
print(data)

with open('/home/setu/Documents/csv/kinnari (4).csv', 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["underlying","identifier","instrumentType","instrument","expiryDate","optionType","strikePrice","lastPrice","pChange","openPrice","highPrice","lowPrice","numberOfContractsTraded","totalTurnover","premiumTurnover","openInterest","underlyingValue"])
    for item in data["value"]:
        csv_file.writerow([item['underlying'],item['identifier'],item['instrumentType'],item['instrument'],item['expiryDate'],item['optionType'],item['strikePrice'],item['lastPrice'],item['pChange'],item['openPrice'],item['highPrice'],item['lowPrice'],item['numberOfContractsTraded'],item['totalTurnover'],item['premiumTurnover'],item['openInterest'],item['underlyingValue']])
    for item in data["volume"]:
        csv_file.writerow(
            [item['underlying'], item['identifier'], item['instrumentType'], item['instrument'], item['expiryDate'],
             item['optionType'], item['strikePrice'], item['lastPrice'], item['pChange'], item['openPrice'],
             item['highPrice'], item['lowPrice'], item['numberOfContractsTraded'], item['totalTurnover'],
             item['premiumTurnover'], item['openInterest'], item['underlyingValue']])


