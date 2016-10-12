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
    if not val.is_date(visit1.arrival_date.value):
        visit1.arrival_date.fill = new_fill
        errors.append(visit1.arrival_date.coordinate)
    if not val.is_time(visit1.arrival_time.value):
        visit1.arrival_time.fill = new_fill
        errors.append(visit1.arrival_time.coordinate)
    if not val.is_date(visit1.departure_date.value):
        visit1.departure_date.fill = new_fill
        errors.append(visit1.departure_date.coordinate)
    if not val.is_time(visit1.departure_time.value):
        visit1.departure_time.fill = new_fill
        errors.append(visit1.departure_time.coordinate)
    if not val.valid_temp(visit1.temp.value):
        visit1.temp.fill = new_fill
        errors.append(visit1.temp.coordinate)
    if not val.valid_pulse(visit1.pulse.value):
        visit1.pulse.fill = new_fill
        errors.append(visit1.pulse.coordinate)
    if not val.valid_resp(visit1.resp.value):
        visit1.resp.fill = new_fill
        errors.append(visit1.resp.coordinate)
    if not val.valid_systolic(visit1.systolic.value):
        visit1.systolic.fill = new_fill
        errors.append(visit1.systolic.coordinate)
    if not val.valid_oxygen(visit1.oxygen_sat):
        visit1.oxygen_sat.fill = new_fill
        errors.append(visit1.oxygen_sat.coordinate)
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
    if val.is_blank(visit1.pharyngeal.value):
        visit1.pharyngeal.fill = new_fill
        errors.append(visit1.pharyngeal.coordinate)
    if val.is_blank(visit1.cervical.value):
        visit1.cervical.fill = new_fill
        errors.append(visit1.cervical.coordinate)
    if val.is_blank(visit1.ams.value):
        visit1.ams.fill = new_fill
        errors.append(visit1.ams.coordinate)
    if not val.valid_ph(visit1.ph.value):
        visit1.ph.fill = new_fill
        errors.append(visit1.ph.coordinate)
    if not val.valid_bun(visit1.bun.value):
        visit1.bun.fill = new_fill
        errors.append(visit1.bun.coordinate)
    if not val.valid_sodium(visit1.sodium.value):
        visit1.sodium.fill = new_fill
        errors.append(visit1.sodium.coordinate)
    if not val.valid_glucose(visit1.glucose.value):
        visit1.glucose.fill = new_fill
        errors.append(visit1.glucose.coordinate)
    if not val.valid_hematocrit(visit1.hematocrit.value):
        visit1.hematocrit.fill = new_fill
        errors.append(visit1.hematocrit.coordinate)
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
    if val.is_blank(visit3.chest_xray):
        visit3.chest_xray = new_fill
        errors.append(visit3.chest_xray.coordinate)
    else:
        if visit3.chest_xray.value == "Yes":
            if val.is_blank(visit3.infiltrate.value):
                visit3.infiltrate.fill = new_fill
                errors.append(visit3.infiltrate.coordinate)
            if val.is_blank(visit3.consolidation.value):
                visit3.consolidation.fill = new_fill
                errors.append(visit3.consolidation.coordinate)
            if val.is_blank(visit3.effusions.value):
                visit3.effusions.fill = new_fill
                errors.append(visit3.effusions.coordinate)
            if val.is_blank(visit3.pneumonia.value):
                visit3.pneumonia.fill = new_fill
                errors.append(visit3.pneumonia.coordinate)
    if val.is_blank(visit3.intubated.value):
        visit3.intubated.fill = new_fill
        errors.append(visit3.intubated.coordinate)
    if val.is_blank(visit3.bipap.value):
        visit3.bipap.fill = new_fill
        errors.append(visit3.bipap.coordinate)
    if val.is_blank(visit3.supplemental_oxy.value):
        visit3.supplemental_oxy.fill = new_fill
        errors.append(visit3.supplemental_oxy.coordinate)
    else:
        if visit3.supplemental_oxy.value == "Yes":
            if val.is_blank(visit3.supplemental_oxy_rate.value):
                visit3.supplemental_oxy_rate.fill = new_fill
                errors.append(visit3.supplemental_oxy_rate.coordinate)
            if val.is_blank(visit3.supplemental_oxy_route.value):
                visit3.supplemental_oxy_route.fill = new_fill
                errors.append(visit3.supplemental_oxy_route.coordinate)
    if val.is_blank(visit3.death.value):
        visit3.death.fill = new_fill
        errors.append(visit3.death.coordinate)
    else:
        if visit3.death.value == "Yes":
            if val.is_blank(visit3.death_date.value) or \
               not val.is_date(visit3.death_date.value):
                visit3.death_date.fill = new_fill
                errors.append(visit3.death_date.coordinate)
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
    if val.is_blank(visit3.disposition.value):
        visit3.disposition.fill = new_fill
        errors.append(visit3.disposition.coordinate)
    if visit3.disposition.value == "Discharge":
        if val.is_blank(visit3.observation.value):
            visit3.observation.fill = new_fill
            errors.append(visit3.observation.coordinate)
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

def antiviral_script_check(antiviral_script):
    errors = []
    if val.is_blank(antiviral_script.antiviral_script_name.value):
        antiviral_script.antiviral_script_name.fill = new_fill
        errors.append(antiviral_script.antiviral_script_name.coordinate)
    return map(remove_num,errors)

def antibiotic_check(antibiotic):
    errors = []
    if val.is_blank(antibiotic.antibiotic_name.value):
        antibiotic.antibiotic_name.fill = new_fill
        errors.append(antibiotic.antibiotic_name.coordinate)
    if val.is_blank(antibiotic.antibiotic_route.value):
        antibiotic.antibiotic_route.fill = new_fill
        errors.append(antibiotic.antibiotic_route.coordinate)
    if val.is_blank(antibiotic.antibiotic_indication.value):
        antibiotic.antibiotic_indication.fill = new_fill
        errors.append(antibiotic.antibiotic_indication.coordinate)
    if not val.is_date(antibiotic.antibiotic_date.value):
        antibiotic.antibiotic_date.fill = new_fill
        errors.append(antibiotic.antibiotic_date.coordinate)
    if not val.is_time(antibiotic.antibiotic_time.value):
        antibiotic.antibiotic_time.fill = new_fill
        errors.append(antibiotic.antibiotic_time.coordinate)
    return map(remove_num,errors)

def antibiotic_script_check(antibiotic_script):
    errors = []
    if val.is_blank(antibiotic_script.antibiotic_script_name.value):
        antibiotic_script.antibiotic_script_name.fill = new_fill
        errors.append(antibiotic_script.antibiotic_script_name.coordinate)
    if val.is_blank(antibiotic_script.antibiotic_script_indication.value):
        antibiotic_script.antibiotic_script_indication.fill = new_fill
        errors.append(antibiotic_script.antibiotic_script_indication.coordinate)
    return map(remove_num,errors)
