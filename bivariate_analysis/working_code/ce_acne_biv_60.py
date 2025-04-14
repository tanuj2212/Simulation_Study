from functions_simulation_diff_weight_hor import *
import copy
# THIS ONE WORKS
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
    [-15, -25, -50],  # Matches original top gender dysphoria scores
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
    [-15, -25, -50],  # Weights for arr[19]
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
    [-15, -25, -50],  # corresponding to mild, moderate, severe
    
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
    [-15, -25, -50],      # For arr[19] (no, mild, moderate, severe)
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
    [-15, -25, -50],  # weights for arr[16]: ["mild", "moderate", "severe"]
    3  # weight for arr[17] != "no"
]
inputs = [
    ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    
]

def calculate_scores_ce_acne_neg(input_arr):
    weights = [-60, -40, -20, 20, 40, 60]

    # Update weights for each method
    weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'patch': copy.deepcopy(original_weight_patch),
            'combo_pill': copy.deepcopy(original_weight_combo_pill),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl)
        }

    original_weights = {
    'copper_iud': original_weight_copper_IUD,
    'hormonal_iud': original_weight_hormonal_IUD,
    'sterilization': original_weight_sterilization
} 

    # Update the cost effectiveness weights
    for method in weights_dict:
        weights_dict[method][0] = weights

    # Calculate scores
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    # Calculate scores using the updated weights
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, original_weights['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    return {
        "Hormonal IUD": hormonal_iud_score,
        "Patch": patch_score,
        "Combination Pill": combo_pill_score,
    }


def calculate_scores_ce_acne_pos(input_arr, positive_weights):
    weights = [-60, -40, -20, 20, 40, 60]


    # Update weights for each method
    weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl),
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
                weights_dict[method][0] = weights
            elif method == 'ring':
                weights_dict[method][8] = positive_weights
                weights_dict[method][0] = weights
            elif method == 'shot':
                weights_dict[method][7] = positive_weights
            else:
                weights_dict[method][0] = weights

    original_weights = {
    'copper_iud': original_weight_copper_IUD,
    'hormonal_iud': original_weight_hormonal_IUD,
    'sterilization': original_weight_sterilization
} 

    # Update the cost effectiveness weights
    for method in weights_dict:
        weights_dict[method][0] = weights

    # Calculate scores
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    # Calculate scores using the updated weights
   
    return {
        "Arm Implant": arm_implant_score,
        "Mini Pill": mini_pill_score,
        "Ring": ring_score,
        "Shot": shot_score
    }

def calculate_scores_ce_acne_zero(input_arr):
     weights = [-60, -40, -20, 20, 40, 60]


    # Update weights for each method
     weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'copper_iud': copy.deepcopy(original_weight_copper_IUD),
            'sterilization': copy.deepcopy(original_weight_sterilization),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl),
        }



    # Update the cost effectiveness weights
     for method in weights_dict:
        if method == 'copper_iud' or method == 'sterilization':
            pass
        else:

            weights_dict[method][0] = weights

        # Calculate scores
        #condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
        #internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
        #cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
        #fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
        #copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
        #sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
        #gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
        #withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
        condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[26]]
        internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[8], input_arr[25], input_arr[26]]
        cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
        fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
        copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
        sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[7], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
        gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[8]]
        withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
    
        # Calculate scores using the updated weights
        condom_score = change_score_condoms(condom_arr, weights_dict['condoms'])
        internal_condom_score = change_internal_condoms(internal_condom_arr, weights_dict['internal_condoms'])
        cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_dict['cervical_cap'])
        fam_score = change_fam(fam_arr, weights_dict['FAM'])
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


v_unp_dict = {

}

for arr in inputs[0:4]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

unp_dict = {

}

for arr in inputs[4:8]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        unp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        unp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        unp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        unp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

sl_unp_dict = {

}

for arr in inputs[8:12]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

neutral_dict = {

}

for arr in inputs[12:16]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        neutral_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        neutral_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        neutral_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        neutral_dict["severe"] = calculate_scores_ce_acne_neg(arr)

sl_imp_dict = {

}

for arr in inputs[16:20]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

imp_dict = {

}

for arr in inputs[20:24]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        imp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        imp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        imp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        imp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

v_imp_dict = {

}

for arr in inputs[24:28]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

# POSITIVE

v_unp_dict_pos = {

}

for arr in inputs[0:4]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i*3)
            v_unp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i*3)
            v_unp_dict_pos[f"{i*3}"] = scores_yes
            unp_dict_pos = {}

unp_dict_pos = {

}
for arr in inputs[4:8]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            unp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            unp_dict_pos[f"{i * 3}"] = scores_yes

