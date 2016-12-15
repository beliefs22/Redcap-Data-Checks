import validators_ed as val

def remove_blanks(mylist):
    for item in mylist[:]:
        if item == "":
            mylist.remove(item)
    return mylist

def ed_check(ed_tuple):
    number_of_visits = ed_tuple.edptchart_visitnumber.value
    errors = []
    if number_of_visits is None:
        number_of_visits = 0
    for i in range(1, number_of_visits + 1):
        errors.append(val.is_date(ed_tuple.ps_edchrev1_arrived))
        errors.append(val.is_time(ed_tuple.ps_edchrev1_arrivet))
        errors.append(val.is_date(ed_tuple.ps_edchrev1_departd))
        errors.append(val.is_time(ed_tuple.ps_edchrev1_departt))
        errors.append(val.valid_temp(ed_tuple.ps_edchrev1_temp))
        errors.append(val.valid_pulse(ed_tuple.ps_edchrev1_pulse))
        errors.append(val.valid_resp(ed_tuple.ps_edchrev1_rr))
        errors.append(val.valid_systolic(ed_tuple.ps_edchrev1_sbp))
        errors.append(val.valid_oxygen(ed_tuple.ps_edchrev1_o2s))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_o2sup))
        if val.is_blank(ed_tuple.ps_edchrev1_o2sup) == "":
            if ed_tuple.ps_edchrev1_o2sup.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_o2sup_l))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_o2sup_r))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_phare))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_cervl))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_ams))
        errors.append(val.valid_ph(ed_tuple.ps_edchrev1_ph))
        errors.append(val.valid_bun(ed_tuple.ps_edchrev1_bun))
        errors.append(val.valid_sodium(ed_tuple.ps_edchrev1_sodium))
        errors.append(val.valid_glucose(ed_tuple.ps_edchrev1_glucose))
        errors.append(val.valid_hematocrit(ed_tuple.ps_edchrev1_hemocr))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_othervir))
        if val.is_blank(ed_tuple.ps_edchrev1_othervir_rsv) == "":
            if ed_tuple.ps_edchrev1_othervir_rsv.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_othervir_rsv))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_othervir_para))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_othervir_rhino))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_othervir_meta))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_othervir_adeno))

        errors.append(val.is_blank(ed_tuple.ps_edchrev1_chest))
        if val.is_blank(ed_tuple.ps_edchrev1_chest) == "":
            if ed_tuple.ps_edchrev1_chest.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_chest_pulm))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_chest_consol))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_chest_pleur))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_chest_suspneum))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_intub))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_bipap))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_suppoxy))
        if val.is_blank(ed_tuple.ps_edchrev1_suppoxy) == "":
            if ed_tuple.ps_edchrev1_suppoxy.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_suppoxyqnty))
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_suppoxyroute))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_death))
        if val.is_blank(ed_tuple.ps_edchrev1_death) == "":
            if ed_tuple.ps_edchrev1_death.value == "Yes":
                errors.append(val.is_date(ed_tuple.ps_edchrev1_deathdate))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dxflu))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dxviralsynd))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dxpneumon))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dxmi))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dxstroke))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_findxnum))
        if val.is_blank(ed_tuple.ps_edchrev1_findxnum) == "":
            if ed_tuple.ps_edchrev1_findxnum.value in [1, "more than three"]:
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_findx1))
                if ed_tuple.ps_edchrev1_findxnum.value in [2, "more than three"]:
                    errors.append(val.is_blank(ed_tuple.ps_edchrev1_findx2))
                    if ed_tuple.ps_edchrev1_findxnum.value in [3, "more than three"]:
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_findx3))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dispo))
        if val.is_blank(ed_tuple.ps_edchrev1_dispo) == "":
            if ed_tuple.ps_edchrev1_dispo.value == "Discharge":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_dispoobs))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_flutesting))
        if val.is_blank(ed_tuple.ps_edchrev1_flutesting) == "":
            if ed_tuple.ps_edchrev1_flutesting.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_flutests))
                if val.is_blank(ed_tuple.ps_edchrev1_flutests) == "":
                    flu_test_num = ed_tuple.ps_edchrev1_flutests.value
                    for i in range(1, flu_test_num + 1):
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_flut1_name))
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_flut1_testtype))
                        if val.is_blank(ed_tuple.ps_edchrev1_flut1_testtype) == "":
                            if ed_tuple.ps_edchrev1_flut1_testtype.value == "Other":
                                errors.append(val.is_blank(ed_tuple.ps_edchrev1_flut1_testsp))
                        errors.append(val.valid_result(ed_tuple.ps_edchrev1_flut1_res))
                        errors.append(val.is_date(ed_tuple.ps_edchrev1_flut1_cold))
                        errors.append(val.is_time(ed_tuple.ps_edchrev1_flut1_colt))
                        errors.append(val.is_date(ed_tuple.ps_edchrev1_flut1_resd))
                        errors.append(val.is_time(ed_tuple.ps_edchrev1_flut1_rest))
                        if val.is_blank(ed_tuple.ps_edchrev1_flut1_res) == "":
                            if ed_tuple.ps_edchrev1_flut1_res.value == "Positive":
                                errors.append(val.is_blank(ed_tuple.ps_edchrev1_flut1_typing))
                                if val.is_blank(ed_tuple.ps_edchrev1_flut1_typing) == "":
                                    if ed_tuple.ps_edchrev1_flut1_typing.value == "Yes":
                                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_flut1_typsp))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_fluav))
        if val.is_blank(ed_tuple.ps_edchrev1_fluav) == "":
            if ed_tuple.ps_edchrev1_fluav.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_fluavnum))
                if val.is_blank(ed_tuple.ps_edchrev1_fluavnum) == "":
                    antiviral_num = ed_tuple.ps_edchrev1_fluavnum.value
                    for i in range(1, antiviral_num + 1):
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_fluav1_name))
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_fluav1route))
                        errors.append(val.is_date(ed_tuple.ps_edchrev1_fluav1date))
                        errors.append(val.is_time(ed_tuple.ps_edchrev1_fluav1time))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_fluavdisc))
        if val.is_blank(ed_tuple.ps_edchrev1_fluavdisc) == "":
            errors.append((val.is_blank(ed_tuple.ps_edchrev1_fluavdiscct)))
            if val.is_blank(ed_tuple.ps_edchrev1_fluavdiscct) == "":
                antiviral_script_num = ed_tuple.ps_edchrev1_fluavdiscct.value
                for i in range(1, antiviral_script_num + 1):
                    errors.append(val.is_blank(ed_tuple.ps_edchrev1_fluavdisc1))
        print ed_tuple.ps_edchrev1_ab_ed.value, val.is_blank(ed_tuple.ps_edchrev1_ab_ed) == ""
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_ab_ed))
        if val.is_blank(ed_tuple.ps_edchrev1_ab_ed) == "":
            if ed_tuple.ps_edchrev1_ab_ed.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_ab_ed_num))
                if val.is_blank(ed_tuple.ps_edchrev1_ab_ed_num) == "":
                    antibiotic_num = ed_tuple.ps_edchrev1_ab_ed_num.value
                    for i in range(1, antibiotic_num + 1):
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_ab_ed1_name))
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_ab_ed1route))
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_ab_ed1_indic))
                        errors.append(val.is_date(ed_tuple.ps_edchrev1_ab_ed1date))
                        errors.append(val.is_time(ed_tuple.ps_edchrev1_ab_ed1time))
        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dabx))
        if val.is_blank(ed_tuple.ps_edchrev1_dabx) == "":
            if ed_tuple.ps_edchrev1_dabx.value == "Yes":
                errors.append(val.is_blank(ed_tuple.ps_edchrev1_abxquant))
                if val.is_blank(ed_tuple.ps_edchrev1_abxquant) == "":
                    antibiotic_script_num = ed_tuple.ps_edchrev1_abxquant.value
                    for i in range(1, antibiotic_script_num + 1):
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dabx1name))
                        errors.append(val.is_blank(ed_tuple.ps_edchrev1_dabx1indication))
    return remove_blanks(errors)
