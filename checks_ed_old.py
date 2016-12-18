import validators_ed as val


def remove_blanks(mylist):
    for item in mylist[:]:
        if item == "":
            mylist.remove(item)
    return mylist


def field_names():
    """Returns dictionary of field names for named tuple"""
    complex_fields = dict()
    simple_fields = ['ps_edchrev%d_arrived','ps_edchrev%d_arrivet','ps_edchrev%d_departd','ps_edchrev%d_departt',
                     'ps_edchrev%d_phare', 'ps_edchrev%d_cervl', 'ps_edchrev%d_ams', 'ps_edchrev%d_dxflu', 
                     'ps_edchrev%d_dxviralsynd', 'ps_edchrev%d_dxpneumon', 'ps_edchrev%d_dxmi','ps_edchrev%d_dxstroke'
                     ]
    # complex_fields['intermediate_fields'] = ['ps_edchrev%d_temp','ps_edchrev%d_pulse', 'ps_edchrev%d_rr', 'ps_edchrev%d_sbp',
    #                        'ps_edchrev%d_o2s', 'ps_edchrev%d_ph', 'ps_edchrev%d_bun',
    #                        'ps_edchrev%d_sodium', 'ps_edchrev%d_glucose', 'ps_edchrev%d_hemocr'
    #                        ]

    complex_fields['o2_fields'] = {'start': 'ps_edchrev%d_o2sup', 'num': None, 'check' : ['ps_edchrev%d_o2sup_l',
                                                                                          'ps_edchrev%d_o2sup_r']}

    complex_fields['o2_discharge_fields'] = {'start': 'ps_edchrev%d_suppoxy', 'num' : None,
                                             'check' : ['ps_edchrev%d_suppoxyqnty', 'ps_edchrev%d_suppoxyroute']}


    complex_fields['influenza_test_fields'] = {'start': 'ps_edchrev%d_flutesting', 'num' : 'ps_edchrev%d_flutests',
                                               'check' : ['ps_edchrev%d_flut%d_name', 'ps_edchrev%d_flut%d_testtype',
                                                          'ps_edchrev%d_flut%d_testsp', 'ps_edchrev%d_flut%d_res',
                                                          'ps_edchrev%d_flut%d_cold', 'ps_edchrev%d_flut%d_colt',
                                                          'ps_edchrev%d_flut%d_resd', 'ps_edchrev%d_flut%d_rest',
                                                          'ps_edchrev%d_flut%d_typing','ps_edchrev%d_flut%d_typsp']
                                               }

    complex_fields['other_virus_test'] = {'start': 'ps_edchrev%d_othervir', 'num': None,
                                          'check': ['ps_edchrev%d_othervir_rsv','ps_edchrev%d_othervir_para',
                                                    'ps_edchrev%d_othervir_rhino', 'ps_edchrev%d_othervir_meta',
                                                    'ps_edchrev%d_othervir_adeno']
                                          }

    complex_fields['influenza_antiviral_fields'] = {'start': 'ps_edchrev%d_fluav', 'num': 'ps_edchrev%d_fluavnum',
                                                    'check': ['ps_edchrev%d_fluav%d_name', 'ps_edchrev%d_fluav%droute',
                                                              'ps_edchrev%d_fluav%ddate', 'ps_edchrev%d_fluav%dtime']
                                                    }

    complex_fields['antiviral_script_fields'] = {'start':'ps_edchrev%d_fluavdisc', 'num': 'ps_edchrev%d_fluavdiscct',
                                                 'check' : ['ps_edchrev%d_fluavdisc%d']
                                                 }

    complex_fields['antibiotic_fields'] = {'start': 'ps_edchrev%d_ab_ed', 'num': 'ps_edchrev%d_ab_ed_num',
                                           'check' : ['ps_edchrev%d_ab_ed%d_name', 'ps_edchrev%d_ab_ed%droute',
                                                      'ps_edchrev%d_ab_ed%d_indic', 'ps_edchrev%d_ab_ed%ddate',
                                                      'ps_edchrev%d_ab_ed%dtime']
                                           }

    complex_fields['antibiotic_script_fields'] = {'start': 'ps_edchrev%d_dabx', 'num': 'ps_edchrev%d_abxquant',
                                                  'check': ['ps_edchrev%d_dabx%dname', 'ps_edchrev%d_dabx%dindication']
                                                  }
    complex_fields['imaging_fields'] = {'start': 'ps_edchrev%d_chest', 'num': None,
                                        'check' : ['ps_edchrev%d_chest_pulm','ps_edchrev%d_chest_consol',
                                                   'ps_edchrev%d_chest_pleur', 'ps_edchrev%d_chest_suspneum']
                                        }
    complex_fields['death_fields'] = {'start': 'ps_edchrev%d_death', 'num': None, 'check': ['ps_edchrev%d_deathdate']}

    complex_fields['diagnosis_fields'] = {'start': 'ps_edchrev%d_findxnum', 'num': 'ps_edchrev%d_findxnum',
                                          'check': ['ps_edchrev%d_findx%d']
                                          }

    return complex_fields, simple_fields


