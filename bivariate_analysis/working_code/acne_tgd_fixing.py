import copy
from functions_simulation_diff_weight_hor import *
import plotly.graph_objects as go
import numpy as np

# THIS WORKS
original_weight_condoms = [
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    3,
    1.5  # Gender dysphoria related to pregnancy (no/yes)
]
original_weight_internal_condoms = [
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)   
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    3,
    [-3, -2, -1, 1, 2, 3], # Vaginal Insertion
    [-15, -25, -50],  # Gender dysphoria related to vaginal insertion
    1.5 # Gender dysphoria related to pregnancy
]
original_weight_cervical_cap = [
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,        
    3,            # Maintenance (arr[2])
    [-3, -2, -1, 1, 2, 3],  # Vaginal Insertion (arr[3])
    [-3, -2, -1, 1, 2, 3],  # Seeking Consultation (arr[4])
    [-15, -25, -50],     # Gender Dysphoria Vaginal Insertion (arr[5])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[6])
]
original_weight_FAM = [
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,
    [-3, -2, -1, 1, 2, 3],  # Partner Willingness (arr[3])
    3,                    # Maintenance (arr[2])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[4])
]
original_weight_arm_implant = [
    [-3, -2, -1, 1, 2, 3],  # Pregnancy Prevention (arr[1])
    [-3, -2, -1, 1, 2, 3],  # Lessens Periods (arr[2])
    [3, 2, 1, -1, -2, -3],  # Maintains Weight (arr[3])
    3,                    # Maintenance (arr[4])
    [3, 3],                    # Hormones Used (arr[5])
    [-3, -2, -1, 1, 2, 3],  # Seeking consultation (arr[6])
    [-3, -2, -1, 1, 2, 3],  # Medical procedure (arr[7])
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

    3,
    
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

    3,
    
    # Gender Pregnancy (mild, moderate, severe)
    [-15, -25, -50]
    
]
original_weight_sterilization = [
    # Pregnancy Prevention (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Lessens Periods (0-5)
    [-3, -2, -1, 1, 2, 3],

    3,
    
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
    [-15, -25, -60],  # Matches original top gender dysphoria scores
    # Top Surgery (index 20)
    -100,  # Matches original top surgery scores
    # BGDP (index 21)
    3,  # BGDP gives +3
    # GDVI (index 22)
    # GDP (index 23)
    1.5,  # Matches original GDP scores
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
    [-15, -25, -60],  # Weights for arr[8]
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
    [-15, -25, -60],  # Weights for arr[19]
    -100,  # Weights for arr[20]
    3,  # Weight for arr[21]
    1.5,  # Weight for arr[22]
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
    [-15, -25, -60],  # corresponding to mild, moderate, severe
    
    # Top Surgery (arr[20])
    -100,  # same as top dysphoria
    
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
    [-15, -25, -60],      # For arr[8] (no, mild, moderate, severe)
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
    [-15, -25, -60],      # For arr[19] (no, mild, moderate, severe)
    -100,      # For arr[20] (no, mild, moderate, severe)
    3,                      # For arr[21]
    1.5,                      # For arr[22]
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
    [-7.5, -12.5, -25, -15, -25, -60],  # [no, mild, moderate, severe]
    
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
    [3, 2, 1, -1, -2, -3],  # weights for arr[3]
    3,  # weight for arr[4] == "yearly"
    [3, 3],  # weights for arr[5]: ["p", "ep"]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[6]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[7]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[8]
    [-15, -25, -60],  # weights for arr[9]: ["mild", "moderate", "severe"]
    [-7.5, -12.5, -25, -15, -25, -50],  # weights for arr[10] based on arr[9]
    [-7.5, -12.5, -25, -15, -25, -50],  # weights for arr[11] based on arr[10]
    -100,  # weight for arr[12] != "no"
    3,  # weight for arr[13] != "no"
    3,  # weight for arr[14] != "no"
    3,  # weight for arr[15] != "no"
    [-15, -25, -60],  # weights for arr[16]: ["mild", "moderate", "severe"]
    3  # weight for arr[17] != "no"
]

inputs = [
    ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],


     
]

def zero_zero(input_arr):

    weights_dict = {

        "condoms": copy.deepcopy(original_weight_condoms),
        "internal_condoms": copy.deepcopy(original_weight_internal_condoms),
        "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
        "fam": copy.deepcopy(original_weight_FAM),
        "copper_iud": copy.deepcopy(original_weight_copper_IUD),
        "sterilization": copy.deepcopy(original_weight_sterilization),
        "spermicide": copy.deepcopy(original_weight_spermicide),
        "withdrawal": copy.deepcopy(original_weight_withdrawl)
    
    }
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[7], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]

    condom_score = change_score_condoms(condom_arr, weights_dict['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, weights_dict['internal_condoms'])
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_dict['cervical_cap'])
    fam_score = change_fam(fam_arr, weights_dict['fam'])
    copper_iud_score = change_copper_iud(copper_iud_arr, weights_dict['copper_iud'])
    sterilization_score = change_score_sterilization(sterilization_arr, weights_dict['sterilization'])
    gel_score = change_score_gel(gel_arr, weights_dict['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, weights_dict['withdrawal'])

    return {
        "Condoms": condom_score,
        "Internal Condoms": internal_condom_score,
        "Cervical Cap": cervical_cap_score,
        "FAM": fam_score,
        "Copper IUD": copper_iud_score,
        "Sterilization": sterilization_score,
        "Spermicide": gel_score,
        "Withdrawal": withdrawal_score
    }

def pos_zero(input_arr, pos_acne):

    weights_dict = {
        "arm_implant": copy.deepcopy(original_weight_arm_implant),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
    }

    for method in weights_dict:
        if method == "arm_implant":
            weights_dict[method][-5] = pos_acne 
        elif method == "mini_pill":
            weights_dict[method][-8] = pos_acne 

    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]


    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])

    return {
        "Arm Implant": arm_implant_score,
        "Mini Pill": mini_pill_score
    }

def pos_neg(input_arr, pos_acne):

    weights_dict = {
        "ring": copy.deepcopy(original_weight_ring),
        "shot": copy.deepcopy(original_weight_shot),
    }

    for method in weights_dict:
        if method == "ring":
            weights_dict[method][-16] = pos_acne
        elif method == "shot":
            weights_dict[method][-16] = pos_acne
    
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
   
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])

    return {
        "Ring": ring_score,
        "Shot": shot_score
    }

def neg_zero(input_arr):

    weights_dict = {
        "hormonal_iud": copy.deepcopy(original_weight_hormonal_IUD)
    }

    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]

    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])

    return {
        "Hormonal IUD": hormonal_iud_score
    }

def neg_neg(input_arr):

    weights_dict = {
        "patch": copy.deepcopy(original_weight_patch),
        "combo_pill": copy.deepcopy(original_weight_combo_pill),
    }

    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])

    return {
        "Patch": patch_score,
        "Combo Pill": combo_pill_score
    }


