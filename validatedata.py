import openpyxl
import collections
import tuplesforvalidation as tup
import checks

tuples = tup.mytuples()
locations = tup.locations()

Visit1 = tuples.visit1
Visit2 = tuples.visit2
Visit3 = tuples.visit3
Influenza_Result = tuples.influenza_result
Antiviral = tuples.antiviral
Antiviral_Script = tuples.antiviral_script
Antibiotic = tuples.antibiotic
Antibiotic_Script = tuples.antibiotic_script

visit1_locations = locations.visit1_locations
visit2_locations = locations.visit2_locations
visit3_locations = locations.visit3_locations
influenza_result_num_locations = locations.influenza_result_num_locations
influenza_result_locations = locations.influenza_result_locations
antiviral_num_locations = locations.antiviral_num_locations
antiviral_locations = locations.antiviral_locations
antiviral_script_num_locations = locations.antiviral_script_num_locations
antiviral_script_locations = locations.antiviral_script_locations
antibiotic_num_locations = locations.antibiotic_num_locations
antibiotic_locations = locations.antibiotic_locations
antibiotic_script_num_locations = locations.antibiotic_script_num_locations
antibiotic_script_locations = locations.antibiotic_script_locations

main_file = openpyxl.load_workbook(
    'Active_ED_Visit_Data_Check_10_6_16.xlsx')
error_file = open('errors.txt','wb')

main_sheet = main_file.active
headers = main_sheet[1]

for i in range(2, main_sheet.max_row+1):
    row = main_sheet[i]
    #print "validating subject", row[0].value
    if row[2].value != None:
        all_errors = []
        number_of_visits = int(row[2].value)
        for j in range(1,number_of_visits + 1):
            visit1 = Visit1(*row[visit1_locations[j][0]:visit1_locations[j][1]])
            results = checks.visit1_check(visit1)
            if results != []:
                for item in results:
                    all_errors.append(item)
            visit2 = Visit2(*row[visit2_locations[j][0]:visit2_locations[j][1]])
            results = checks.visit2_check(visit2)
            if results != []:
                for item in results:
                    all_errors.append(item)
            visit3 = Visit3(*row[visit3_locations[j][0]:visit3_locations[j][1]])
            results = checks.visit3_check(visit3)
            if results != []:
                for item in results:
                    all_errors.append(item)
            #7 possible influenza test done
            influenza_result_num = row[influenza_result_num_locations[j]].value
            if influenza_result_num != None:
                for k in range(1,influenza_result_num+1):
                    start = influenza_result_locations[j][0] + ((k-1) * 10)
                    influenza_result = Influenza_Result(*row[start: start + 10])
                    results =checks.influenza_result_check(influenza_result)
                    if results != []:
                        for item in results:
                            all_errors.append(item)
            #2 possible antiviral
            antiviral_num = row[antiviral_num_locations[j]].value
            if antiviral_num != None:
                for l in range(1,antiviral_num+1):
                    start = antiviral_locations[j][0] + ((l-1) * 4)
                    antiviral = Antiviral(*row[start:start+4])
                    results = checks.antiviral_check(antiviral)
                    if results != []:
                        for item in results:
                            all_errors.append(item)
            #2 possible antiviral scripts
            antiviral_script_num = row[antiviral_script_num_locations[j]].value
            if antiviral_script_num != None:
                for m in range(1,antiviral_script_num+1):
                    start = antiviral_script_locations[j][0] + ((m-1))
                    antiviral_script = Antiviral_Script(*row[start:start+1])
                    results = checks.antiviral_script_check(antiviral_script)
                    if results != []:
                        for item in results:
                            all_errors.append(item)
            #5 possible antibiotics given
            antibiotic_num = row[antibiotic_num_locations[j]].value
            if antibiotic_num != None:
                for n in range(1,antibiotic_num+1):
                    start = antibiotic_locations[j][0] + ((n-1)* 5)
                    antibiotic = Antibiotic(*row[start:start+5])
                    results = checks.antibiotic_check(antibiotic)
                    if results != []:
                        for item in results:
                            all_errors.append(item)
            #3 possible anitiiotc scripts given
            antibiotic_script_num = row[antibiotic_script_num_locations[j]].value
            if antibiotic_script_num != None:
                for o in range(1,antibiotic_script_num):
                    start = antibiotic_script_locations[j][0] + ((o-1) * 2)
                    antibiotic_script = Antibiotic_Script(*row[start:start+2])
                    results = checks.antibiotic_script_check(antibiotic_script)
                    if results != []:
                        for item in results:
                            all_errors.append(item)
        if all_errors != []:
            all_errors = [main_sheet[item].value
                          for item in all_errors]
            error_file.write(row[0].value + ": " + ",".join(all_errors) + "\n")
            

main_file.save('test.xlsx')
error_file.close()
