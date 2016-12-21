import validators_ip as val


def remove_blanks(mylist):
    for item in mylist[:]:
        if item == "":
            mylist.remove(item)
    return mylist


def field_names():
    """Returns dictionary of field names for named tuple"""
    complex_fields = dict()
    simple_fields = ['ps_ipchrev%d_inptstart','ps_ipchrev%d_inptend', 'ps_ipchrev%d_dxflu',
                     'ps_ipchrev%d_dxviralsynd', 'ps_ipchrev%d_dxpneumon', 'ps_ipchrev%d_dxmi','ps_ipchrev%d_dxstroke'
                     ]
    # complex_fields['intermediate_fields'] = ['ps_ipchrev%d_temp','ps_ipchrev%d_pulse', 'ps_ipchrev%d_rr', 'ps_ipchrev%d_sbp',
    #                        'ps_ipchrev%d_o2s', 'ps_ipchrev%d_ph', 'ps_ipchrev%d_bun',
    #                        'ps_ipchrev%d_sodium', 'ps_ipchrev%d_glucose', 'ps_ipchrev%d_hemocr'
    #                        ]

    complex_fields['o2_fields'] = {'start': 'ps_ipchrev%d_o2sup', 'num': None, 'check' : ['ps_ipchrev%d_o2sup_l',
                                                                                          'ps_ipchrev%d_o2sup_r']}

    complex_fields['influenza_test_fields'] = {'start': 'ps_ipchrev%d_flutesting', 'num' : 'ps_ipchrev%d_flutests',
                                               'check' : ['ps_ipchrev%d_flut%d_name', 'ps_ipchrev%d_flut%d_testtype',
                                                          ['ps_ipchrev%d_flut%d_testsp',
                                                           "ed_tuple.ps_ipchrev%d_flut%d_testtype.value == 'Other'"],
                                                          'ps_ipchrev%d_flut%d_res', 'ps_ipchrev%d_flut%d_cold',
                                                          'ps_ipchrev%d_flut%d_colt', 'ps_ipchrev%d_flut%d_resd',
                                                          'ps_ipchrev%d_flut%d_rest',
                                                          ['ps_ipchrev%d_flut%d_typing',
                                                           "ed_tuple.ps_ipchrev%d_flut%d_res.value == 'Positive'"],
                                                          ['ps_ipchrev%d_flut%d_typsp',
                                                           "ed_tuple.ps_ipchrev%d_flut%d_typsp.value == 'Other'"]]
                                               }

    complex_fields['other_virus_test'] = {'start': 'ps_ipchrev%d_othervir', 'num': None,
                                          'check': ['ps_ipchrev%d_othervir_rsv','ps_ipchrev%d_othervir_para',
                                                    'ps_ipchrev%d_othervir_rhino', 'ps_ipchrev%d_othervir_meta',
                                                    'ps_ipchrev%d_othervir_adeno']
                                          }

    complex_fields['influenza_antiviral_fields'] = {'start': 'ps_ipchrev%d_fluav', 'num': 'ps_ipchrev%d_fluavnum',
                                                    'check': ['ps_ipchrev%d_fluav%d_name', 'ps_ipchrev%d_fluav%droute',
                                                              'ps_ipchrev%d_fluav%ddate', 'ps_ipchrev%d_fluav%dtime']
                                                    }


    complex_fields['antibiotic_fields'] = {'start': 'ps_ipchrev%d_ab_ed', 'num': 'ps_ipchrev%d_ab_ed_num',
                                           'check' : ['ps_ipchrev%d_ab_ed%d_name', 'ps_ipchrev%d_ab_ed%d_days',
                                                      'ps_ipchrev%d_ab_ed%d_indic', 'ps_ipchrev%d_ab_ed%d_date']
                                           }


    complex_fields['death_fields'] = {'start': 'ps_ipchrev%d_die', 'num': None,
                                      'check': [['ps_ipchrev%d_diedate',
                                                 "ed_tuple.ps_ipchrev%d_die.value == 'Yes'"]]
                                      }

    complex_fields['diagnosis_fields'] = {'start': 'ps_ipchrev%d_findxnum', 'num': 'ps_ipchrev%d_findxnum',
                                          'check': ['ps_ipchrev%d_findx%d']
                                          }

    return complex_fields, simple_fields


def simple_blank_check(ed_tuple, simple_fields):
    """Checks cells that don't require complex testing for blank values"""
    #number of visits to check for
    visit_number = ed_tuple.inptchart_visitnumber.value
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
    visit_num = ed_tuple.inptchart_visitnumber.value
    if visit_num is None or visit_num == 0:
        return []
    for i in range(1, visit_num + 1):
        # filed that starts the complex check
        start = complex_fields['start'] % visit_num
        # number of items to check for if None means its a single item field
        num = complex_fields['num']
        if num is not None:
            num = eval('ed_tuple.%s.value' % (num % visit_num))
        # fields to check if they are blank only if start isn't blank
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
