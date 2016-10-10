import collections
#data that only has one possible entry
visit1_data_fields = ['arrival_date', 'arrival_time', 'departure_date',
                            'departure_time', 'temp', 'pulse', 'resp',
                            'systolic', 'oxygen_sat', 'oxygen_sup',
                            'oxygen_sup_rate', 'oxygen_sup_route',
                            'pharyngeal', 'cervical', 'ams','ph','bun','sodium',
                            'glucose', 'hematocrit'
                             ]
visit2_data_fields = ['other_virus','rsv','parainfluenza','rhinovirus',
                            'metapneumovirus','adenovirus'
                            ]

visit3_data_fields = ['chest_xray', 'infiltrate','consolidation',
                            'effusions','pneumonia', 'intubated', 'bipap',
                            'supplemental_oxy','supplemental_oxy_rate',
                            'supplemental_oxy_route','death',
                            'death_date', 'diagnosis_influenza',
                            'diagnosis_viral', 'diagnosis_pneumonia',
                            'diagnosis_mi', 'diagnosis_stroke', 'diagnosis_num',
                            'diagnosis1', 'diagnosis2', 'diagnosis3',
                            'disposition', 'observation'
                            ]
#container to hold data from the excel file
Visit1 = collections.namedtuple('Visit1', field_names=visit1_data_fields)
Visit2 = collections.namedtuple('Visit2', field_names=visit2_data_fields)
Visit3 = collections.namedtuple('Visit3', field_names=visit3_data_fields)

#row numbers are based on six visits per patient with no "other disposition"
visit1_locations = {1:[9, 29], 2:[179,199],3:[349,369],
                          4:[519,539],5:[689,709],6:[859,879]}

visit2_locations  = {1:[101,107], 2:[271,277],3:[441,447],
                           4:[611,617],5:[781, 787],6:[952,957]
                           }

visit3_locations = {1:[156,179],2:[326,349],3:[496,519],
                          4:[666,689],5:[836,859],6:[1006,1029]
                          }

#represent one instance of influenza results
influenza_result_fields = ['influenza_name', 'influenza_test_type',
                                 'influenza_type_other', 'influenza_result',
                                 'influenza_test_date', 'influenza_test_time',
                                 'influenza_result_date',
                                 'influenza_result_time',
                                 'influenza_typing_done','influenza_type'
                                 ]
influenza_result_locations = {1:[31,101],2:[201,271],3:[371,441],4:[541,611],
                              5:[711,781],6:[881,951]}
influenza_location_modifier = 10
Influenza_Result = collections.namedtuple('Influenza_Results',
                                                 field_names=influenza_result_fields)

#represents one instance of antivirals given
antiviral_fields = ['antiviral_name', 'antiviral_route',
                                  'antiviral_date', 'antiviral_time'
                                  ]
antiviral_locations = {1:[109,117],2:[279, 287],3:[449,457],4:[619,627],
                       5:[789,797],6:[959,967]}
antiviral_modifier = 4

Antiviral = collections.namedtuple('Antiviral', field_names=antiviral_fields)

#represents once instance of antiviral scrips given
antiviral_script_fields = ['antiviral_script_name']

antiviral_script_locations = {1:[119,121],2:[289,291],3:[459,461],4:[629,631],
                              5:[799,801],6:[969,971]}

antiviral_script_modifier = 2

Antiviral_Script = collections.namedtuple('Antiviral_Script',
                                                 field_names=antiviral_script_fields)

#represent once instance of antibiotics
antibiotic_fields = ['antibiotic_name', 'antibiotic_route',
                            'antibiotic_indication','antibiotic_date',
                            'antibiotic_time'
                            ]

antibiotic_locations = {1:[123,148],2:[293,318],3:[463,488],4:[633,658],
                        5:[803,828],6:[973,998]}

antibiotic_modifier = 5

Antibiotic = collections.namedtuple('Antibiotic', field_names=antibiotic_fields)

#represents one instance of antiboitic script given
antibiotic_script_fields = ['antibiotic_script_name',
                                   'antibiotic_script_indication'
                                   ]

antibiotic_script_locations = {1:[150,156],2:[320,326],3:[490,496],4:[660,666],
                               5:[830,836],6:[1000,1006]}

antibiotic_script_modifier = 5
Antibiotic_Script = collections.namedtuple('Antibiotic_Script',
                                           field_names=antibiotic_script_fields)

def locations():
    field_names = ['visit1_locations','visit2_locations','visit3_locations',
                   'influenza_result_locations','antiviral_locations',
                   'antiviral_script_locations', 'antibiotic_locations',
                   'antibiotic_script_locations']
    all_locations = [visit1_locations,visit2_locations,visit3_locations,
                     influenza_result_locations,antiviral_locations,
                     antiviral_script_locations,antibiotic_locations,
                     antibiotic_script_locations]
    Locations = collections.namedtuple('Location',field_names=field_names)
    return Locations(*all_locations)

def mytuples():
    field_names = ['visit1', 'visit2', 'visit3','influenza_result','antiviral',
                   'antiviral_script','antibiotic','antibiotic_script']
    all_tuples = [Visit1, Visit2, Visit3, Influenza_Result, Antiviral,
                  Antiviral_Script, Antibiotic, Antibiotic_Script]

    Main_Tuples = collections.namedtuple('Main_Tuples', field_names=field_names)
    return Main_Tuples(*all_tuples)
