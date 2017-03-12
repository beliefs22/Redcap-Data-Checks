import validators_ed as val


def remove_blanks(mylist):
    for item in mylist[:]:
        if item == "":
            mylist.remove(item)
    return mylist


def field_names():
    """Returns dictionary of field names for named tuple"""
    complex_fields = dict()
    simple_fields = [['ps_edchrev%d_arrived','date'],['ps_edchrev%d_arrivet', 'time'],
                     ['ps_edchrev%d_departd', 'date'],['ps_edchrev%d_departt', 'time'],
                     ['ps_edchrev%d_phare','blank'],['ps_edchrev%d_cervl', 'blank'],
                     ['ps_edchrev%d_ams','blank'], ['ps_edchrev%d_dxflu', 'blank'],
                     ['ps_edchrev%d_dxviralsynd', 'blank'], ['ps_edchrev%d_dxpneumon','blank'],
                     ['ps_edchrev%d_dxmi', 'blank'],['ps_edchrev%d_dxstroke','blank'],
                     ['ps_edchrev%d_temp', 'temp'], ['ps_edchrev%d_pulse','pulse'],['ps_edchrev%d_rr','resp'],
                     ['ps_edchrev%d_sbp','systolic'],['ps_edchrev%d_o2s','oxygen'],['ps_edchrev%d_ph','ph'],
                     ['ps_edchrev%d_bun', 'bun'],['ps_edchrev%d_sodium', 'sodium'],
                     ['ps_edchrev%d_glucose','glucose'], ['ps_edchrev%d_hemocr','hematocrit']]

    complex_fields['o2_fields'] = {'start': 'ps_edchrev%d_o2sup', 'num': None, 'check' : ['ps_edchrev%d_o2sup_l',
                                                                                          'ps_edchrev%d_o2sup_r']}

    complex_fields['o2_discharge_fields'] = {'start': 'ps_edchrev%d_suppoxy', 'num' : None,
                                             'check' : ['ps_edchrev%d_suppoxyqnty', 'ps_edchrev%d_suppoxyroute']}


    complex_fields['influenza_test_fields'] = {'start': 'ps_edchrev%d_flutesting', 'num' : 'ps_edchrev%d_flutests',
                                               'check' : ['ps_edchrev%d_flut%d_name', 'ps_edchrev%d_flut%d_testtype',
                                                          #you will only check index 0 if index 1 evalutates to true
                                                          ['ps_edchrev%d_flut%d_testsp',
                                                           "ed_tuple.ps_edchrev%d_flut%d_testtype.value == 'Other'"],
                                                          'ps_edchrev%d_flut%d_res', 'ps_edchrev%d_flut%d_cold',
                                                          'ps_edchrev%d_flut%d_colt', 'ps_edchrev%d_flut%d_resd',
                                                          'ps_edchrev%d_flut%d_rest',
                                                          ['ps_edchrev%d_flut%d_typing',
                                                           "ed_tuple.ps_edchrev%d_flut%d_res.value == 'Positive'"],
                                                          ['ps_edchrev%d_flut%d_typsp',
                                                           "ed_tuple.ps_edchrev%d_flut%d_typsp.value == 'Other'"]]
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
    complex_fields['death_fields'] = {'start': 'ps_edchrev%d_death', 'num': None,
                                      'check': [['ps_edchrev%d_deathdate',
                                                 "ed_tuple.ps_edchrev%d_death.value == 'Yes'"]]
                                      }

    complex_fields['diagnosis_fields'] = {'start': 'ps_edchrev%d_findxnum', 'num': 'ps_edchrev%d_findxnum',
                                          'check': ['ps_edchrev%d_findx%d']
                                          }
    complex_fields['disposition_fields'] = {'start': 'ps_edchrev%d_dispo', 'num' : None,
                                            'check': [
                                                ['ps_edchrev%d_dispother',
                                                 "ed_tuple.ps_edchrev%d_dispo.value == 'Other'"],
                                                ['ps_edchrev1_dispoobs',
                                                 "ed_tuple.ps_edchrev%d_dispo == 'Discharge'"]
                                            ]
                                            }

    return complex_fields, simple_fields


def test_by_type(cell, test_type):
    test = {'date': val.is_date, 'time': val.is_time, 'pulse': val.valid_pulse,'temp': val.valid_temp,
            'resp': val.valid_resp, 'systolic': val.valid_systolic, 'sodium': val.valid_sodium,
            'glucose': val.valid_glucose, 'hematocrit': val.valid_hematocrit, 'oxygen': val.valid_oxygen,
            'bun': val.valid_bun, 'blank': val.is_blank, 'ph': val.valid_ph
            }

    return test[test_type](cell)


def simple_blank_check(ed_tuple, simple_fields):
    """Checks cells that don't require complex testing for blank values"""
    # 7number of visits to check for
    visit_number = ed_tuple.edptchart_visitnumber.value
    fields_to_check = []
    errors = []
    if visit_number:
        for i in range(1, visit_number + 1):
            for pair in simple_fields:
                field = pair[0] % i
                cell = eval('ed_tuple.%s' % field)
                test_type = pair[1]
                errors.append(test_by_type(cell, test_type))
        return remove_blanks(errors)


def complex_check(ed_tuple, complex_fields):
    ed_tuple = ed_tuple
    visit_num = ed_tuple.edptchart_visitnumber.value
    if visit_num is None:
        return []
    for i in range(1, visit_num + 1):
        # filed that starts the complex check
        start = complex_fields['start'] % visit_num
        # number of items to check for if None means its a single item field
        num = complex_fields['num']
        if num is not None:
            num = eval('ed_tuple.%s.value' % (num % visit_num))
        # fields to check if they are blank only start if isn't blank
        check = complex_fields['check']
        errors = []
        start_statement = 'val.is_blank(ed_tuple.%s)' % start
        start_check = eval(start_statement)
        errors.append(start_check)
        # if not blank do complex search
        if start_check == "":
            positive_result = eval('ed_tuple.%s.value' % start)
            if positive_result in [1,2,3,'more than three', "Yes"]:
                for field_name in check:
                    if num is not None:
                        if num == 'more than three':
                            num = 3
                        for i in range(1, num + 1):
                            if type(field_name) == list:
                                check_statement = field_name[1] % (visit_num, i)
                                if eval(check_statement):
                                    field = field_name[0] % (visit_num, i)
                                    statement = 'val.is_blank(ed_tuple.%s)' % field
                                    errors.append(eval(statement))
                            else:
                                field = field_name % (visit_num, i)
                                statement = 'val.is_blank(ed_tuple.%s)' % field
                                errors.append(eval(statement))
                    if num is None:
                        if type(field_name) == list:
                            check_statement = field_name[1] % visit_num
                            if eval(check_statement):
                                field = field_name[0] % visit_num
                                statement = 'val.is_blank(ed_tuple.%s)' % field
                                errors.append(eval(statement))
                        else:
                            field = field_name % visit_num
                            statement = 'val.is_blank(ed_tuple.%s)' % field
                            errors.append(eval(statement))
    return remove_blanks(errors)