sl_unp_dict_pos = {}

for arr in inputs[8:12]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_unp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_unp_dict_pos[f"{i * 3}"] = scores_yes

neutral_dict_pos = {}

for arr in inputs[12:16]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            neutral_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            neutral_dict_pos[f"{i * 3}"] = scores_yes

sl_imp_dict_pos = {}

for arr in inputs[16:20]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_imp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_imp_dict_pos[f"{i * 3}"] = scores_yes

imp_dict_pos = {}

for arr in inputs[20:24]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            imp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            imp_dict_pos[f"{i * 3}"] = scores_yes

v_imp_dict_pos = {}

for arr in inputs[24:28]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            v_imp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            v_imp_dict_pos[f"{i * 3}"] = scores_yes


# Zero 


v_unp_dict_zero = {

}

for arr in inputs[0:4]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        v_unp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)


unp_dict_zero = {

}

for arr in inputs[4:8]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        unp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)

sl_unp_dict_zero = {

}

for arr in inputs[8:12]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        sl_unp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)

neutral_dict_zero = {

}

for arr in inputs[12:16]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        neutral_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)

sl_imp_dict_zero = {

}

for arr in inputs[16:20]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        sl_imp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)
    

imp_dict_zero = {

}

for arr in inputs[20:24]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        imp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        imp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        imp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        imp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        imp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)
 
v_imp_dict_zero = {

}

for arr in inputs[24:28]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        v_imp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)


# LATEST
import numpy as np
import plotly.graph_objects as go

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
x_values = [-60, -40, -20, 0, 20, 40, 60]
x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]

