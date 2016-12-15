import collections
import csv
import openpyxl
import checks_ed
from openpyxl.styles import PatternFill, colors

new_fill = PatternFill('solid', fgColor=colors.RED)

with open('CEIRSActiveSurveilla_DATA_2016-12-14_1657.csv') as myfile,\
    open('CEIRSActiveSurveilla_DATA_LABELS_2016-12-14_1856.xlsx') as testfile:
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
    for atuple in mytuples:
        result = {}
        result[atuple.id.value] = checks_ed.ed_check(atuple)
        results.append(result)
    for result in results:
        key, value = result.items()[0]
        if value:
            print key, value
    subject_data.save('new_test_ouput.xlsx')



