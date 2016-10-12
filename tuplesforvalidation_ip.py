import collections
#data that only has one possible entry
visit1_data_fields = ['start_date', 'end_date','oxygen_sup',
                      'oxygen_sup_rate','oxygen_sup_route','icu', 'icu_start',
                      'icu_days', 'death','death_date'
                      ]

visit2_data_fields = ['other_virus','rsv','parainfluenza','rhinovirus',
                            'metapneumovirus','adenovirus'
                      ]

visit3_data_fields = ['diagnosis_influenza','diagnosis_viral',
                      'diagnosis_pneumonia', 'diagnosis_mi', 'diagnosis_stroke',
                      'diagnosis_num','diagnosis1', 'diagnosis2','diagnosis3'
                      ]
#container to hold data from the excel file
Visit1 = collections.namedtuple('Visit1', field_names=visit1_data_fields)
Visit2 = collections.namedtuple('Visit2', field_names=visit2_data_fields)
Visit3 = collections.namedtuple('Visit3', field_names=visit3_data_fields)

#row numbers are based on six visits per patient with no "other disposition"
visit1_locations = {1:[9, 19], 2:[138,148],3:[267,277],
                          4:[396,406],5:[525,535],6:[654,664]}

visit2_locations  = {1:[113,119], 2:[242,248],3:[371,377],
                           4:[500,506],5:[629, 635],6:[758,764]
                           }

visit3_locations = {1:[129,138],2:[258,267],3:[387,396],
                          4:[516,525],5:[645,654],6:[774,783]
                          }

#represent one instance of influenza results
influenza_result_fields = ['influenza_name', 'influenza_test_type',
                                 'influenza_type_other', 'influenza_result',
                                 'influenza_test_date', 'influenza_test_time',
                                 'influenza_result_date',
                                 'influenza_result_time',
                                 'influenza_typing_done','influenza_type'
                                 ]
influenza_result_locations = {1:[43,113],2:[172,242],3:[301,371],4:[430,500],
                              5:[559,629],6:[688,758]}
influenza_location_modifier = 10
Influenza_Result = collections.namedtuple('Influenza_Results',
                                                 field_names=influenza_result_fields)

#represents one instance of antivirals given
antiviral_fields = ['antiviral_name', 'antiviral_route',
                                  'antiviral_date', 'antiviral_time'
                                  ]
antiviral_locations = {1:[121,129],2:[250, 258],3:[379,387],4:[508,516],
                       5:[637,645],6:[766,774]}
antiviral_modifier = 4

Antiviral = collections.namedtuple('Antiviral', field_names=antiviral_fields)

#represent once instance of antibiotics
antibiotic_fields = ['antibiotic_name', 'antibiotic_date','antibiotic_days',
                     'antibiotic_indication'
                     ]
antibiotic_locations = {1:[22,41],2:[151,170],3:[280,299],4:[409,428],
                        5:[538,557],6:[667,686]}

antibiotic_modifier = 5

Antibiotic = collections.namedtuple('Antibiotic', field_names=antibiotic_fields)

def locations():
    
    field_names = ['visit1_locations','visit2_locations','visit3_locations',
                   'influenza_result_locations','antiviral_locations',
                   'antibiotic_locations',]
    
    all_locations = [visit1_locations,visit2_locations,visit3_locations,
                     influenza_result_locations,antiviral_locations,
                     antibiotic_locations]
    
    Locations = collections.namedtuple('Location',field_names=field_names)
    
    return Locations(*all_locations)

def mytuples():
    field_names = ['visit1', 'visit2', 'visit3','influenza_result','antiviral',
                   'antibiotic']
    all_tuples = [Visit1, Visit2, Visit3, Influenza_Result, Antiviral,
                  Antibiotic]

    Main_Tuples = collections.namedtuple('Main_Tuples', field_names=field_names)
    return Main_Tuples(*all_tuples)
