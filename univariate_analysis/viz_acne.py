import pandas as pd
import copy
import matplotlib.pyplot as plt
from functions_simulation_diff_weight import *
import csv

# Input data
inputs = [
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
]

# Define original weights (example values, replace with actual weights)
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
    [3, 2, 1, -1, -2, -3],  # weights for arr[3]
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



inputs_2 = [
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ]
"""
APPROACH:

1) CREATE A FUNCTION FOR POSTIVE CORRELATIONS. THE FUNCTION WILL RETURN THE RESULTS OF POSITIVE CONTRACEPTIVE ON DIFFERENT WEIGHTS
2) CREATE A FUNCTION FOR NEGATIVE CORRELATIONS. THE FUNCTION WILL RETURN THE RESULTS OF NEGAVTIVE / ZERO CONTRACEPTIVE ON 
MILF/MODERATE/SEVERE
3) CREATE A PLOT BASED ON THAT
"""

def calculate_scores_negative(input_arr):
    weights_negative = [-15, -25, -50]
    weights_dict = {
            'hormonal_iud': copy.deepcopy(original_weight_hormonal_IUD),
            'patch': copy.deepcopy(original_weight_patch),
            'combo_pill': copy.deepcopy(original_weight_combo_pill),
        }
    '''
    for method in weights_dict:
            if method == 'hormonal_iud':
                weights_dict[method][8] = weights_negative
            elif method == 'patch':
                weights_dict[method][7] = weights_negative
            elif method == 'combo_pill':
                weights_dict[method][7] = weights_negative
        '''
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
       # Calculate scores using the updated weights
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    contraceptive_scores = {
        "hormonal_IUD": hormonal_iud_score,
        "patch": patch_score,
        "combo_pill": combo_pill_score,
    }
    return contraceptive_scores

def calculate_scores_positive(input_arr, positive_weights):
    weights_dict = {
        "arm_implant": copy.deepcopy(original_weight_arm_implant),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
        "ring": copy.deepcopy(original_weight_ring),
        "shot": copy.deepcopy(original_weight_shot)
    }

    for method in weights_dict:
            if method == 'arm_implant':
                weights_dict[method][7] = positive_weights
            elif method == 'mini_pill':
                weights_dict[method][7] = positive_weights
            elif method == 'ring':
                weights_dict[method][8] = positive_weights
            elif method == 'shot':
                weights_dict[method][7] = positive_weights
        
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    # Calculate scores using the updated weights
    
    contraceptive_scores = {
    "arm_implant": arm_implant_score,
    "mini_pill": mini_pill_score,
    "ring": ring_score,
    "shot": shot_score 
        }
    return contraceptive_scores

