import validators as val
from openpyxl.styles import PatternFill, colors

new_fill = PatternFill('solid', fgColor=colors.RED)

def visit1_check(visit1):
    if not val.is_date(visit1.arrival_date.value):
        visit1.arrival_date.fill = new_fill
    if not val.is_time(visit1.arrival_time.value):
        visit1.arrival_time.fill = new_fill
    if not val.is_date(visit1.departure_date.value):
        visit1.arrival_date.fill = new_fill
    if not val.is_time(visit1.departure_time.value):
        visit1.arrival_time.fill = new_fill
    if not val.valid_temp(visit1.temp.value):
        visit1.temp.fill = new_fill
    if not val.valid_pulse(visit1.pulse.value):
        visit1.pulse.fill = new_fill
    if not val.valid_resp(visit1.resp.value):
        visit1.resp.fill = new_fill
    if not val.valid_systolic(visit1.systolic.value):
        visit1.systolic.fill = new_fill
    if not val.valid_oxygen(visit1.oxygen_sat):
        visit1.oxygen_sat.fill = new_fill
    if val.is_blank(visit1.oxygen_sup.value):
        visit1.oxygen_sup.fill = new_fill
    else:
        if visit1.oxygen_sup.value == "Yes":
            if val.is_blank(visit1.oxygen_sup_rate.value):
                visit1.oxygen_sup_rate.fill = new_fill
            if val.is_blank(visit1.oxygen_sup_route.value):
                visit1.oxygen_sup_route.fill = new_fill
    if val.is_blank(visit1.pharyngeal.value):
        visit1.pharyngeal.fill = new_fill
    if val.is_blank(visit1.cervical.value):
        visit1.cervical.fill = new_fill
    if val.is_blank(visit1.ams.value):
        visit1.aml.fill = new_fill
    if not val.valid_ph(visit1.ph.value):
        visit1.ph.fill = new_fill
    if not val.valid_bun(visit1.bun.value):
        visit1.bun.fill = new_fill
    if not val.valid_sodium(visit1.sodium.value):
        visit1.sodium.fill = new_fill
    if not val.valid_glucose(visit1.glucose.value):
        visit1.glucose.fill = new_fill
    if not val.valid_hematocrit(visit1.hematocrit.value):
        visit1.hematocrit.fill = new_fill
