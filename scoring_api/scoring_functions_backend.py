original_weight_condoms = [
    [-8, 8],
    [-100, 3],
    [-3, -2, -1, 1, 2, 3],  # Cost effectiveness
    [-1.5, -1, -0.5, 0.5, 1, 1.5],  # Pregnancy prevention
    3,  # Maintenance (daily use)
    [-3, -2, -1, 1, 2, 3],  # Partner willingness
    [-3, -2, -1, 1, 2, 3],  # STI prevention
    3,
    1.5  # Gender dysphoria related to pregnancy (no/yes)
]
original_weight_internal_condoms = [
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,        
    3,            # Maintenance (arr[2])
    [-3, -2, -1, 1, 2, 3],  # Vaginal Insertion (arr[3])
    [-3, -2, -1, 1, 2, 3],  # Seeking Consultation (arr[4])
    [-15, -25, -50],     # Gender Dysphoria Vaginal Insertion (arr[5])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[6])
]
original_weight_FAM = [
    [-8, 8],
    [-100, 3],
    [-3, -2, -1, 1, 2, 3],  # Cost Effectiveness (arr[1])
    3,
    [-3, -2, -1, 1, 2, 3],  # Partner Willingness (arr[3])
    3,                    # Maintenance (arr[2])
    [-15, -25, -50]      # Gender Dysphoria Pregnancy (arr[4])
]
original_weight_arm_implant = [
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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
    [-8, 8],
    [-100, 3],
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


def score_ring(arr, weights):
    ring_score = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        ring_score += weights[0][0]
    elif arr[1] == "negative":
        ring_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        ring_score += weights[1][0]
    elif arr[2] == "yes":
        ring_score += weights[1][1]
    else:
        pass

    # Cost Effectiveness
    if arr[3] == "v_unp":
        ring_score += weights[2][0]
    elif arr[3] == "unp":
        ring_score += weights[2][1]
    elif arr[3] == "sl_unp":
        ring_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        ring_score += weights[2][3]
    elif arr[3] == "imp":
        ring_score += weights[2][4]
    else:
        ring_score += weights[2][5]
    
    # Pregnancy Prevention
    if arr[4] == "v_unp":
        ring_score += weights[3][0]
    elif arr[4] == "unp":
        ring_score += weights[3][1]
    elif arr[4] == "sl_unp":
        ring_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        ring_score += weights[3][3]
    elif arr[4] == "imp":
        ring_score += weights[3][4]
    else:
        ring_score += weights[3][5]
    
    # Management of Periods 
    if arr[5] == "v_unp":
        ring_score += weights[4][0]
    elif arr[5] == "unp":
        ring_score += weights[4][1]
    elif arr[5] == "sl_unp":
        ring_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        ring_score += weights[4][3]
    elif arr[5] == "imp":
        ring_score += weights[4][4]
    else:
        ring_score += weights[4][5]
    
    # Weight Management
    if arr[6] == "v_unp":
        ring_score += weights[5][0]
    elif arr[6] == "unp":
        ring_score += weights[5][1]
    elif arr[6] == "sl_unp":
        ring_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        ring_score += weights[5][3]
    elif arr[6] == "imp":
        ring_score += weights[5][4]
    else:
        ring_score += weights[5][5]
    
    # Maintainance 
    if arr[7] == "monthly":
        ring_score += weights[6]

    # Hormones
    if arr[8] == 'ep':
        ring_score += weights[7]
    else:
        pass
    
    # Seeking consultation
    if arr[9] == "v_unp":
        ring_score += weights[8][0]
    elif arr[9] == "unp":
        ring_score += weights[8][1]
    elif arr[9] == "sl_unp":
        ring_score += weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        ring_score += weights[8][3]
    elif arr[9] == "imp":
        ring_score += weights[8][4]
    else:
        ring_score += weights[8][5]

    # Medical Procedure
    if arr[10] == "v_unp":
        ring_score += weights[9][0]
    elif arr[10] == "unp":
        ring_score += weights[9][1]
    elif arr[10] == "sl_unp":
        ring_score += weights[9][2]
    elif arr[10] == "neutral":
        pass
    elif arr[10] == "sl_imp":
        ring_score += weights[9][3]
    elif arr[10] == "imp":
        ring_score += weights[9][4]
    else:
        ring_score += weights[9][5]
    
    # Acne
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' or arr[11] == 'moderate' or arr[11] == 'severe':
        ring_score += weights[10]
    
    # Anxiety
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[11] != 'no':
        ring_score += weights[11][0]
    elif arr[12] == 'moderate' and arr[11] != 'no':
        ring_score += weights[11][1]
    elif arr[12]=='severe' and arr[11] != 'no':
        ring_score += weights[11][2]
    elif arr[12] == 'mild' and arr[11] == 'no':
        ring_score += weights[11][3]
    elif arr[12] == 'moderate' and arr[11] == 'no':
        ring_score += weights[11][4]
    elif arr[12]== 'severe' and arr[11] == 'no':
        ring_score += weights[11][5]
    
    # Depression
    if arr[13] == 'no':
        pass
    elif arr[13] == 'mild' and arr[10] != 'no':
        ring_score += weights[12][0]
    elif arr[13] == 'moderate' and arr[10] != 'no':
        ring_score += weights[12][1]
    elif arr[13] == 'severe' and arr[10] != 'no':
        ring_score += weights[12][2]
    elif arr[13] == 'mild' and arr[10] == 'no':
        ring_score += weights[12][3]
    elif arr[13] == 'moderate' and arr[10] == 'no':
        ring_score += weights[12][4]
    elif arr[13]== 'severe' and arr[10] == 'no':
        ring_score += weights[12][5]
    
    # Hyper
    if arr[14] == 'no':
        pass
    else:
        ring_score += weights[13]
    
    # Blood Clots
    if arr[15] == 'no':
        pass
    else:
        ring_score += weights[14]
    
    # CHF_CAD
    if arr[16] == 'no':
        pass
    else:
        ring_score += weights[15]
    
    # Breast
    if arr[17] == 'no':
        pass
    else:
        ring_score += weights[16]
    
    # Smoker
    if arr[18] == 'no':
        pass
    else:
        ring_score += weights[17]
    
    # Migraine
    if arr[19] == 'no':
        pass
    else:
        ring_score += weights[18]
    
    # PCOS
    if arr[20] == 'no':
        pass
    else:
        ring_score += weights[19]
    
    # Endometriosis
    if arr[21] == 'no':
        pass
    else:
        ring_score += weights[20]
    
    # Top Gender Dysphoria
    if arr[22] == 'no':
        pass
    elif arr[22] == 'mild':
        ring_score += weights[21][0]
    elif arr[22] == 'moderate':
        ring_score += weights[21][1]
    else:
        ring_score += weights[21][2]
    
    # Top Surgery
    if arr[23] == 'no':
        pass
    else:
        ring_score += weights[22]

    # BGDP
    if arr[24] == 'no':
        pass
    else:
        ring_score += weights[23]

    # GDVI

    
    # GDP
    if arr[25] == 'no':
        pass
    else:
        ring_score += weights[24]

    # HRT
    if arr[26] == 'no':
        pass
    else:
        ring_score += weights[25]
    
    return ring_score
   

def change_score_shot(arr, weights):
    shot_score = 3

    # Pregnancy Prevention
    
    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        shot_score += weights[0][0]
    elif arr[1] == "negative":
        shot_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        shot_score += weights[1][0]
    elif arr[2] == "yes":
        shot_score += weights[1][1]
    else:
        pass

    if arr[3] == "v_unp":
        shot_score += weights[2][0]
    elif arr[3] == "unp":
        shot_score += weights[2][1]
    elif arr[3] == "sl_unp":
        shot_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        shot_score += weights[2][3]
    elif arr[3] == "imp":
        shot_score += weights[2][4]
    else:
        shot_score += weights[2][5]
    
    # Management of Periods
    if arr[4] == "v_unp":
        shot_score += weights[3][0]
    elif arr[4] == "unp":
        shot_score += weights[3][1]
    elif arr[4] == "sl_unp":
        shot_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        shot_score += weights[3][3]
    elif arr[4] == "imp":
        shot_score += weights[3][4]
    else:
        shot_score += weights[3][5]
    
    # Weight Management
    if arr[5] == "v_unp":
        shot_score += weights[4][0]
    elif arr[5] == "unp":
        shot_score += weights[4][1]
    elif arr[5] == "sl_unp":
        shot_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        shot_score += weights[4][3]
    elif arr[5] == "imp":
        shot_score += weights[4][4]
    else:
        shot_score += weights[4][5]
    
     # Maintainance
    if arr[6] == "monthly":
        shot_score += weights[5]
    
    # Hormones
    if arr[7] == 'p':
        shot_score += weights[6][0]
    elif arr[7] == 'ep':
        shot_score += weights[6][1]
    else:
        pass

    # Seeking consultation
    if arr[8] == "v_unp":
        shot_score += weights[7][0]
    elif arr[8] == "unp":
        shot_score += weights[7][1]
    elif arr[8] == "sl_unp":
        shot_score += weights[7][2]
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        shot_score += weights[7][3]
    elif arr[8] == "imp":
        shot_score += weights[7][4]
    else:
        shot_score += weights[7][5]
    
    # Medical Procedure
    if arr[9] == "v_unp":
        shot_score += weights[8][0]
    elif arr[9] == "unp":
        shot_score += weights[8][1]
    elif arr[9] == "sl_unp":
        shot_score += weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        shot_score += weights[8][3]
    elif arr[9] == "imp":
        shot_score += weights[8][4]
    else:
        shot_score += weights[8][5]
    
    # Acne
    if arr[10] == 'no':
        pass
    else:
        shot_score += weights[9]
    
    # Anxiety
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        shot_score += weights[10][0]
    elif arr[11] == 'moderate' and arr[10] != 'no':
        shot_score += weights[10][1]
    elif arr[11]=='severe' and arr[10] != 'no':
        shot_score += weights[10][2]
    elif arr[11] == 'mild' and arr[10] == 'no':
        shot_score += weights[10][3]
    elif arr[11] == 'moderate' and arr[10] == 'no':
        shot_score += weights[10][4]
    elif arr[11]== 'severe' and arr[10] == 'no':
        shot_score += weights[10][5]
    
    # Depression
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[9] != 'no':
        shot_score += weights[11][0]
    elif arr[12] == 'moderate' and arr[9] != 'no':
        shot_score += weights[11][1]
    elif arr[12] == 'severe' and arr[9] != 'no':
        shot_score += weights[11][2]
    elif arr[12] == 'mild' and arr[9] == 'no':
        shot_score += weights[11][3]
    elif arr[12] == 'moderate' and arr[9] == 'no':
        shot_score += weights[11][4]
    elif arr[12]== 'severe' and arr[9] == 'no':
        shot_score += weights[11][5]
    
    # Hyper
    if arr[13] == 'no':
        pass
    else:
        shot_score += weights[12]
    
    # Blood Clots
    if arr[14] == 'no':
        pass
    else:
        shot_score += weights[13]
    
    # CHF_CAD
    if arr[15] == 'no':
        pass
    else:
        shot_score += weights[14]
    
    # Breast
    if arr[16] == 'no':
        pass
    else:
        shot_score += weights[15]
    
    # Smoker
    if arr[17] == 'no':
        pass
    else:
        shot_score += weights[16]
    
    # Migraine
    if arr[18] == 'no':
        pass
    else:
        shot_score += weights[17]
    
    # PCOS
    if arr[19] == 'no':
        pass
    else:
        shot_score += weights[18]

    # Endometriosis
    if arr[20] == 'no':
        pass
    else:
        shot_score += weights[19]
    
    # Top gender dysphoria
    if arr[21] == 'no':
        pass
    elif arr[21] == 'mild':
        shot_score += weights[20][0]
    elif arr[21] == 'moderate':
        shot_score += weights[20][1]
    else:
        shot_score += weights[20][2]
    
    # Top Surgery
    if arr[22] == 'no':
        pass
    else:
        shot_score += weights[21]
    
    # BGDP
    if arr[23] == 'no':
        pass
    else:
        shot_score += weights[22]
    
    # Gender Dypshoria Preganancy
    if arr[24] == 'no':
        pass
    else:
        shot_score += weights[23]
    
    # HRT
    if arr[25] == 'no':
        pass
    else:
        shot_score += weights[24]
    
    return shot_score


def change_score_combo_pill(arr, weights):
    combo_pill_score = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        combo_pill_score += weights[0][0]
    elif arr[1] == "negative":
        combo_pill_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        combo_pill_score += weights[1][0]
    elif arr[2] == "yes":
        combo_pill_score += weights[1][1]
    else:
        pass

    if arr[3] == "v_unp":
        combo_pill_score += weights[2][0]
    elif arr[3] == "unp":
        combo_pill_score += weights[2][1]
    elif arr[3] == "sl_unp":
        combo_pill_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        combo_pill_score += weights[2][3]
    elif arr[3] == "imp":
        combo_pill_score += weights[2][4]
    else:
        combo_pill_score += weights[2][5]
    
    if arr[4] == "v_unp":
        combo_pill_score += weights[3][0]
    elif arr[4] == "unp":
        combo_pill_score += weights[3][1]
    elif arr[4] == "sl_unp":
        combo_pill_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        combo_pill_score += weights[3][3]
    elif arr[4] == "imp":
        combo_pill_score += weights[3][4]
    else:
        combo_pill_score += weights[3][5]
    
    if arr[5] == "v_unp":
        combo_pill_score += weights[4][0]
    elif arr[5] == "unp":
        combo_pill_score += weights[4][1]
    elif arr[5] == "sl_unp":
        combo_pill_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        combo_pill_score += weights[4][3]
    elif arr[5] == "imp":
        combo_pill_score += weights[4][4]
    else:
        combo_pill_score += weights[4][5]
    
    if arr[6] == "v_unp":
        combo_pill_score += weights[5][0]
    elif arr[6] == "unp":
        combo_pill_score += weights[5][1]
    elif arr[6] == "sl_unp":
        combo_pill_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        combo_pill_score += weights[5][3]
    elif arr[6] == "imp":
        combo_pill_score += weights[5][4]
    else:
        combo_pill_score += weights[5][5]
    
    if arr[7] == "daily":
        combo_pill_score += weights[6]
    
    if arr[8] == 'ep':
        combo_pill_score += weights[7]
    else:
        pass

    if arr[9] == "v_unp":
        combo_pill_score += weights[8][0]
    elif arr[9] == "unp":
        combo_pill_score += weights[8][1]
    elif arr[9] == "sl_unp":
        combo_pill_score += weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        combo_pill_score+= weights[8][3]
    elif arr[9] == "imp":
        combo_pill_score += weights[8][4]
    else:
        combo_pill_score += weights[8][5]
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild':
        combo_pill_score += weights[9][0]
    elif arr[10] == 'moderate':
        combo_pill_score += weights[9][1]
    else:
        combo_pill_score += weights[9][2]

    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[12] != 'no':
        combo_pill_score += weights[10][0]
    elif arr[11] == 'moderate' and arr[12] != 'no':
        combo_pill_score += weights[10][1]
    elif arr[11]=='severe' and arr[12] != 'no':
        combo_pill_score += weights[10][2]
    elif arr[11] == 'mild' and arr[12] == 'no':
        combo_pill_score += weights[10][3]
    elif arr[11] == 'moderate' and arr[12] == 'no':
        combo_pill_score += weights[10][4]
    elif arr[11]== 'severe' and arr[12] == 'no':
        combo_pill_score += weights[10][5]
    
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[11] != 'no':
        combo_pill_score += weights[11][0]
    elif arr[12] == 'moderate' and arr[11] != 'no':
        combo_pill_score += weights[11][1]
    elif arr[12] == 'severe' and arr[11] != 'no':
        combo_pill_score += weights[11][2]
    elif arr[12] == 'mild' and arr[11] == 'no':
        combo_pill_score += weights[11][3]
    elif arr[12] == 'moderate' and arr[11] == 'no':
        combo_pill_score += weights[11][4]
    elif arr[12]== 'severe' and arr[11] == 'no':
        combo_pill_score += weights[11][5]
    
    if arr[13] == 'no':
        pass
    else:
        combo_pill_score += weights[12]
    
    if arr[14] == 'no':
        pass
    else:
        combo_pill_score += weights[13]
    
    if arr[15] == 'no':
        pass
    else:
        combo_pill_score += weights[14]
    
    if arr[16] == 'no':
        pass
    else:
        combo_pill_score += weights[15]
    
    if arr[17] == 'no':
        pass
    else:
        combo_pill_score += weights[16]
    
    if arr[18] == 'no':
        pass
    else:
        combo_pill_score += weights[17]
    
    if arr[19] == 'no':
        pass
    else:
        combo_pill_score += weights[18]
    
    if arr[20] == 'no':
        pass
    else:
        combo_pill_score += weights[19]
    
    if arr[21] == 'no':
        pass
    elif arr[21] == 'mild':
        combo_pill_score += weights[20][0]
    elif arr[21] == 'moderate':
        combo_pill_score += weights[20][1]
    else:
        combo_pill_score += weights[20][2]
    
    if arr[22] == 'no':
        pass
    else:
        combo_pill_score += weights[21]
    
    if arr[23] == 'no':
        pass
    else:
         combo_pill_score += weights[22]
    
    if arr[24] == 'no':
        pass
    else:
         combo_pill_score += weights[23]
    
    if arr[25] == 'no':
        pass
    else:
        combo_pill_score += weights[24]
    
    return combo_pill_score


def change_score_patch(arr, weights):
    patch_score = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        patch_score += weights[0][0]
    elif arr[1] == "negative":
        patch_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        patch_score += weights[1][0]
    elif arr[2] == "yes":
        patch_score += weights[1][1]
    else:
        pass

    if arr[3] == "v_unp":
        patch_score += weights[2][0]
    elif arr[3] == "unp":
        patch_score += weights[2][1]
    elif arr[3] == "sl_unp":
        patch_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        patch_score += weights[2][3]
    elif arr[3] == "imp":
        patch_score += weights[2][4]
    else:
        patch_score += weights[2][5]
    
    if arr[4] == "v_unp":
        patch_score += weights[3][0]
    elif arr[4] == "unp":
        patch_score += weights[3][1]
    elif arr[4] == "sl_unp":
        patch_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        patch_score += weights[3][3]
    elif arr[4] == "imp":
        patch_score += weights[3][4]
    else:
        patch_score += weights[3][5]
    
    if arr[5] == "v_unp":
        patch_score += weights[4][0]
    elif arr[5] == "unp":
        patch_score += weights[4][1]
    elif arr[5] == "sl_unp":
        patch_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        patch_score += weights[4][3]
    elif arr[5] == "imp":
        patch_score += weights[4][4]
    else:
        patch_score += weights[4][5]
    
    if arr[6] == "v_unp":
        patch_score += weights[5][0]
    elif arr[6] == "unp":
        patch_score += weights[5][1]
    elif arr[6] == "sl_unp":
        patch_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        patch_score += weights[5][3] 
    elif arr[6] == "imp":
        patch_score += weights[5][4]
    else:
        patch_score += weights[5][5]
    
    if arr[7] == "weekly":
        patch_score += weights[6]
    
    if arr[8] == 'ep':
        patch_score += weights[7]
    else:
        pass

    if arr[9] == "v_unp":
        patch_score += weights[8][0]
    elif arr[9] == "unp":
        patch_score += weights[8][1]
    elif arr[9] == "sl_unp":
        patch_score += weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        patch_score+= weights[8][3]
    elif arr[9] == "imp":
        patch_score += weights[8][4]
    else:
        patch_score += weights[8][5]
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild':
        patch_score += weights[9][0]
    elif arr[10] == 'moderate':
        patch_score += weights[9][1]
    else:
        patch_score += weights[9][2]

    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        patch_score += weights[10][0]
    elif arr[11] == 'moderate' and arr[10] != 'no':
        patch_score += weights[10][1]
    elif arr[11]=='severe' and arr[10] != 'no':
        patch_score += weights[10][2]
    elif arr[11] == 'mild' and arr[10] == 'no':
        patch_score += weights[10][3]
    elif arr[11] == 'moderate' and arr[10] == 'no':
        patch_score += weights[10][4]
    elif arr[11]== 'severe' and arr[10] == 'no':
        patch_score += weights[10][5]
    
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[9] != 'no':
        patch_score += weights[11][0]
    elif arr[12] == 'moderate' and arr[9] != 'no':
        patch_score += weights[11][1]
    elif arr[12] == 'severe' and arr[9] != 'no':
        patch_score += weights[11][2]
    elif arr[12] == 'mild' and arr[9] == 'no':
        patch_score += weights[11][3]
    elif arr[12] == 'moderate' and arr[9] == 'no':
        patch_score += weights[11][4]
    elif arr[12]== 'severe' and arr[9] == 'no':
        patch_score += weights[11][5]
    
    if arr[13] == 'no':
        pass
    else:
        patch_score += weights[12]
    
    if arr[14] == 'no':
        pass
    else:
        patch_score += weights[13]
    
    if arr[15] == 'no':
        pass
    else:
        patch_score += weights[14]
    
    if arr[16] == 'no':
        pass
    else:
        patch_score += weights[15]
    
    if arr[17] == 'no':
        pass
    else:
        patch_score += weights[16]
    
    if arr[18] == 'no':
        pass
    else:
        patch_score += weights[17]
    
    if arr[19] == 'no':
        pass
    else:
        patch_score += weights[18]
    
    if arr[20] == 'no':
        pass
    else:
        patch_score += weights[19]
    
    if arr[21] == 'no':
        pass
    elif arr[21] == 'mild':
        patch_score += weights[20][0]
    elif arr[21] == 'moderate':
        patch_score += weights[20][1]
    else:
        patch_score += weights[20][2]
    
    if arr[22] == 'no':
        pass
    else:
        patch_score += weights[21]
    
    if arr[23] == 'no':
        pass
    else:
         patch_score += weights[22]
    
    if arr[24] == 'no':
        pass
    else:
         patch_score += weights[23]
    
    if arr[25] == 'no':
        pass
    else:
        patch_score += weights[24]
    
    return patch_score


def change_score_hormonal_iud(arr, weights):
    hormonal_iud_score = 3
    
    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        hormonal_iud_score += weights[0][0]
    elif arr[1] == "negative":
        hormonal_iud_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        hormonal_iud_score += weights[1][0]
    elif arr[2] == "yes":
        hormonal_iud_score += weights[1][1]
    else:
        pass

    if arr[3] == "v_unp":
        hormonal_iud_score += weights[2][0]
    elif arr[3] == "unp":
        hormonal_iud_score += weights[2][1]
    elif arr[3] == "sl_unp":
        hormonal_iud_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        hormonal_iud_score += weights[2][3]
    elif arr[3] == "imp":
        hormonal_iud_score += weights[2][4]
    else:
        hormonal_iud_score += weights[2][5]
    
    if arr[4] == "v_unp":
        hormonal_iud_score += weights[3][0]
    elif arr[4] == "unp":
        hormonal_iud_score += weights[3][1]
    elif arr[4] == "sl_unp":
        hormonal_iud_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        hormonal_iud_score += weights[3][3]
    elif arr[4] == "imp":
        hormonal_iud_score += weights[3][4]
    else:
        hormonal_iud_score += weights[3][5]

    if arr[5] == "v_unp":
        hormonal_iud_score += weights[4][0]
    elif arr[5] == "unp":
        hormonal_iud_score += weights[4][1]
    elif arr[5] == "sl_unp":
        hormonal_iud_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        hormonal_iud_score += weights[4][3]
    elif arr[5] == "imp":
        hormonal_iud_score += weights[4][4]
    else:
        hormonal_iud_score += weights[4][5]
    
    if arr[6] == "yearly":
        hormonal_iud_score += weights[5]
    
    if arr[7] == 'p':
        hormonal_iud_score += weights[6][0]
    elif arr[7] == 'ep':
        hormonal_iud_score += weights[6][1]
    else:
        pass
    
    if arr[8] == "v_unp":
        hormonal_iud_score += weights[7][0]
    elif arr[8] == "unp":
        hormonal_iud_score += weights[7][1]
    elif arr[8] == "sl_unp":
        hormonal_iud_score += weights[7][2]
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        hormonal_iud_score += weights[7][3]
    elif arr[8] == "imp":
        hormonal_iud_score += weights[7][4]
    else:
        hormonal_iud_score += weights[7][5]
    
    if arr[9] == "v_unp":
        hormonal_iud_score += weights[8][0]
    elif arr[9] == "unp":
        hormonal_iud_score += weights[8][1]
    elif arr[9] == "sl_unp":
        hormonal_iud_score += weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        hormonal_iud_score += weights[8][3]
    elif arr[9] == "imp":
        hormonal_iud_score += weights[8][4]
    else:
        hormonal_iud_score += weights[8][5]
    
    if arr[10] == "v_unp":
        hormonal_iud_score += weights[9][0]
    elif arr[10] == "unp":
        hormonal_iud_score += weights[9][1]
    elif arr[10] == "sl_unp":
        hormonal_iud_score += weights[9][2]
    elif arr[10] == "neutral":
        pass
    elif arr[10] == "sl_imp":
        hormonal_iud_score += weights[9][3]
    elif arr[10] == "imp":
        hormonal_iud_score += weights[9][4]
    else:
        hormonal_iud_score += weights[9][5]
    
    if arr[11] == 'no':
        pass
    elif arr[11]  == 'mild':
        hormonal_iud_score += weights[10][0]
    elif arr[11] == 'moderate':
        hormonal_iud_score += weights[10][1]
    else:
        hormonal_iud_score += weights[10][2]
    
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[11] != 'no':
        hormonal_iud_score += weights[11][0]
    elif arr[12] == 'moderate' and arr[11] != 'no':
        hormonal_iud_score += weights[11][1]
    elif arr[12]=='severe' and arr[11] != 'no':
        hormonal_iud_score += weights[11][2]
    elif arr[12] == 'mild' and arr[11] == 'no':
        hormonal_iud_score += weights[11][3]
    elif arr[12] == 'moderate' and arr[11] == 'no':
        hormonal_iud_score += weights[11][4]
    elif arr[12]== 'severe' and arr[11] == 'no':
        hormonal_iud_score += weights[11][5]
    
    if arr[13] == 'no':
        pass
    elif arr[13] == 'mild' and arr[10] != 'no':
        hormonal_iud_score += weights[12][0]
    elif arr[13] == 'moderate' and arr[10] != 'no':
        hormonal_iud_score += weights[12][1]
    elif arr[13] == 'severe' and arr[10] != 'no':
        hormonal_iud_score += weights[12][2]
    elif arr[13] == 'mild' and arr[10] == 'no':
        hormonal_iud_score += weights[12][3]
    elif arr[13] == 'moderate' and arr[10] == 'no':
        hormonal_iud_score += weights[12][4]
    elif arr[13]== 'severe' and arr[10] == 'no':
        hormonal_iud_score += weights[12][5]
    
    if arr[14] == 'no':
        pass
    else:
        hormonal_iud_score += weights[13]
    
    if arr[15] == 'no':
        pass
    else:
        hormonal_iud_score += weights[14]
    
    if arr[16] == 'no':
        pass
    else:
        hormonal_iud_score += weights[15]
    
    if arr[17] == 'no':
        pass
    else:
        hormonal_iud_score += weights[16]
    
    if arr[18] == 'no':
        pass
    elif arr[18]  == 'mild':
        hormonal_iud_score += weights[17][0]
    elif arr[18] == 'moderate':
        hormonal_iud_score += weights[17][1]
    else:
        hormonal_iud_score += weights[17][2]
    
    if arr[19] == 'no':
        pass
    else:
        hormonal_iud_score += weights[18]
    
    return hormonal_iud_score 

# Condoms
def change_score_condoms(arr, weights):
    score_condoms = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        score_condoms += weights[0][0]
    elif arr[1] == "negative":
        score_condoms += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        score_condoms += weights[1][0]
    elif arr[2] == "yes":
        score_condoms += weights[1][1]
    else:
        pass
    
    # Cost Effectiveness
    if arr[3] == "v_unp":
        score_condoms += 1 * weights[2][0]
    elif arr[3] == "unp":
        score_condoms += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        score_condoms += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        score_condoms += 1 * weights[2][3]
    elif arr[3] == "imp":
        score_condoms += 1 * weights[2][4]
    else:
        score_condoms += 1 * weights[2][5]
    
    # Pregnancy prevention
    if arr[4] == "v_unp":
        score_condoms += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_condoms += 1  * weights[3][1]
    elif arr[4] == "sl_unp":
        score_condoms += 1 * weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_condoms += 1 * weights[3][3]
    elif arr[4] == "imp":
        score_condoms += 1 * weights[3][4]
    else:
        score_condoms += 1 * weights[3][5]
    
    # Maintainance
    if arr[5] == "daily":
        score_condoms += 1 * weights[4]
    else:
        pass

    # Partner Willingness
    if arr[6] == "v_unp":
        score_condoms += 1 * weights[5][0]
    elif arr[6] == "unp":
        score_condoms += 1 * weights[5][1]
    elif arr[6] == "sl_unp":
        score_condoms += 1 * weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        score_condoms += 1 * weights[5][3]
    elif arr[6] == "imp":
        score_condoms += 1 * weights[5][4]
    else:
        score_condoms += 1 * weights[5][5]
    
    # STI
    if arr[7] == "v_unp":
        score_condoms += 1 * weights[6][0]
    elif arr[7] == "unp":
        score_condoms += 1 * weights[6][1]
    elif arr[7] == "sl_unp":
        score_condoms += 1 * weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        score_condoms += 1 * weights[6][3]
    elif arr[7] == "imp":
        score_condoms += 1 * weights[6][4]
    else:
        score_condoms += 1 * weights[6][5]
    
    # Bottom gender dysphoria pregnancy
    if arr[8] == "none":
        score_condoms += weights[7]

    if arr[9] == 'no':
        pass
    else:
        score_condoms += 1 * weights[8]
    
    return score_condoms

def change_internal_condoms(arr, weights):
    score_internal_condoms = 3

    
    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        score_internal_condoms += weights[0][0]
    elif arr[1] == "negative":
        score_internal_condoms += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        score_internal_condoms += weights[1][0]
    elif arr[2] == "yes":
        score_internal_condoms += weights[1][1]
    else:
        pass

    # Cost Effectiveness
    if arr[3] == "v_unp":
        score_internal_condoms += 1 * weights[2][0]
    elif arr[3] == "unp":
        score_internal_condoms += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        score_internal_condoms += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        score_internal_condoms += 1 * weights[2][3]
    elif arr[3] == "imp":
        score_internal_condoms += 1 * weights[2][4]
    else:
        score_internal_condoms += 1 * weights[2][5]
    
    # Pregnancy Prevention
    if arr[4] == "v_unp":
        score_internal_condoms += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_internal_condoms += 1  * weights[3][1]
    elif arr[4] == "sl_unp":
        score_internal_condoms += 1 * weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_internal_condoms += 1 * weights[3][3]
    elif arr[4] == "imp":
        score_internal_condoms += 1 * weights[3][4]
    else:
        score_internal_condoms += 1 * weights[3][5]
    
    # Maintainance
    if arr[5] == "daily":
        score_internal_condoms += 1 * weights[4]
    else:
        pass

    # Partner Willingness
    if arr[6] == "v_unp":
        score_internal_condoms += 1 * weights[5][0]
    elif arr[6] == "unp":
        score_internal_condoms += 1 * weights[5][1]
    elif arr[6] == "sl_unp":
        score_internal_condoms += 1 * weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        score_internal_condoms += 1 * weights[5][3]
    elif arr[6] == "imp":
        score_internal_condoms += 1 * weights[5][4]
    else:
        score_internal_condoms += 1 * weights[5][5]
    
    # Prevents STI
    if arr[7] == "v_unp":
        score_internal_condoms += 1 * weights[6][0]
    elif arr[7] == "unp":
        score_internal_condoms += 1 * weights[6][1]
    elif arr[7] == "sl_unp":
        score_internal_condoms += 1 * weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        score_internal_condoms += 1 * weights[6][3]
    elif arr[7] == "imp":
        score_internal_condoms += 1 * weights[6][4]
    else:
        score_internal_condoms += 1 * weights[6][5]
    
    if arr[8] == "none":
        score_internal_condoms += weights[7]
    
    # Vaginal Insertion
    if arr[9] == "v_unp":
        score_internal_condoms += 1 * weights[8][0]
    elif arr[9] == "unp":
        score_internal_condoms += 1 * weights[8][1]
    elif arr[9] == "sl_unp":
        score_internal_condoms += 1 * weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        score_internal_condoms += 1 * weights[8][3]
    elif arr[9] == "imp":
        score_internal_condoms += 1 * weights[8][4]
    else:
        score_internal_condoms += 1 * weights[8][5]
    
    # Gender Dysphoria Vaginal Insertion
    if arr[10] == "no":
        pass
    elif arr[10] == "mild":
        score_internal_condoms += weights[9][0]
    elif arr[10] == "moderate":
        score_internal_condoms += weights[9][1]
    else:
        score_internal_condoms += weights[9][2]
    
    # Gender Dysphoria Pregnancy
    if arr[11] == "no":
        pass
    
    else:
        score_internal_condoms += weights[10]

    return score_internal_condoms
# Cervical Cap

def change_score_cervical_cap(arr, weights):
    score_cervical_cap = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        score_cervical_cap += weights[0][0]
    elif arr[1] == "negative":
        score_cervical_cap += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        score_cervical_cap += weights[1][0]
    elif arr[2] == "yes":
        score_cervical_cap += weights[1][1]
    else:
        pass
    # Cost effectiveness
    if arr[3] == "v_unp":
        score_cervical_cap += 1 * weights[2][0]
    elif arr[3] == "unp":
        score_cervical_cap += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        score_cervical_cap += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        score_cervical_cap += 1 * weights[2][3]
    elif arr[3] == "imp":
        score_cervical_cap += 1 * weights[2][4]
    else:
        score_cervical_cap += 1 * weights[2][5]

    # Maintainance
    if arr[4] == "daily":
        score_cervical_cap += 1 * weights[3]
    else:
        pass

    #print(weights[2])
    if arr[5] == "none":
        score_cervical_cap += weights[4]

    # Vaginal insertion
    if arr[6] == "v_unp":
        score_cervical_cap += 1 * weights[5][0]
    elif arr[6] == "unp":
        score_cervical_cap += 1 * weights[5][1]
    elif arr[6] == "sl_unp":
        score_cervical_cap += 1 * weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        score_cervical_cap += 1 * weights[5][3]
    elif arr[6] == "imp":
        score_cervical_cap += 1 * weights[5][4]
    else:
        score_cervical_cap += 1 * weights[5][5]
    
    # Seeking consultation
    if arr[7] == "v_unp":
        score_cervical_cap += 1 * weights[6][0]
    elif arr[7] == "unp":
        score_cervical_cap += 1 * weights[6][1]
    elif arr[7] == "sl_unp":
        score_cervical_cap += 1 * weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        score_cervical_cap += 1 * weights[6][3]
    elif arr[7] == "imp":
        score_cervical_cap += 1 * weights[6][4]
    else:
        score_cervical_cap += 1 * weights[6][5]
    
    # Gender Dysphoria Vaginal Insertion
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        score_cervical_cap += 1 * weights[7][0]
    elif arr[8] == 'moderate':
        score_cervical_cap += 1 * weights[7][1]
    else:
        score_cervical_cap += 1 * weights[7][2]
    
    # Gender dysphoria pregnancy
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild':
        score_cervical_cap += 1 * weights[8][0]
    elif arr[9] == 'moderate':
        score_cervical_cap += 1 * weights[8][1]
    else:
        score_cervical_cap += 1 * weights[8][2]
    
    return score_cervical_cap


# FAM
def change_fam(arr, weights):
    score_fam = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        score_fam += weights[0][0]
    elif arr[1] == "negative":
        score_fam += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        score_fam += weights[1][0]
    elif arr[2] == "yes":
        score_fam += weights[1][1]
    else:
        pass
    # Cost effectiveness
    if arr[3] == "v_unp":
        score_fam += 1 * weights[2][0]
    elif arr[3] == "unp":
        score_fam += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        score_fam += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        score_fam += 1 * weights[2][3]
    elif arr[3] == "imp":
        score_fam += 1 * weights[2][4]
    else:
        score_fam += 1 * weights[2][5]
    
    # Maintainance
    if arr[4] == "daily":
        score_fam += 1 * weights[3]
    else:
        pass

    # Partner Willingness
    if arr[5] == "v_unp":
        score_fam += 1 * weights[4][0]
    elif arr[5] == "unp":
        score_fam += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        score_fam += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        score_fam += 1 * weights[4][3]
    elif arr[5] == "imp":
        score_fam += 1 * weights[4][4]
    else:
        score_fam += 1 * weights[4][5]
    
    if arr[6] == "none":
        score_fam += weights[5]
    
    # Gender Dysphoria Pregnancy
    if arr[7] == "no":
        pass
    elif arr[7] == "mild":
        score_fam += 1 * weights[6][0]
    elif arr[7] == "moderate":
        score_fam += 1 * weights[6][1]
    else:
        score_fam += 1 * weights[6][2]
    
    return score_fam

'''
# Arm Implant
'''
def change_arm_implant(arr, weights):
    score_arm_implant = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        score_arm_implant += weights[0][0]
    elif arr[1] == "negative":
        score_arm_implant += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        score_arm_implant += weights[1][0]
    elif arr[2] == "yes":
        score_arm_implant += weights[1][1]
    else:
        pass

    # Pregnancy Prevention
    if arr[3] == "v_unp":
        score_arm_implant += 1 * weights[2][0]
    elif arr[3] == "unp":
        score_arm_implant += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        score_arm_implant += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        score_arm_implant += 1 * weights[2][3]
    elif arr[3] == "imp":
        score_arm_implant += 1 * weights[2][4]
    else:
        score_arm_implant += 1 * weights[2][5]
    
    # Lessens Periods
    if arr[4] == "v_unp":
        score_arm_implant += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_arm_implant += 1  * weights[3][1]
    elif arr[4] == "sl_unp":
        score_arm_implant += 1 * weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_arm_implant += 1 * weights[3][3]
    elif arr[4] == "imp":
        score_arm_implant += 1 * weights[3][4]
    else:
        score_arm_implant += 1 * weights[3][5]
    
    # Maintains Weight
    if arr[5] == "v_unp":
        score_arm_implant += 1 * weights[4][0]
    elif arr[5] == "unp":
        score_arm_implant += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        score_arm_implant += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        score_arm_implant += 1 * weights[4][3]
    elif arr[5] == "imp":
        score_arm_implant += 1 * weights[4][4]
    else:
        score_arm_implant += 1 * weights[4][5]
    
    # Maintainance
    if arr[6] == "yearly":
        score_arm_implant += 1 * weights[5]
    else:
        pass

    # Hormones Used
    if arr[7] == "p":
        score_arm_implant += 1 * weights[6][0]
    elif arr[7] == "ep":
        score_arm_implant += 1 * weights[6][1]
    else:
        pass

    # Seeking consultation
    if arr[8] == "v_unp":
        score_arm_implant += 1 * weights[7][0]
    elif arr[8] == "unp":
        score_arm_implant += 1 * weights[7][1]
    elif arr[8] == "sl_unp":
        score_arm_implant += 1 * weights[7][2]
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        score_arm_implant += 1 * weights[7][3]
    elif arr[8] == "imp":
        score_arm_implant += 1 * weights[7][4]
    else:
        score_arm_implant += 1 * weights[7][5]
    
    # Medical procedure
    if arr[9] == "v_unp":
        score_arm_implant += 1 * weights[8][0]
    elif arr[9] == "unp":
        score_arm_implant += 1 * weights[8][1]
    elif arr[9] == "sl_unp":
        score_arm_implant += 1 * weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        score_arm_implant += 1 * weights[8][3]
    elif arr[9] == "imp":
        score_arm_implant += 1 * weights[8][4]
    else:
        score_arm_implant += 1 * weights[8][5]
    
    # Acne
    if arr[10] == "no":
        pass
    else:
        score_arm_implant += 1 * weights[9]
    
    # Anxiety 
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        score_arm_implant += weights[10][0]
    elif arr[11] == 'moderate' and arr[10] != 'no':
        score_arm_implant += weights[10][1]
    elif arr[11]=='severe' and arr[10] != 'no':
        score_arm_implant += weights[10][2]
    elif arr[11] == 'mild' and arr[10] == 'no':
        score_arm_implant += weights[10][3]
    elif arr[11] == 'moderate' and arr[10] == 'no':
        score_arm_implant += weights[10][4]
    elif arr[11]== 'severe' and arr[10] == 'no':
        score_arm_implant += weights[10][5]
    
    # Depression
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[9] != 'no':
        score_arm_implant += weights[11][0]
    elif arr[12] == 'moderate' and arr[9] != 'no':
        score_arm_implant += weights[11][1]
    elif arr[12] == 'severe' and arr[9] != 'no':
        score_arm_implant += weights[11][2]
    elif arr[12] == 'mild' and arr[9] == 'no':
        score_arm_implant += weights[11][3]
    elif arr[12] == 'moderate' and arr[9] == 'no':
        score_arm_implant += weights[11][4]
    elif arr[12]== 'severe' and arr[9] == 'no':
        score_arm_implant += weights[11][5]
    
    # Gender dysphoria period
    if arr[13] == 'no':
        pass
    else:
        score_arm_implant += weights[12]
    
    # Gender dysphoria pregnancy
    if arr[14] == 'no':
        pass
    else:
        score_arm_implant += weights[13]
    
    return score_arm_implant



# Copper IUD
def change_copper_iud(arr, weights):
    copper_iud_score = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        copper_iud_score += weights[0][0]
    elif arr[1] == "negative":
        copper_iud_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        copper_iud_score += weights[1][0]
    elif arr[2] == "yes":
        copper_iud_score += weights[1][1]
    else:
        pass

    # Pregnancy Prevention
    if arr[3] == "v_unp":
        copper_iud_score += 1 * weights[2][0]
    elif arr[3] == "unp":
        copper_iud_score += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        copper_iud_score += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        copper_iud_score += 1 * weights[2][3]
    elif arr[3] == "imp":
        copper_iud_score += 1 * weights[2][4]
    else:
        copper_iud_score += 1 * weights[2][5]
    
    # Maintainance
    if arr[4] == 'yearly':
        copper_iud_score += weights[3]
    
    if arr[5] == "none":
        copper_iud_score += weights[4]
    
    # Vaginal insertion
    if arr[6] == "v_unp":
        copper_iud_score += weights[5][0]
    elif arr[6] == "unp":
        copper_iud_score += weights[5][1]
    elif arr[6] == "sl_unp":
        copper_iud_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        copper_iud_score += weights[5][3]
    elif arr[6] == "imp":
        copper_iud_score += weights[5][4]
    else:
        copper_iud_score += weights[5][5]
    
    # Seeking consultation
    if arr[7] == "v_unp":
        copper_iud_score += 1 * weights[6][0]
    elif arr[7] == "unp":
        copper_iud_score += 1 * weights[6][1]
    elif arr[7] == "sl_unp":
        copper_iud_score += 1 * weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        copper_iud_score += 1 * weights[6][3]
    elif arr[7] == "imp":
        copper_iud_score += 1 * weights[6][4]
    else:
        copper_iud_score += 1 * weights[6][5]
    
    # Medical Procedure
    if arr[8] == "v_unp":
        copper_iud_score += weights[7][0]
    elif arr[8] == "unp":
        copper_iud_score += weights[7][1]
    elif arr[8] == "sl_unp":
        copper_iud_score += weights[7][2]
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        copper_iud_score += weights[7][3]
    elif arr[8] == "imp":
        copper_iud_score += weights[7][4]
    else:
        copper_iud_score += weights[7][5]
    
    # Gender dysphoria period
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild':
        copper_iud_score += weights[8][0]
    elif arr[9] == 'moderate':
        copper_iud_score += weights[8][1]
    else:
        copper_iud_score += weights[8][2]
    
    # Gender Dysphoria Vaginal Insertion
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild':
        copper_iud_score += weights[9][0] 
    elif arr[10] == 'moderate':
        copper_iud_score += weights[9][1]
    else:
        copper_iud_score += weights[9][2]
    
    # Gender Dysphoria Pregnancy
    if arr[11] == 'no':
        pass
    else:
        copper_iud_score += weights[10]
    
    return copper_iud_score

# Sterilization
def change_score_sterilization(arr, weights):
    sterilization_scores = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        sterilization_scores += weights[0][0]
    elif arr[1] == "negative":
        sterilization_scores += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        sterilization_scores += weights[1][0]
    elif arr[2] == "yes":
        sterilization_scores += weights[1][1]
    else:
        pass

    # Pregnancy prevention
    if arr[3] == "v_unp":
        sterilization_scores += weights[2][0]
    elif arr[3] == "unp":
        sterilization_scores += weights[2][1]
    elif arr[3] == "sl_unp":
        sterilization_scores += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        sterilization_scores += weights[2][3]
    elif arr[3] == "imp":
        sterilization_scores += weights[2][4]
    else:
        sterilization_scores += weights[2][5]
    
    # Lessens periods
    if arr[4] == "v_unp":
        sterilization_scores += weights[3][0]
    elif arr[4] == "unp":
        sterilization_scores += weights[3][1]
    elif arr[4] == "sl_unp":
        sterilization_scores += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        sterilization_scores += weights[3][3]
    elif arr[4] == "imp":
        sterilization_scores += weights[3][4]
    else:
        sterilization_scores += weights[3][5]
    
    if arr[5] == "none":
        sterilization_scores += weights[4]
    
    # Seeking consultation
    if arr[6] == "v_unp":
        sterilization_scores += weights[5][0]
    elif arr[6] == "unp":
        sterilization_scores += weights[5][1]
    elif arr[6] == "sl_unp":
        sterilization_scores += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        sterilization_scores += weights[5][3]
    elif arr[6] == "imp":
        sterilization_scores += weights[5][4]
    else:
        sterilization_scores += weights[5][5]
    
    # Medical Procedure
    if arr[7] == "v_unp":
        sterilization_scores += weights[6][0]
    elif arr[7] == "unp":
        sterilization_scores += weights[6][1]
    elif arr[7] == "sl_unp":
        sterilization_scores += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        sterilization_scores += weights[6][3]
    elif arr[7] == "imp":
        sterilization_scores += weights[6][4]
    else:
        sterilization_scores += weights[6][5]
    
    # PCOS
    if arr[8] == 'no':
        pass
    else:
        sterilization_scores += weights[7]
    
    # ENDMT
    if arr[9] == 'no':
        pass
    else:
        sterilization_scores += weights[8]
    
    # Gender Dypsphoria Period
    if arr[10] == 'no':
        pass
    else:
        sterilization_scores += weights[9]
    
    # Gender Dysphoria Pregnancy
    if arr[11] == 'no':
        pass
    else:
        sterilization_scores += weights[10]
    
    return sterilization_scores

def change_score_gel(arr, weights):
    gel_score = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        gel_score += weights[0][0]
    elif arr[1] == "negative":
        gel_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        gel_score += weights[1][0]
    elif arr[2] == "yes":
        gel_score += weights[1][1]
    else:
        pass

    # Cost Effectiveness
    if arr[3] == "v_unp":
        gel_score += 1 * weights[2][0]
    elif arr[3] == "unp":
        gel_score += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        gel_score += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        gel_score += 1 * weights[2][3]
    elif arr[3] == "imp":
        gel_score += 1 * weights[2][4]
    else:
        gel_score += 1 * weights[2][5]
    
    # Maintainance
    if arr[4] == "daily":
        gel_score += weights[3]
    else:
        pass
    
    # Partner Willingness 
    if arr[5] == "v_unp":
        gel_score += 1 * weights[4][0]
    elif arr[5] == "unp":
        gel_score += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        gel_score += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        gel_score += 1 * weights[4][3]
    elif arr[5] == "imp":
        gel_score += 1 * weights[4][4]
    else:
        gel_score += 1 * weights[4][5]
    
    if arr[6] == "none":
        gel_score += weights[5]
    
    # Vaginal Insertion
    if arr[7] == "v_unp":
        gel_score += 1 * weights[6][0]
    elif arr[7] == "unp":
        gel_score += 1 * weights[6][1]
    elif arr[7] == "sl_unp":
        gel_score += 1 * weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        gel_score += 1 * weights[6][3]
    elif arr[7] == "imp":
        gel_score += 1 * weights[6][4]
    else:
        gel_score += 1 * weights[6][5]
    
    return gel_score

def change_score_withdrawal(arr, weights):
    withdrawal_score = 3

    # Experience. If this contraceptive is None in decision factors, then "none"
    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        withdrawal_score+= weights[0][0]
    elif arr[1] == "negative":
        withdrawal_score+= weights[0][1]
    else: # Neutral
        pass
    
    # Will use again. If this contraceptive is None in decision factors, then "none"
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        withdrawal_score+= weights[1][0]
    elif arr[2] == "yes":
        withdrawal_score += weights[1][1]
    else: # I dont know
        pass

    # Cost Effectivess
    if arr[3] == "v_unp":
        withdrawal_score += 1 * weights[2][0]
    elif arr[3] == "unp":
        withdrawal_score += 1 * weights[2][1]
    elif arr[3] == "sl_unp":
        withdrawal_score += 1 * weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        withdrawal_score += 1 * weights[2][3]
    elif arr[3] == "imp":
        withdrawal_score += 1 * weights[2][4]
    else:
        withdrawal_score += 1 * weights[2][5]

    # Maintainance
    if arr[4] == "daily":
        withdrawal_score += weights[3]
    
    # Partner Willingness
    if arr[5] == "v_unp":
        withdrawal_score += weights[4][0]
    elif arr[5] == "unp":
        withdrawal_score += weights[4][1]
    elif arr[5] == "sl_unp":
        withdrawal_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        withdrawal_score += weights[4][3]
    elif arr[5] == "imp":
        withdrawal_score += weights[4][4]
    else:
        withdrawal_score += weights[4][5]
    
    if arr[6] == "none":
        withdrawal_score += weights[5]
    
    # Gender Dysphoria Pregnancy
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        withdrawal_score += weights[6][0]
    elif arr[7]== 'moderate':
        withdrawal_score += weights[6][1]
    else:
        withdrawal_score += weights[6][2]
    
    return withdrawal_score

def change_scoring_mini_pill(arr, weights):
    mini_pill_score = 3

    if arr[1] == "none":
        pass
    elif arr[1] == "positive":
        mini_pill_score += weights[0][0]
    elif arr[1] == "negative":
        mini_pill_score += weights[0][1]
    else:
        pass
    
    if arr[2] == "none":
        pass
    elif arr[2] == "no":
        mini_pill_score += weights[1][0]
    elif arr[2] == "yes":
        mini_pill_score += weights[1][1]
    else:
        pass

    # Cost Effectiveness
    if arr[3] == "v_unp":
        mini_pill_score += weights[2][0]
    elif arr[3] == "unp":
        mini_pill_score += weights[2][1]
    elif arr[3] == "sl_unp":
        mini_pill_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        mini_pill_score += weights[2][3]
    elif arr[3] == "imp":
        mini_pill_score += weights[2][4]
    else:
        mini_pill_score += weights[2][5]
    
    # Pregnancy Prevention
    if arr[4] == "v_unp":
        mini_pill_score += weights[3][0]
    elif arr[4] == "unp":
        mini_pill_score += weights[3][1]
    elif arr[4] == "sl_unp":
        mini_pill_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        mini_pill_score += weights[3][3]
    elif arr[4] == "imp":
        mini_pill_score += weights[3][4]
    else:
        mini_pill_score += weights[3][5]
    
    # Management of Periods 
    if arr[5] == "v_unp":
        mini_pill_score += weights[4][0]
    elif arr[5] == "unp":
        mini_pill_score += weights[4][1]
    elif arr[5] == "sl_unp":
        mini_pill_score += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        mini_pill_score += weights[4][3]
    elif arr[5] == "imp":
        mini_pill_score += weights[4][4]
    else:
        mini_pill_score += weights[4][5]
    
    # Weight Management
    if arr[6] == "v_unp":
        mini_pill_score += weights[5][0]
    elif arr[6] == "unp":
        mini_pill_score += weights[5][1]
    elif arr[6] == "sl_unp":
        mini_pill_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        mini_pill_score += weights[5][3]
    elif arr[6] == "imp":
        mini_pill_score += weights[5][4]
    else:
        mini_pill_score += weights[5][5]
    
    # Maintainance
    if arr[7] == "daily":
        mini_pill_score += weights[6] 
    
    # Hormones 
    if arr[8] == 'p':
        mini_pill_score += weights[7][0]
    elif arr[8] == 'ep':
        mini_pill_score += weights[7][1]
    else:   
        pass
    
    # Seeking consultations
    if arr[9] == "v_unp":
        mini_pill_score += weights[8][0]
    elif arr[9] == "unp":
        mini_pill_score += weights[8][1]
    elif arr[9] == "sl_unp":
        mini_pill_score += weights[8][2]
    elif arr[9] == "neutral":
        pass
    elif arr[9] == "sl_imp":
        mini_pill_score += weights[8][3]
    elif arr[9] == "imp":
        mini_pill_score += weights[8][4]
    else:
        mini_pill_score += weights[8][5]
    
    # Acne
    if arr[10] == 'no':
        pass
    else:
        mini_pill_score += weights[9]
    
    # Anxiety
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        mini_pill_score += weights[10][0]
    elif arr[11] == 'moderate' and arr[10] != 'no':
        mini_pill_score += weights[10][1]
    elif arr[11]=='severe' and arr[10] != 'no':
        mini_pill_score += weights[10][2]
    elif arr[11] == 'mild' and arr[10] == 'no':
        mini_pill_score += weights[10][3]
    elif arr[11] == 'moderate' and arr[10] == 'no':
        mini_pill_score += weights[10][4]
    elif arr[11]== 'severe' and arr[10] == 'no':
        mini_pill_score += weights[10][5]
    
    # Depression
    if arr[12] == 'no':
        pass
    elif arr[12] == 'mild' and arr[9] != 'no':
        mini_pill_score += weights[11][0]
    elif arr[12] == 'moderate' and arr[9] != 'no':
        mini_pill_score += weights[11][1]
    elif arr[12] == 'severe' and arr[9] != 'no':
        mini_pill_score += weights[11][2]
    elif arr[12] == 'mild' and arr[9] == 'no':
        mini_pill_score += weights[11][3]
    elif arr[12] == 'moderate' and arr[9] == 'no':
        mini_pill_score += weights[11][4]
    elif arr[12]== 'severe' and arr[9] == 'no':
        mini_pill_score += weights[11][5]
    
    # Breast
    if arr[13] == 'no':
        pass
    else:
        mini_pill_score += weights[12]
    
    # PCOS
    if arr[14] == 'no':
        pass
    else:
        mini_pill_score += weights[13]
    
    # ENDMT
    if arr[15] == 'no':
        pass
    else:
        mini_pill_score += weights[14]
    
    # Gender dysphoria period
    if arr[16] == 'no':
        pass
    else:
        mini_pill_score += weights[15]
    
    # Gender dysphoria pregnancy
    if arr[17] == 'no':
        pass
    else:
        mini_pill_score += weights[16]
    
    return mini_pill_score