def calculate_scores_zero(input_arr):

    original_weights = {
        "condoms": copy.deepcopy(original_weight_condoms),
        'copper_iud': copy.deepcopy(original_weight_copper_IUD),
        'sterilization': copy.deepcopy(original_weight_sterilization),
        'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
        "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
        "FAM": copy.deepcopy(original_weight_FAM),
        "spermicide": copy.deepcopy(original_weight_spermicide),
        "withdrawal": copy.deepcopy(original_weight_withdrawl)
        }
    
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    # Calculate scores using the updated weights
    condom_score = change_score_condoms(condom_arr, original_weights['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, original_weights['internal_condoms'])
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, original_weights['cervical_cap'])
    fam_score = change_fam(fam_arr, original_weights['FAM'])
    copper_iud_score = change_copper_iud(copper_iud_arr, original_weights['copper_iud'])
    sterilization_score = change_score_sterilization(sterilization_arr, original_weights['sterilization'])
    gel_score = change_score_gel(gel_arr, original_weights['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, original_weights['withdrawal'])

    contraceptive_scores = {
        "Condom": condom_score,
        "Internal Condom": internal_condom_score,
        "Cervical Cap": cervical_cap_score,
        "FAM": fam_score,
        "Copper IUD": copper_iud_score,
        "sterilization": sterilization_score,
        "gel": gel_score,
        "Withdrawal": withdrawal_score
    }
    return contraceptive_scores


neg_scores = {

}
for arr in inputs:
    score_neg = calculate_scores_negative(arr)
    if arr[11] == "no":
        neg_scores["no"] = score_neg
    elif arr[11] == "mild":
        neg_scores["mild"] = score_neg
    elif arr[11] == "moderate":
        neg_scores["moderate"] = score_neg
    elif arr[11] == "severe":
        neg_scores["severe"] = score_neg

n_pos = 21

pos_scores = {

}

for i in range(1, n_pos):
    positive_weight = 3 * i
    for arr in inputs:
        score_pos = calculate_scores_positive(arr, positive_weight)
        pos_scores[f"{positive_weight}"] = score_pos

zero_scores = {

}

for i in range(1, 25):
    for arr in inputs:
        zero_scores[f"{i}"] = calculate_scores_zero(arr)




# Plotting the graph
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

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
'''
def plot_contraceptive_scores(neg_scores, pos_scores, zero_scores):
    # Set up the plot
    plt.figure(figsize=(12, 8))
    
    # Define weight labels and multipliers
    #weight_labels = ['severe', 'moderate', 'mild', 'no'] + [str(i) for i in range(3, 63, 3)]
    weight_labels = ['-50', '-25', '-15', '0'] + [str(i) for i in range(3, 63, 3)]
    weight_multipliers = [-50, -35, -20, 0] + list(range(3, 63, 3))
    weight_labels = ['0', '-15', '-25', '-50'] +  [str(i) for i in range(3, 63, 3)]
    
    # Prepare data for each contraceptive type
    all_scores = {}
    
    # Process negative scores
    for method in neg_scores['severe'].keys():
        scores = [scores[method] for scores in neg_scores.values()]
        scores.extend([None] * (len(weight_multipliers) - len(scores)))  # Pad with None for positive range
        all_scores[method] = scores
    
    # Process positive scores
    for method in pos_scores['3'].keys():
        scores = [None] * 4  # Pad with None for negative range
        method_scores = [scores[method] for scores in pos_scores.values()]
        scores.extend(method_scores)
        all_scores[method] = scores
    
    # Process zero scores (constant across the range)
    for method in zero_scores['1'].keys():
        scores = [zero_scores['1'][method]] * len(weight_multipliers)
        all_scores[method] = scores
    
    # Group methods with identical score patterns
    grouped_methods = {}
    for method, scores in all_scores.items():
        scores_tuple = tuple(scores)  # Convert scores list to tuple for hashing
        if scores_tuple in grouped_methods:
            grouped_methods[scores_tuple].append(method)
        else:
            grouped_methods[scores_tuple] = [method]
    
    # Plot each unique score pattern
    for i, (scores_tuple, methods) in enumerate(grouped_methods.items()):
        #combined_label = ' + '.join(methods)
        combined_label = f"{' + '.join(methods)}"
        valid_indices = [i for i, score in enumerate(scores_tuple) if score is not None]
        valid_scores = [score for score in scores_tuple if score is not None]
        valid_multipliers = [weight_multipliers[i] for i in valid_indices]
        
        plt.plot(valid_multipliers, valid_scores, 
                label=combined_label, 
                marker='o',
                color=distinct_colors[i % len(distinct_colors)])
    
    # Customize the plot
    plt.xlabel('Weight Categories')
    plt.ylabel('Contraceptive Score')
    plt.title('Contraceptive Scores across weights for Acne')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
    
    # Set x-ticks
    plt.xticks(weight_multipliers, weight_labels, rotation=45)
    
    # Add axes at y=0 and x=0
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt

# Example usage:
#plt = plot_contraceptive_scores(neg_scores, pos_scores, zero_scores)
#filename = f'acne_univ_viz.png'  # or .pdf, .jpg, etc.
#plt.savefig(filename, dpi=300, bbox_inches='tight')
#plt.show()

# Adjust the weight labels and multipliers to reflect the correct order
weight_labels = ['-50', '-25', '-15', '0'] + [str(i) for i in range(3, 63, 3)]
weight_multipliers = [-50, -25, -15, 0] + list(range(3, 63, 3))

# Prepare data for each contraceptive type
all_scores = {}

# Process negative scores
for method in neg_scores['severe'].keys():
    scores = [neg_scores[severity][method] for severity in ['severe', 'moderate', 'mild', 'no']]
    scores.extend([None] * (len(weight_multipliers) - len(scores)))  # Pad with None for positive range
    all_scores[method] = scores

# Process positive scores
for method in pos_scores['3'].keys():
    scores = [None] * 4  # Pad with None for negative range
    method_scores = [pos_scores[str(weight)][method] for weight in range(3, 63, 3)]
    scores.extend(method_scores)
    all_scores[method] = scores

# Process zero scores (constant across the range)
for method in zero_scores['1'].keys():
    scores = [zero_scores['1'][method]] * len(weight_multipliers)
    all_scores[method] = scores

# Group methods with identical score patterns
grouped_methods = {}
for method, scores in all_scores.items():
    scores_tuple = tuple(scores)  # Convert scores list to tuple for hashing
    if scores_tuple in grouped_methods:
        grouped_methods[scores_tuple].append(method)
    else:
        grouped_methods[scores_tuple] = [method]

# Plot each unique score pattern
for i, (scores_tuple, methods) in enumerate(grouped_methods.items()):
    combined_label = ' + '.join(methods)
    valid_indices = [i for i, score in enumerate(scores_tuple) if score is not None]
    valid_scores = [score for score in scores_tuple if score is not None]
    valid_multipliers = [weight_multipliers[i] for i in valid_indices]
    
    plt.plot(valid_multipliers, valid_scores, 
             label=combined_label, 
             marker='o',
             color=distinct_colors[i % len(distinct_colors)])

# Customize the plot
plt.xlabel('Weight Categories')
plt.ylabel('Contraceptive Score')
plt.title('Contraceptive Scores across weights for Acne')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Set x-ticks
plt.xticks(weight_multipliers, weight_labels, rotation=45)

# Add axes at y=0 and x=0
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Adjust layout
plt.tight_layout()

# Example usage:
plt = plot_contraceptive_scores(neg_scores, pos_scores, zero_scores)
filename = f'acne_univ_viz.png'  # or .pdf, .jpg, etc.
#plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.show()

'''
for key, value in neg_scores.items():
    print(key, value)
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def plot_contraceptive_scores(neg_scores, pos_scores, zero_scores):
    # Set up the plot
    plt.figure(figsize=(12, 8))
    
    # Define weight labels and multipliers
    weight_labels = ['-50', '-25', '-15', '0'] + [str(i) for i in range(3, 63, 3)]
    weight_multipliers = [-50, -25, -15, 0] + list(range(3, 63, 3))
    
    # Prepare data for each contraceptive type
    all_scores = {}

    # Process negative scores
    for method in neg_scores['severe'].keys():
        scores = [neg_scores[severity][method] for severity in ['severe', 'moderate', 'mild', 'no']]
        scores.extend([None] * (len(weight_multipliers) - len(scores)))  # Pad with None for positive range
        all_scores[method] = scores

    # Process positive scores
    for method in pos_scores['3'].keys():
        scores = [None] * 4  # Pad with None for negative range
        method_scores = [pos_scores[str(weight)][method] for weight in range(3, 63, 3)]
        scores.extend(method_scores)
        all_scores[method] = scores

    # Process zero scores (constant across the range)
    for method in zero_scores['1'].keys():
        scores = [zero_scores['1'][method]] * len(weight_multipliers)
        all_scores[method] = scores

    # Group methods with identical score patterns
    grouped_methods = {}
    for method, scores in all_scores.items():
        scores_tuple = tuple(scores)  # Convert scores list to tuple for hashing
        if scores_tuple in grouped_methods:
            grouped_methods[scores_tuple].append(method)
        else:
            grouped_methods[scores_tuple] = [method]

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

    # Plot each unique score pattern
    for i, (scores_tuple, methods) in enumerate(grouped_methods.items()):
        combined_label = ' + '.join(methods)
        valid_indices = [i for i, score in enumerate(scores_tuple) if score is not None]
        valid_scores = [score for score in scores_tuple if score is not None]
        valid_multipliers = [weight_multipliers[i] for i in valid_indices]
        
        plt.plot(valid_multipliers, valid_scores, 
                 label=combined_label, 
                 marker='o',
                 color=distinct_colors[i % len(distinct_colors)])

    # Customize the plot
    plt.xlabel('Weight Categories')
    plt.ylabel('Contraceptive Score')
    plt.title('Contraceptive Scores across weights for Acne')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

    # Set x-ticks
    plt.xticks(weight_multipliers, weight_labels, rotation=45)

    plt.ylim(-550, 100)
    # Add axes at y=0 and x=0
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Adjust layout
    plt.tight_layout()
    
    return plt

# Example usage:
plt = plot_contraceptive_scores(neg_scores, pos_scores, zero_scores)
filename = f'acne_univ_viz.png'  # or .pdf, .jpg, etc.
plt.savefig(filename, dpi=300, bbox_inches='tight')
#plt.show()
