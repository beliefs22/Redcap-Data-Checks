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
influenza_result_locations = locations.influenza_result_locations
antiviral_locations = locations.antiviral_locations
antiviral_script_locations = locations.antiviral_script_locations
antibiotic_locations = locations.antibiotic_locations
antibiotic_script_locations = locations.antibiotic_script_locations

main_file = openpyxl.load_workbook(
    'Active_ED_Visit_Data_Check_10_6_16.xlsx')

main_sheet = main_file.active

for i in range(2, main_sheet.max_row):
    visit1_tuples = []
    visit2_tuples = []
    visit3_tuples = []
    influenza_result_tuples = []
    antiviral_tuples = []
    antiviral_script_tuples = []
    antibiotic_tuples = []
    antibiotic_script_tuples = []
    row = main_sheet[i]
    print "validating subject", row[0].value
    if row[2].value != None:
        number_of_visits = int(row[2].value)
        for j in range(1,number_of_visits + 1):
            visit1 = Visit1(*row[visit1_locations[j][0]:visit1_locations[j][1]])
            checks.visit1_check(visit1)
            visit2 = Visit2(*row[visit2_locations[j][0]:visit2_locations[j][1]])
            visit3 = Visit3(*row[visit3_locations[j][0]:visit3_locations[j][1]])
            visit1_tuples.append(visit1)
            visit2_tuples.append(visit2)
            visit3_tuples.append(visit3)
            #7 possible influenza test done
            for k in range(1,8):
                start = influenza_result_locations[j][0] + ((k-1) * 10)
                influenza_result = Influenza_Result(*row[start: start + 10])
                influenza_result_tuples.append(influenza_result)
            #2 possible antiviral
            for l in range(1,3):
                start = antiviral_locations[j][0] + ((l-1) * 4)
                antiviral = Antiviral(*row[start:start+4])
                antiviral_tuples.append(antiviral)
            #2 possible antiviral scripts
            for m in range(1,3):
                start = antiviral_script_locations[j][0] + ((m-1))
                antiviral_script = Antiviral_Script(*row[start:start+1])
                antiviral_script_tuples.append(antiviral_script)
            #5 possible antibiotics given
            for n in range(1,6):
                start = antibiotic_locations[j][0] + ((n-1)* 5)
                antibiotic = Antibiotic(*row[start:start+5])
                antibiotic_tuples.append(antibiotic)
            #3 possible anitiiotc scripts given
            for o in range(1,4):
                start = antibiotic_script_locations[j][0] + ((o-1) * 2)
                antibiotic_scipt = Antibiotic_Script(*row[start:start+2])
                antibiotic_script_tuples.append(Antibiotic_Script)

main_file.save('test.xlsx')
