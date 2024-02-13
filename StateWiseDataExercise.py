import time
import pandas
import csv

start_time = time.time()
Out_put = {}
with open('/home/setu/Downloads/PrepareCSVExercise1/hospital_directory.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        if lines['State'] not in Out_put:
            Out_put[lines["State"]] = []
        Out_put[lines["State"]].append(lines)

with pandas.ExcelWriter('/home/setu/Downloads/Extracted.xlsx', engine='openpyxl', mode='a',
                        if_sheet_exists='replace') as writer:
    for i in Out_put:
        Data_Frame = pandas.DataFrame(Out_put[i])
        Data_Frame.to_excel(writer, sheet_name=i)
        print(i)

print("--- %s seconds ---" % (time.time() - start_time))
# Sr_No, Location_Coordinates, Location, Hospital_Name, Hospital_Category, Hospital_Care_Type, Discipline_Systems_of_Medicine, Address_Original_First_Line, State, District, Subdistrict, Pincode, Telephone, Mobile_Number, Emergency_Num, Ambulance_Phone_No, Bloodbank_Phone_No, Foreign_pcare, Tollfree, Helpline, Hospital_Fax, Hospital_Primary_Email_Id, Hospital_Secondary_Email_Id, Website, Specialties, Facilities, Accreditation, Hospital_Regis_Number, Registeration_Number_Scan, Nodal_Person_Info, Nodal_Person_Tele, Nodal_Person_Email_Id, Town, Subtown, Village, Establised_Year, Ayush, Miscellaneous_Facilities, Number_Doctor, Num_Mediconsultant_or_Expert, Total_Num_Beds, Number_Private_Wards, Num_Bed_for_Eco_Weaker_Sec, Empanelment_or_Collaboration_with, Emergency_Services, Tariff_Range, State_ID, District_ID = \
#     Data_csv['Sr_No'], Data_csv['Location_Coordinates'], Data_csv['Location'], Data_csv['Hospital_Name'], Data_csv[
#         'Hospital_Category'], Data_csv['Hospital_Care_Type'], Data_csv['Discipline_Systems_of_Medicine'], Data_csv[
#         'Address_Original_First_Line'], Data_csv['State'], Data_csv['District'], Data_csv['Subdistrict'], Data_csv[
#         'Pincode'], Data_csv['Telephone'], Data_csv['Mobile_Number'], Data_csv['Emergency_Num'], Data_csv[
#         'Ambulance_Phone_No'], Data_csv['Bloodbank_Phone_No'], Data_csv['Foreign_pcare'], Data_csv['Tollfree'], \
#         Data_csv['Helpline'], Data_csv['Hospital_Fax'], Data_csv['Hospital_Primary_Email_Id'], Data_csv[
#         'Hospital_Secondary_Email_Id'], Data_csv['Website'], Data_csv['Specialties'], Data_csv['Facilities'], Data_csv[
#         'Accreditation'], Data_csv['Hospital_Regis_Number'], Data_csv['Registeration_Number_Scan'], Data_csv[
#         'Nodal_Person_Info'], Data_csv['Nodal_Person_Tele'], Data_csv['Nodal_Person_Email_Id'], Data_csv['Town'], \
#         Data_csv['Subtown'], Data_csv['Village'], Data_csv['Establised_Year'], Data_csv['Ayush'], Data_csv[
#         'Miscellaneous_Facilities'], Data_csv['Number_Doctor'], Data_csv['Num_Mediconsultant_or_Expert'], Data_csv[
#         'Total_Num_Beds'], Data_csv['Number_Private_Wards'], Data_csv['Num_Bed_for_Eco_Weaker_Sec'], Data_csv[
#         'Empanelment_or_Collaboration_with'], Data_csv['Emergency_Services'], Data_csv['Tariff_Range'], Data_csv[
#         'State_ID'], Data_csv['District_ID']

# Out_Put = {}
# for i in range(len(Data_csv)):
#     data = {'Sr_No': Sr_No[i], 'Location_Coordinates': Location_Coordinates[i], 'Location': Location[i],
#             'Hospital_Name': Hospital_Name[i], 'Hospital_Category': Hospital_Category[i],
#             'Hospital_Care_Type': Hospital_Care_Type[i],
#             'Discipline_Systems_of_Medicine': Discipline_Systems_of_Medicine[i],
#             'Address_Original_First_Line': Address_Original_First_Line[i], 'State': State[i],
#             'District': District[i], 'Subdistrict': Subdistrict[i], 'Pincode': Pincode[i],
#             'Telephone': Telephone[i], 'Mobile_Number': Mobile_Number[i], 'Emergency_Num': Emergency_Num[i],
#             'Ambulance_Phone_No': Ambulance_Phone_No[i], 'Bloodbank_Phone_No': Bloodbank_Phone_No[i],
#             'Foreign_pcare': Foreign_pcare[i], 'Tollfree': Tollfree[i], 'Helpline': Helpline[i],
#             'Hospital_Fax': Hospital_Fax[i], 'Hospital_Primary_Email_Id': Hospital_Primary_Email_Id[i],
#             'Hospital_Secondary_Email_Id': Hospital_Secondary_Email_Id[i], 'Website': Website[i],
#             'Specialties': Specialties[i], 'Facilities': Facilities[i], 'Accreditation': Accreditation[i],
#             'Hospital_Regis_Number': Hospital_Regis_Number[i],
#             'Registeration_Number_Scan': Registeration_Number_Scan[i], 'Nodal_Person_Info': Nodal_Person_Info[i],
#             'Nodal_Person_Tele': Nodal_Person_Tele[i], 'Nodal_Person_Email_Id': Nodal_Person_Email_Id[i],
#             'Town': Town[i], 'Subtown': Subtown[i], 'Village': Village[i], 'Establised_Year': Establised_Year[i],
#             'Ayush': Ayush[i], 'Miscellaneous_Facilities': Miscellaneous_Facilities[i],
#             'Number_Doctor': Number_Doctor[i], 'Num_Mediconsultant_or_Expert': Num_Mediconsultant_or_Expert[i],
#             'Total_Num_Beds': Total_Num_Beds[i], 'Number_Private_Wards': Number_Private_Wards[i],
#             'Num_Bed_for_Eco_Weaker_Sec': Num_Bed_for_Eco_Weaker_Sec[i],
#             'Empanelment_or_Collaboration_with': Empanelment_or_Collaboration_with[i],
#             'Emergency_Services': Emergency_Services[i], 'Tariff_Range': Tariff_Range[i], 'State_ID': State_ID[i],
#             'District_ID': District_ID[i]}
#     if State[i] not in Out_Put:
#         Out_Put[State[i]] = []
#     Out_Put[State[i]].append(data)
#
# with pandas.ExcelWriter('/home/setu/Downloads/Extracted.xlsx', engine='openpyxl', mode='a',
#                         if_sheet_exists='replace') as writer:
#     for i in Out_Put:
#         Data_Frame = pandas.DataFrame(Out_Put[i])
#         Data_Frame.to_excel(writer, sheet_name=i)
#         print(i)
