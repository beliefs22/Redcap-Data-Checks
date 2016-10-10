import validators as val
from openpyxl.styles import PatternFill, colors

def check(visit, row):
    new_fill = PatternFill('solid', fgColor=colors.RED)
    if not val.is_date(visit.arrival_date):
        row[0].fill = new_fill
    if not val.is_time(visit.arrival_time):
        row[1].fill = new_fill
    if not val.is_date(visit.departure_date):
        row[2].fill = new_fill
    if not val.is_time(visit.departure_time):
        row[3].fill = new_fill
    if not val.valid_temp(visit.temp):
        row[4].fill = new_fill
    if not val.valid_pulse(visit.pulse):
        row[5].fill = new_fill
    if not val.valid_resp(visit.resp):
        row[6].fill = new_fill
    if not val.valid_systolic(visit.stystolic):
        row[7].fill = new_fill
    if not val.valid_oxygen(visit.oxygen_sat):
        row[8].fill = new_fill
    if val.is_blank(visit.oxygen_sup):
        row[9].fill = new_fill
    else:
        #expecting a value for oxygen sup rate
        if visit.oxygen_sup == "Yes":
            if val.is_blank(visit.oxygen_sup_rate):
                row[10].fill = new_fill
            if not val.is_blank(visit.oxygen_sup_route):
                row[11].fill = new_fill
    if val.is_blank(visit.pharyngeal):
        row[12].fill = new_fill
    if val.is_blank(visit.cerival):
        row[13].fill = new_fill
    if val.is_blank(visit.ams):
        row[14].fill = new_fill
    if not val.valid_ph(visit.ph):
        row[15].fill = new_fill
    if not val.valid_bun(visit.bun):
        row[16].fill = new_fill
    if not val.valid_sodium(visit.sodium):
        row[17].fill = new_fill
    if not val.valid_glucose(visit.glucose):
        row[18].fill = new_fill
    if not val.valid_hematocrit(visit.hematocrit):
        row[19].fill = new_fill
    if val.is_blank(visit.influenza1_typing_done):
        row[20].fill = new_fill
    else:
        if visit.influenza1_typing_done == "Yes":
            if val.is_blank(visit.influenza_test_num):
                row[21].fill = new_fill
            else:
                if visit.influenza_test_num >=1:
                    if is_blank(visit.influenza1_name):
                        row[22].fill = new_fill
                    if is_blank(visit.influenza1_test_type):
                        row[23].fill = new_fill
                    if visit.influenza1_test_type == "Other":
                        if is_blank(
                    if visit.influenza_test_num >=2:
                        if is_blank(visit.influenza2
                        
    
        
