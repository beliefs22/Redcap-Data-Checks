import validators as val
from openpyxl.styles import PatternFill, colors

new_fill = PatternFill('solid', fgColor=colors.RED)
def remove_num(num):
    for item in num[:]:
        if item.isdigit():
            num = num.replace(item,"")
    return num + "1"
def visit1_check(visit1):
    errors = []
    if not val.is_date(visit1.start_date.value):
        visit1.start_date.fill = new_fill
        errors.append(visit1.start_date.coordinate)
    if not val.is_date(visit1.end_date.value):
        visit1.end_date.fill = new_fill
        errors.append(visit1.end_date.coordinate)
    if val.is_blank(visit1.oxygen_sup.value):
        visit1.oxygen_sup.fill = new_fill
        errors.append(visit1.oxygen_sup.coordinate)
    else:
        if visit1.oxygen_sup.value == "Yes":
            if val.is_blank(visit1.oxygen_sup_rate.value):
                visit1.oxygen_sup_rate.fill = new_fill
                errors.append(visit1.oxygen_sup_rate.coordinate)
            if val.is_blank(visit1.oxygen_sup_route.value):
                visit1.oxygen_sup_route.fill = new_fill
                errors.append(visit1.oxygen_sup_route.coordinate)
    if val.is_blank(visit1.icu.value):
        visit1.icu.fill = new_fill
        errors.append(visit1.icu.coordinate)
    else:
        if visit1.icu.value == "Yes":
            if val.is_blank(visit1.icu_start.value):
                visit1.icu_start.fill = new_fill
                errors.append(visit1.icu_start.coordinate)
            if val.is_blank(visit1.icu_days.value):
                visit1.icu_start.fill = new_fill
                errors.append(visit1.icu_start.coordinate)
    if val.is_blank(visit1.death.value):
        visit1.death.fill = new_fill
        errors.append(visit1.death.coordinate)
    else:
        if visit1.death.value == "Yes":
            if val.is_blank(visit1.death_date.value):
                visit1.death_date.fill = new_fill
                errors.append(visit1.death_date.coordinate)
    return map(remove_num,errors)

def visit2_check(visit2):
    errors = []
    if val.is_blank(visit2.other_virus.value):
        visit2.other_virus.fill =  new_fill
        errors.append(visit2.other_virus.coordinate)
    else:
        if visit2.other_virus.value == "Yes":
            if val.is_blank(visit2.rsv.value):
                visit2.rsv.fill = new_fill
                errors.append(visit2.other_virus.coordinate)
            if val.is_blank(visit2.parainfluenza.value):
                visit2.parainfluenza.fill = new_fill
                errors.append(visit2.parainfluenza.coordinate)
            if val.is_blank(visit2.rhinovirus.value):
                visit2.rhinovirus.fill = new_fill
                errors.append(visit2.rhinovirus.coordinate)
            if val.is_blank(visit2.metapneumovirus.value):
                visit2.metapneumovirus.fill = new_fill
                errors.append(visit2.metapneumovirus.coordinate)
            if val.is_blank(visit2.adenovirus.value):
                visit2.adenovirus.fill = new_fill
                errors.append(visit2.adenovirus.coordinate)
    return map(remove_num,errors)

def visit3_check(visit3):
    errors = []
    if val.is_blank(visit3.diagnosis_influenza.value):
        visit3.diagnosis_influenza.fill = new_fill
        errors.append(visit3.diagnosis_influenza.coordinate)
    if val.is_blank(visit3.diagnosis_viral.value):
        visit3.diagnosis_viral.fill = new_fill
        errors.append(visit3.diagnosis_viral.coordinate)
    if val.is_blank(visit3.diagnosis_pneumonia.value):
        visit3.diagnosis_pneumonia.fill = new_fill
        errors.append(visit3.diagnosis_pneumonia.coordinate)
    if val.is_blank(visit3.diagnosis_mi.value):
        visit3.diagnosis_mi.fill = new_fill
        errors.append(visit3.diagnosis_mi.coordinate)
    if val.is_blank(visit3.diagnosis_stroke.value):
        visit3.diagnosis_stroke.fill = new_fill
        errors.append(visit3.diagnosis_stroke.coordinate)
    if val.is_blank(visit3.diagnosis_num.value):
        visit3.diagnosis_num.fill = new_fill
        errors.append(visit3.diagnosis_num.coordinate)
    else:
        if visit3.diagnosis_num in [1,"more than three"]:
            if val.is_blank(visit3.diagnosis1.value):
                visit3.diagnosis1.fill = new_fill
                errors.append(visit3.diagnosis1.coordinate)
            if visit3.diagnosis_num in [2, "more than three"]:
                if val.is_blank(visit3.diagnosis2.value):
                    visit3.diagnosis2.fill  = new_fill
                    errors.append(visit3.diagnosis2.coordinate)
                if visit3.diagnosis_num.value in [3, "more than three"]:
                    if val.is_blank(visit3.diagnosis3.value):
                        visit3.diagnosis3.fill = new_fill
                        errors.append(visit3.diagnosis3.coordinate)
    return map(remove_num,errors)
                        
