import collections
import csv
import openpyxl
import checks_ed_old
from openpyxl.styles import PatternFill, colors

new_fill = PatternFill('solid', fgColor=colors.RED)

with open('CEIRSActiveSurveilla_DATA_2016-12-18_1135.csv', 'rb') as myfile,\
    open('CEIRSActiveSurveilla_DATA_LABELS_2016-12-18_1137.xlsx', 'rb') as testfile, \
    open('output.txt', 'w') as outfile:
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
        for field_names in complex:
            print "looking for fields", field_names
            answer = checks_ed_old.complex_check(atuple, complex[field_names])
            if answer:
                results.append((atuple.id.value, answer))

    final_result = collections.defaultdict(list)
    for item in results:
        final_result[item[0]] += item[1]
    for key, value in final_result.iteritems():
        outfile.write("Subject: {} Errors: {}\n\n\n".format(key, value))
    subject_data.save('text.xlsx')