# Scoring Condoms
condom_no = {} 
condoms_mild = {}
condoms_moderate = {}
condoms_severe = {}
condoms_3 = {}
condoms_21 = {}
condoms_42 = {}
condoms_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        condom_no["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condom_no["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condom_no["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condom_no["severe"] = zero_zero(arr)["Condoms"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        condoms_mild["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condoms_mild["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condoms_mild["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condoms_mild["severe"] = zero_zero(arr)["Condoms"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        condoms_moderate["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condoms_moderate["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condoms_moderate["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condoms_moderate["severe"] = zero_zero(arr)["Condoms"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        condoms_severe["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condoms_severe["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condoms_severe["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condoms_severe["severe"] = zero_zero(arr)["Condoms"]


condoms_3["3"] = zero_zero(inputs[0])["Condoms"]
condoms_3["21"] = zero_zero(inputs[0])["Condoms"]
condoms_3["42"] = zero_zero(inputs[0])["Condoms"]
condoms_3["60"] = zero_zero(inputs[0])["Condoms"]

condoms_21["3"] = zero_zero(inputs[0])["Condoms"]
condoms_21["21"] = zero_zero(inputs[0])["Condoms"]
condoms_21["42"] = zero_zero(inputs[0])["Condoms"]
condoms_21["60"] = zero_zero(inputs[0])["Condoms"]

condoms_42["3"] = zero_zero(inputs[0])["Condoms"]
condoms_42["21"] = zero_zero(inputs[0])["Condoms"]
condoms_42["42"] = zero_zero(inputs[0])["Condoms"]
condoms_42["60"] = zero_zero(inputs[0])["Condoms"]

condoms_60["3"] = zero_zero(inputs[0])["Condoms"]
condoms_60["21"] = zero_zero(inputs[0])["Condoms"]
condoms_60["42"] = zero_zero(inputs[0])["Condoms"]
condoms_60["60"] = zero_zero(inputs[0])["Condoms"]

# Internal Condoms
internal_condom_no = {}
internal_condom_mild = {}
internal_condom_moderate = {}
internal_condom_severe = {}
internal_condom_3 = {}
internal_condom_21 = {}
internal_condom_42 = {}
internal_condom_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        internal_condom_no["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_no["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_no["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_no["severe"] = zero_zero(arr)["Internal Condoms"]


for arr in inputs[4:8]:
    if arr[-6] == "no":
        internal_condom_mild["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_mild["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_mild["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_mild["severe"] = zero_zero(arr)["Internal Condoms"]


for arr in inputs[8:12]:
    if arr[-6] == "no":
        internal_condom_moderate["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_moderate["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_moderate["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_moderate["severe"] = zero_zero(arr)["Internal Condoms"]


for arr in inputs[12:16]:
    if arr[-6] == "no":
        internal_condom_severe["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_severe["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_severe["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_severe["severe"] = zero_zero(arr)["Internal Condoms"]


internal_condom_3["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_21["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_42["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_60["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["60"] = zero_zero(inputs[0])["Internal Condoms"]

# Cervical Cap
cervical_cap_no = {}
cervical_cap_mild = {}
cervical_cap_moderate = {}
cervical_cap_severe = {}
cervical_cap_3 = {}
cervical_cap_21 = {}
cervical_cap_42 = {}
cervical_cap_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        cervical_cap_no["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_no["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_no["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_no["severe"] = zero_zero(arr)["Cervical Cap"]


for arr in inputs[4:8]:
    if arr[-6] == "no":
        cervical_cap_mild["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_mild["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_mild["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_mild["severe"] = zero_zero(arr)["Cervical Cap"]


for arr in inputs[8:12]:
    if arr[-6] == "no":
        cervical_cap_moderate["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_moderate["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_moderate["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_moderate["severe"] = zero_zero(arr)["Cervical Cap"]


for arr in inputs[12:16]:
    if arr[-6] == "no":
        cervical_cap_severe["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_severe["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_severe["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_severe["severe"] = zero_zero(arr)["Cervical Cap"]




cervical_cap_3["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_21["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_42["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_60["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["60"] = zero_zero(inputs[0])["Cervical Cap"]

# FAM
fam_no = {}
fam_mild = {}
fam_moderate = {}
fam_severe = {}
fam_3 = {}
fam_21 = {}
fam_42 = {}
fam_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        fam_no["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_no["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_no["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_no["severe"] = zero_zero(arr)["FAM"]


for arr in inputs[4:8]:
    if arr[-6] == "no":
        fam_mild["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_mild["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_mild["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_mild["severe"] = zero_zero(arr)["FAM"]


for arr in inputs[8:12]:
    if arr[-6] == "no":
        fam_moderate["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_moderate["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_moderate["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_moderate["severe"] = zero_zero(arr)["FAM"]


for arr in inputs[12:16]:
    if arr[-6] == "no":
        fam_severe["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_severe["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_severe["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_severe["severe"] = zero_zero(arr)["FAM"]


fam_3["3"] = zero_zero(inputs[0])["FAM"]
fam_3["21"] = zero_zero(inputs[0])["FAM"]
fam_3["42"] = zero_zero(inputs[0])["FAM"]
fam_3["60"] = zero_zero(inputs[0])["FAM"]

fam_21["3"] = zero_zero(inputs[0])["FAM"]
fam_21["21"] = zero_zero(inputs[0])["FAM"]
fam_21["42"] = zero_zero(inputs[0])["FAM"]
fam_21["60"] = zero_zero(inputs[0])["FAM"]

fam_42["3"] = zero_zero(inputs[0])["FAM"]
fam_42["21"] = zero_zero(inputs[0])["FAM"]
fam_42["42"] = zero_zero(inputs[0])["FAM"]
fam_42["60"] = zero_zero(inputs[0])["FAM"]

fam_60["3"] = zero_zero(inputs[0])["FAM"]
fam_60["21"] = zero_zero(inputs[0])["FAM"]
fam_60["42"] = zero_zero(inputs[0])["FAM"]
fam_60["60"] = zero_zero(inputs[0])["FAM"]

# Copper IUD
copper_iud_no = {}
copper_iud_mild = {}
copper_iud_moderate = {}
copper_iud_severe = {}
copper_iud_3 = {}
copper_iud_21 = {}
copper_iud_42 = {}
copper_iud_60 = {}


for arr in inputs[0:4]:
    if arr[-6] == "no":
        copper_iud_no["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_no["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate":
        copper_iud_no["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_no["severe"] = zero_zero(arr)["Copper IUD"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        copper_iud_mild["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_mild["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate":
        copper_iud_mild["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_mild["severe"] = zero_zero(arr)["Copper IUD"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        copper_iud_moderate["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_moderate["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate": 
        copper_iud_moderate["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_moderate["severe"] = zero_zero(arr)["Copper IUD"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        copper_iud_severe["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_severe["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate":
        copper_iud_severe["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_severe["severe"] = zero_zero(arr)["Copper IUD"]

copper_iud_3["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_21["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_42["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_60["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["60"] = zero_zero(inputs[0])["Copper IUD"]

# Sterilization
sterilization_no = {}
sterilization_mild = {}
sterilization_moderate = {}
sterilization_severe = {}
sterilization_3 = {}
sterilization_21 = {}
sterilization_42 = {}
sterilization_60 = {} 

for arr in inputs[0:4]:
    if arr[-6] == "no":
        sterilization_no["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_no["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_no["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_no["severe"] = zero_zero(arr)["Sterilization"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        sterilization_mild["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_mild["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_mild["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_mild["severe"] = zero_zero(arr)["Sterilization"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        sterilization_moderate["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_moderate["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_moderate["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_moderate["severe"] = zero_zero(arr)["Sterilization"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        sterilization_severe["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_severe["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_severe["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_severe["severe"] = zero_zero(arr)["Sterilization"]

sterilization_3["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_21["3"] = zero_zero(inputs[0])["Sterilization"]    
sterilization_21["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_42["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_60["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["60"] = zero_zero(inputs[0])["Sterilization"]

# Spermicide
spermicide_no = {}
spermicide_mild = {}
spermicide_moderate = {}
spermicide_severe = {}
spermicide_3 = {}
spermicide_21 = {}
spermicide_42 = {}
spermicide_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        spermicide_no["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_no["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_no["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_no["severe"] = zero_zero(arr)["Spermicide"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        spermicide_mild["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_mild["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_mild["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_mild["severe"] = zero_zero(arr)["Spermicide"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        spermicide_moderate["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_moderate["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_moderate["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_moderate["severe"] = zero_zero(arr)["Spermicide"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        spermicide_severe["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_severe["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_severe["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_severe["severe"] = zero_zero(arr)["Spermicide"]

spermicide_3["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_21["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_42["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_60["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["60"] = zero_zero(inputs[0])["Spermicide"]

# Withdrawal
withdrawal_no = {}
withdrawal_mild = {}
withdrawal_moderate = {}
withdrawal_severe = {}
withdrawal_3 = {}
withdrawal_21 = {}
withdrawal_42 = {}
withdrawal_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        withdrawal_no["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_no["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_no["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_no["severe"] = zero_zero(arr)["Withdrawal"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        withdrawal_mild["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_mild["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_mild["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_mild["severe"] = zero_zero(arr)["Withdrawal"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        withdrawal_moderate["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_moderate["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_moderate["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_moderate["severe"] = zero_zero(arr)["Withdrawal"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        withdrawal_severe["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_severe["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_severe["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_severe["severe"] = zero_zero(arr)["Withdrawal"]

withdrawal_3["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["60"] = zero_zero(inputs[0])["Withdrawal"]

withdrawal_21["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["60"] = zero_zero(inputs[0])["Withdrawal"]

withdrawal_42["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["60"] = zero_zero(inputs[0])["Withdrawal"]

withdrawal_60["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["60"] = zero_zero(inputs[0])["Withdrawal"]

# Arm Implant

arm_implant_3 = {}
arm_implant_21 = {}
arm_implant_42 = {}
arm_implant_60 = {}


arr_arm = inputs[5]
arm_implant_3["3"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["21"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["42"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["60"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["no"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["mild"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["moderate"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["severe"] = pos_zero(arr_arm, 3)["Arm Implant"]

arm_implant_21["3"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["21"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["42"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["60"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["no"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["mild"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["moderate"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["severe"] = pos_zero(arr_arm, 21)["Arm Implant"]

arm_implant_42["3"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["21"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["42"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["60"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["no"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["mild"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["moderate"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["severe"] = pos_zero(arr_arm, 42)["Arm Implant"]

arm_implant_60["3"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["21"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["42"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["60"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["no"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["mild"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["moderate"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["severe"] = pos_zero(arr_arm, 60)["Arm Implant"]

    
# Mini Pill

mini_pill_3 = {}
mini_pill_21 = {}
mini_pill_42 = {}
mini_pill_60 = {}

arr_mini = inputs[6]
mini_pill_3["3"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["21"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["42"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["60"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["no"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["mild"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["moderate"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["severe"] = pos_zero(arr_mini, 3)["Mini Pill"]

mini_pill_21["3"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["21"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["42"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["60"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["no"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["mild"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["moderate"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["severe"] = pos_zero(arr_mini, 21)["Mini Pill"]

mini_pill_42["3"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["21"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["42"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["60"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["no"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["mild"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["moderate"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["severe"] = pos_zero(arr_mini, 42)["Mini Pill"]

mini_pill_60["3"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["21"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["42"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["60"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["no"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["mild"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["moderate"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["severe"] = pos_zero(arr_mini, 60)["Mini Pill"]

# Hormonal IUD
hormonal_iud_no = {}
hormonal_iud_mild = {}
hormonal_iud_moderate = {}
hormonal_iud_severe = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        hormonal_iud_no["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_no["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_no["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_no["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["60"] = neg_zero(arr)["Hormonal IUD"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        hormonal_iud_mild["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_mild["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_mild["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_mild["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["60"] = neg_zero(arr)["Hormonal IUD"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        hormonal_iud_moderate["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_moderate["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_moderate["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_moderate["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["60"] = neg_zero(arr)["Hormonal IUD"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        hormonal_iud_severe["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_severe["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_severe["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_severe["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["60"] = neg_zero(arr)["Hormonal IUD"]

# Ring
ring_3 = {}
ring_21 = {}
ring_42 = {}
ring_60 = {}

for arr in inputs[4:8]:
    if arr[-6] == "no":
        ring_3["no"] = pos_neg(arr, 3)["Ring"]
        ring_21["no"] = pos_neg(arr, 21)["Ring"]
        ring_42["no"] = pos_neg(arr, 42)["Ring"]
        ring_60["no"] = pos_neg(arr, 60)["Ring"]
    elif arr[-6] == "mild":
        ring_3["mild"] = pos_neg(arr, 3)["Ring"]
        ring_21["mild"] = pos_neg(arr, 21)["Ring"]
        ring_42["mild"] = pos_neg(arr, 42)["Ring"]
        ring_60["mild"] = pos_neg(arr, 60)["Ring"]
    elif arr[-6] == "moderate":
        ring_3["moderate"] = pos_neg(arr, 3)["Ring"]
        ring_21["moderate"] = pos_neg(arr, 21)["Ring"]
        ring_42["moderate"] = pos_neg(arr, 42)["Ring"]
        ring_60["moderate"] = pos_neg(arr, 60)["Ring"]
    elif arr[-6] == "severe":
        ring_3["severe"] = pos_neg(arr, 3)["Ring"]
        ring_21["severe"] = pos_neg(arr, 21)["Ring"]
        ring_42["severe"] = pos_neg(arr, 42)["Ring"]
        ring_60["severe"] = pos_neg(arr, 60)["Ring"]

# Shot
shot_3 = {}
shot_21 = {}
shot_42 = {}
shot_60 = {}

for arr in inputs[4:8]:
    if arr[-6] == "no":
        shot_3["no"] = pos_neg(arr, 3)["Shot"]
        shot_21["no"] = pos_neg(arr, 21)["Shot"]
        shot_42["no"] = pos_neg(arr, 42)["Shot"]
        shot_60["no"] = pos_neg(arr, 60)["Shot"]
    elif arr[-6] == "mild":
        shot_3["mild"] = pos_neg(arr, 3)["Shot"]
        shot_21["mild"] = pos_neg(arr, 21)["Shot"]
        shot_42["mild"] = pos_neg(arr, 42)["Shot"]
        shot_60["mild"] = pos_neg(arr, 60)["Shot"]
    elif arr[-6] == "moderate":
        shot_3["moderate"] = pos_neg(arr, 3)["Shot"]
        shot_21["moderate"] = pos_neg(arr, 21)["Shot"]
        shot_42["moderate"] = pos_neg(arr, 42)["Shot"]
        shot_60["moderate"] = pos_neg(arr, 60)["Shot"]
    elif arr[-6] == "severe":
        shot_3["severe"] = pos_neg(arr, 3)["Shot"]
        shot_21["severe"] = pos_neg(arr, 21)["Shot"]
        shot_42["severe"] = pos_neg(arr, 42)["Shot"]
        shot_60["severe"] = pos_neg(arr, 60)["Shot"]


# Patch
patch_no = {}
patch_mild = {}
patch_moderate = {}
patch_severe = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        patch_no["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_no["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_no["moderate"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "severe":
        patch_no["severe"] = neg_neg(arr)["Patch"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        patch_mild["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_mild["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_mild["moderate"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "severe":
        patch_mild["severe"] = neg_neg(arr)["Patch"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        patch_moderate["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_moderate["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_moderate["moderate"] = neg_neg(arr)["Patch"]  
    elif arr[-6] == "severe":
        patch_moderate["severe"] = neg_neg(arr)["Patch"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        patch_severe["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_severe["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_severe["moderate"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "severe":
        patch_severe["severe"] = neg_neg(arr)["Patch"]
        
# Combo Pill
combo_no = {}
combo_mild = {}
combo_moderate = {}
combo_severe = {}


for arr in inputs[0:4]:
    if arr[-6] == "no":
        combo_no["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_no["mild"] = neg_neg(arr)["Combo Pill"]   
    elif arr[-6] == "moderate":
        combo_no["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_no["severe"] = neg_neg(arr)["Combo Pill"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        combo_mild["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_mild["mild"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "moderate":
        combo_mild["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_mild["severe"] = neg_neg(arr)["Combo Pill"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        combo_moderate["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_moderate["mild"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "moderate":
        combo_moderate["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_moderate["severe"] = neg_neg(arr)["Combo Pill"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        combo_severe["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_severe["mild"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "moderate":
        combo_severe["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_severe["severe"] = neg_neg(arr)["Combo Pill"]
        
 

        
# After all the dictionaries are populated, add visualization code:

import plotly.graph_objects as go
import numpy as np
# Create matrices from the actual dictionaries
def create_full_matrix(method_dicts):
    no_dict, mild_dict, mod_dict, sev_dict, t3_dict, t21_dict, t42_dict, t60_dict = method_dicts

    return np.array([
        [sev_dict['severe'], sev_dict['moderate'], sev_dict['mild'], sev_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [mod_dict['severe'], mod_dict['moderate'], mod_dict['mild'], mod_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [mild_dict['severe'], mild_dict['moderate'], mild_dict['mild'], mild_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [no_dict['severe'], no_dict['moderate'], no_dict['mild'], no_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [t21_dict['3'], t21_dict['3'], t21_dict['3'], t21_dict['3'], t21_dict['3'], t21_dict['21'], t21_dict['42'], t21_dict['60']],
        [t42_dict['3'], t42_dict['3'], t42_dict['3'], t42_dict['3'], t42_dict['3'], t42_dict['21'], t42_dict['42'], t42_dict['60']],
        [t60_dict['3'], t60_dict['3'], t60_dict['3'], t60_dict['3'], t60_dict['3'], t60_dict['21'], t60_dict['42'], t60_dict['60']],
    ])
    
# Create all matrices
z_condoms = create_full_matrix([condom_no, condoms_mild, condoms_moderate, condoms_severe, condoms_3, condoms_21, condoms_42, condoms_60])
z_internal_condoms = create_full_matrix([internal_condom_no, internal_condom_mild, internal_condom_moderate, internal_condom_severe, internal_condom_3, internal_condom_21, internal_condom_42, internal_condom_60])
z_cervical_cap = create_full_matrix([cervical_cap_no, cervical_cap_mild, cervical_cap_moderate, cervical_cap_severe, cervical_cap_3, cervical_cap_21, cervical_cap_42, cervical_cap_60])
z_fam = create_full_matrix([fam_no, fam_mild, fam_moderate, fam_severe, fam_3, fam_21, fam_42, fam_60])
z_copper_iud = create_full_matrix([copper_iud_no, copper_iud_mild, copper_iud_moderate, copper_iud_severe, copper_iud_3, copper_iud_21, copper_iud_42, copper_iud_60])
z_sterilization = create_full_matrix([sterilization_no, sterilization_mild, sterilization_moderate, sterilization_severe, sterilization_3, sterilization_21, sterilization_42, sterilization_60])
z_spermicide = create_full_matrix([spermicide_no, spermicide_mild, spermicide_moderate, spermicide_severe, spermicide_3, spermicide_21, spermicide_42, spermicide_60])
z_withdrawal = create_full_matrix([withdrawal_no, withdrawal_mild, withdrawal_moderate, withdrawal_severe, withdrawal_3, withdrawal_21, withdrawal_42, withdrawal_60])


'''
z_arm_implant = np.array([
    [arm_implant_3['60'], arm_implant_3['42'], arm_implant_3['21'],arm_implant_3['3'], arm_implant_3['no'], arm_implant_3['mild'], arm_implant_3['moderate'], arm_implant_3['severe']],
    [arm_implant_21['60'], arm_implant_21['42'], arm_implant_21['21'], arm_implant_21['3'] ,arm_implant_21['no'], arm_implant_21['mild'], arm_implant_21['moderate'], arm_implant_21['severe']],
    [arm_implant_42['60'], arm_implant_42['42'], arm_implant_42['21'], arm_implant_42['3'], arm_implant_42['no'], arm_implant_42['mild'], arm_implant_42['moderate'], arm_implant_42['severe']],
    [arm_implant_60['60'], arm_implant_60['42'], arm_implant_60['21'], arm_implant_60['3'], arm_implant_60['no'], arm_implant_60['mild'], arm_implant_60['moderate'], arm_implant_60['severe']],
])
'''
z_arm_implant = np.array([
    [arm_implant_3['severe'], arm_implant_3['moderate'], arm_implant_3['mild'], arm_implant_3['no'], arm_implant_3['3'], arm_implant_3['21'], arm_implant_3['42'], arm_implant_3['60']],
    [arm_implant_21['severe'], arm_implant_21['moderate'], arm_implant_21['mild'], arm_implant_21['no'], arm_implant_21['3'], arm_implant_21['21'], arm_implant_21['42'], arm_implant_21['60']],
    [arm_implant_42['severe'], arm_implant_42['moderate'], arm_implant_42['mild'], arm_implant_42['no'], arm_implant_42['3'], arm_implant_42['21'], arm_implant_42['42'], arm_implant_42['60']],
    [arm_implant_60['severe'], arm_implant_60['moderate'], arm_implant_60['mild'], arm_implant_60['no'], arm_implant_60['3'], arm_implant_60['21'], arm_implant_60['42'], arm_implant_60['60']],
])

'''
z_mini = np.array([
    [mini_pill_3['3'], mini_pill_3['21'], mini_pill_3['42'], mini_pill_3['3'], mini_pill_3['no'], mini_pill_3['mild'], mini_pill_3['moderate'], mini_pill_3['severe']],
    [mini_pill_21['3'], mini_pill_21['21'], mini_pill_21['42'], mini_pill_21['3'], mini_pill_21['no'], mini_pill_21['mild'], mini_pill_21['moderate'], mini_pill_21['severe']],
    [mini_pill_42['3'], mini_pill_42['21'], mini_pill_42['42'], mini_pill_42['3'], mini_pill_42['no'], mini_pill_42['mild'], mini_pill_42['moderate'], mini_pill_42['severe']],
    [mini_pill_60['3'], mini_pill_60['21'], mini_pill_60['42'], mini_pill_60['3'], mini_pill_60['no'], mini_pill_60['mild'], mini_pill_60['moderate'], mini_pill_60['severe']],
])
'''
z_mini = np.array([
    [mini_pill_3['severe'], mini_pill_3['moderate'], mini_pill_3['mild'], mini_pill_3['no'], mini_pill_3['3'], mini_pill_3['21'], mini_pill_3['42'], mini_pill_3['60']],
    [mini_pill_21['severe'], mini_pill_21['moderate'], mini_pill_21['mild'], mini_pill_21['no'], mini_pill_21['3'], mini_pill_21['21'], mini_pill_21['42'], mini_pill_21['60']],
    [mini_pill_42['severe'], mini_pill_42['moderate'], mini_pill_42['mild'], mini_pill_42['no'], mini_pill_42['3'], mini_pill_42['21'], mini_pill_42['42'], mini_pill_42['60']],
    [mini_pill_60['severe'], mini_pill_60['moderate'], mini_pill_60['mild'], mini_pill_60['no'], mini_pill_60['3'], mini_pill_60['21'], mini_pill_60['42'], mini_pill_60['60']],
])

'''
z_hormonal_iud = np.array([
    [hormonal_iud_severe['60'], hormonal_iud_severe['42'], hormonal_iud_severe['21'], hormonal_iud_severe['3'], hormonal_iud_severe['no'], hormonal_iud_severe['mild'], hormonal_iud_severe['moderate'], hormonal_iud_severe['severe']],
    [hormonal_iud_moderate['60'], hormonal_iud_moderate['42'], hormonal_iud_moderate['21'], hormonal_iud_moderate['3'], hormonal_iud_moderate['no'], hormonal_iud_moderate['mild'], hormonal_iud_moderate['moderate'], hormonal_iud_moderate['severe']],
    [hormonal_iud_mild['60'], hormonal_iud_mild['42'], hormonal_iud_mild['21'], hormonal_iud_mild['3'], hormonal_iud_mild['no'], hormonal_iud_mild['mild'], hormonal_iud_mild['moderate'], hormonal_iud_mild['severe']],
    [hormonal_iud_no['60'], hormonal_iud_no['42'], hormonal_iud_no['21'], hormonal_iud_no['3'], hormonal_iud_no['no'], hormonal_iud_no['mild'], hormonal_iud_no['moderate'], hormonal_iud_no['severe']],
])
'''
z_hormonal_iud = np.array([
    [hormonal_iud_severe['severe'], hormonal_iud_severe['moderate'], hormonal_iud_severe['mild'], hormonal_iud_severe['no'], hormonal_iud_severe['3'], hormonal_iud_severe['21'], hormonal_iud_severe['42'], hormonal_iud_severe['60']],
    [hormonal_iud_moderate['severe'], hormonal_iud_moderate['moderate'], hormonal_iud_moderate['mild'], hormonal_iud_moderate['no'], hormonal_iud_moderate['3'], hormonal_iud_moderate['21'], hormonal_iud_moderate['42'], hormonal_iud_moderate['60']],
    [hormonal_iud_mild['severe'], hormonal_iud_mild['moderate'], hormonal_iud_mild['mild'], hormonal_iud_mild['no'], hormonal_iud_mild['3'], hormonal_iud_mild['21'], hormonal_iud_mild['42'], hormonal_iud_mild['60']],
    [hormonal_iud_no['severe'], hormonal_iud_no['moderate'], hormonal_iud_no['mild'], hormonal_iud_no['no'], hormonal_iud_no['3'], hormonal_iud_no['21'], hormonal_iud_no['42'], hormonal_iud_no['60']],
])


z_ring = np.array([
    [ring_3['no'], ring_3['mild'], ring_3['moderate'], ring_3['severe']],
    [ring_21['no'], ring_21['mild'], ring_21['moderate'], ring_21['severe']],
    [ring_42['no'], ring_42['mild'], ring_42['moderate'], ring_42['severe']],
    [ring_60['no'], ring_60['mild'], ring_60['moderate'], ring_60['severe']]
])

z_ring = np.array([
    [ring_3['severe'], ring_3['moderate'], ring_3['mild'], ring_3['no']],
    [ring_21['severe'], ring_21['moderate'], ring_21['mild'], ring_21['no']],
    [ring_42['severe'], ring_42['moderate'], ring_42['mild'], ring_42['no']],
    [ring_60['severe'], ring_60['moderate'], ring_60['mild'], ring_60['no']]
])
'''
# Create shot matrix (4x3 matrix)
z_shot = np.array([
    [shot_3['no'], shot_3['mild'], shot_3['moderate'], shot_3['severe']],
    [shot_21['no'], shot_21['mild'], shot_21['moderate'], shot_21['severe']],
    [shot_42['no'], shot_42['mild'], shot_42['moderate'], shot_42['severe']],
    [shot_60['no'], shot_60['mild'], shot_60['moderate'], shot_60['severe']]
])
'''
z_shot = np.array([
    [shot_3['severe'], shot_3['moderate'], shot_3['mild'], shot_3['no']],
    [shot_21['severe'], shot_21['moderate'], shot_21['mild'], shot_21['no']],
    [shot_42['severe'], shot_42['moderate'], shot_42['mild'], shot_42['no']],
    [shot_60['severe'], shot_60['moderate'], shot_60['mild'], shot_60['no']]
])
# Create patch matrix (4x4 matrix)

z_patch = np.array([
    [patch_severe['no'], patch_severe['mild'], patch_severe['moderate'], patch_severe['severe']],
    [patch_moderate['no'], patch_moderate['mild'], patch_moderate['moderate'], patch_moderate['severe']],
    [patch_mild['no'], patch_mild['mild'], patch_mild['moderate'], patch_mild['severe']],
    [patch_no['no'], patch_no['mild'], patch_no['moderate'], patch_no['severe']],
])

z_patch = np.array([
    [patch_severe['severe'], patch_severe['moderate'], patch_severe['mild'], patch_severe['no']],
    [patch_moderate['severe'], patch_moderate['moderate'], patch_moderate['mild'], patch_moderate['no']],
    [patch_mild['severe'], patch_mild['moderate'], patch_mild['mild'], patch_mild['no']],
    [patch_no['severe'], patch_no['moderate'], patch_no['mild'], patch_no['no']],
])

# Add patch surface with its specific axes

z_combo_pill = np.array([
    [combo_severe['no'], combo_severe['mild'], combo_severe['moderate'], combo_severe['severe']],
    [combo_moderate['no'], combo_moderate['mild'], combo_moderate['moderate'], combo_moderate['severe']],
    [combo_mild['no'], combo_mild['mild'], combo_mild['moderate'], combo_mild['severe']],
    [combo_no['no'], combo_no['mild'], combo_no['moderate'], combo_no['severe']],
])
z_combo_pill = np.array([
    [combo_severe['severe'], combo_severe['moderate'], combo_severe['mild'], combo_severe['no']],
    [combo_moderate['severe'], combo_moderate['moderate'], combo_moderate['mild'], combo_moderate['no']],
    [combo_mild['severe'], combo_mild['moderate'], combo_mild['mild'], combo_mild['no']],
    [combo_no['severe'], combo_no['moderate'], combo_no['mild'], combo_no['no']],
])
# Define distinct colors
distinct_colors = [
    '#FF0000',  # Red
    '#0000FF',  # Blue
    '#FFD700',  # Gold
    '#FF1493',  # Deep Pink
    '#00FF00',  # Lime
    '#8B008B',  # Dark Magenta
    '#FF8C00',  # Dark Orange
    '#00FFFF',  # Cyan
    '#800000',  # Maroon
    '#000080',  # Navy
    '#808000',  # Olive
    '#FF00FF',  # Magenta
    '#008080',  # Teal
    '#FFA500',  # Orange
    '#4B0082'   # Indigo
]
#x_full = ['60', '42', '21', '3', '0', '-15', '-25', '-50']
#y_full = ['-50', '-25', '-15', '0', '3', '21', '42', '60']

x_full = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
y_full = ['-60', '-25', '-15', '0', '3', '21', '42', '60']

x_partial = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
#y_partial = ['-50', '-25', '-15', '0', '3', '21', '42', '60']
y_partial = ['3', '21', '42', '60']

x_partial_mini = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
y_partial_mini = ['3', '21', '42', '60']

x_hormonal = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
y_hormonal = ['-60', '-25', '-15', '0']

x_ring_shot = ['-60', '-25', '-15', '0']
y_ring_shot = ['3', '21', '42', '60']

x_patch_combo = ['-60', '-25', '-15', '0']
y_patch_combo = ['-60', '-25', '-15', '0']
severity_map = {
    'severe': -60,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [3, 21, 42, 60]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-60", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values] # Include 0 for continuity
all_y_values = negative_y_values + positive_values[1:]

# Create figure
fig = go.Figure()


fig.add_trace(go.Surface(
    x=x_patch_combo,
    y=y_patch_combo,
    z=z_patch,
    name='Patch',
    colorscale=[[0, distinct_colors[13]], [1, distinct_colors[13]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Patch',
    hoverinfo='name+z'
))

# Add combo pill surface
fig.add_trace(go.Surface(
    x=x_patch_combo,
    y=y_patch_combo,
    z=z_combo_pill,
    name='Combo Pill',
    colorscale=[[0, distinct_colors[14]], [1, distinct_colors[14]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Combo Pill',
    hoverinfo='name+z'
))

# Add ring surface with its specific axes

fig.add_trace(go.Surface(
    x=x_ring_shot,
    y=y_ring_shot,
    z=z_ring,
    name='Ring',
    colorscale=[[0, distinct_colors[11]], [1, distinct_colors[11]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Ring',
    hoverinfo='name+z'
))

# Add shot surface
fig.add_trace(go.Surface(
    x=x_ring_shot,
    y=y_ring_shot,
    z=z_shot,
    name='Shot',
    colorscale=[[0, distinct_colors[12]], [1, distinct_colors[12]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Shot',
    hoverinfo='name+z'
))


# Add hormonal IUD surface with its specific axes
#y_hormonal = ['no', 'mild', 'moderate', 'severe']


fig.add_trace(go.Surface(
    x=x_hormonal,
    y=y_hormonal,
    z=z_hormonal_iud,
    name='Hormonal IUD',
    colorscale=[[0, distinct_colors[10]], [1, distinct_colors[10]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Hormonal IUD',
    hoverinfo='name+z'
))

# Add mini pill surface
fig.add_trace(go.Surface(
    x=x_partial_mini,
    y=y_partial_mini,
    z=z_mini,
    name='Mini Pill',
    colorscale=[[0, distinct_colors[9]], [1, distinct_colors[9]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Mini Pill',
    hoverinfo='name+z'
))


# Define consistent axis labels
# Update the surfaces list to use consistent axis definitions

import numpy as np
import plotly.graph_objects as go


'''
# Define the numerical values for the labels (in ascending order)
x_values = [60, 25, 10, -10, -13, -27, -42, -60]  # Ascending order
#x_labels = [60, 42, 21, 3, 0, -15, -25, -50]  # Reverse order for display
x_labels = [-60, -25, -15, 0, 3, 21, 42, 60]  # Correct order for display
y_values = [-60, -25, -10, 10, 13, 27, 42, 60]  # Ascending order
y_labels = [-60, -25, -15, 0, 3, 21, 42, 60]  # Correct order for display
# Define the numerical values for the labels (in ascending order)
 # Correct order for display
'''
x_values = [60, 25, 15, 0, -3, -21, -42, -60]  # Ascending order
#x_labels = [60, 42, 21, 3, 0, -15, -25, -50]  # Reverse order for display
x_labels = [-60, -25, -15, 0, 3, 21, 42, 60]  # Correct order for display
y_values = [-60, -25, -15, 0, 3, 21, 42, 60]  # Ascending order
y_labels = [-60, -25, -15, 0, 3, 21, 42, 60] 
# Update the surfaces list to use numerical values for x and y
surfaces = [
    ('Condom', z_condoms, x_values, y_values),
    ('Internal Condom', z_internal_condoms, x_values, y_values),
    ('Cervical Cap', z_cervical_cap, x_values, y_values),
    ('FAM', z_fam, x_values, y_values),
    ('Copper IUD', z_copper_iud, x_values, y_values),
    ('Sterilization', z_sterilization, x_values, y_values),
    ('Gel', z_spermicide, x_values, y_values),
    ('Withdrawal', z_withdrawal, x_values, y_values),
    ('Arm Implant', z_arm_implant, x_values, y_partial_mini),
    ('Mini Pill', z_mini, x_values, y_partial_mini),
    ('Hormonal IUD', z_hormonal_iud, x_values, y_values),
    ('Ring', z_ring, x_values, y_ring_shot),
    ('Shot', z_shot, x_values, y_ring_shot),
    ('Patch', z_patch, x_values, y_values),
    ('Combo Pill', z_combo_pill, x_values, y_values),
]
contraceptive_colors = {
    "Hormonal IUD": '#FF0000',  # Red
    "Patch": '#0000FF',         # Blue
    "Combo Pill": '#FFD700',    # Gold
    "Arm Implant": '#FF1493',   # Deep Pink
    "Mini Pill": '#00FF00',     # Lime
    "Ring": '#8B008B',          # Dark Magenta
    "Shot": '#FF8C00',          # Dark Orange
    "Condom": '#00FFFF',        # Cyan
    "Internal Condom": '#800000',# Maroon
    "Cervical Cap": '#000080',  # Navy
    "FAM": '#808000',           # Olive
    "Copper IUD": '#FF00FF',    # Magenta
    "Sterilization": '#008080', # Teal
    "Gel": '#FFA500',           # Orange
    "Withdrawal": '#4B0082'     # Indigo
}
# Create figure
fig = go.Figure()

# Add all surfaces with consistent axis definitions
for i, (name, z, x, y) in enumerate(surfaces):
    color = contraceptive_colors[name]
    fig.add_trace(go.Surface(
        x=x,  # Use ascending numerical values for spacing
        y=y,  # Use ascending numerical values for spacing
        z=z,
        name=name,
        colorscale=[[0, color], [1, color]],
        showscale=False,
        opacity=0.7,
        showlegend=True,
        legendgroup=name,
        hoverinfo='name+z'
    ))

# Update layout with improved legend and accurate axis labels
fig.update_layout(
    title='Contraceptive Methods Scores - 3D Surface Plot',
    scene=dict(
        xaxis=dict(
            title='TGD',
            ticktext=x_labels,  # Labels in reverse order
            tickvals=x_values,  # Numerical values in ascending order
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        yaxis=dict(
            title='Acne',
            ticktext=y_labels,  # Labels in correct order
            tickvals=y_values,  # Numerical values in ascending order
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        zaxis_title='Score',
        camera=dict(
            eye=dict(x=1.7, y=1.7, z=1.2)
        ),
        aspectratio=dict(x=1, y=1, z=0.8),
    ),
    width=1200,
    height=1000,
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='rgba(0, 0, 0, 0.5)',
        borderwidth=2,
        font=dict(
            size=14,
            color='black'
        ),
        itemsizing='constant',
        itemwidth=30,
        orientation="v",
        title=dict(
            text="Contraceptive Methods",
            font=dict(
                size=16,
                color='black'
            )
        )
    )
)

fig.show()

import copy
from functions_simulation_diff_weight_hor import *
import plotly.graph_objects as go
import numpy as np

# THIS WORKS
original_weight_condoms = [
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    3,
    1.5  # Gender dysphoria related to pregnancy (no/yes)
]
original_weight_internal_condoms = [
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)   
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    3,
    [-3, -2, -1, 1, 2, 3], # Vaginal Insertion
    [-15, -25, -50],  # Gender dysphoria related to vaginal insertion
    1.5 # Gender dysphoria related to pregnancy
]
original_weight_cervical_cap = [
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,        
    3,            # Maintenance (arr[2])
    [-3, -2, -1, 1, 2, 3],  # Vaginal Insertion (arr[3])
    [-3, -2, -1, 1, 2, 3],  # Seeking Consultation (arr[4])
    [-15, -25, -50],     # Gender Dysphoria Vaginal Insertion (arr[5])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[6])
]
original_weight_FAM = [
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,
    [-3, -2, -1, 1, 2, 3],  # Partner Willingness (arr[3])
    3,                    # Maintenance (arr[2])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[4])
]
original_weight_arm_implant = [
    [-3, -2, -1, 1, 2, 3],  # Pregnancy Prevention (arr[1])
    [-3, -2, -1, 1, 2, 3],  # Lessens Periods (arr[2])
    [3, 2, 1, -1, -2, -3],  # Maintains Weight (arr[3])
    3,                    # Maintenance (arr[4])
    [3, 3],                    # Hormones Used (arr[5])
    [-3, -2, -1, 1, 2, 3],  # Seeking consultation (arr[6])
    [-3, -2, -1, 1, 2, 3],  # Medical procedure (arr[7])
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

    3,
    
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

    3,
    
    # Gender Pregnancy (mild, moderate, severe)
    [-15, -25, -50]
    
]
original_weight_sterilization = [
    # Pregnancy Prevention (0-5)
    [-3, -2, -1, 1, 2, 3],
    
    # Lessens Periods (0-5)
    [-3, -2, -1, 1, 2, 3],

    3,
    
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
    [-15, -25, -60],  # Matches original top gender dysphoria scores
    # Top Surgery (index 20)
    -100,  # Matches original top surgery scores
    # BGDP (index 21)
    3,  # BGDP gives +3
    # GDVI (index 22)
    # GDP (index 23)
    1.5,  # Matches original GDP scores
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
    [-15, -25, -60],  # Weights for arr[8]
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
    [-15, -25, -60],  # Weights for arr[19]
    -100,  # Weights for arr[20]
    3,  # Weight for arr[21]
    1.5,  # Weight for arr[22]
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
    [-15, -25, -60],  # corresponding to mild, moderate, severe
    
    # Top Surgery (arr[20])
    -100,  # same as top dysphoria
    
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
    [-15, -25, -60],      # For arr[8] (no, mild, moderate, severe)
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
    [-15, -25, -60],      # For arr[19] (no, mild, moderate, severe)
    -100,      # For arr[20] (no, mild, moderate, severe)
    3,                      # For arr[21]
    1.5,                      # For arr[22]
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
    [-7.5, -12.5, -25, -15, -25, -60],  # [no, mild, moderate, severe]
    
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
    [3, 2, 1, -1, -2, -3],  # weights for arr[3]
    3,  # weight for arr[4] == "yearly"
    [3, 3],  # weights for arr[5]: ["p", "ep"]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[6]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[7]
    [-3, -2, -1, 1, 2, 3],  # weights for arr[8]
    [-15, -25, -60],  # weights for arr[9]: ["mild", "moderate", "severe"]
    [-7.5, -12.5, -25, -15, -25, -50],  # weights for arr[10] based on arr[9]
    [-7.5, -12.5, -25, -15, -25, -50],  # weights for arr[11] based on arr[10]
    -100,  # weight for arr[12] != "no"
    3,  # weight for arr[13] != "no"
    3,  # weight for arr[14] != "no"
    3,  # weight for arr[15] != "no"
    [-15, -25, -60],  # weights for arr[16]: ["mild", "moderate", "severe"]
    3  # weight for arr[17] != "no"
]

inputs = [
    ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'no', 'moderate', 'moderate', 'no', 'yes'],


     
]

def zero_zero(input_arr):

    weights_dict = {

        "condoms": copy.deepcopy(original_weight_condoms),
        "internal_condoms": copy.deepcopy(original_weight_internal_condoms),
        "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
        "fam": copy.deepcopy(original_weight_FAM),
        "copper_iud": copy.deepcopy(original_weight_copper_IUD),
        "sterilization": copy.deepcopy(original_weight_sterilization),
        "spermicide": copy.deepcopy(original_weight_spermicide),
        "withdrawal": copy.deepcopy(original_weight_withdrawl)
    
    }
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[7], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]

    condom_score = change_score_condoms(condom_arr, weights_dict['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, weights_dict['internal_condoms'])
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_dict['cervical_cap'])
    fam_score = change_fam(fam_arr, weights_dict['fam'])
    copper_iud_score = change_copper_iud(copper_iud_arr, weights_dict['copper_iud'])
    sterilization_score = change_score_sterilization(sterilization_arr, weights_dict['sterilization'])
    gel_score = change_score_gel(gel_arr, weights_dict['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, weights_dict['withdrawal'])

    return {
        "Condoms": condom_score,
        "Internal Condoms": internal_condom_score,
        "Cervical Cap": cervical_cap_score,
        "FAM": fam_score,
        "Copper IUD": copper_iud_score,
        "Sterilization": sterilization_score,
        "Spermicide": gel_score,
        "Withdrawal": withdrawal_score
    }

def pos_zero(input_arr, pos_acne):

    weights_dict = {
        "arm_implant": copy.deepcopy(original_weight_arm_implant),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
    }

    for method in weights_dict:
        if method == "arm_implant":
            weights_dict[method][-5] = pos_acne 
        elif method == "mini_pill":
            weights_dict[method][-8] = pos_acne 

    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]


    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])

    return {
        "Arm Implant": arm_implant_score,
        "Mini Pill": mini_pill_score
    }

def pos_neg(input_arr, pos_acne):

    weights_dict = {
        "ring": copy.deepcopy(original_weight_ring),
        "shot": copy.deepcopy(original_weight_shot),
    }

    for method in weights_dict:
        if method == "ring":
            weights_dict[method][-16] = pos_acne
        elif method == "shot":
            weights_dict[method][-16] = pos_acne
    
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
   
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])

    return {
        "Ring": ring_score,
        "Shot": shot_score
    }

def neg_zero(input_arr):

    weights_dict = {
        "hormonal_iud": copy.deepcopy(original_weight_hormonal_IUD)
    }

    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]

    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])

    return {
        "Hormonal IUD": hormonal_iud_score
    }

def neg_neg(input_arr):

    weights_dict = {
        "patch": copy.deepcopy(original_weight_patch),
        "combo_pill": copy.deepcopy(original_weight_combo_pill),
    }

    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])

    return {
        "Patch": patch_score,
        "Combo Pill": combo_pill_score
    }


# Scoring Condoms
condom_no = {} 
condoms_mild = {}
condoms_moderate = {}
condoms_severe = {}
condoms_3 = {}
condoms_21 = {}
condoms_42 = {}
condoms_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        condom_no["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condom_no["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condom_no["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condom_no["severe"] = zero_zero(arr)["Condoms"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        condoms_mild["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condoms_mild["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condoms_mild["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condoms_mild["severe"] = zero_zero(arr)["Condoms"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        condoms_moderate["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condoms_moderate["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condoms_moderate["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condoms_moderate["severe"] = zero_zero(arr)["Condoms"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        condoms_severe["no"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "mild":
        condoms_severe["mild"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "moderate":
        condoms_severe["moderate"] = zero_zero(arr)["Condoms"]
    elif arr[-6] == "severe":
        condoms_severe["severe"] = zero_zero(arr)["Condoms"]


condoms_3["3"] = zero_zero(inputs[0])["Condoms"]
condoms_3["21"] = zero_zero(inputs[0])["Condoms"]
condoms_3["42"] = zero_zero(inputs[0])["Condoms"]
condoms_3["60"] = zero_zero(inputs[0])["Condoms"]

condoms_21["3"] = zero_zero(inputs[0])["Condoms"]
condoms_21["21"] = zero_zero(inputs[0])["Condoms"]
condoms_21["42"] = zero_zero(inputs[0])["Condoms"]
condoms_21["60"] = zero_zero(inputs[0])["Condoms"]

condoms_42["3"] = zero_zero(inputs[0])["Condoms"]
condoms_42["21"] = zero_zero(inputs[0])["Condoms"]
condoms_42["42"] = zero_zero(inputs[0])["Condoms"]
condoms_42["60"] = zero_zero(inputs[0])["Condoms"]

condoms_60["3"] = zero_zero(inputs[0])["Condoms"]
condoms_60["21"] = zero_zero(inputs[0])["Condoms"]
condoms_60["42"] = zero_zero(inputs[0])["Condoms"]
condoms_60["60"] = zero_zero(inputs[0])["Condoms"]

# Internal Condoms
internal_condom_no = {}
internal_condom_mild = {}
internal_condom_moderate = {}
internal_condom_severe = {}
internal_condom_3 = {}
internal_condom_21 = {}
internal_condom_42 = {}
internal_condom_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        internal_condom_no["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_no["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_no["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_no["severe"] = zero_zero(arr)["Internal Condoms"]


for arr in inputs[4:8]:
    if arr[-6] == "no":
        internal_condom_mild["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_mild["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_mild["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_mild["severe"] = zero_zero(arr)["Internal Condoms"]


for arr in inputs[8:12]:
    if arr[-6] == "no":
        internal_condom_moderate["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_moderate["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_moderate["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_moderate["severe"] = zero_zero(arr)["Internal Condoms"]


for arr in inputs[12:16]:
    if arr[-6] == "no":
        internal_condom_severe["no"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "mild":
        internal_condom_severe["mild"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "moderate":
        internal_condom_severe["moderate"] = zero_zero(arr)["Internal Condoms"]
    elif arr[-6] == "severe":
        internal_condom_severe["severe"] = zero_zero(arr)["Internal Condoms"]


internal_condom_3["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_21["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_42["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_60["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["60"] = zero_zero(inputs[0])["Internal Condoms"]

# Cervical Cap
cervical_cap_no = {}
cervical_cap_mild = {}
cervical_cap_moderate = {}
cervical_cap_severe = {}
cervical_cap_3 = {}
cervical_cap_21 = {}
cervical_cap_42 = {}
cervical_cap_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        cervical_cap_no["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_no["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_no["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_no["severe"] = zero_zero(arr)["Cervical Cap"]


for arr in inputs[4:8]:
    if arr[-6] == "no":
        cervical_cap_mild["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_mild["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_mild["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_mild["severe"] = zero_zero(arr)["Cervical Cap"]


for arr in inputs[8:12]:
    if arr[-6] == "no":
        cervical_cap_moderate["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_moderate["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_moderate["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_moderate["severe"] = zero_zero(arr)["Cervical Cap"]


for arr in inputs[12:16]:
    if arr[-6] == "no":
        cervical_cap_severe["no"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "mild":
        cervical_cap_severe["mild"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "moderate":
        cervical_cap_severe["moderate"] = zero_zero(arr)["Cervical Cap"]
    elif arr[-6] == "severe":
        cervical_cap_severe["severe"] = zero_zero(arr)["Cervical Cap"]




cervical_cap_3["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_21["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_42["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_60["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["60"] = zero_zero(inputs[0])["Cervical Cap"]

# FAM
fam_no = {}
fam_mild = {}
fam_moderate = {}
fam_severe = {}
fam_3 = {}
fam_21 = {}
fam_42 = {}
fam_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        fam_no["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_no["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_no["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_no["severe"] = zero_zero(arr)["FAM"]


for arr in inputs[4:8]:
    if arr[-6] == "no":
        fam_mild["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_mild["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_mild["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_mild["severe"] = zero_zero(arr)["FAM"]


for arr in inputs[8:12]:
    if arr[-6] == "no":
        fam_moderate["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_moderate["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_moderate["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_moderate["severe"] = zero_zero(arr)["FAM"]


for arr in inputs[12:16]:
    if arr[-6] == "no":
        fam_severe["no"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "mild":
        fam_severe["mild"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "moderate":
        fam_severe["moderate"] = zero_zero(arr)["FAM"]
    elif arr[-6] == "severe":
        fam_severe["severe"] = zero_zero(arr)["FAM"]


fam_3["3"] = zero_zero(inputs[0])["FAM"]
fam_3["21"] = zero_zero(inputs[0])["FAM"]
fam_3["42"] = zero_zero(inputs[0])["FAM"]
fam_3["60"] = zero_zero(inputs[0])["FAM"]

fam_21["3"] = zero_zero(inputs[0])["FAM"]
fam_21["21"] = zero_zero(inputs[0])["FAM"]
fam_21["42"] = zero_zero(inputs[0])["FAM"]
fam_21["60"] = zero_zero(inputs[0])["FAM"]

fam_42["3"] = zero_zero(inputs[0])["FAM"]
fam_42["21"] = zero_zero(inputs[0])["FAM"]
fam_42["42"] = zero_zero(inputs[0])["FAM"]
fam_42["60"] = zero_zero(inputs[0])["FAM"]

fam_60["3"] = zero_zero(inputs[0])["FAM"]
fam_60["21"] = zero_zero(inputs[0])["FAM"]
fam_60["42"] = zero_zero(inputs[0])["FAM"]
fam_60["60"] = zero_zero(inputs[0])["FAM"]

# Copper IUD
copper_iud_no = {}
copper_iud_mild = {}
copper_iud_moderate = {}
copper_iud_severe = {}
copper_iud_3 = {}
copper_iud_21 = {}
copper_iud_42 = {}
copper_iud_60 = {}


for arr in inputs[0:4]:
    if arr[-6] == "no":
        copper_iud_no["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_no["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate":
        copper_iud_no["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_no["severe"] = zero_zero(arr)["Copper IUD"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        copper_iud_mild["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_mild["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate":
        copper_iud_mild["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_mild["severe"] = zero_zero(arr)["Copper IUD"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        copper_iud_moderate["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_moderate["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate": 
        copper_iud_moderate["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_moderate["severe"] = zero_zero(arr)["Copper IUD"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        copper_iud_severe["no"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "mild":
        copper_iud_severe["mild"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "moderate":
        copper_iud_severe["moderate"] = zero_zero(arr)["Copper IUD"]
    elif arr[-6] == "severe":
        copper_iud_severe["severe"] = zero_zero(arr)["Copper IUD"]

copper_iud_3["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_21["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_42["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_60["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["60"] = zero_zero(inputs[0])["Copper IUD"]

# Sterilization
sterilization_no = {}
sterilization_mild = {}
sterilization_moderate = {}
sterilization_severe = {}
sterilization_3 = {}
sterilization_21 = {}
sterilization_42 = {}
sterilization_60 = {} 

for arr in inputs[0:4]:
    if arr[-6] == "no":
        sterilization_no["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_no["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_no["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_no["severe"] = zero_zero(arr)["Sterilization"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        sterilization_mild["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_mild["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_mild["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_mild["severe"] = zero_zero(arr)["Sterilization"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        sterilization_moderate["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_moderate["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_moderate["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_moderate["severe"] = zero_zero(arr)["Sterilization"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        sterilization_severe["no"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "mild":
        sterilization_severe["mild"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "moderate":
        sterilization_severe["moderate"] = zero_zero(arr)["Sterilization"]
    elif arr[-6] == "severe":
        sterilization_severe["severe"] = zero_zero(arr)["Sterilization"]

sterilization_3["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_21["3"] = zero_zero(inputs[0])["Sterilization"]    
sterilization_21["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_42["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_60["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["60"] = zero_zero(inputs[0])["Sterilization"]

# Spermicide
spermicide_no = {}
spermicide_mild = {}
spermicide_moderate = {}
spermicide_severe = {}
spermicide_3 = {}
spermicide_21 = {}
spermicide_42 = {}
spermicide_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        spermicide_no["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_no["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_no["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_no["severe"] = zero_zero(arr)["Spermicide"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        spermicide_mild["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_mild["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_mild["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_mild["severe"] = zero_zero(arr)["Spermicide"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        spermicide_moderate["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_moderate["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_moderate["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_moderate["severe"] = zero_zero(arr)["Spermicide"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        spermicide_severe["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "mild":
        spermicide_severe["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "moderate":
        spermicide_severe["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-6] == "severe":
        spermicide_severe["severe"] = zero_zero(arr)["Spermicide"]

spermicide_3["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_21["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_42["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_60["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["60"] = zero_zero(inputs[0])["Spermicide"]

# Withdrawal
withdrawal_no = {}
withdrawal_mild = {}
withdrawal_moderate = {}
withdrawal_severe = {}
withdrawal_3 = {}
withdrawal_21 = {}
withdrawal_42 = {}
withdrawal_60 = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        withdrawal_no["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_no["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_no["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_no["severe"] = zero_zero(arr)["Withdrawal"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        withdrawal_mild["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_mild["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_mild["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_mild["severe"] = zero_zero(arr)["Withdrawal"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        withdrawal_moderate["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_moderate["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_moderate["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_moderate["severe"] = zero_zero(arr)["Withdrawal"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        withdrawal_severe["no"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "mild":
        withdrawal_severe["mild"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "moderate":
        withdrawal_severe["moderate"] = zero_zero(arr)["Withdrawal"]
    elif arr[-6] == "severe":
        withdrawal_severe["severe"] = zero_zero(arr)["Withdrawal"]

withdrawal_3["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["60"] = zero_zero(inputs[0])["Withdrawal"]

withdrawal_21["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["60"] = zero_zero(inputs[0])["Withdrawal"]

withdrawal_42["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["60"] = zero_zero(inputs[0])["Withdrawal"]

withdrawal_60["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["60"] = zero_zero(inputs[0])["Withdrawal"]

# Arm Implant

arm_implant_3 = {}
arm_implant_21 = {}
arm_implant_42 = {}
arm_implant_60 = {}


arr_arm = inputs[5]
arm_implant_3["3"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["21"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["42"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["60"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["no"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["mild"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["moderate"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["severe"] = pos_zero(arr_arm, 3)["Arm Implant"]

arm_implant_21["3"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["21"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["42"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["60"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["no"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["mild"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["moderate"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["severe"] = pos_zero(arr_arm, 21)["Arm Implant"]

arm_implant_42["3"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["21"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["42"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["60"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["no"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["mild"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["moderate"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["severe"] = pos_zero(arr_arm, 42)["Arm Implant"]

arm_implant_60["3"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["21"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["42"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["60"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["no"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["mild"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["moderate"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["severe"] = pos_zero(arr_arm, 60)["Arm Implant"]

    
# Mini Pill

mini_pill_3 = {}
mini_pill_21 = {}
mini_pill_42 = {}
mini_pill_60 = {}

arr_mini = inputs[6]
mini_pill_3["3"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["21"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["42"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["60"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["no"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["mild"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["moderate"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["severe"] = pos_zero(arr_mini, 3)["Mini Pill"]

mini_pill_21["3"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["21"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["42"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["60"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["no"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["mild"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["moderate"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["severe"] = pos_zero(arr_mini, 21)["Mini Pill"]

mini_pill_42["3"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["21"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["42"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["60"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["no"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["mild"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["moderate"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["severe"] = pos_zero(arr_mini, 42)["Mini Pill"]

mini_pill_60["3"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["21"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["42"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["60"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["no"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["mild"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["moderate"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["severe"] = pos_zero(arr_mini, 60)["Mini Pill"]

# Hormonal IUD
hormonal_iud_no = {}
hormonal_iud_mild = {}
hormonal_iud_moderate = {}
hormonal_iud_severe = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        hormonal_iud_no["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_no["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_no["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_no["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["60"] = neg_zero(arr)["Hormonal IUD"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        hormonal_iud_mild["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_mild["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_mild["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_mild["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["60"] = neg_zero(arr)["Hormonal IUD"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        hormonal_iud_moderate["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_moderate["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_moderate["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_moderate["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["60"] = neg_zero(arr)["Hormonal IUD"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        hormonal_iud_severe["no"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "mild":
        hormonal_iud_severe["mild"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "moderate":
        hormonal_iud_severe["moderate"] = neg_zero(arr)["Hormonal IUD"]
    elif arr[-6] == "severe":
        hormonal_iud_severe["severe"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["3"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["60"] = neg_zero(arr)["Hormonal IUD"]

# Ring
ring_3 = {}
ring_21 = {}
ring_42 = {}
ring_60 = {}

for arr in inputs[4:8]:
    if arr[-6] == "no":
        ring_3["no"] = pos_neg(arr, 3)["Ring"]
        ring_21["no"] = pos_neg(arr, 21)["Ring"]
        ring_42["no"] = pos_neg(arr, 42)["Ring"]
        ring_60["no"] = pos_neg(arr, 60)["Ring"]
    elif arr[-6] == "mild":
        ring_3["mild"] = pos_neg(arr, 3)["Ring"]
        ring_21["mild"] = pos_neg(arr, 21)["Ring"]
        ring_42["mild"] = pos_neg(arr, 42)["Ring"]
        ring_60["mild"] = pos_neg(arr, 60)["Ring"]
    elif arr[-6] == "moderate":
        ring_3["moderate"] = pos_neg(arr, 3)["Ring"]
        ring_21["moderate"] = pos_neg(arr, 21)["Ring"]
        ring_42["moderate"] = pos_neg(arr, 42)["Ring"]
        ring_60["moderate"] = pos_neg(arr, 60)["Ring"]
    elif arr[-6] == "severe":
        ring_3["severe"] = pos_neg(arr, 3)["Ring"]
        ring_21["severe"] = pos_neg(arr, 21)["Ring"]
        ring_42["severe"] = pos_neg(arr, 42)["Ring"]
        ring_60["severe"] = pos_neg(arr, 60)["Ring"]

# Shot
shot_3 = {}
shot_21 = {}
shot_42 = {}
shot_60 = {}

for arr in inputs[4:8]:
    if arr[-6] == "no":
        shot_3["no"] = pos_neg(arr, 3)["Shot"]
        shot_21["no"] = pos_neg(arr, 21)["Shot"]
        shot_42["no"] = pos_neg(arr, 42)["Shot"]
        shot_60["no"] = pos_neg(arr, 60)["Shot"]
    elif arr[-6] == "mild":
        shot_3["mild"] = pos_neg(arr, 3)["Shot"]
        shot_21["mild"] = pos_neg(arr, 21)["Shot"]
        shot_42["mild"] = pos_neg(arr, 42)["Shot"]
        shot_60["mild"] = pos_neg(arr, 60)["Shot"]
    elif arr[-6] == "moderate":
        shot_3["moderate"] = pos_neg(arr, 3)["Shot"]
        shot_21["moderate"] = pos_neg(arr, 21)["Shot"]
        shot_42["moderate"] = pos_neg(arr, 42)["Shot"]
        shot_60["moderate"] = pos_neg(arr, 60)["Shot"]
    elif arr[-6] == "severe":
        shot_3["severe"] = pos_neg(arr, 3)["Shot"]
        shot_21["severe"] = pos_neg(arr, 21)["Shot"]
        shot_42["severe"] = pos_neg(arr, 42)["Shot"]
        shot_60["severe"] = pos_neg(arr, 60)["Shot"]


# Patch
patch_no = {}
patch_mild = {}
patch_moderate = {}
patch_severe = {}

for arr in inputs[0:4]:
    if arr[-6] == "no":
        patch_no["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_no["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_no["moderate"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "severe":
        patch_no["severe"] = neg_neg(arr)["Patch"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        patch_mild["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_mild["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_mild["moderate"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "severe":
        patch_mild["severe"] = neg_neg(arr)["Patch"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        patch_moderate["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_moderate["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_moderate["moderate"] = neg_neg(arr)["Patch"]  
    elif arr[-6] == "severe":
        patch_moderate["severe"] = neg_neg(arr)["Patch"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        patch_severe["no"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "mild":
        patch_severe["mild"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "moderate":
        patch_severe["moderate"] = neg_neg(arr)["Patch"]
    elif arr[-6] == "severe":
        patch_severe["severe"] = neg_neg(arr)["Patch"]
        
# Combo Pill
combo_no = {}
combo_mild = {}
combo_moderate = {}
combo_severe = {}


for arr in inputs[0:4]:
    if arr[-6] == "no":
        combo_no["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_no["mild"] = neg_neg(arr)["Combo Pill"]   
    elif arr[-6] == "moderate":
        combo_no["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_no["severe"] = neg_neg(arr)["Combo Pill"]

for arr in inputs[4:8]:
    if arr[-6] == "no":
        combo_mild["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_mild["mild"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "moderate":
        combo_mild["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_mild["severe"] = neg_neg(arr)["Combo Pill"]

for arr in inputs[8:12]:
    if arr[-6] == "no":
        combo_moderate["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_moderate["mild"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "moderate":
        combo_moderate["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_moderate["severe"] = neg_neg(arr)["Combo Pill"]

for arr in inputs[12:16]:
    if arr[-6] == "no":
        combo_severe["no"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "mild":
        combo_severe["mild"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "moderate":
        combo_severe["moderate"] = neg_neg(arr)["Combo Pill"]
    elif arr[-6] == "severe":
        combo_severe["severe"] = neg_neg(arr)["Combo Pill"]
        
 

        
# After all the dictionaries are populated, add visualization code:

import plotly.graph_objects as go
import numpy as np
# Create matrices from the actual dictionaries
def create_full_matrix(method_dicts):
    no_dict, mild_dict, mod_dict, sev_dict, t3_dict, t21_dict, t42_dict, t60_dict = method_dicts

    return np.array([
        [sev_dict['severe'], sev_dict['moderate'], sev_dict['mild'], sev_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [mod_dict['severe'], mod_dict['moderate'], mod_dict['mild'], mod_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [mild_dict['severe'], mild_dict['moderate'], mild_dict['mild'], mild_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [no_dict['severe'], no_dict['moderate'], no_dict['mild'], no_dict['no'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['21'], t3_dict['42'], t3_dict['60']],
        [t21_dict['3'], t21_dict['3'], t21_dict['3'], t21_dict['3'], t21_dict['3'], t21_dict['21'], t21_dict['42'], t21_dict['60']],
        [t42_dict['3'], t42_dict['3'], t42_dict['3'], t42_dict['3'], t42_dict['3'], t42_dict['21'], t42_dict['42'], t42_dict['60']],
        [t60_dict['3'], t60_dict['3'], t60_dict['3'], t60_dict['3'], t60_dict['3'], t60_dict['21'], t60_dict['42'], t60_dict['60']],
    ])
    
# Create all matrices
z_condoms = create_full_matrix([condom_no, condoms_mild, condoms_moderate, condoms_severe, condoms_3, condoms_21, condoms_42, condoms_60])
z_internal_condoms = create_full_matrix([internal_condom_no, internal_condom_mild, internal_condom_moderate, internal_condom_severe, internal_condom_3, internal_condom_21, internal_condom_42, internal_condom_60])
z_cervical_cap = create_full_matrix([cervical_cap_no, cervical_cap_mild, cervical_cap_moderate, cervical_cap_severe, cervical_cap_3, cervical_cap_21, cervical_cap_42, cervical_cap_60])
z_fam = create_full_matrix([fam_no, fam_mild, fam_moderate, fam_severe, fam_3, fam_21, fam_42, fam_60])
z_copper_iud = create_full_matrix([copper_iud_no, copper_iud_mild, copper_iud_moderate, copper_iud_severe, copper_iud_3, copper_iud_21, copper_iud_42, copper_iud_60])
z_sterilization = create_full_matrix([sterilization_no, sterilization_mild, sterilization_moderate, sterilization_severe, sterilization_3, sterilization_21, sterilization_42, sterilization_60])
z_spermicide = create_full_matrix([spermicide_no, spermicide_mild, spermicide_moderate, spermicide_severe, spermicide_3, spermicide_21, spermicide_42, spermicide_60])
z_withdrawal = create_full_matrix([withdrawal_no, withdrawal_mild, withdrawal_moderate, withdrawal_severe, withdrawal_3, withdrawal_21, withdrawal_42, withdrawal_60])


'''
z_arm_implant = np.array([
    [arm_implant_3['60'], arm_implant_3['42'], arm_implant_3['21'],arm_implant_3['3'], arm_implant_3['no'], arm_implant_3['mild'], arm_implant_3['moderate'], arm_implant_3['severe']],
    [arm_implant_21['60'], arm_implant_21['42'], arm_implant_21['21'], arm_implant_21['3'] ,arm_implant_21['no'], arm_implant_21['mild'], arm_implant_21['moderate'], arm_implant_21['severe']],
    [arm_implant_42['60'], arm_implant_42['42'], arm_implant_42['21'], arm_implant_42['3'], arm_implant_42['no'], arm_implant_42['mild'], arm_implant_42['moderate'], arm_implant_42['severe']],
    [arm_implant_60['60'], arm_implant_60['42'], arm_implant_60['21'], arm_implant_60['3'], arm_implant_60['no'], arm_implant_60['mild'], arm_implant_60['moderate'], arm_implant_60['severe']],
])
'''
z_arm_implant = np.array([
    [arm_implant_3['severe'], arm_implant_3['moderate'], arm_implant_3['mild'], arm_implant_3['no'], arm_implant_3['3'], arm_implant_3['21'], arm_implant_3['42'], arm_implant_3['60']],
    [arm_implant_21['severe'], arm_implant_21['moderate'], arm_implant_21['mild'], arm_implant_21['no'], arm_implant_21['3'], arm_implant_21['21'], arm_implant_21['42'], arm_implant_21['60']],
    [arm_implant_42['severe'], arm_implant_42['moderate'], arm_implant_42['mild'], arm_implant_42['no'], arm_implant_42['3'], arm_implant_42['21'], arm_implant_42['42'], arm_implant_42['60']],
    [arm_implant_60['severe'], arm_implant_60['moderate'], arm_implant_60['mild'], arm_implant_60['no'], arm_implant_60['3'], arm_implant_60['21'], arm_implant_60['42'], arm_implant_60['60']],
])

'''
z_mini = np.array([
    [mini_pill_3['3'], mini_pill_3['21'], mini_pill_3['42'], mini_pill_3['3'], mini_pill_3['no'], mini_pill_3['mild'], mini_pill_3['moderate'], mini_pill_3['severe']],
    [mini_pill_21['3'], mini_pill_21['21'], mini_pill_21['42'], mini_pill_21['3'], mini_pill_21['no'], mini_pill_21['mild'], mini_pill_21['moderate'], mini_pill_21['severe']],
    [mini_pill_42['3'], mini_pill_42['21'], mini_pill_42['42'], mini_pill_42['3'], mini_pill_42['no'], mini_pill_42['mild'], mini_pill_42['moderate'], mini_pill_42['severe']],
    [mini_pill_60['3'], mini_pill_60['21'], mini_pill_60['42'], mini_pill_60['3'], mini_pill_60['no'], mini_pill_60['mild'], mini_pill_60['moderate'], mini_pill_60['severe']],
])
'''
z_mini = np.array([
    [mini_pill_3['severe'], mini_pill_3['moderate'], mini_pill_3['mild'], mini_pill_3['no'], mini_pill_3['3'], mini_pill_3['21'], mini_pill_3['42'], mini_pill_3['60']],
    [mini_pill_21['severe'], mini_pill_21['moderate'], mini_pill_21['mild'], mini_pill_21['no'], mini_pill_21['3'], mini_pill_21['21'], mini_pill_21['42'], mini_pill_21['60']],
    [mini_pill_42['severe'], mini_pill_42['moderate'], mini_pill_42['mild'], mini_pill_42['no'], mini_pill_42['3'], mini_pill_42['21'], mini_pill_42['42'], mini_pill_42['60']],
    [mini_pill_60['severe'], mini_pill_60['moderate'], mini_pill_60['mild'], mini_pill_60['no'], mini_pill_60['3'], mini_pill_60['21'], mini_pill_60['42'], mini_pill_60['60']],
])

'''
z_hormonal_iud = np.array([
    [hormonal_iud_severe['60'], hormonal_iud_severe['42'], hormonal_iud_severe['21'], hormonal_iud_severe['3'], hormonal_iud_severe['no'], hormonal_iud_severe['mild'], hormonal_iud_severe['moderate'], hormonal_iud_severe['severe']],
    [hormonal_iud_moderate['60'], hormonal_iud_moderate['42'], hormonal_iud_moderate['21'], hormonal_iud_moderate['3'], hormonal_iud_moderate['no'], hormonal_iud_moderate['mild'], hormonal_iud_moderate['moderate'], hormonal_iud_moderate['severe']],
    [hormonal_iud_mild['60'], hormonal_iud_mild['42'], hormonal_iud_mild['21'], hormonal_iud_mild['3'], hormonal_iud_mild['no'], hormonal_iud_mild['mild'], hormonal_iud_mild['moderate'], hormonal_iud_mild['severe']],
    [hormonal_iud_no['60'], hormonal_iud_no['42'], hormonal_iud_no['21'], hormonal_iud_no['3'], hormonal_iud_no['no'], hormonal_iud_no['mild'], hormonal_iud_no['moderate'], hormonal_iud_no['severe']],
])
'''
z_hormonal_iud = np.array([
    [hormonal_iud_severe['severe'], hormonal_iud_severe['moderate'], hormonal_iud_severe['mild'], hormonal_iud_severe['no'], hormonal_iud_severe['3'], hormonal_iud_severe['21'], hormonal_iud_severe['42'], hormonal_iud_severe['60']],
    [hormonal_iud_moderate['severe'], hormonal_iud_moderate['moderate'], hormonal_iud_moderate['mild'], hormonal_iud_moderate['no'], hormonal_iud_moderate['3'], hormonal_iud_moderate['21'], hormonal_iud_moderate['42'], hormonal_iud_moderate['60']],
    [hormonal_iud_mild['severe'], hormonal_iud_mild['moderate'], hormonal_iud_mild['mild'], hormonal_iud_mild['no'], hormonal_iud_mild['3'], hormonal_iud_mild['21'], hormonal_iud_mild['42'], hormonal_iud_mild['60']],
    [hormonal_iud_no['severe'], hormonal_iud_no['moderate'], hormonal_iud_no['mild'], hormonal_iud_no['no'], hormonal_iud_no['3'], hormonal_iud_no['21'], hormonal_iud_no['42'], hormonal_iud_no['60']],
])


z_ring = np.array([
    [ring_3['no'], ring_3['mild'], ring_3['moderate'], ring_3['severe']],
    [ring_21['no'], ring_21['mild'], ring_21['moderate'], ring_21['severe']],
    [ring_42['no'], ring_42['mild'], ring_42['moderate'], ring_42['severe']],
    [ring_60['no'], ring_60['mild'], ring_60['moderate'], ring_60['severe']]
])

z_ring = np.array([
    [ring_3['severe'], ring_3['moderate'], ring_3['mild'], ring_3['no']],
    [ring_21['severe'], ring_21['moderate'], ring_21['mild'], ring_21['no']],
    [ring_42['severe'], ring_42['moderate'], ring_42['mild'], ring_42['no']],
    [ring_60['severe'], ring_60['moderate'], ring_60['mild'], ring_60['no']]
])
'''
# Create shot matrix (4x3 matrix)
z_shot = np.array([
    [shot_3['no'], shot_3['mild'], shot_3['moderate'], shot_3['severe']],
    [shot_21['no'], shot_21['mild'], shot_21['moderate'], shot_21['severe']],
    [shot_42['no'], shot_42['mild'], shot_42['moderate'], shot_42['severe']],
    [shot_60['no'], shot_60['mild'], shot_60['moderate'], shot_60['severe']]
])
'''
z_shot = np.array([
    [shot_3['severe'], shot_3['moderate'], shot_3['mild'], shot_3['no']],
    [shot_21['severe'], shot_21['moderate'], shot_21['mild'], shot_21['no']],
    [shot_42['severe'], shot_42['moderate'], shot_42['mild'], shot_42['no']],
    [shot_60['severe'], shot_60['moderate'], shot_60['mild'], shot_60['no']]
])
# Create patch matrix (4x4 matrix)

z_patch = np.array([
    [patch_severe['no'], patch_severe['mild'], patch_severe['moderate'], patch_severe['severe']],
    [patch_moderate['no'], patch_moderate['mild'], patch_moderate['moderate'], patch_moderate['severe']],
    [patch_mild['no'], patch_mild['mild'], patch_mild['moderate'], patch_mild['severe']],
    [patch_no['no'], patch_no['mild'], patch_no['moderate'], patch_no['severe']],
])

z_patch = np.array([
    [patch_severe['severe'], patch_severe['moderate'], patch_severe['mild'], patch_severe['no']],
    [patch_moderate['severe'], patch_moderate['moderate'], patch_moderate['mild'], patch_moderate['no']],
    [patch_mild['severe'], patch_mild['moderate'], patch_mild['mild'], patch_mild['no']],
    [patch_no['severe'], patch_no['moderate'], patch_no['mild'], patch_no['no']],
])

# Add patch surface with its specific axes

z_combo_pill = np.array([
    [combo_severe['no'], combo_severe['mild'], combo_severe['moderate'], combo_severe['severe']],
    [combo_moderate['no'], combo_moderate['mild'], combo_moderate['moderate'], combo_moderate['severe']],
    [combo_mild['no'], combo_mild['mild'], combo_mild['moderate'], combo_mild['severe']],
    [combo_no['no'], combo_no['mild'], combo_no['moderate'], combo_no['severe']],
])
z_combo_pill = np.array([
    [combo_severe['severe'], combo_severe['moderate'], combo_severe['mild'], combo_severe['no']],
    [combo_moderate['severe'], combo_moderate['moderate'], combo_moderate['mild'], combo_moderate['no']],
    [combo_mild['severe'], combo_mild['moderate'], combo_mild['mild'], combo_mild['no']],
    [combo_no['severe'], combo_no['moderate'], combo_no['mild'], combo_no['no']],
])
# Define distinct colors
distinct_colors = [
    '#FF0000',  # Red
    '#0000FF',  # Blue
    '#FFD700',  # Gold
    '#FF1493',  # Deep Pink
    '#00FF00',  # Lime
    '#8B008B',  # Dark Magenta
    '#FF8C00',  # Dark Orange
    '#00FFFF',  # Cyan
    '#800000',  # Maroon
    '#000080',  # Navy
    '#808000',  # Olive
    '#FF00FF',  # Magenta
    '#008080',  # Teal
    '#FFA500',  # Orange
    '#4B0082'   # Indigo
]
#x_full = ['60', '42', '21', '3', '0', '-15', '-25', '-50']
#y_full = ['-50', '-25', '-15', '0', '3', '21', '42', '60']

x_full = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
y_full = ['-60', '-25', '-15', '0', '3', '21', '42', '60']

x_partial = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
#y_partial = ['-50', '-25', '-15', '0', '3', '21', '42', '60']
y_partial = ['3', '21', '42', '60']

x_partial_mini = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
y_partial_mini = ['3', '21', '42', '60']

x_hormonal = ['-60', '-25', '-15', '0', '3', '21', '42', '60']
y_hormonal = ['-60', '-25', '-15', '0']

x_ring_shot = ['-60', '-25', '-15', '0']
y_ring_shot = ['3', '21', '42', '60']

x_patch_combo = ['-60', '-25', '-15', '0']
y_patch_combo = ['-60', '-25', '-15', '0']
severity_map = {
    'severe': -60,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [3, 21, 42, 60]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-60", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values] # Include 0 for continuity
all_y_values = negative_y_values + positive_values[1:]

# Create figure
fig = go.Figure()


fig.add_trace(go.Surface(
    x=x_patch_combo,
    y=y_patch_combo,
    z=z_patch,
    name='Patch',
    colorscale=[[0, distinct_colors[13]], [1, distinct_colors[13]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Patch',
    hoverinfo='name+z'
))

# Add combo pill surface
fig.add_trace(go.Surface(
    x=x_patch_combo,
    y=y_patch_combo,
    z=z_combo_pill,
    name='Combo Pill',
    colorscale=[[0, distinct_colors[14]], [1, distinct_colors[14]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Combo Pill',
    hoverinfo='name+z'
))

# Add ring surface with its specific axes

fig.add_trace(go.Surface(
    x=x_ring_shot,
    y=y_ring_shot,
    z=z_ring,
    name='Ring',
    colorscale=[[0, distinct_colors[11]], [1, distinct_colors[11]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Ring',
    hoverinfo='name+z'
))

# Add shot surface
fig.add_trace(go.Surface(
    x=x_ring_shot,
    y=y_ring_shot,
    z=z_shot,
    name='Shot',
    colorscale=[[0, distinct_colors[12]], [1, distinct_colors[12]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Shot',
    hoverinfo='name+z'
))


# Add hormonal IUD surface with its specific axes
#y_hormonal = ['no', 'mild', 'moderate', 'severe']


fig.add_trace(go.Surface(
    x=x_hormonal,
    y=y_hormonal,
    z=z_hormonal_iud,
    name='Hormonal IUD',
    colorscale=[[0, distinct_colors[10]], [1, distinct_colors[10]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Hormonal IUD',
    hoverinfo='name+z'
))

# Add mini pill surface
fig.add_trace(go.Surface(
    x=x_partial_mini,
    y=y_partial_mini,
    z=z_mini,
    name='Mini Pill',
    colorscale=[[0, distinct_colors[9]], [1, distinct_colors[9]]],
    showscale=False,
    opacity=0.7,
    showlegend=True,
    legendgroup='Mini Pill',
    hoverinfo='name+z'
))


# Define consistent axis labels
# Update the surfaces list to use consistent axis definitions

import numpy as np
import plotly.graph_objects as go


'''
# Define the numerical values for the labels (in ascending order)
x_values = [60, 25, 10, -10, -13, -27, -42, -60]  # Ascending order
#x_labels = [60, 42, 21, 3, 0, -15, -25, -50]  # Reverse order for display
x_labels = [-60, -25, -15, 0, 3, 21, 42, 60]  # Correct order for display
y_values = [-60, -25, -10, 10, 13, 27, 42, 60]  # Ascending order
y_labels = [-60, -25, -15, 0, 3, 21, 42, 60]  # Correct order for display
# Define the numerical values for the labels (in ascending order)
 # Correct order for display
'''
x_values = [60, 25, 15, 0, -3, -21, -42, -60]  # Ascending order
#x_labels = [60, 42, 21, 3, 0, -15, -25, -50]  # Reverse order for display
x_labels = [-60, -25, -15, 0, 3, 21, 42, 60]  # Correct order for display
y_values = [-60, -25, -15, 0, 3, 21, 42, 60]  # Ascending order
y_labels = [-60, -25, -15, 0, 3, 21, 42, 60] 
# Update the surfaces list to use numerical values for x and y
surfaces = [
    ('Condom', z_condoms, x_values, y_values),
    ('Internal Condom', z_internal_condoms, x_values, y_values),
    ('Cervical Cap', z_cervical_cap, x_values, y_values),
    ('FAM', z_fam, x_values, y_values),
    ('Copper IUD', z_copper_iud, x_values, y_values),
    ('Sterilization', z_sterilization, x_values, y_values),
    ('Gel', z_spermicide, x_values, y_values),
    ('Withdrawal', z_withdrawal, x_values, y_values),
    ('Arm Implant', z_arm_implant, x_values, y_partial_mini),
    ('Mini Pill', z_mini, x_values, y_partial_mini),
    ('Hormonal IUD', z_hormonal_iud, x_values, y_values),
    ('Ring', z_ring, x_values, y_ring_shot),
    ('Shot', z_shot, x_values, y_ring_shot),
    ('Patch', z_patch, x_values, y_values),
    ('Combo Pill', z_combo_pill, x_values, y_values),
]
contraceptive_colors = {
    "Hormonal IUD": '#FF0000',  # Red
    "Patch": '#0000FF',         # Blue
    "Combo Pill": '#FFD700',    # Gold
    "Arm Implant": '#FF1493',   # Deep Pink
    "Mini Pill": '#00FF00',     # Lime
    "Ring": '#8B008B',          # Dark Magenta
    "Shot": '#FF8C00',          # Dark Orange
    "Condom": '#00FFFF',        # Cyan
    "Internal Condom": '#800000',# Maroon
    "Cervical Cap": '#000080',  # Navy
    "FAM": '#808000',           # Olive
    "Copper IUD": '#FF00FF',    # Magenta
    "Sterilization": '#008080', # Teal
    "Gel": '#FFA500',           # Orange
    "Withdrawal": '#4B0082'     # Indigo
}
# Create figure
fig = go.Figure()

# Add all surfaces with consistent axis definitions
for i, (name, z, x, y) in enumerate(surfaces):
    color = contraceptive_colors[name]
    fig.add_trace(go.Surface(
        x=x,  # Use ascending numerical values for spacing
        y=y,  # Use ascending numerical values for spacing
        z=z,
        name=name,
        colorscale=[[0, color], [1, color]],
        showscale=False,
        opacity=0.7,
        showlegend=True,
        legendgroup=name,
        hoverinfo='name+z'
    ))

# Update layout with improved legend and accurate axis labels
fig.update_layout(
    title='Contraceptive Scores across weights for Acne and Top Gender Dysphoria',
    scene=dict(
        xaxis=dict(
            title='Top Gender Dysphoria',
            ticktext=x_labels,  # Labels in reverse order
            tickvals=x_values,  # Numerical values in ascending order
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        yaxis=dict(
            title='Acne',
            ticktext=y_labels,  # Labels in correct order
            tickvals=y_values,  # Numerical values in ascending order
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        zaxis_title='Contraceptive Score',
        camera=dict(
            eye=dict(x=1.7, y=1.7, z=1.2)
        ),
        aspectratio=dict(x=1, y=1, z=0.8),
    ),
    width=1200,
    height=1000,
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='rgba(0, 0, 0, 0.5)',
        borderwidth=2,
        font=dict(
            size=14,
            color='black'
        ),
        itemsizing='constant',
        itemwidth=30,
        orientation="v",
        title=dict(
            text="Methods",
            font=dict(
                size=16,
                color='black'
            )
        )
    )
)

fig.show()
