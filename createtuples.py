import collections
import csv
import openpyxl
import checks_ed_old
import checks_ip_updated
from openpyxl.styles import PatternFill, colors

new_fill = PatternFill('solid', fgColor=colors.RED)

with open('CEIRSActiveSurveilla_DATA_2016-12-18_1135.csv', 'rb') as myfile,\
    open('CEIRSActiveSurveilla_DATA_LABELS_2016-12-18_1137.xlsx', 'rb') as testfile, \
    open('output_ed.txt', 'w') as outfile:
    csvreader = csv.DictReader(myfile)
    headers = csvreader.fieldnames
    subject_data = openpyxl.load_workbook(testfile)
    data_sheet = subject_data.active

    ed_tuple = collections.namedtuple('ED', field_names=headers)
    rows = data_sheet.iter_rows()
    rows.next()
    mytuples = []
    for row in rows:
        one_visit = ed_tuple(*[cell
                               for cell in row
                               ])
        mytuples.append(one_visit)
    results = []
    complex, simple = checks_ed_old.field_names()
    for atuple in mytuples:
        answer = checks_ed_old.simple_blank_check(atuple, simple)
        if answer:
            results.append((atuple.id.value, answer))
        for field_names in complex:
            print "looking for fields", field_names
            answer = checks_ed_old.complex_check(atuple, complex[field_names])
            if answer:
                results.append((atuple.id.value, answer))

    final_result = collections.defaultdict(list)
    for item in results:
        final_result[item[0]] += item[1]
    print "writing output file"
    for key, value in final_result.iteritems():
        outfile.write("Subject: {} Errors: {}\n\n\n".format(key, value))
    print "finished output file"
    print "saving output excel"
    subject_data.save('ed_text.xlsx')
    print "finished"

with open('CEIRSActiveSurveilla_DATA_2016-12-19_1814.csv', 'rb') as myfile,\
    open('CEIRSActiveSurveilla_DATA_LABELS_2016-12-19_1814.xlsx', 'rb') as testfile, \
    open('output_ip.txt', 'w') as outfile:
    csvreader = csv.DictReader(myfile)
    headers = csvreader.fieldnames
    subject_data = openpyxl.load_workbook(testfile)
    data_sheet = subject_data.active

    ip_tuple = collections.namedtuple('IP', field_names=headers)
    rows = data_sheet.iter_rows()
    rows.next()
    mytuples = []
    for row in rows:
        one_visit = ip_tuple(*[cell
                               for cell in row
                               ])
        mytuples.append(one_visit)
    results = []
    complex, simple = checks_ip_updated.field_names()
    for atuple in mytuples:
        for field_names in complex:
            print "looking for fields", field_names
            answer = checks_ip_updated.complex_check(atuple, complex[field_names])
            if answer:
                results.append((atuple.id.value, answer))

    final_result = collections.defaultdict(list)
    for item in results:
        final_result[item[0]] += item[1]
    print "writing IP output file"
    for key, value in final_result.iteritems():
        outfile.write("Subject: {} Errors: {}\n\n\n".format(key, value))
    print "finished output file"
    print "saving output excel"
    subject_data.save('IP_text.xlsx')
    print "finished"
