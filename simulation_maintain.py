from functions_simulation_diff_weight import *
import pandas as pd

original_weight_condoms = [
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    1.5  # Gender dysphoria related to pregnancy (no/yes)
]
original_weight_internal_condoms = [
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)   
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    [-3, -2, -1, 1, 2, 3], # Vaginal Insertion
    [-15, -25, -50],  # Gender dysphoria related to vaginal insertion
    1.5 # Gender dysphoria related to pregnancy
]
original_weight_cervical_cap = [
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,                    # Maintenance (arr[2])
    [-3, -2, -1, 1, 2, 3],  # Vaginal Insertion (arr[3])
    [-3, -2, -1, 1, 2, 3],  # Seeking Consultation (arr[4])
    [-15, -25, -50],     # Gender Dysphoria Vaginal Insertion (arr[5])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[6])
]
original_weight_FAM = [
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,                    # Maintenance (arr[2])
    [-3, -2, -1, 1, 2, 3],  # Partner Willingness (arr[3])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[4])
]
original_weight_arm_implant = [
    [-3, -2, -1, 1, 2, 3],  # Pregnancy Prevention (arr[1])
    [-3, -2, -1, 1, 2, 3],  # Lessens Periods (arr[2])
    [3, 2, 1, -1, -2, -3],  # Maintains Weight (arr[3])
    3,                    # Maintenance (arr[4])
    [3, 3],                    # Hormones Used (arr[5])
    [3, 2, 1, -1, -2, -3],  # Seeking consultation (arr[6])
    [3, 2, 1, -1, -2, -3],  # Medical procedure (arr[7])
    3,                    # Acne (arr[8])
    [-7.5, -12.5, -25, -15, -25, -50],  # Anxiety (arr[9])
    [-7.5, -12.5, -25, -15, -25, -50],  # Depression (arr[10])
    3,                    # Gender dysphoria period (arr[11])
    3,                    # Gender dysphoria pregnancy (arr[12])
]
original_weight_spermicide = [
    # Pregnancy Prevention (0-5)
    [-3, -2, -1, 1, 2, 3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Maintainance (Yearly) [single value for yearly]
    3,
    
    # Vaginal Insertion (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Seeking Consultation (0-5)
    [-3, -2, -1, 1, 2, 3],

]
original_weight_withdrawl = [
    # Pregnancy Prevention (0-5)
    [-3, -2, -1, 1, 2, 3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Maintainance (Yearly) [single value for yearly]
    3,
    
    # Vaginal Insertion (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Gender Pregnancy (mild, moderate, severe)
    [-15, -25, -50]
    
]
original_weight_sterilization = [
    # Pregnancy Prevention (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Lessens Periods (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Seeking Consultation (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Medical Procedure (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # PCOS (0 for 'no', some weight for conditions)
    3,
    
    # ENDMT (0 for 'no', some weight for conditions)
    3,
    
    # Gender Dysphoria Period (0 for 'no', weights for conditions)
    3,
    
    # Gender Dysphoria Pregnancy (0 for 'no', weight for conditions)
    3
]
original_weight_ring = [
    # Cost Effectiveness (index 0)
    [-3, -2, -1, 1, 2, 3],  # Matches the original cost-effectiveness scores
    # Pregnancy Prevention (index 1)
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Matches original pregnancy prevention scores
    # Management of Periods (index 2)
    [-3, -2, -1, 1, 2, 3],  # Matches original management of periods scores
    # Weight Management (index 3)
    [3, 2, 1, -1, -2, -3],  # Matches original weight management scores
    # Monthly Maintenance (index 4)
    3,  # Additional score for monthly
    # Hormones (index 5)
    3,  # Hormones (ep score of +3)
    # Willingness Vagina (index 6)
    [-3, -2, -1, 1, 2, 3],  # Matches original vaginal willingness scores
    # Medical Practitioner (index 7)
    [-3, -2, -1, 1, 2, 3],  # Matches original medical practitioner scores
    # Acne (index 8)
    3,  # Acne severity gives +3
    # Anxiety (index 9)
    [-7.5, -12.5, -25, -15, -25, -50],  # Matches original anxiety scores
    # Depression (index 10)
    [-7.5, -12.5, -25, -15, -25, -50],  # Matches original depression scores
    # Hyper (index 11)
    -100,  # Hyper gives -100
    # Blood Clots (index 12)
    -100,  # Blood clots give -100
    # CHF/CAD (index 13)
    -100,  # CHF/CAD gives -100
    # Breast Cancer (index 14)
    -100,  # Breast issues give -100
    # Smoker (index 15)
    -100,  # Smoking gives -100
    # Migraine (index 16)
    -100,  # Migraines give -100
    # PCOS (index 17)
    3,  # PCOS gives +3
    # Endometriosis (index 18)
    3,  # Endometriosis gives +3
    # Top Gender Dysphoria (index 19)
    [-15, -25, -50],  # Matches original top gender dysphoria scores
    # Top Surgery (index 20)
    [-15, -25, -50],  # Matches original top surgery scores
    # BGDP (index 21)
    3,  # BGDP gives +3
    # GDVI (index 22)
    # GDP (index 23)
    [-7.5, -12.5, -25],  # Matches original GDP scores
    # HRT (index 24)
    -100,  # HRT gives -100
]                                                                                         
original_weight_patch = [
    [-3, -2, -1, 1,2,3],  # Weights for arr[1]: ["v_unp", "unp", "sl_unp", "neutral", "sl_imp", "imp", "other"]
    [-1.5, -1, -0.5, 0.5, 1,1.5],  # Weights for arr[2]                                   
    [-3, -2, -1, 1,2,3],  # Weights for arr[3]                                            
    [3, 2, 1, -1,-2,-3],  # Weights for arr[4]
    3,  # Weight for arr[5]: "weekly"
    3,  # Weight for arr[6]: "ep"
   [-3, -2, -1, 1,2,3],  # Weights for arr[7]
    [-15, -25, -50],  # Weights for arr[8]
    [-7.5, -12.5, -25, -15, -25, -50],  # Weights for arr[9]
    [-7.5, -12.5, -25, -15, -25, -50],  # Weights for arr[10]
    -100,  # Weight for arr[11]
    -100,  # Weight for arr[12]
    -100,  # Weight for arr[13]
    -100,  # Weight for arr[14]
    -100,  # Weight for arr[15]
    -100,  # Weight for arr[16]
    3,  # Weight for arr[17]
    3,  # Weight for arr[18]
    [-15, -25, -50],  # Weights for arr[19]
    [-15, -25, -50],  # Weights for arr[20]
    3,  # Weight for arr[21]
    3,  # Weight for arr[22]
    -100,  # Weight for arr[23]
]
original_weight_shot = [
    # Pregnancy Prevention (arr[1])
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # corresponding to v_unp, unp, sl_unp, sl_imp, imp, very imp
    
    # Management of Periods (arr[2])
    [-3, -2, -1, 1, 2, 3],  # corresponding to v_unp, unp, sl_unp, sl_imp, imp, very imp
    
    # Weight Management (arr[3])
    [3, 2, 1, -1, -2, -3],  # corresponding to v_unp, unp, sl_unp, sl_imp, imp, very imp
    
    # Maintenance (arr[4])
    3,  # "monthly" adds +3
    
    # Hormones (arr[5])
    [3, 3],  # 'p' adds +3, 'ep' and any other have no effect
    
    # Consultation (arr[6])
    [-3, -2, -1, 1, 2, 3],  # corresponding to v_unp, unp, sl_unp, sl_imp, imp, very imp
    
    # Medical Procedure (arr[7])
    [-3, -2, -1, 1, 2, 3],  # corresponding to v_unp, unp, sl_unp, sl_imp, imp, very imp
    
    # Acne (arr[8])
    3,  # non-"no" adds +3
    
    # Anxiety (arr[9])
    [-7.5, -12.5, -25, -15, -25, -50],  # corresponding to mild-moderate-severe with or without acne
    
    # Depression (arr[10])
    [-7.5, -12.5, -25, -15, -25, -50],  # similar to anxiety
    
    # Hyper (arr[11])
    -100,  # any non-"no" adds -100
    
    # Blood Clots (arr[12])
    -100,  # same
    
    # CHF/CAD (arr[13])
    -100,  # same
    
    # Breast (arr[14])
    -100,  # same
    
    # Smoker (arr[15])
    -100,  # same
    
    # Migraine (arr[16])
    -100,  # same
    
    # PCOS (arr[17])
    3,  # non-"no" adds +3
    
    # Endometriosis (arr[18])
    3,  # non-"no" adds +3
    
    # Top Gender Dysphoria (arr[19])
    [-15, -25, -50],  # corresponding to mild, moderate, severe
    
    # Top Surgery (arr[20])
    [-15, -25, -50],  # same as top dysphoria
    
    # BGDP (arr[21])
    3,  # non-"no" adds +3
    
    # Gender Dysphoria Pregnancy (arr[22])
    1.5,  # non-"no" adds +1.5
    
    # HRT (arr[23])
    -100  # non-"no" adds -100
]

original_weight_combo_pill = [
    [-3, -2, -1, 1, 2, 3],   # For arr[1] (v_unp, unp, sl_unp, neutral, sl_imp, imp)
    [-1.5, -1, -0.5, 0.5, 1, 1.5],   # For arr[2]
    [-3, -2, -1, 1, 2, 3],   # For arr[3]
    [3, 2, 1, -1, -2, -3],    # For arr[4] (reverse signs compared to previous)
    3,                      # For arr[5] (daily adds +3)
    3,                      # For arr[6] (ep adds +3)
    [-3, -2, -1, 1, 2, 3],   # For arr[7]
    [-15, -25, -50],      # For arr[8] (no, mild, moderate, severe)
    [-7.5, -12.5, -25, -15, -25, -50],  # For arr[9] with combinations of arr[8]
    [-7.5, -12.5, -25, -15, -25, -50],  # For arr[10] with combinations of arr[9]
    -100,                  # For arr[11]
    -100,                  # For arr[12]
    -100,                  # For arr[13]
    -100,                  # For arr[14]
    -100,                  # For arr[15]
    -100,                  # For arr[16]
    3,                      # For arr[17]
    3,                      # For arr[18]
    [-15, -25, -50],      # For arr[19] (no, mild, moderate, severe)
    [-15, -25, -50],      # For arr[20] (no, mild, moderate, severe)
    3,                      # For arr[21]
    3,                      # For arr[22]
    -100                   # For arr[23]
]

original_weight_mini_pill = [
    # Cost Effectiveness
    [-3, -2, -1, 1, 2, 3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Pregnancy Prevention
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Management of Periods 
    [-3, -2, -1, 1, 2, 3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Weight Management
    [3, 2, 1, -1, -2, -3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Maintainance (Daily) 
    3,  # daily
    
    # Hormones (p, ep)
    [3, 3],  # [p, ep]
    
    # Seeking consultations
    [-3, -2, -1, 1, 2, 3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Acne (yes/no)
    3,  # no
    
    # Anxiety (no, mild, moderate, severe)
    [-7.5, -12.5, -25, -15, -25, -50],  # [no, mild, moderate, severe]
    
    # Depression (no, mild, moderate, severe)
    [-7.5, -12.5, -25, -15, -25, -50],  # [no, mild, moderate, severe]
    
    # Breast (yes/no)
    -100,  # no
    
    # PCOS (yes/no)
    3,  # no
    
    # ENDMT (yes/no)
    3,  # no
    
    # Gender Dysphoria Period (yes/no)
    3,  # no
    
    # Gender Dysphoria Pregnancy (yes/no)
    1.5   # no
]
original_weight_copper_IUD = [
    # Pregnancy Prevention (0-5)
    [-3, -2, -1, 1, 2, 3],  # [v_unp, unp, sl_unp, neutral, sl_imp, imp]
    
    # Maintainance (Yearly) [single value for yearly]
    3,
    
    # Vaginal Insertion (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Seeking Consultation (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Medical Procedure (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Gender Dysphoria (mild, moderate, severe)
    [-15, -25, -50],
    
    # Gender Dysphoria Vaginal Insertion (mild, moderate, severe)
    [-15, -25, -50],
    
    # Gender Dysphoria Pregnancy
    3
]
original_weight_hormonal_IUD = [
    [-3, -2, -1, 1, 2, 3],  # weights for arr[1] values: ["v_unp", "unp", "sl_unp", "neutral", "sl_imp", "imp"]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[2]
    [3, 2, 1, 0, -1, -2, -3],  # weights for arr[3]
    3,  # weight for arr[4] == "yearly"
    [3, 0],  # weights for arr[5]: ["p", "ep"]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[6]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[7]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[8]
    [-15, -25, -50],  # weights for arr[9]: ["mild", "moderate", "severe"]
    [-7.5, -12.5, -25, -15, -25, -50],  # weights for arr[10] based on arr[9]
    [-7.5, -12.5, -25, -15, -25, -50],  # weights for arr[11] based on arr[10]
    -100,  # weight for arr[12] != "no"
    3,  # weight for arr[13] != "no"
    3,  # weight for arr[14] != "no"
    3,  # weight for arr[15] != "no"
    [-15, -25, -50],  # weights for arr[16]: ["mild", "moderate", "severe"]
    3  # weight for arr[17] != "no"
]

cost_effectiveness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
partner_willingness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
pregnancy_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
prevents_sti = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
management_of_periods = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
weight_management = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
hormones_used = ['ep', 'p', 'none']
willingness_vagina = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
medical_practitioner = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
medical_procedure = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
acne = ['no', 'mild', 'moderate', 'severe']
anxiety = ['no', 'mild', 'moderate', 'severe']
depression = ['no', 'mild', 'moderate', 'severe']
hyper = ['no', 'yes']
bclots = ['no', 'yes']
chf_cad = ['no', 'yes']
breast = ['no', 'yes']
smoker = ['no', 'yes']
migraine = ['no', 'yes']
pcos = ['no', 'yes']
endmt = ['no', 'yes']
tgd = ['no', 'mild', 'moderate', 'severe']
ts = ['no', 'yes']
bgdper = ['no', 'mild', 'moderate', 'severe']
gd_vaginal_insertion = ['no', 'mild', 'moderate', 'severe']
gdp = ['no', 'mild', 'moderate', 'severe']
hrt = ['no', 'yes']
maintainance = ['daily', 'weekly', 'monthly', 'yearly']

'''
0-Cost Efectiveness
1-Pregnancy Prevention
2-Lessens Periods
3-Maintains Weight
4-Maintenance
5-Willingness
6-Prevents STI
7-Hormones Used
8-Vaginal Insertion
9-Seeking consultation
10-Medical Procedure Required
11-Acne
12-Anxiety
13-Depression
14-Hypertension
15-Blood Clots
16-History CHF or CAD
17-History of Breast Cancer
18-Smoker over 35 years
19-Migraine with aura
20-PCOS
21-Endometriosis
22-Top gender dysphoria
23-Top surgery
24-Bottom gender dysphoria period
24-Bottom gender dysphoria vaginal insertion
26-Bottom gender dysphoria pregnancy
27-HRT
'''

import copy


weights_cost_effectiveness_to_change= {
           'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'patch': copy.deepcopy(original_weight_patch),
            'combo_pill': copy.deepcopy(original_weight_combo_pill),
            'mini_pill': copy.deepcopy(original_weight_mini_pill),
            'ring': copy.deepcopy(original_weight_ring),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl),
            'arm_implant': copy.deepcopy(original_weight_arm_implant),
            "copper_iud": copy.deepcopy(original_weight_copper_IUD),
            "hormonal_iud": copy.deepcopy(original_weight_hormonal_IUD),
            "shot": copy.deepcopy(original_weight_shot),
        }

inputs = [
    ['v_unp', 'neutral', 'neutral', 'neutral', 'daily', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'no', 'yes'],
     
    ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'monthly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'yearly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'no', 'yes'] ] 

for i in inputs:
    condom_arr = ["condom", i[0], i[1], i[4], i[5], i[6], i[26]]  
    internal_condom_arr = ["int_condom", i[0], i[1], i[4], i[5], i[6], i[8], i[25], i[26]]
    cervical_cap_arr = ["cervical_cap", i[0], i[4], i[8], i[9], i[25], i[26]]
    fam_arr = ["fam", i[0], i[4], i[5], i[26]]
    arm_implant_arr = ["arm_implant", i[1], i[2], i[3], i[4], i[7], i[9], i[10], i[11], i[12], i[13], i[24], i[26]]
    copper_iud_arr = ["copper_iud", i[1], i[4], i[8], i[9], i[10], i[24], i[25], i[26]]
    hormonal_iud_arr = ["hormonal_iud", i[1], i[2], i[3], i[4], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[17], i[20],
                        i[21], i[24], i[25], i[26]]
    patch_arr = ["patch", i[0], i[1], i[2], i[3], i[4], i[7], i[9], [11], i[12], i[13], i[14], i[15], i[16], i[17], i[18],
                 i[19], i[20], i[21], i[22], i[23], i[24], i[26], i[27]]
    combo_pill_arr = ["combo_pill", i[0], i[1], i[2], i[3], i[4], i[7], i[9], [11], i[12], i[13], i[14], i[15], i[16], i[17], i[18],
                 i[19], i[20], i[21], i[22], i[23], i[24], i[26], i[27]]
    mini_pill_arr = ["mini_pill", i[0], i[1], i[2], i[3], i[4], i[7], i[9], i[11], i[12], i[13], i[17], i[20], i[21], i[24], i[26]]
    ring_arr = ["ring", i[0], i[1], i[2], i[3], i[4], i[7], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17],
                i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[26], i[27]]
    shot_arr = ["shot", i[1], i[2], i[3], i[4], i[7], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17],
                i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[26], i[27]]
    sterilization_arr = ["sterilization", i[1], i[2], i[9], i[10], i[20], i[21], i[24], i[26]]
    gel_arr = ["gel", i[0], i[4], i[5], i[8]]
    withdrawal_arr = ["withdrawal", i[0], i[4], i[5], i[26]]


condom_score = change_score_condoms(condom_arr, original_weight_condoms)
internal_condom_score = change_internal_condoms(internal_condom_arr, original_weight_internal_condoms)
cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, original_weight_cervical_cap)
fam_score = change_fam(fam_arr, original_weight_FAM)
arm_implant_score = change_arm_implant(arm_implant_arr, original_weight_arm_implant)
copper_iud_score = change_copper_iud(copper_iud_arr, original_weight_copper_IUD)
hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, original_weight_hormonal_IUD)
patch_score = change_score_patch(patch_arr, original_weight_patch)
combo_pill_score = change_score_combo_pill(combo_pill_arr, original_weight_combo_pill)
mini_pill_score = change_scoring_mini_pill(mini_pill_arr, original_weight_mini_pill)
ring_score = change_score_ring(ring_arr, original_weight_ring)
shot_score = change_score_shot(shot_arr, original_weight_shot)
sterilization_score = change_score_sterilization(sterilization_arr, original_weight_sterilization)
gel_score = change_score_gel(gel_arr, original_weight_spermicide)
withsrawal_score = change_score_withdrawal(withdrawal_arr, original_weight_withdrawl)