def influenza_result_check(influenza_result):
    errors = []
    if val.is_blank(influenza_result.influenza_name.value):
        influenza_result.influenza_name.fill = new_fill
        errors.append(influenza_result.influenza_name.coordinate)        
    if val.is_blank(influenza_result.influenza_test_type.value):
        influenza_result.influenza_test_type.fill = new_fill
        errors.append(influenza_result.influenza_test_type.coordinate)
    else:
        if influenza_result.influenza_test_type.value == "Other":
            if val.is_blank(influenza_result.influenza_type_other.value):
                influenza_result.influenza_type_other.fill = new_fill
                errors.append(influenza_result.influenza_type_other.coordinate)
    if not val.valid_result(influenza_result.influenza_result.value):
        influenza_result.influenza_result.fill = new_fill
        errors.append(influenza_result.influenza_result.coordinate)
    if not val.is_date(influenza_result.influenza_test_date.value):
        influenza_result.influenza_test_date.fill = new_fill
        errors.append(influenza_result.influenza_test_date.coordinate)
    if not val.is_time(influenza_result.influenza_test_time.value):
        influenza_result.influenza_test_time.fill = new_fill
        errors.append(influenza_result.influenza_test_time.coordinate)
    if not val.is_date(influenza_result.influenza_result_date.value):
        influenza_result.influenza_result_date.fill = new_fill
        errors.append(influenza_result.influenza_result_date.coordinate)
    if not val.is_time(influenza_result.influenza_result_time.value):
        influenza_result.influenza_result_time.fill = new_fill
        errors.append(influenza_result.influenza_result_time.coordinate)
    if val.is_blank(influenza_result.influenza_typing_done.value):
        influenza_result.influenza_typing_done.fill = new_fill
        errors.append(influenza_result.influenza_typing_done.coordinate)
    else:
        if influenza_result.influenza_typing_done.value == "Yes":
            if val.is_blank(influenza_result.influenza_type.value):
                influenza_result.influenza_type.fill =  new_fill
                errors.append(influenza_result.influenza_type.coordinate)
    return map(remove_num,errors)

def antiviral_check(antiviral):
    errors = []
    if val.is_blank(antiviral.antiviral_name.value):
        antiviral.antiviral_name.fill = new_fill
        errors.append(antiviral.antiviral_name.coordinate)
    if val.is_blank(antiviral.antiviral_route.value):
        antiviral.antiviral_route.fill = new_fill
        errors.append(antiviral.antiviral_route.coordinate)
    if not val.is_date(antiviral.antiviral_date.value):
        antiviral.antiviral_date.fill = new_fill
        errors.append(antiviral.antiviral_date.coordinate)
    if not val.is_time(antiviral.antiviral_time.value):
        antiviral.antiviral_time.fill = new_fill
        errors.append(antiviral.antiviral_time.coordinate)
    return map(remove_num,errors)


def antibiotic_check(antibiotic):
    errors = []
    if val.is_blank(antibiotic.antibiotic_name.value):
        antibiotic.antibiotic_name.fill = new_fill
        errors.append(antibiotic.antibiotic_name.coordinate)
    if not val.is_date(antibiotic.antibiotic_date.value):
        antibiotic.antibiotic_date.fill = new_fill
        errors.append(antibiotic.antibiotic_date.coordinate)
    if val.is_blank(antibiotic.antibiotic_days.value):
        antibiotic.antibiotic_days.fill = new_fill
        errors.append(antibiotic.antibiotic_days.coordinate)
    if val.is_blank(antibiotic.antibiotic_indication.value):
        antibiotic.antibiotic_indication.fill = new_fill
        errors.append(antibiotic.antibiotic_indication.coordinate)

    return map(remove_num,errors)

