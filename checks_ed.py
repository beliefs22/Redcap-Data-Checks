import validators_ed as val

def remove_blanks(mylist):
    for item in mylist[:]:
        if item == "":
            mylist.remove(item)
    return mylist

def visit1_check(visit1):
    errors = []
    errors.append(val.is_date(visit1.arrival_date))
    errors.append(val.is_time(visit1.arrival_time))
    errors.append(val.is_date(visit1.departure_date))
    errors.append(val.is_time(visit1.departure_time))
    errors.append(val.valid_temp(visit1.temp))
    errors.append(val.valid_pulse(visit1.pulse))
    errors.append(val.valid_resp(visit1.resp))
    errors.append(val.valid_systolic(visit1.systolic))
    errors.append(val.valid_oxygen(visit1.oxygen_sat))
    errors.append(val.is_blank(visit1.oxygen_sup))
    if val.is_blank(visit1.oxygen_sup) == "":
        if visit1.oxygen_sup.value == "Yes":
            errors.append(val.is_blank(visit1.oxygen_sup_rate))
            errors.append(val.is_blank(visit1.oxygen_sup_route))
    errors.append(val.is_blank(visit1.pharyngeal))
    errors.append(val.is_blank(visit1.cervical))
    errors.append(val.is_blank(visit1.ams))
    errors.append(val.valid_ph(visit1.ph))
    errors.append(val.valid_bun(visit1.bun))
    errors.append(val.valid_sodium(visit1.sodium))
    errors.append(val.valid_glucose(visit1.glucose))
    errors.append(val.valid_hematocrit(visit1.hematocrit))
    
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
    errors.append(val.is_blank(visit3.chest_xray))
    if val.is_blank(visit3.chest_xray) == "":
        if visit3.chest_xray.value == "Yes":
            errors.append(val.is_blank(visit3.infiltrate))
            errors.append(val.is_blank(visit3.consolidation))
            errors.append(val.is_blank(visit3.effusions))
            errors.append(val.is_blank(visit3.pneumonia))
    errors.append(val.is_blank(visit3.intubated))
    errors.append(val.is_blank(visit3.bipap))
    errors.append(val.is_blank(visit3.supplemental_oxy))
    if val.is_blank(visit3.supplemental_oxy) == "":
        if visit3.supplemental_oxy.value == "Yes":
            errors.append(val.is_blank(visit3.supplemental_oxy_rate))
            errors.append(val.is_blank(visit3.supplemental_oxy_route))
    errors.append(val.is_blank(visit3.death))
    if val.is_blank(visit3.death) == "":
        if visit3.death.value == "Yes":
            errors.append(val.is_date(visit3.death_date))
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
    errors.append(val.is_blank(visit3.disposition))
    if val.is_blank(visit3.disposition) == "":
        if visit3.disposition.value == "Discharge":
            errors.append(val.is_blank(visit3.observation))

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
    if val.is_blank(influenza_result.influenza_result) == "":
        if influenza_result.influenza_result == "Positive":
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

def antiviral_script_check(antiviral_script):
    errors = []
    errors.append(val.is_blank(antiviral_script.antiviral_script_name))
    
    return remove_blanks(errors)

def antibiotic_check(antibiotic):
    errors = []
    errors.append(val.is_blank(antibiotic.antibiotic_name))
    errors.append(val.is_blank(antibiotic.antibiotic_route))
    errors.append(val.is_blank(antibiotic.antibiotic_indication))
    errors.append(val.is_date(antibiotic.antibiotic_date))
    errors.append(val.is_time(antibiotic.antibiotic_time))
    
    return remove_blanks(errors)

def antibiotic_script_check(antibiotic_script):
    errors = []
    errors.append(val.is_blank(antibiotic_script.antibiotic_script_name))
    errors.append(val.is_blank(antibiotic_script.antibiotic_script_indication))
    
    return remove_blanks(errors)
