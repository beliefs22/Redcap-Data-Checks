import openpyxl
import collections
import csv
import validators_ed as val

def get_fields():

    with open('Master_Header_File_14_0076.xlsx', 'rb') as master_header_file:
        all_headers = openpyxl.load_workbook(master_header_file)

        #Get sheets for each file type
        eligibility_sheet = all_headers.get_sheet_by_name('Eligibility')
        demographic_sheet = all_headers.get_sheet_by_name('Demographic')
        symptom_sheet = all_headers.get_sheet_by_name('Symptoms')
        medical_sheet = all_headers.get_sheet_by_name('Medical')
        enrollment_specimen_sheet = all_headers.get_sheet_by_name('Enrollment_Specimen')

        all_sheets = {'eligibility': eligibility_sheet, 'demographic': demographic_sheet, 'symptoms': symptom_sheet,
                      'medical': medical_sheet, 'enrollment_specimen': enrollment_specimen_sheet}
        headers_and_fields = {}
        for sheet_name, sheet in all_sheets.iteritems():
            data_in_sheet = sheet.iter_rows()
            #first that correspond to the fields and data
            headers = [cell.value
                       for cell in data_in_sheet.next()
                       ]
            headers = headers[1:]

            fields = [[cell.value for cell in row
                       if cell.value]
                      for row in data_in_sheet
                      ]
            headers_and_fields[sheet_name] = {'headers': headers,
                                              'fields': fields}
        return headers_and_fields

def test_by_type(cell, test_type):
    test = {'date': val.is_date, 'time': val.is_time, 'pulse': val.valid_pulse,'temp': val.valid_temp,
            'resp': val.valid_resp, 'systolic': val.valid_systolic, 'sodium': val.valid_sodium,
            'glucose': val.valid_glucose, 'hematocrit': val.valid_hematocrit, 'oxygen': val.valid_oxygen,
            'bun': val.valid_bun, 'blank': val.is_blank, 'ph': val.valid_ph
            }

    return test[test_type](cell)

def eligibility_check():
    with open('14_0076_Eligibility.xlsx', 'rb') as eligibility_file:
        eligibility_workbook = openpyxl.load_workbook(eligibility_file)
        eligibility_worksheet = eligibility_workbook.active
        headers_and_fields = get_fields()
        eligibility_headers = headers_and_fields['eligibility']['headers']
        eligibility_fields = headers_and_fields['eligibility']['fields']

        eligibility_tuple = collections.namedtuple('eligibility', field_names=eligibility_headers)
        eligibility_data = eligibility_worksheet.iter_rows()
        #skip human readable headres eligibility_file
        eligibility_data.next()
        eligibility_data_to_check = []

        for row in eligibility_data:
            one_subjects_data = eligibility_tuple(*[cell
                                                    for cell in row
                                                    ])
            eligibility_data_to_check.append(one_subjects_data)

        statement = "eligibility_tuple.%s"
        for eligibility_tuple in eligibility_data_to_check:
            for field in eligibility_fields:
                if field[0] == 'simple':
                    print "simple ran"
                    simple_field_names = field[1:]
                    for field_name in simple_field_names:
                        eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex without number':
                    print "complex without number ran"
                    start_check = field[1]
                    complex_field_names = field[2:]
                    #check start condition
                    if eval("eligibility_tuple.%s" % start_check) == True:
                        for field_name in complex_field_names:
                            eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex with number':
                    start_check = field[1]
                    number_to_check = field[2]
                    complex_field_names = field[3:]
                    #check start condition
                    if eval("eligibility_tuple.%s" % start_check) == True:
                        for i in range(1, number_to_check + 1):
                            for field_name in complex_field_names:
                                eval("val.is_blank(" + statement % (field_name % i,) + ")")

        eligibility_workbook.save('14_0076_Eligibility_w_highlighted_erroros.xlsx')

def demographic_check():
    with open('14_0076_Demographic.xlsx', 'rb') as demographic_file:
        demographic_workbook = openpyxl.load_workbook(demographic_file)
        demographic_worksheet = demographic_workbook.active
        headers_and_fields = get_fields()
        demographic_headers = headers_and_fields['demographic']['headers']
        demographic_fields = headers_and_fields['demographic']['fields']

        demographic_tuple = collections.namedtuple('demographic', field_names=demographic_headers)
        demographic_data = demographic_worksheet.iter_rows()
        #skip human readable headres demographic_file
        demographic_data.next()
        demographic_data_to_check = []

        for row in demographic_data:
            one_subjects_data = demographic_tuple(*[cell
                                                    for cell in row
                                                    ])
            demographic_data_to_check.append(one_subjects_data)

        statement = "demographic_tuple.%s"
        for demographic_tuple in demographic_data_to_check:
            for field in demographic_fields:
                if field[0] == 'simple':
                    print "simple ran"
                    simple_field_names = field[1:]
                    for field_name in simple_field_names:
                        eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex without number':
                    print "complex without number ran"
                    start_check = field[1]
                    complex_field_names = field[2:]
                    #check start condition
                    if eval("demographic_tuple.%s" % start_check) == True:
                        for field_name in complex_field_names:
                            eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex with number':
                    start_check = field[1]
                    number_to_check = field[2]
                    complex_field_names = field[3:]
                    #check start condition
                    if eval("demographic_tuple.%s" % start_check) == True:
                        for i in range(1, number_to_check + 1):
                            for field_name in complex_field_names:
                                eval("val.is_blank(" + statement % (field_name % i,) + ")")

        demographic_workbook.save('14_0076_demographic_w_highlighted_erroros.xlsx')
        