scores = {}
n = 20

for i in range(n):
    # Update weights for cost effectiveness
    multiplier = i + 1
    current_weights = [3 * multiplier]
    
    # Update the cost effectiveness weights for methods that use it
    weights_cost_effectiveness_to_change['condoms'][0] = current_weights
    weights_cost_effectiveness_to_change['internal_condoms'][0] = current_weights
    weights_cost_effectiveness_to_change['cervical_cap'][0] = current_weights
    weights_cost_effectiveness_to_change['FAM'][0] = current_weights
    weights_cost_effectiveness_to_change['patch'][0] = current_weights
    weights_cost_effectiveness_to_change['combo_pill'][0] = current_weights
    weights_cost_effectiveness_to_change['mini_pill'][0] = current_weights
    weights_cost_effectiveness_to_change['ring'][0] = current_weights
    weights_cost_effectiveness_to_change['spermicide'][0] = current_weights
    weights_cost_effectiveness_to_change['withdrawal'][0] = current_weights
    weights_cost_effectiveness_to_change['arm_implant'][0] = current_weights
    weights_cost_effectiveness_to_change['copper_iud'][0] = current_weights
    weights_cost_effectiveness_to_change['hormonal_iud'][0] = current_weights
    weights_cost_effectiveness_to_change['shot'][0] = current_weights


    # Calculate scores for each method
    condom_score = change_score_condoms(condom_arr, weights_cost_effectiveness_to_change['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, weights_cost_effectiveness_to_change['internal_condoms'])
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_cost_effectiveness_to_change['cervical_cap'])
    fam_score = change_fam(fam_arr, weights_cost_effectiveness_to_change['FAM'])
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_cost_effectiveness_to_change['arm_implant'])
    copper_iud_score = change_copper_iud(copper_iud_arr, weights_cost_effectiveness_to_change['copper_iud'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr,  weights_cost_effectiveness_to_change['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_cost_effectiveness_to_change['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_cost_effectiveness_to_change['combo_pill'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_cost_effectiveness_to_change['mini_pill'])
    ring_score = change_score_ring(ring_arr, weights_cost_effectiveness_to_change['ring'])
    shot_score = change_score_shot(shot_arr, weights_cost_effectiveness_to_change['shot'])
    sterilization_score = change_score_sterilization(sterilization_arr, original_weight_sterilization)
    gel_score = change_score_gel(gel_arr, weights_cost_effectiveness_to_change['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, weights_cost_effectiveness_to_change['withdrawal'])

  # Store contraceptive methods and their scores in a dictionary
    contraceptive_scores = {
        "Condom": condom_score,
        "Internal Condom": internal_condom_score,
        "Cervical Cap": cervical_cap_score,
        "FAM": fam_score,
        "Arm Implant": arm_implant_score,
        "Copper IUD": copper_iud_score,
        "Hormonal IUD": hormonal_iud_score,
        "Patch": patch_score,
        "Combination Pill": combo_pill_score,
        "Mini Pill": mini_pill_score,
        "Ring": ring_score,
        "Shot": shot_score,
        "Sterilization": sterilization_score,
        "Spermicide Gel": gel_score,
        "Withdrawal": withdrawal_score
    }
  # Sort and get top 5
    top_5_methods = sorted(contraceptive_scores.items(), key=lambda x: x[1], reverse=True)[:5]
    top_5_ranking = [method for method, _ in top_5_methods]

    # Store rankings with weights as key
    weight_key = f"({', '.join(map(str, current_weights))})"
    scores[weight_key] = top_5_ranking

# Create DataFrame and save to CSV
column_names = []
for i in range(n):
    multiplier = i + 1
    weights = [3 * multiplier]
    column_name = f"Iteration {i+1} {tuple(weights)}"
    column_names.append(column_name)

# Create DataFrame
df = pd.DataFrame(index=range(5))

# Fill DataFrame with rankings
for i in range(n):
    multiplier = i + 1
    weights = [3 * multiplier]
    weight_key = f"({', '.join(map(str, weights))})"
    column_name = f"Iteration {i+1} {tuple(weights)}"
    df[column_name] = scores[weight_key]                                                 

# Save to CSV
df.to_csv('simulation_study/maintain_contraceptive_rankings.csv', index=False)
print("Rankings have been saved to 'contraceptive_rankings.csv'")
print("\nFirst few rows of the DataFrame:")
print(df.head())    