def simple_blank_check(ed_tuple, simple_fields):
    """Checks cells that don't require complex testing for blank values"""
    #number of visits to check for
    visit_number = ed_tuple.edptchart_visitnumber.value
    fields_to_check = []
    errors = []
    if visit_number:
        for i in range(1, visit_number + 1):
            for field in simple_fields:
                fields_to_check.append(field % i)
        for field in fields_to_check:
            statement = 'val.is_blank(ed_tuple.%s)' % field
            errors.append(eval(statement))
        return remove_blanks(errors)


def complex_check(ed_tuple, complex_fields):
    ed_tuple = ed_tuple
    visit_num = ed_tuple.edptchart_visitnumber.value
    if visit_num is None:
        return []
    for i in range(1, visit_num + 1):
        start = complex_fields['start'] % visit_num
        num = complex_fields['num']
        if num is not None:
            num = eval('ed_tuple.%s.value' % (num % visit_num))
        check = complex_fields['check']
        errors = []
        start_statement = 'val.is_blank(ed_tuple.%s)' % start
        start_check = eval(start_statement)
        errors.append(start_check)
        #if not blank
        if start_check == "":
            positive_result = eval('ed_tuple.%s.value' % start)
            if positive_result in [1,2,3,'more than three', "Yes"]:
                for field_name in check:
                    if num is not None:
                        if num == 'more than three':
                            num = 3
                        for i in range(1, num + 1):
                            field = field_name % (visit_num, i)
                            statement = 'val.is_blank(ed_tuple.%s)' % field
                            errors.append(eval(statement))
                    if num is None:
                        print field_name, ed_tuple.id.value
                        field = field_name % visit_num
                        statement = 'val.is_blank(ed_tuple.%s)' % field
                        errors.append(eval(statement))
    return remove_blanks(errors)




