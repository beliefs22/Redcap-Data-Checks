import validators_updated as val
from openpyxl.styles import PatternFill, colors

new_fill = PatternFill('solid', fgColor=colors.RED)
def remove_blanks(mylist):
    for item in mylist[:]:
        if item == "":
            mylist.remove(item)
    return mylist
def visit1_check(visit1):
    errors = []
    errors.append(val.is_date(visit1.start_date))
    errors.append(val.is_date(visit1.end_date))
    errors.append(val.is_blank(visit1.oxygen_sup))
    if val.is_blank(visit1.oxygen_sup) == "":
        if visit1.oxygen_sup.value == "Yes":
            errors.append(val.is_blank(visit1.oxygen_sup_rate))
            errors.append(val.is_blank(visit1.oxygen_sup_route))
    errors.append(val.is_blank(visit1.icu))
    if val.is_blank(visit1.icu) == "":
        if visit1.icu.value == "Yes":
            errors.append(val.is_blank(visit1.icu_start))
            errors.append(val.is_blank(visit1.icu_days))
    errors.append(val.is_blank(visit1.death))
    if val.is_blank(visit1.death) == "":
        if visit1.death.value == "Yes":
            errors.append(val.is_blank(visit1.death_date))
    return remove_blanks(errors)

def visit2_check(visit2):
    errors = []
    errors.append(val.is_blank(visit2.other_virus))
    if val.is_blank(visit2.other_virus) == "":
        if visit2.other_virus.value == "Yes":
            errors.append(val.is_blank(visit2.rsv))
            errors.append(val.is_blank(visit2.parainfluenza))
            errors.append(val.is_blank(visit2.rhinovirus))
            errors.append(val.is_blank(visit2.metapneumovirus))
            errors.append(val.is_blank(visit2.adenovirus))
    return remove_blanks(errors)

def visit3_check(visit3):
    errors = []
    errors.append(val.is_blank(visit3.diagnosis_influenza))
    errors.append(val.is_blank(visit3.diagnosis_viral))
    errors.append(val.is_blank(visit3.diagnosis_pneumonia))
    errors.append(val.is_blank(visit3.diagnosis_mi))
    errors.append(val.is_blank(visit3.diagnosis_stroke))
    errors.append(val.is_blank(visit3.diagnosis_num))
    if val.is_blank(visit3.diagnosis_num) == "":
        if visit3.diagnosis_num.value in [1,"more than three"]:
            errors.append(val.is_blank(visit3.diagnosis1))
            if visit3.diagnosis_num.value in [2, "more than three"]:
                errors.append(val.is_blank(visit3.diagnosis2))
                if visit3.diagnosis_num.value in [3, "more than three"]:
                    errors.append(val.is_blank(visit3.diagnosis3))
    return remove_blanks(errors)
                        
def influenza_result_check(influenza_result):
    errors = []
    errors.append(val.is_blank(influenza_result.influenza_name))       
    errors.append(val.is_blank(influenza_result.influenza_test_type))
    if val.is_blank(influenza_result.influenza_test_type) == "":
        if influenza_result.influenza_test_type.value == "Other":
            errors.append(val.is_blank(influenza_result.influenza_type_other))
    errors.append(val.valid_result(influenza_result.influenza_result))
    errors.append(val.is_date(influenza_result.influenza_test_date))
    errors.append(val.is_time(influenza_result.influenza_test_time))
    errors.append(val.is_date(influenza_result.influenza_result_date))
    errors.append(val.is_time(influenza_result.influenza_result_time))
    errors.append(val.is_blank(influenza_result.influenza_typing_done))
    if val.is_blank(influenza_result.influenza_typing_done) == "":
        if influenza_result.influenza_typing_done.value == "Yes":
            errors.append(val.is_blank(influenza_result.influenza_type))
    return remove_blanks(errors)

def antiviral_check(antiviral):
    errors = []
    errors.append(val.is_blank(antiviral.antiviral_name))
    errors.append(val.is_blank(antiviral.antiviral_route))
    errors.append(val.is_date(antiviral.antiviral_date))
    errors.append(val.is_time(antiviral.antiviral_time))
    return remove_blanks(errors)


def antibiotic_check(antibiotic):
    errors = []
    errors.append(val.is_blank(antibiotic.antibiotic_name))
    errors.append(val.is_date(antibiotic.antibiotic_date))
    errors.append(val.is_blank(antibiotic.antibiotic_days))
    errors.append(val.is_blank(antibiotic.antibiotic_indication))
    return remove_blanks(errors)