def symptoms_check():
    with open('14_0076_Symptoms.xlsx', 'rb') as symptoms_file:
        symptoms_workbook = openpyxl.load_workbook(symptoms_file)
        symptoms_worksheet = symptoms_workbook.active
        headers_and_fields = get_fields()
        symptoms_headers = headers_and_fields['symptoms']['headers']
        symptoms_fields = headers_and_fields['symptoms']['fields']

        symptoms_tuple = collections.namedtuple('symptoms', field_names=symptoms_headers)
        symptoms_data = symptoms_worksheet.iter_rows()
        #skip human readable headres symptoms_file
        symptoms_data.next()
        symptoms_data_to_check = []

        for row in symptoms_data:
            one_subjects_data = symptoms_tuple(*[cell
                                                    for cell in row
                                                    ])
            symptoms_data_to_check.append(one_subjects_data)

        statement = "symptoms_tuple.%s"
        for symptoms_tuple in symptoms_data_to_check:
            for field in symptoms_fields:
                if field[0] == 'simple':
                    print "simple ran"
                    simple_field_names = field[1:]
                    for field_name in simple_field_names:
                        eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex without number':
                    print "complex without number ran"
                    start_check = field[1]
                    complex_field_names = field[2:]
                    #check start condition
                    if eval("symptoms_tuple.%s" % start_check) == True:
                        for field_name in complex_field_names:
                            eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex with number':
                    start_check = field[1]
                    number_to_check = field[2]
                    complex_field_names = field[3:]
                    #check start condition
                    if eval("symptoms_tuple.%s" % start_check) == True:
                        for i in range(1, number_to_check + 1):
                            for field_name in complex_field_names:
                                eval("val.is_blank(" + statement % (field_name % i,) + ")")

        symptoms_workbook.save('14_0076_symptoms_w_highlighted_erroros.xlsx')

def medical_check():
    with open('14_0076_medical.xlsx', 'rb') as medical_file:
        medical_workbook = openpyxl.load_workbook(medical_file)
        medical_worksheet = medical_workbook.active
        headers_and_fields = get_fields()
        medical_headers = headers_and_fields['medical']['headers']
        medical_fields = headers_and_fields['medical']['fields']

        medical_tuple = collections.namedtuple('medical', field_names=medical_headers)
        medical_data = medical_worksheet.iter_rows()
        #skip human readable headres medical_file
        medical_data.next()
        medical_data_to_check = []

        for row in medical_data:
            one_subjects_data = medical_tuple(*[cell
                                                    for cell in row
                                                    ])
            medical_data_to_check.append(one_subjects_data)

        statement = "medical_tuple.%s"
        for medical_tuple in medical_data_to_check:
            for field in medical_fields:
                if field[0] == 'simple':
                    print "simple ran"
                    simple_field_names = field[1:]
                    for field_name in simple_field_names:
                        eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex without number':
                    print "complex without number ran"
                    start_check = field[1]
                    complex_field_names = field[2:]
                    #check start condition
                    if eval("medical_tuple.%s" % start_check) == True:
                        for field_name in complex_field_names:
                            eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex with number':
                    start_check = field[1]
                    number_to_check = field[2]
                    complex_field_names = field[3:]
                    #check start condition
                    if eval("medical_tuple.%s" % start_check) == True:
                        for i in range(1, number_to_check + 1):
                            for field_name in complex_field_names:
                                eval("val.is_blank(" + statement % (field_name % i,) + ")")

        medical_workbook.save('14_0076_medical_w_highlighted_erroros.xlsx')

def enrollment_specimen_check():
    with open('14_0076_Enrollment_Specimen.xlsx', 'rb') as enrollment_specimen_file:
        enrollment_specimen_workbook = openpyxl.load_workbook(enrollment_specimen_file)
        enrollment_specimen_worksheet = enrollment_specimen_workbook.active
        headers_and_fields = get_fields()
        enrollment_specimen_headers = headers_and_fields['enrollment_specimen']['headers']
        enrollment_specimen_fields = headers_and_fields['enrollment_specimen']['fields']

        enrollment_specimen_tuple = collections.namedtuple('enrollment_specimen', field_names=enrollment_specimen_headers)
        enrollment_specimen_data = enrollment_specimen_worksheet.iter_rows()
        #skip human readable headres enrollment_specimen_file
        enrollment_specimen_data.next()
        enrollment_specimen_data_to_check = []

        for row in enrollment_specimen_data:
            one_subjects_data = enrollment_specimen_tuple(*[cell
                                                    for cell in row
                                                    ])
            enrollment_specimen_data_to_check.append(one_subjects_data)

        statement = "enrollment_specimen_tuple.%s"
        for enrollment_specimen_tuple in enrollment_specimen_data_to_check:
            for field in enrollment_specimen_fields:
                if field[0] == 'simple':
                    print "simple ran"
                    simple_field_names = field[1:]
                    for field_name in simple_field_names:
                        eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex without number':
                    print "complex without number ran"
                    start_check = field[1]
                    complex_field_names = field[2:]
                    #check start condition
                    if eval("enrollment_specimen_tuple.%s" % start_check) == True:
                        for field_name in complex_field_names:
                            eval("val.is_blank(" + statement % (field_name,) + ")")

                if field[0] == 'complex with number':
                    start_check = field[1]
                    number_to_check = field[2]
                    complex_field_names = field[3:]
                    #check start condition
                    if eval("enrollment_specimen_tuple.%s" % start_check) == True:
                        for i in range(1, number_to_check + 1):
                            for field_name in complex_field_names:
                                eval("val.is_blank(" + statement % (field_name % i,) + ")")

        enrollment_specimen_workbook.save('14_0076_enrollment_specimen_w_highlighted_erroros.xlsx')
def main():
    eligibility_check()
    demographic_check()
    symptoms_check()
    medical_check()
    enrollment_specimen_check()

if __name__ == '__main__':
    main()