# def visit1_check(ed_tuple, visit_num):
#     errors = []
#     errors.append(val.is_date(ed_tuple.arrival_date))
#     errors.append(val.is_time(ed_tuple.arrival_time))
#     errors.append(val.is_date(ed_tuple.departure_date))
#     errors.append(val.is_time(ed_tuple.departure_time))
#     errors.append(val.valid_temp(ed_tuple.temp))
#     errors.append(val.valid_pulse(ed_tuple.pulse))
#     errors.append(val.valid_resp(ed_tuple.resp))
#     errors.append(val.valid_systolic(ed_tuple.systolic))
#     errors.append(val.valid_oxygen(ed_tuple.oxygen_sat))
#     errors.append(val.is_blank(ed_tuple.oxygen_sup))
#     if val.is_blank(ed_tuple.oxygen_sup) == "":
#         if ed_tuple.oxygen_sup.value == "Yes":
#             errors.append(val.is_blank(ed_tuple.oxygen_sup_rate))
#             errors.append(val.is_blank(ed_tuple.oxygen_sup_route))
#     errors.append(val.is_blank(ed_tuple.pharyngeal))
#     errors.append(val.is_blank(ed_tuple.cervical))
#     errors.append(val.is_blank(ed_tuple.ams))
#     errors.append(val.valid_ph(ed_tuple.ph))
#     errors.append(val.valid_bun(ed_tuple.bun))
#     errors.append(val.valid_sodium(ed_tuple.sodium))
#     errors.append(val.valid_glucose(ed_tuple.glucose))
#     errors.append(val.valid_hematocrit(ed_tuple.hematocrit))
#
#     return remove_blanks(errors)
#
# def visit2_check(visit2):
#     errors = []
#     errors.append(val.is_blank(visit2.other_virus))
#     if val.is_blank(visit2.other_virus) == "":
#         if visit2.other_virus.value == "Yes":
#             errors.append(val.is_blank(visit2.rsv))
#             errors.append(val.is_blank(visit2.parainfluenza))
#             errors.append(val.is_blank(visit2.rhinovirus))
#             errors.append(val.is_blank(visit2.metapneumovirus))
#             errors.append(val.is_blank(visit2.adenovirus))
#
#     return remove_blanks(errors)
#
# def visit3_check(visit3):
#     errors = []
#     errors.append(val.is_blank(visit3.chest_xray))
#     if val.is_blank(visit3.chest_xray) == "":
#         if visit3.chest_xray.value == "Yes":
#             errors.append(val.is_blank(visit3.infiltrate))
#             errors.append(val.is_blank(visit3.consolidation))
#             errors.append(val.is_blank(visit3.effusions))
#             errors.append(val.is_blank(visit3.pneumonia))
#     errors.append(val.is_blank(visit3.intubated))
#     errors.append(val.is_blank(visit3.bipap))
#     errors.append(val.is_blank(visit3.supplemental_oxy))
#     if val.is_blank(visit3.supplemental_oxy) == "":
#         if visit3.supplemental_oxy.value == "Yes":
#             errors.append(val.is_blank(visit3.supplemental_oxy_rate))
#             errors.append(val.is_blank(visit3.supplemental_oxy_route))
#     errors.append(val.is_blank(visit3.death))
#     if val.is_blank(visit3.death) == "":
#         if visit3.death.value == "Yes":
#             errors.append(val.is_date(visit3.death_date))
#     errors.append(val.is_blank(visit3.diagnosis_influenza))
#     errors.append(val.is_blank(visit3.diagnosis_viral))
#     errors.append(val.is_blank(visit3.diagnosis_pneumonia))
#     errors.append(val.is_blank(visit3.diagnosis_mi))
#     errors.append(val.is_blank(visit3.diagnosis_stroke))
#     errors.append(val.is_blank(visit3.diagnosis_num))
#     if val.is_blank(visit3.diagnosis_num) == "":
#         if visit3.diagnosis_num.value in [1,"more than three"]:
#             errors.append(val.is_blank(visit3.diagnosis1))
#             if visit3.diagnosis_num.value in [2, "more than three"]:
#                 errors.append(val.is_blank(visit3.diagnosis2))
#                 if visit3.diagnosis_num.value in [3, "more than three"]:
#                     errors.append(val.is_blank(visit3.diagnosis3))
#     errors.append(val.is_blank(visit3.disposition))
#     if val.is_blank(visit3.disposition) == "":
#         if visit3.disposition.value == "Discharge":
#             errors.append(val.is_blank(visit3.observation))
#
#     return remove_blanks(errors)
#
# def influenza_result_check(influenza_result):
#     errors = []
#     errors.append(val.is_blank(influenza_result.influenza_name))
#     errors.append(val.is_blank(influenza_result.influenza_test_type))
#     if val.is_blank(influenza_result.influenza_test_type) == "":
#         if influenza_result.influenza_test_type.value == "Other":
#             errors.append(val.is_blank(influenza_result.influenza_type_other))
#     errors.append(val.valid_result(influenza_result.influenza_result))
#     errors.append(val.is_date(influenza_result.influenza_test_date))
#     errors.append(val.is_time(influenza_result.influenza_test_time))
#     errors.append(val.is_date(influenza_result.influenza_result_date))
#     errors.append(val.is_time(influenza_result.influenza_result_time))
#     if val.is_blank(influenza_result.influenza_result) == "":
#         if influenza_result.influenza_result == "Positive":
#             errors.append(val.is_blank(influenza_result.influenza_typing_done))
#             if val.is_blank(influenza_result.influenza_typing_done) == "":
#                 if influenza_result.influenza_typing_done.value == "Yes":
#                     errors.append(val.is_blank(influenza_result.influenza_type))
#     return remove_blanks(errors)
#
# def antiviral_check(antiviral):
#     errors = []
#     errors.append(val.is_blank(antiviral.antiviral_name))
#     errors.append(val.is_blank(antiviral.antiviral_route))
#     errors.append(val.is_date(antiviral.antiviral_date))
#     errors.append(val.is_time(antiviral.antiviral_time))
#     return remove_blanks(errors)
#
# def antiviral_script_check(antiviral_script):
#     errors = []
#     errors.append(val.is_blank(antiviral_script.antiviral_script_name))
#
#     return remove_blanks(errors)
#
# def antibiotic_check(antibiotic):
#     errors = []
#     errors.append(val.is_blank(antibiotic.antibiotic_name))
#     errors.append(val.is_blank(antibiotic.antibiotic_route))
#     errors.append(val.is_blank(antibiotic.antibiotic_indication))
#     errors.append(val.is_date(antibiotic.antibiotic_date))
#     errors.append(val.is_time(antibiotic.antibiotic_time))
#
#     return remove_blanks(errors)
#
# def antibiotic_script_check(antibiotic_script):
#     errors = []
#     errors.append(val.is_blank(antibiotic_script.antibiotic_script_name))
#     errors.append(val.is_blank(antibiotic_script.antibiotic_script_indication))
#
#     return remove_blanks(errors)
