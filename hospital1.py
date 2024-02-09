import pandas as pd
import xlsxwriter

x = '/home/setu52/Downloads/hospital_directory.csv'
df = pd.read_csv(x)
# output = ('new_out.xlsx')

Andaman = df[df["State"] == "Andaman and Nicobar Islands"]
Andhra_Pradesh = df[df["State"]=="Andhra Pradesh"]
Assam = df[df["State"]=="Assam"]
Bihar = df[df["State"]=="Bihar"]
Chandigarh = df[df["State"] == "Chandigarh"]
Chhattisgarh = df[df["State"] =="Chhattisgarh"]
Dadra_haveli = df[df["State"] =="Dadra and Nagar Haveli"]
Daman = df[df["State"] =="Daman and Diu"]
Goa = df[df["State"]=="Goa"]
Gujarat = df[df["State"] == "Gujarat"]
Haryana = df[df["State"]=="Haryana"]
Himachal_Pradesh= df[df["State"]=="Himachal Pradesh"]
Jammu_and_Kashmir = df[df["State"]=="Jammu and Kashmir"]
Jharkhand = df[df["State"]=="Jharkhand"]
Karnataka = df[df["State"]=="Karnataka"]
Kerala = df[df["State"]=="Kerala"]
Lakshadweep = df[df["State"] =="Lakshadweep"]
Madhy_Pradesh = df[df["State"]=="Madhya Pradesh"]
Maharashtra = df[df["State"]=="Maharashtra"]
Manipur = df[df["State"] =="Manipur"]
Meghalaya = df[df["State"] =="Meghalaya"]
Mizoram = df[df["State"] =="Mizoram"]
Nagaland = df[df["State"] =="Nagaland"]
Odisha = df[df["State"]=="Odisha"]
Puducherry = df[df["State"] =="Puducherry"]
Punjab = df[df["State"]=="Punjab"]
Rajasthan= df[df["State"]=="Rajasthan"]
Sikkim = df[df["State"] =="Sikkim"]
Tamil_Nadu = df[df["State"]=="Tamil Nadu"]
Telangana = df[df["State"]=="Telangana"]
Tripura = df[df["State"] =="Tripura"]
Uttar_Pradesh = df[df["State"]=="Uttar Pradesh"]
Uttrakhand = df[df["State"]=="Uttarakhand"]
West_Bengal = df[df["State"]=="West Bengal"]

# with pandas.ExcelWriter('weather.xlsx'):
with pd.ExcelWriter('new_out.xlsx', engine = 'xlsxwriter')as excel_writer:
    Andaman.to_excel(excel_writer, sheet_name="Andaman and Nicobar Islands", index=False)
    Andhra_Pradesh.to_excel(excel_writer, sheet_name="Andhra", index=False)

    Assam.to_excel(excel_writer, sheet_name="Assam", index=False)
    Bihar.to_excel(excel_writer, sheet_name="Bihar", index=False)

    Chandigarh.to_excel(excel_writer, sheet_name="Chandigarh", index=False)
    Chhattisgarh.to_excel(excel_writer, sheet_name="Chhattisgarh", index=False)
    Dadra_haveli.to_excel(excel_writer, sheet_name="Dadra", index=False)
    Daman.to_excel(excel_writer, sheet_name="Daman", index=False)
    Goa.to_excel(excel_writer, sheet_name="Goa", index=False)
    Gujarat.to_excel(excel_writer, sheet_name="Gujarat", index=False)
    Haryana.to_excel(excel_writer, sheet_name="Haryana", index=False)
    Himachal_Pradesh.to_excel(excel_writer, sheet_name="Himachal Pradesh", index=False)
    Jammu_and_Kashmir.to_excel(excel_writer, sheet_name="Jammu and Kashmir", index=False)
    Jharkhand.to_excel(excel_writer, sheet_name="Jharkhand", index=False)
    Karnataka.to_excel(excel_writer, sheet_name="Karnataka", index=False)
    Kerala.to_excel(excel_writer, sheet_name="Kerala", index=False)
    Madhy_Pradesh.to_excel(excel_writer, sheet_name="Madhya Pradesh", index=False)
    Maharashtra.to_excel(excel_writer, sheet_name="Maharashtra", index=False)
    Manipur.to_excel(excel_writer, sheet_name="Manipur", index=False)
    Mizoram.to_excel(excel_writer, sheet_name="Mizoram", index=False)
    Nagaland.to_excel(excel_writer, sheet_name="Nagaland", index=False)
    Odisha.to_excel(excel_writer, sheet_name="Odisha", index=False)
    Puducherry.to_excel(excel_writer, sheet_name="Puducherry", index=False)
    Punjab.to_excel(excel_writer, sheet_name="Punjab", index=False)
    Rajasthan.to_excel(excel_writer, sheet_name="Rajasthan", index=False)
    Tamil_Nadu.to_excel(excel_writer, sheet_name="Tamil Nadu", index=False)
    Telangana.to_excel(excel_writer, sheet_name="Telangana", index=False)
    Tripura.to_excel(excel_writer, sheet_name="Tripura", index=False)
    Uttar_Pradesh.to_excel(excel_writer, sheet_name="Uttar Pradesh", index=False)
    Uttrakhand.to_excel(excel_writer, sheet_name="Uttarakhand", index=False)
    West_Bengal.to_excel(excel_writer, sheet_name="West Bengal", index=False)


