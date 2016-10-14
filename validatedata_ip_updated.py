import openpyxl
import collections
import tuplesforvalidation_ip as tup
import checks_ip_updated as checks
import csv
#named tuples representing sections of the excel file
tuples = tup.mytuples()
#locations in the excel file where the field in each tuple lives
locations = tup.locations()
#visit tubples are the parts of the excel form that are always present
#for each subject
Visit1 = tuples.visit1
Visit2 = tuples.visit2
Visit3 = tuples.visit3
#Influenza_result tuples parts of excel that represent influenza testing done
Influenza_Result = tuples.influenza_result
#Part of excel that represents antiviral testing done
Antiviral = tuples.antiviral
#Part of excel that represents antibiotics given
Antibiotic = tuples.antibiotic

visit1_locations = locations.visit1_locations
visit2_locations = locations.visit2_locations
visit3_locations = locations.visit3_locations
#Section of the excel file that tells how many influenza test were done
influenza_result_num_locations = locations.influenza_result_num_locations
influenza_result_locations = locations.influenza_result_locations
#How many antiviral test were done
antiviral_num_locations = locations.antiviral_num_locations
antiviral_locations = locations.antiviral_locations
#how many antibiotics were given
antibiotic_num_locations = locations.antibiotic_num_locations
antibiotic_locations = locations.antibiotic_locations

#File that contains data to validate
main_file = openpyxl.load_workbook(
    'Active_IP_Visit_Data_Check_10_6_16.xlsx')
#Excel File with errors highlighted red
error_file = open('IP_Errors.csv','wb')
csvwriter = csv.writer(error_file)
#CSV file that tells where errors were found
csvwriter.writerow(['Subject ID',
                    'Error Structure =[Visit Number,Value Found(None=Blank),\
Redcap Label'])
#Each sheet only has one sheet which will be the active sheet
main_sheet = main_file.active

#Skip row one as it's just headers
for i in range(2, main_sheet.max_row+1):
    row = main_sheet[i]
    #print "validating subject", row[0].value
    if row[2].value != None:
        all_errors = []
        number_of_visits = int(row[2].value)
        for visit in range(1,number_of_visits + 1):
            visit1 = Visit1(
                *row[visit1_locations[visit][0]:visit1_locations[visit][1]])
            results = checks.visit1_check(visit1)
            if results != []:
                for item in results:
                    all_errors.append(
                        (("Visit" + str(visit),item)))                        
            visit2 = Visit2(
                *row[visit2_locations[visit][0]:visit2_locations[visit][1]])
            results = checks.visit2_check(visit2)
            if results != []:
                for item in results:
                    all_errors.append(
                        (("Visit" + str(visit),item)))  
            visit3 = Visit3(
                *row[visit3_locations[visit][0]:visit3_locations[visit][1]])
            results = checks.visit3_check(visit3)
            if results != []:
                for item in results:
                    all_errors.append(
                        (("Visit" + str(visit),item)))  
            #7 possible influenza test done
            influenza_result_num = row[influenza_result_num_locations[visit]].value
            if influenza_result_num != None:
                for influenza_test in range(1,influenza_result_num+1):
                    start = influenza_result_locations[visit][0] \
                            + ((influenza_test-1) * 10)
                    influenza_result = Influenza_Result(*row[start: start + 10])
                    results =checks.influenza_result_check(influenza_result)
                    if results != []:
                        for item in results:
                            all_errors.append(
                                (("Visit" + str(visit),item)))  
            #2 possible antiviral
            antiviral_num = row[antiviral_num_locations[visit]].value
            if antiviral_num != None:
                for antiviral_test in range(1,antiviral_num+1):
                    start = antiviral_locations[visit][0] +\
                            ((antiviral_test-1) * 4)
                    antiviral = Antiviral(*row[start:start+4])
                    results = checks.antiviral_check(antiviral)
                    if results != []:
                        for item in results:
                            all_errors.append(
                                (("Visit" + str(visit),item)))  
            #5 possible antibiotics given
            antibiotic_num = row[antibiotic_num_locations[visit]].value
            if antibiotic_num != None:
                for antibiotics in range(1,antibiotic_num+1):
                    start = antibiotic_locations[visit][0] +\
                            ((antibiotics-1)* 4)
                    antibiotic = Antibiotic(*row[start:start+4])
                    results = checks.antibiotic_check(antibiotic)
                    if results != []:
                        for item in results:
                            all_errors.append(
                                (("Visit" + str(visit),item)))  
        if all_errors != []:
            print "writing errors for" + row[0].value
            all_errors.insert(0,row[0].value)
            csvwriter.writerow(all_errors)
            
main_file.save('IP_Form_REDCap_Errors.xlsx')
error_file.close()
print "Done"