# Define y values and labels for negative and positive ranges separately
severity_map = {
    'severe': -60,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-60", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values]

# Dictionary mapping preference levels to their respective dictionaries
preference_dicts = {
    'v_unp': (v_unp_dict, v_unp_dict_pos),
    'unp': (unp_dict, unp_dict_pos),
    'sl_unp': (sl_unp_dict, sl_unp_dict_pos),
    'neutral': (neutral_dict, neutral_dict_pos),
    'sl_imp': (sl_imp_dict, sl_imp_dict_pos),
    'imp': (imp_dict, imp_dict_pos),
    'v_imp': (v_imp_dict, v_imp_dict_pos)
}

# Methods classification
negative_only_methods = [
   
    "Hormonal IUD", "Patch", "Combination Pill"
]

positive_methods = [
    "Arm Implant", "Mini Pill", "Ring", "Shot"
]

# Create distinct color scale
distinct_colors = [
    '#FF0000', '#0000FF', '#FFD700', '#FF1493', '#00FF00', '#8B008B', '#FF8C00',
    '#00FFFF', '#800000', '#000080', '#808000', '#FF00FF', '#008080', '#FFA500', '#4B0082'
]

# Create the 3D visualization
fig = go.Figure()

# Create coordinate matrices for negative methods
X_neg, Y_neg = np.meshgrid(x_values, negative_y_values)

# Create coordinate matrices for positive methods
X_pos, Y_pos = np.meshgrid(x_values, positive_y_values)

# Process negative-only methods
for method_idx, method in enumerate(negative_only_methods):
    Z = np.zeros((len(negative_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _ = preference_dicts[x_label]
        
        for severity, y_pos in severity_map.items():
            y_idx = negative_y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    
    fig.add_trace(go.Surface(
        x=X_neg, y=Y_neg, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Process positive methods
for method_idx, method in enumerate(positive_methods, start=len(negative_only_methods)):
    Z = np.zeros((len(positive_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, pos_dict = preference_dicts[x_label]
        
        # Handle the 'no' case (y=0)
        y_idx = 0  # First index in positive_y_values (corresponds to 0)
        if 'no' in pos_dict and method in pos_dict['no']:
            Z[y_idx, x_idx] = pos_dict['no'][method]
        
        # Handle positive values
        for i, y_value in enumerate(positive_values, start=1):
            if str(y_value) in pos_dict and method in pos_dict[str(y_value)]:
                Z[i, x_idx] = pos_dict[str(y_value)][method]

    fig.add_trace(go.Surface(
        x=X_pos, y=Y_pos, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Update layout
fig.update_layout(
    title='3D Visualization of Contraceptive Scores',
    scene=dict(
        xaxis=dict(title='Preference Level', ticktext=x_labels, tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne Severity/Positive Weight', ticktext=negative_y_labels + positive_y_labels[1:], 
                  tickvals=negative_y_values + positive_values, range=[-60, 60]),
        zaxis=dict(title='Score')
    ),
    showlegend=True,
    legend=dict(
        x=1.05, y=0.5,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='rgba(0, 0, 0, 0.2)',
        borderwidth=1
    ),
    width=1200, height=800
)

'''
# Add buttons to show/hide individual surfaces
buttons = []
all_methods = negative_only_methods + positive_methods
for method_idx, method in enumerate(all_methods):
    visible = [False] * len(all_methods)
    visible[method_idx] = True
    buttons.append(dict(
        label=method,
        method='update',
        args=[{'visible': visible}]
    ))

buttons.append(dict(
    label="Show All",
    method='update',
    args=[{'visible': [True] * len(all_methods)}]
))

fig.update_layout(
    updatemenus=[dict(
        type="dropdown",
        direction="down",
        x=0.1,
        y=1.1,
        showactive=True,
        buttons=buttons
    )]
)

#fig.show()

'''

#BUGGY CODE- FIX DROP/INCREASE IN ZERO CORR CONTRACAPTIVES, FULL LENGTH NOT SHOWN

import numpy as np
import plotly.graph_objects as go

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
#x_values = [-60, -40, -20, 0, 20, 40, 60]
x_values = [60, 40, 20, 0, -20, -40, -60]
#x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]
x_labels = ["60", "40", "20", "0", "-20", "-40", "-60"]

# Define y values and labels for negative and positive ranges
severity_map = {
    'severe': -60,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-60", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values]
negative_only_methods = [
    "Hormonal IUD", "Patch", "Combination Pill"
]

positive_methods = [
    "Arm Implant", "Mini Pill", "Ring", "Shot"
]

zero_correlation_methods = [
    "Condoms", "Internal Condoms", "Cervical Cap", "FAM", 
    "Copper IUD", "Sterilization", "Spermicide", "Withdrawal"
]
# All contraceptive methods
all_methods = {
    "negative_only": [
        "Hormonal IUD", "Patch", "Combination Pill"
    ],
    "positive": [
        "Arm Implant", "Mini Pill", "Ring", "Shot"
    ],
    "zero": [
        "Condoms", "Internal Condoms", "Cervical Cap", "FAM", 
        "Copper IUD", "Sterilization", "Spermicide", "Withdrawal"
    ]
}

# Dictionary mapping preference levels to their respective dictionaries
preference_dicts = {
    'v_unp': (v_unp_dict, v_unp_dict_pos, v_unp_dict_zero),
    'unp': (unp_dict, unp_dict_pos, unp_dict_zero),
    'sl_unp': (sl_unp_dict, sl_unp_dict_pos, sl_unp_dict_zero),
    'neutral': (neutral_dict, neutral_dict_pos, neutral_dict_zero),
    'sl_imp': (sl_imp_dict, sl_imp_dict_pos, sl_imp_dict_zero),
    'imp': (imp_dict, imp_dict_pos, imp_dict_zero),
    'v_imp': (v_imp_dict, v_imp_dict_pos, v_imp_dict_zero)
}

# Create distinct color scale
distinct_colors = [
    '#FF0000', '#0000FF', '#FFD700', '#FF1493', '#00FF00', '#8B008B', '#FF8C00',
    '#00FFFF', '#800000', '#000080', '#808000', '#FF00FF', '#008080', '#FFA500', '#4B0082'
]

# Create the 3D visualization
fig = go.Figure()
all_y_values = negative_y_values + positive_values[1:]
# Create coordinate matrices for negative methods
X_neg, Y_neg = np.meshgrid(x_values, negative_y_values)

all_y_labels = negative_y_labels + [str(i) for i in positive_values[1:]]
# Create coordinate matrices for positive methods
X_pos, Y_pos = np.meshgrid(x_values, positive_y_values)

# Create coordinate matrices for zero methods (using negative y-values for consistency)
X_zero, Y_zero = np.meshgrid(x_values, all_y_values)

# Process negative-only methods
for method_idx, method in enumerate(all_methods["negative_only"]):
    Z = np.zeros((len(negative_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _, _ = preference_dicts[x_label]
        
        for severity, y_pos in severity_map.items():
            y_idx = negative_y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    
    fig.add_trace(go.Surface(
        x=X_neg, y=Y_neg, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Process positive methods
for method_idx, method in enumerate(all_methods["positive"], start=len(all_methods["negative_only"])):
    Z = np.zeros((len(positive_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, pos_dict, _ = preference_dicts[x_label]
        
        # Handle the 'no' case (y=0)
        y_idx = 0
        if 'no' in pos_dict and method in pos_dict['no']:
            Z[y_idx, x_idx] = pos_dict['no'][method]
        
        # Handle positive values
        for i, y_value in enumerate(positive_values, start=1):
            if str(y_value) in pos_dict and method in pos_dict[str(y_value)]:
                Z[i, x_idx] = pos_dict[str(y_value)][method]

    fig.add_trace(go.Surface(
        x=X_pos, y=Y_pos, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Process zero-effect methods
for method_idx, method in enumerate(zero_correlation_methods, start=len(negative_only_methods) + len(positive_methods)):
    Z = np.zeros((len(all_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, _, zero_dict = preference_dicts[x_label]
        
        # Handle negative severity values
        for severity, y_pos in severity_map.items():
            if y_pos in all_y_values:
                y_idx = all_y_values.index(y_pos)
                if severity in zero_dict and method in zero_dict[severity]:
                    Z[y_idx, x_idx] = zero_dict[severity][method]
        
        # Handle positive values
        for i, y_value in enumerate(positive_values):
            if y_value in all_y_values:
                y_idx = all_y_values.index(y_value)
                if str(y_value) in zero_dict and method in zero_dict[str(y_value)]:
                    Z[y_idx, x_idx] = zero_dict[str(y_value)][method]

    fig.add_trace(go.Surface(
        x=X_zero, y=Y_zero, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))
# Update layout
fig.update_layout(
    title='3D Visualization of All Contraceptive Methods',
    scene=dict(
        xaxis=dict(title='Cost Effectiveness weights', ticktext=x_labels[::-1], tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne weights', ticktext=all_y_labels, 
                  tickvals=all_y_values, range=[-60, 60]),
        zaxis=dict(title='Score')
    ),
    showlegend=True,
    legend=dict(
        x=1.05, y=0.5,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='rgba(0, 0, 0, 0.2)',
        borderwidth=1
    ),
    width=1200, height=800
)
'''
# Add buttons to show/hide individual surfaces
buttons = []
all_method_names = (all_methods["negative_only"] + 
                   all_methods["positive"] + 
                   all_methods["zero"])

for method_idx, method in enumerate(all_method_names):
    visible = [False] * len(all_method_names)
    visible[method_idx] = True
    buttons.append(dict(
        label=method,
        method='update',
        args=[{'visible': visible}]
    ))

# Add button to show all methods
buttons.append(dict(
    label="Show All",
    method='update',
    args=[{'visible': [True] * len(all_method_names)}]
))

# Add category buttons
for category in ["negative_only", "positive", "zero"]:
    visible = [False] * len(all_method_names)
    start_idx = 0
    if category == "positive":
        start_idx = len(all_methods["negative_only"])
    elif category == "zero":
        start_idx = len(all_methods["negative_only"]) + len(all_methods["positive"])
    
    for i in range(len(all_methods[category])):
        visible[start_idx + i] = True
        
    buttons.append(dict(
        label=f"Show {category.replace('_', ' ').title()} Methods",
        method='update',
        args=[{'visible': visible}]
    ))
fig.update_layout(
    updatemenus=[dict(
        type="dropdown",
        direction="down",
        x=0.1,
        y=1.1,
        showactive=True,
        buttons=buttons
    )]
)

contraceptive_colors = {
        "Condom": '#FF0000',  # Red
        "Internal Condom": '#0000FF',  # Blue
        "Cervical Cap": '#FFD700',  # Gold
        "FAM": '#FF1493',  # Deep Pink
        "Cervical Cap": '#00FF00',  # Lime
        "Copper IUD": '#8B008B',  # Dark Magenta
        "Patch": '#FF8C00',  # Dark Orange
        "Combo Pill": '#00FFFF',  # Cyan
        "Mini Pill": '#800000',  # Maroon
        "Hormonal IUD": '#000080',  # Navy
        "Gel": '#808000',  # Olive
        "Sterilization": '#FF00FF',  # Magenta
        "Withdrawal": '#008080',  # Teal
        "Ring": '#FFA500',  # Orange
        "Shot": '#4B0082'   # Indigo
    }
'''
fig.show()

from functions_simulation_diff_weight_hor import *
import copy
# THIS ONE WORKS
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
    [-15, -25, -50],  # Matches original top gender dysphoria scores
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
    [-15, -25, -50],  # Weights for arr[19]
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
    [-15, -25, -50],  # corresponding to mild, moderate, severe
    
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
    [-15, -25, -50],      # For arr[19] (no, mild, moderate, severe)
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
    [-15, -25, -50],  # weights for arr[16]: ["mild", "moderate", "severe"]
    3  # weight for arr[17] != "no"
]
inputs = [
    ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    
]

def calculate_scores_ce_acne_neg(input_arr):
    weights = [-60, -40, -20, 20, 40, 60]

    # Update weights for each method
    weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'patch': copy.deepcopy(original_weight_patch),
            'combo_pill': copy.deepcopy(original_weight_combo_pill),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl)
        }

    original_weights = {
    'copper_iud': original_weight_copper_IUD,
    'hormonal_iud': original_weight_hormonal_IUD,
    'sterilization': original_weight_sterilization
} 

    # Update the cost effectiveness weights
    for method in weights_dict:
        weights_dict[method][0] = weights

    # Calculate scores
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    # Calculate scores using the updated weights
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, original_weights['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    return {
        "Hormonal IUD": hormonal_iud_score,
        "Patch": patch_score,
        "Combination Pill": combo_pill_score,
    }


def calculate_scores_ce_acne_pos(input_arr, positive_weights):
    weights = [-60, -40, -20, 20, 40, 60]


    # Update weights for each method
    weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl),
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
                weights_dict[method][0] = weights
            elif method == 'ring':
                weights_dict[method][8] = positive_weights
                weights_dict[method][0] = weights
            elif method == 'shot':
                weights_dict[method][7] = positive_weights
            else:
                weights_dict[method][0] = weights

    original_weights = {
    'copper_iud': original_weight_copper_IUD,
    'hormonal_iud': original_weight_hormonal_IUD,
    'sterilization': original_weight_sterilization
} 

    # Update the cost effectiveness weights
    for method in weights_dict:
        weights_dict[method][0] = weights

    # Calculate scores
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    # Calculate scores using the updated weights
   
    return {
        "Arm Implant": arm_implant_score,
        "Mini Pill": mini_pill_score,
        "Ring": ring_score,
        "Shot": shot_score
    }

def calculate_scores_ce_acne_zero(input_arr):
     weights = [-60, -40, -20, 20, 40, 60]


    # Update weights for each method
     weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'copper_iud': copy.deepcopy(original_weight_copper_IUD),
            'sterilization': copy.deepcopy(original_weight_sterilization),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl),
        }



    # Update the cost effectiveness weights
     for method in weights_dict:
        if method == 'copper_iud' or method == 'sterilization':
            pass
        else:

            weights_dict[method][0] = weights

        # Calculate scores
        #condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
        #internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
        #cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
        #fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
        #copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
        #sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
        #gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
        #withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
        condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[26]]
        internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[8], input_arr[25], input_arr[26]]
        cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
        fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
        copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
        sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[7], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
        gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[8]]
        withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
    
        # Calculate scores using the updated weights
        condom_score = change_score_condoms(condom_arr, weights_dict['condoms'])
        internal_condom_score = change_internal_condoms(internal_condom_arr, weights_dict['internal_condoms'])
        cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_dict['cervical_cap'])
        fam_score = change_fam(fam_arr, weights_dict['FAM'])
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


v_unp_dict = {

}

for arr in inputs[0:4]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        v_unp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

unp_dict = {

}

for arr in inputs[4:8]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        unp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        unp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        unp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        unp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

sl_unp_dict = {

}

for arr in inputs[8:12]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        sl_unp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

neutral_dict = {

}

for arr in inputs[12:16]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        neutral_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        neutral_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        neutral_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        neutral_dict["severe"] = calculate_scores_ce_acne_neg(arr)

sl_imp_dict = {

}

for arr in inputs[16:20]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        sl_imp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

imp_dict = {

}

for arr in inputs[20:24]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        imp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        imp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        imp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        imp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

v_imp_dict = {

}

for arr in inputs[24:28]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["mild"] = calculate_scores_ce_acne_neg(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["moderate"] = calculate_scores_ce_acne_neg(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        v_imp_dict["severe"] = calculate_scores_ce_acne_neg(arr)

# POSITIVE

v_unp_dict_pos = {

}

for arr in inputs[0:4]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i*3)
            v_unp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i*3)
            v_unp_dict_pos[f"{i*3}"] = scores_yes
            unp_dict_pos = {}

unp_dict_pos = {

}
for arr in inputs[4:8]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            unp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            unp_dict_pos[f"{i * 3}"] = scores_yes

sl_unp_dict_pos = {}

for arr in inputs[8:12]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_unp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_unp_dict_pos[f"{i * 3}"] = scores_yes

neutral_dict_pos = {}

for arr in inputs[12:16]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            neutral_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            neutral_dict_pos[f"{i * 3}"] = scores_yes

sl_imp_dict_pos = {}

for arr in inputs[16:20]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_imp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            sl_imp_dict_pos[f"{i * 3}"] = scores_yes

imp_dict_pos = {}

for arr in inputs[20:24]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            imp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            imp_dict_pos[f"{i * 3}"] = scores_yes

v_imp_dict_pos = {}

for arr in inputs[24:28]:
    for i in range(1, 21):
        if arr[11] == "no":
            scores_no = calculate_scores_ce_acne_pos(arr, i * 3)
            v_imp_dict_pos["no"] = scores_no
        else:
            scores_yes = calculate_scores_ce_acne_pos(arr, i * 3)
            v_imp_dict_pos[f"{i * 3}"] = scores_yes


# Zero 


v_unp_dict_zero = {

}

for arr in inputs[0:4]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        v_unp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        v_unp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)


unp_dict_zero = {

}

for arr in inputs[4:8]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        unp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        unp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)

sl_unp_dict_zero = {

}

for arr in inputs[8:12]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        sl_unp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        sl_unp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)

neutral_dict_zero = {

}

for arr in inputs[12:16]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        neutral_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        neutral_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)

sl_imp_dict_zero = {

}

for arr in inputs[16:20]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        sl_imp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        sl_imp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)
    

imp_dict_zero = {

}

for arr in inputs[20:24]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        imp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        imp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        imp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_neg(arr)
        imp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        imp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)
 
v_imp_dict_zero = {

}

for arr in inputs[24:28]:
    if arr[11] == "no":
        scores_no = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["no"] = scores_no

    elif arr[11] == "mild":
        scores_mild = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["mild"] = calculate_scores_ce_acne_zero(arr)
    
    elif arr[11] == "moderate":
        scores_moderate = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["moderate"] = calculate_scores_ce_acne_zero(arr)
    elif arr[11] == "severe":
        scores_severe = calculate_scores_ce_acne_zero(arr)
        v_imp_dict_zero["severe"] = calculate_scores_ce_acne_zero(arr)
    
    for i in range(1, 21):
        v_imp_dict_zero[f"{i*3}"] = calculate_scores_ce_acne_zero(arr)


# LATEST
import numpy as np
import plotly.graph_objects as go

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
x_values = [-60, -40, -20, 0, 20, 40, 60]
x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]

# Define y values and labels for negative and positive ranges separately
severity_map = {
    'severe': -60,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-60", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values]

# Dictionary mapping preference levels to their respective dictionaries
preference_dicts = {
    'v_unp': (v_unp_dict, v_unp_dict_pos),
    'unp': (unp_dict, unp_dict_pos),
    'sl_unp': (sl_unp_dict, sl_unp_dict_pos),
    'neutral': (neutral_dict, neutral_dict_pos),
    'sl_imp': (sl_imp_dict, sl_imp_dict_pos),
    'imp': (imp_dict, imp_dict_pos),
    'v_imp': (v_imp_dict, v_imp_dict_pos)
}

# Methods classification
negative_only_methods = [
   
    "Hormonal IUD", "Patch", "Combination Pill"
]

positive_methods = [
    "Arm Implant", "Mini Pill", "Ring", "Shot"
]

# Create distinct color scale
distinct_colors = [
    '#FF0000', '#0000FF', '#FFD700', '#FF1493', '#00FF00', '#8B008B', '#FF8C00',
    '#00FFFF', '#800000', '#000080', '#808000', '#FF00FF', '#008080', '#FFA500', '#4B0082'
]

# Create the 3D visualization
fig = go.Figure()

# Create coordinate matrices for negative methods
X_neg, Y_neg = np.meshgrid(x_values, negative_y_values)

# Create coordinate matrices for positive methods
X_pos, Y_pos = np.meshgrid(x_values, positive_y_values)

# Process negative-only methods
for method_idx, method in enumerate(negative_only_methods):
    Z = np.zeros((len(negative_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _ = preference_dicts[x_label]
        
        for severity, y_pos in severity_map.items():
            y_idx = negative_y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    
    fig.add_trace(go.Surface(
        x=X_neg, y=Y_neg, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Process positive methods
for method_idx, method in enumerate(positive_methods, start=len(negative_only_methods)):
    Z = np.zeros((len(positive_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, pos_dict = preference_dicts[x_label]
        
        # Handle the 'no' case (y=0)
        y_idx = 0  # First index in positive_y_values (corresponds to 0)
        if 'no' in pos_dict and method in pos_dict['no']:
            Z[y_idx, x_idx] = pos_dict['no'][method]
        
        # Handle positive values
        for i, y_value in enumerate(positive_values, start=1):
            if str(y_value) in pos_dict and method in pos_dict[str(y_value)]:
                Z[i, x_idx] = pos_dict[str(y_value)][method]

    fig.add_trace(go.Surface(
        x=X_pos, y=Y_pos, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Update layout
fig.update_layout(
    title='3D Visualization of Contraceptive Scores',
    scene=dict(
        xaxis=dict(title='Preference Level', ticktext=x_labels, tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne Severity/Positive Weight', ticktext=negative_y_labels + positive_y_labels[1:], 
                  tickvals=negative_y_values + positive_values, range=[-60, 60]),
        zaxis=dict(title='Score')
    ),
    showlegend=True,
    legend=dict(
        x=1.05, y=0.5,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='rgba(0, 0, 0, 0.2)',
        borderwidth=1
    ),
    width=1200, height=800
)

'''
# Add buttons to show/hide individual surfaces
buttons = []
all_methods = negative_only_methods + positive_methods
for method_idx, method in enumerate(all_methods):
    visible = [False] * len(all_methods)
    visible[method_idx] = True
    buttons.append(dict(
        label=method,
        method='update',
        args=[{'visible': visible}]
    ))

buttons.append(dict(
    label="Show All",
    method='update',
    args=[{'visible': [True] * len(all_methods)}]
))

fig.update_layout(
    updatemenus=[dict(
        type="dropdown",
        direction="down",
        x=0.1,
        y=1.1,
        showactive=True,
        buttons=buttons
    )]
)

#fig.show()

'''

#BUGGY CODE- FIX DROP/INCREASE IN ZERO CORR CONTRACAPTIVES, FULL LENGTH NOT SHOWN

import numpy as np
import plotly.graph_objects as go

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
#x_values = [-60, -40, -20, 0, 20, 40, 60]
x_values = [60, 40, 20, 0, -20, -40, -60]
#x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]
x_labels = ["60", "40", "20", "0", "-20", "-40", "-60"]

# Define y values and labels for negative and positive ranges
severity_map = {
    'severe': -60,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-60", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values]
negative_only_methods = [
    "Hormonal IUD", "Patch", "Combination Pill"
]

positive_methods = [
    "Arm Implant", "Mini Pill", "Ring", "Shot"
]

zero_correlation_methods = [
    "Condom", "Internal Condom", "Cervical Cap", "FAM", 
    "Copper IUD", "Sterilization", "Gel", "Withdrawal"
]
# All contraceptive methods
all_methods = {
    "negative_only": [
        "Hormonal IUD", "Patch", "Combo Pill"
    ],
    "positive": [
        "Arm Implant", "Mini Pill", "Ring", "Shot"
    ],
    "zero": [
        "Condom", "Internal Condom", "Cervical Cap", "FAM", 
        "Copper IUD", "Sterilization", "Gel", "Withdrawal"
    ]
}

# Dictionary mapping preference levels to their respective dictionaries
preference_dicts = {
    'v_unp': (v_unp_dict, v_unp_dict_pos, v_unp_dict_zero),
    'unp': (unp_dict, unp_dict_pos, unp_dict_zero),
    'sl_unp': (sl_unp_dict, sl_unp_dict_pos, sl_unp_dict_zero),
    'neutral': (neutral_dict, neutral_dict_pos, neutral_dict_zero),
    'sl_imp': (sl_imp_dict, sl_imp_dict_pos, sl_imp_dict_zero),
    'imp': (imp_dict, imp_dict_pos, imp_dict_zero),
    'v_imp': (v_imp_dict, v_imp_dict_pos, v_imp_dict_zero)
}

# Create distinct color scale
distinct_colors = [
    '#FF0000', '#0000FF', '#FFD700', '#FF1493', '#00FF00', '#8B008B', '#FF8C00',
    '#00FFFF', '#800000', '#000080', '#808000', '#FF00FF', '#008080', '#FFA500', '#4B0082'
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

# Create the 3D visualization
fig = go.Figure()
all_y_values = negative_y_values + positive_values[1:]
# Create coordinate matrices for negative methods
X_neg, Y_neg = np.meshgrid(x_values, negative_y_values)

all_y_labels = negative_y_labels + [str(i) for i in positive_values[1:]]
# Create coordinate matrices for positive methods
X_pos, Y_pos = np.meshgrid(x_values, positive_y_values)

# Create coordinate matrices for zero methods (using negative y-values for consistency)
X_zero, Y_zero = np.meshgrid(x_values, all_y_values)

# Process negative-only methods
for method_idx, method in enumerate(all_methods["negative_only"]):
    Z = np.zeros((len(negative_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _, _ = preference_dicts[x_label]
        
        for severity, y_pos in severity_map.items():
            y_idx = negative_y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    color = contraceptive_colors[method]
    fig.add_trace(go.Surface(
        x=X_neg, y=Y_neg, z=Z,
        name=method, showscale=False,
        colorscale=[[0, color], [1, color]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Process positive methods
for method_idx, method in enumerate(all_methods["positive"], start=len(all_methods["negative_only"])):
    Z = np.zeros((len(positive_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, pos_dict, _ = preference_dicts[x_label]
        
        # Handle the 'no' case (y=0)
        y_idx = 0
        if 'no' in pos_dict and method in pos_dict['no']:
            Z[y_idx, x_idx] = pos_dict['no'][method]
        
        # Handle positive values
        for i, y_value in enumerate(positive_values, start=1):
            if str(y_value) in pos_dict and method in pos_dict[str(y_value)]:
                Z[i, x_idx] = pos_dict[str(y_value)][method]
    color = contraceptive_colors[method]
    fig.add_trace(go.Surface(
        x=X_pos, y=Y_pos, z=Z,
        name=method, showscale=False,
        colorscale=[[0, color], [1, color]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Process zero-effect methods
for method_idx, method in enumerate(zero_correlation_methods, start=len(negative_only_methods) + len(positive_methods)):
    Z = np.zeros((len(all_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, _, zero_dict = preference_dicts[x_label]
        
        # Handle negative severity values
        for severity, y_pos in severity_map.items():
            if y_pos in all_y_values:
                y_idx = all_y_values.index(y_pos)
                if severity in zero_dict and method in zero_dict[severity]:
                    Z[y_idx, x_idx] = zero_dict[severity][method]
        
        # Handle positive values
        for i, y_value in enumerate(positive_values):
            if y_value in all_y_values:
                y_idx = all_y_values.index(y_value)
                if str(y_value) in zero_dict and method in zero_dict[str(y_value)]:
                    Z[y_idx, x_idx] = zero_dict[str(y_value)][method]
    color = contraceptive_colors[method]

    fig.add_trace(go.Surface(
        x=X_zero, y=Y_zero, z=Z,
        name=method, showscale=False,
        colorscale=[[0, color], [1, color]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))
# Update layout
fig.update_layout(
    title='3D Visualization of All Contraceptive Methods',
    scene=dict(
        xaxis=dict(title='Cost Effectiveness weights', ticktext=x_labels[::-1], tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne weights', ticktext=all_y_labels, 
                  tickvals=all_y_values, range=[-60, 60]),
        zaxis=dict(title='Score')
    ),
    showlegend=True,
    legend=dict(
        x=1.05, y=0.5,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='rgba(0, 0, 0, 0.2)',
        borderwidth=1
    ),
    width=1200, height=800
)
'''
# Add buttons to show/hide individual surfaces
buttons = []
all_method_names = (all_methods["negative_only"] + 
                   all_methods["positive"] + 
                   all_methods["zero"])

for method_idx, method in enumerate(all_method_names):
    visible = [False] * len(all_method_names)
    visible[method_idx] = True
    buttons.append(dict(
        label=method,
        method='update',
        args=[{'visible': visible}]
    ))

# Add button to show all methods
buttons.append(dict(
    label="Show All",
    method='update',
    args=[{'visible': [True] * len(all_method_names)}]
))

# Add category buttons
for category in ["negative_only", "positive", "zero"]:
    visible = [False] * len(all_method_names)
    start_idx = 0
    if category == "positive":
        start_idx = len(all_methods["negative_only"])
    elif category == "zero":
        start_idx = len(all_methods["negative_only"]) + len(all_methods["positive"])
    
    for i in range(len(all_methods[category])):
        visible[start_idx + i] = True
        
    buttons.append(dict(
        label=f"Show {category.replace('_', ' ').title()} Methods",
        method='update',
        args=[{'visible': visible}]
    ))
fig.update_layout(
    updatemenus=[dict(
        type="dropdown",
        direction="down",
        x=0.1,
        y=1.1,
        showactive=True,
        buttons=buttons
    )]
)

contraceptive_colors = {
        "Condom": '#FF0000',  # Red
        "Internal Condom": '#0000FF',  # Blue
        "Cervical Cap": '#FFD700',  # Gold
        "FAM": '#FF1493',  # Deep Pink
        "Cervical Cap": '#00FF00',  # Lime
        "Copper IUD": '#8B008B',  # Dark Magenta
        "Patch": '#FF8C00',  # Dark Orange
        "Combo Pill": '#00FFFF',  # Cyan
        "Mini Pill": '#800000',  # Maroon
        "Hormonal IUD": '#000080',  # Navy
        "Gel": '#808000',  # Olive
        "Sterilization": '#FF00FF',  # Magenta
        "Withdrawal": '#008080',  # Teal
        "Ring": '#FFA500',  # Orange
        "Shot": '#4B0082'   # Indigo
    }
'''
fig.show()
