import pandas as pd
import openpyxl
df = pd.read_csv('input/hospital_directory.csv')

Sr_No, Location_Coordinates, Location, Hospital_Name, Hospital_Category, Hospital_Care_Type, Discipline_Systems_of_Medicine, Address_Original_First_Line, State, District, Subdistrict, Pincode, Telephone, Mobile_Number, Emergency_Num, Ambulance_Phone_No, Bloodbank_Phone_No, Foreign_pcare, Tollfree, Helpline, Hospital_Fax, Hospital_Primary_Email_Id, Hospital_Secondary_Email_Id, Website, Specialties, Facilities, Accreditation, Hospital_Regis_Number, Registeration_Number_Scan, Nodal_Person_Info, Nodal_Person_Tele, Nodal_Person_Email_Id, Town, Subtown, Village, Establised_Year, Ayush, Miscellaneous_Facilities, Number_Doctor, Num_Mediconsultant_or_Expert, Total_Num_Beds, Number_Private_Wards, Num_Bed_for_Eco_Weaker_Sec, Empanelment_or_Collaboration_with, Emergency_Services, Tariff_Range, State_ID, District_ID = df['Sr_No'], df['Location_Coordinates'], df['Location'], df['Hospital_Name'], df['Hospital_Category'], df['Hospital_Care_Type'], df['Discipline_Systems_of_Medicine'], df['Address_Original_First_Line'], df['State'], df['District'], df['Subdistrict'], df['Pincode'], df['Telephone'], df['Mobile_Number'], df['Emergency_Num'], df['Ambulance_Phone_No'], df['Bloodbank_Phone_No'], df['Foreign_pcare'], df['Tollfree'], df['Helpline'], df['Hospital_Fax'], df['Hospital_Primary_Email_Id'], df['Hospital_Secondary_Email_Id'], df['Website'], df['Specialties'], df['Facilities'], df['Accreditation'], df['Hospital_Regis_Number'], df['Registeration_Number_Scan'], df['Nodal_Person_Info'], df['Nodal_Person_Tele'], df['Nodal_Person_Email_Id'], df['Town'], df['Subtown'], df['Village'], df['Establised_Year'], df['Ayush'], df['Miscellaneous_Facilities'], df['Number_Doctor'], df['Num_Mediconsultant_or_Expert'], df['Total_Num_Beds'], df['Number_Private_Wards'], df['Num_Bed_for_Eco_Weaker_Sec'], df['Empanelment_or_Collaboration_with'], df['Emergency_Services'], df['Tariff_Range'], df['State_ID'], df['District_ID']
Sr_No=df['Sr_No']
output = {}
for i in range(len(Sr_No)):
    temp = {"Sr_No": Sr_No[i], "Location_Coordinates": Location_Coordinates[i], "Location": Location[i], "Hospital_Name": Hospital_Name[i], "Hospital_Category": Hospital_Category[i], "Hospital_Care_Type": Hospital_Care_Type[i], "Discipline_Systems_of_Medicine": Discipline_Systems_of_Medicine[i], "Address_Original_First_Line": Address_Original_First_Line[i], "State": State[i], "District": District[i], "Subdistrict": Subdistrict[i], "Pincode": Pincode[i], "Telephone": Telephone[i], "Mobile_Number": Mobile_Number[i], "Emergency_Num": Emergency_Num[i], "Ambulance_Phone_No": Ambulance_Phone_No[i], "Bloodbank_Phone_No": Bloodbank_Phone_No[i], "Foreign_pcare": Foreign_pcare[i], "Tollfree": Tollfree[i], "Helpline": Helpline[i], "Hospital_Fax": Hospital_Fax[i], "Hospital_Primary_Email_Id": Hospital_Primary_Email_Id[i], "Hospital_Secondary_Email_Id": Hospital_Secondary_Email_Id[i], "Website": Website[i], "Specialties": Specialties[i], "Facilities": Facilities[i], "Accreditation": Accreditation[i], "Hospital_Regis_Number": Hospital_Regis_Number[i], "Registeration_Number_Scan": Registeration_Number_Scan[i], "Nodal_Person_Info": Nodal_Person_Info[i], "Nodal_Person_Tele": Nodal_Person_Tele[i], "Nodal_Person_Email_Id": Nodal_Person_Email_Id[i], "Town": Town[i], "Subtown": Subtown[i], "Village": Village[i], "Establised_Year": Establised_Year[i], "Ayush": Ayush[i], "Miscellaneous_Facilities": Miscellaneous_Facilities[i], "Number_Doctor": Number_Doctor[i], "Num_Mediconsultant_or_Expert": Num_Mediconsultant_or_Expert[i], "Total_Num_Beds": Total_Num_Beds[i], "Number_Private_Wards": Number_Private_Wards[i], "Num_Bed_for_Eco_Weaker_Sec": Num_Bed_for_Eco_Weaker_Sec[i], "Empanelment_or_Collaboration_with": Empanelment_or_Collaboration_with[i], "Emergency_Services": Emergency_Services[i], "Tariff_Range": Tariff_Range[i], "State_ID": State_ID[i], "District_ID": District_ID[i]}
    if State[i] in output:
        output[State[i]].append(temp)
    else:
        output[State[i]] = [temp]

xpath = 'output/data10.xlsx'
workbook = openpyxl.Workbook()
workbook.save(xpath)

for i in output:
    df = pd.DataFrame(output[i])
    with pd.ExcelWriter(xpath, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=i, index=False)
    print(i)

