def ring(arr):
    ring_score = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        ring_score -= 3
    elif arr[1] == "unp":
        ring_score -= 2
    elif arr[1] == "sl_unp":
        ring_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        ring_score += 1
    elif arr[1] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        ring_score -= 1.5
    elif arr[2] == "unp":
        ring_score -= 1
    elif arr[2] == "sl_unp":
        ring_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        ring_score += 0.5
    elif arr[2] == "imp":
        ring_score += 1
    else:
        ring_score += 1.5
    
    # Management of Periods 
    if arr[3] == "v_unp":
        ring_score -= 3
    elif arr[3] == "unp":
        ring_score -= 2
    elif arr[3] == "sl_unp":
        ring_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        ring_score += 1
    elif arr[3] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Weight Management
    if arr[4] == "v_unp":
        ring_score += 3
    elif arr[4] == "unp":
        ring_score += 2
    elif arr[4] == "sl_unp":
        ring_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        ring_score -= 1
    elif arr[4] == "imp":
        ring_score -= 2
    else:
        ring_score -= 3
    
    if arr[5] == "monthly":
        ring_score += 3

    # Hormones
    if arr[6] == 'ep':
        ring_score += 3
    
    # Willingness Vagina
    if arr[7] == "v_unp":
        ring_score -= 3
    elif arr[7] == "unp":
        ring_score -= 2
    elif arr[7] == "sl_unp":
        ring_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        ring_score += 1
    elif arr[7] == "imp":
        ring_score += 2
    else:
        ring_score += 3

    # Medical Practioner 
    if arr[8] == "v_unp":
        ring_score -= 3 
    elif arr[8] == "unp":
        ring_score -= 2
    elif arr[8] == "sl_unp":
        ring_score -= 1
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        ring_score += 1
    elif arr[8] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    # Acne, 1
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' or arr[9] == 'moderate' or arr[9] == 'severe':
        ring_score += 3
    
    # Anxiety, -1
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[11] != 'no':
        ring_score -= 7.5
    elif arr[10] == 'moderate' and arr[11] != 'no':
        ring_score -= 12.5
    elif arr[10]=='severe' and arr[11] != 'no':
        ring_score -= 25
    elif arr[10] == 'mild' and arr[11] == 'no':
        ring_score -= 15
    elif arr[10] == 'moderate' and arr[11] == 'no':
        ring_score -= 25
    elif arr[10]== 'severe' and arr[11] == 'no':
        ring_score -= 50
    
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        ring_score -= 7.5
    elif arr[11] == 'moderate' and arr[10] != 'no':
        ring_score -= 12.5
    elif arr[11] == 'severe' and arr[10] != 'no':
        ring_score -= 25
    elif arr[11] == 'mild' and arr[10] == 'no':
        ring_score -= 15
    elif arr[11] == 'moderate' and arr[10] == 'no':
        ring_score -= 25
    elif arr[11]== 'severe' and arr[10] == 'no':
        ring_score -= 50
    
    # Hyper, -1
    if arr[12] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Blood Clots
    if arr[13] == 'no':
        pass
    else:
        ring_score -= 100
    
    # CHF_CAD
    if arr[14] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Breast
    if arr[15] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Smoker
    if arr[16] == 'no':
        pass
    else:
        ring_score -= 100
    
    # Migraine
    if arr[17] == 'no':
        pass
    else:
        ring_score -= 100
    
    # PCOS
    if arr[18] == 'no':
        pass
    else:
        ring_score += 3
    
    # Endometriosis
    if arr[19] == 'no':
        pass
    else:
        ring_score += 3
    
    # Top Gender Dysphoria
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        ring_score -= 15
    elif arr[20] == 'moderate':
        ring_score -= 25
    else:
        ring_score -= 50
    
    # Top Surgery
    if arr[21] == 'no':
        pass
    elif arr[21] == 'mild':
        ring_score -= 15
    elif arr[21] == 'moderate':
        ring_score -= 25
    else:
        ring_score -= 50

    # BGDP
    if arr[22] == 'no':
        pass
    else:
        ring_score += 3

    # GDVI

    # GDP

    if arr[23] == 'no':
        pass
    else:
        ring_score += 1.5

    # HRT

    if arr[24] == 'no':
        pass
    else:
        ring_score -= 100
    
    return ring_score

def score_ring(arr, weights):
    ring_score = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        ring_score += weights[0][0]
    elif arr[1] == "unp":
        ring_score += weights[0][1]
    elif arr[1] == "sl_unp":
        ring_score += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        ring_score += weights[0][3]
    elif arr[1] == "imp":
        ring_score += weights[0][4]
    else:
        ring_score += weights[0][5]
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        ring_score += weights[1][0]
    elif arr[2] == "unp":
        ring_score += weights[1][1]
    elif arr[2] == "sl_unp":
        ring_score += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        ring_score += weights[1][3]
    elif arr[2] == "imp":
        ring_score += weights[1][4]
    else:
        ring_score += weights[1][5]
    
    # Management of Periods 
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
    
    # Weight Management
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
    
    # Maintainance 
    if arr[5] == "monthly":
        ring_score += weights[4]

    # Hormones
    if arr[6] == 'ep':
        ring_score += weights[5]
    else:
        pass
    
    # Seeking consultation
    if arr[7] == "v_unp":
        ring_score += weights[6][0]
    elif arr[7] == "unp":
        ring_score += weights[6][1]
    elif arr[7] == "sl_unp":
        ring_score += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        ring_score += weights[6][3]
    elif arr[7] == "imp":
        ring_score += weights[6][4]
    else:
        ring_score += weights[6][5]

    # Medical Procedure
    if arr[8] == "v_unp":
        ring_score += weights[7][0]
    elif arr[8] == "unp":
        ring_score += weights[7][1]
    elif arr[8] == "sl_unp":
        ring_score += weights[7][2]
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        ring_score += weights[7][3]
    elif arr[8] == "imp":
        ring_score += weights[7][4]
    else:
        ring_score += weights[7][5]
    
    # Acne
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' or arr[9] == 'moderate' or arr[9] == 'severe':
        ring_score += weights[8]
    
    # Anxiety
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[11] != 'no':
        ring_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[11] != 'no':
        ring_score += weights[9][1]
    elif arr[10]=='severe' and arr[11] != 'no':
        ring_score += weights[9][2]
    elif arr[10] == 'mild' and arr[11] == 'no':
        ring_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[11] == 'no':
        ring_score += weights[9][4]
    elif arr[10]== 'severe' and arr[11] == 'no':
        ring_score += weights[9][5]
    
    # Depression
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        ring_score += weights[10][0]
    elif arr[11] == 'moderate' and arr[10] != 'no':
        ring_score += weights[10][1]
    elif arr[11] == 'severe' and arr[10] != 'no':
        ring_score += weights[10][2]
    elif arr[11] == 'mild' and arr[10] == 'no':
        ring_score += weights[10][3]
    elif arr[11] == 'moderate' and arr[10] == 'no':
        ring_score += weights[10][4]
    elif arr[11]== 'severe' and arr[10] == 'no':
        ring_score += weights[10][5]
    
    # Hyper
    if arr[12] == 'no':
        pass
    else:
        ring_score += weights[11]
    
    # Blood Clots
    if arr[13] == 'no':
        pass
    else:
        ring_score += weights[12]
    
    # CHF_CAD
    if arr[14] == 'no':
        pass
    else:
        ring_score += weights[13]
    
    # Breast
    if arr[15] == 'no':
        pass
    else:
        ring_score += weights[14]
    
    # Smoker
    if arr[16] == 'no':
        pass
    else:
        ring_score += weights[15]
    
    # Migraine
    if arr[17] == 'no':
        pass
    else:
        ring_score += weights[16]
    
    # PCOS
    if arr[18] == 'no':
        pass
    else:
        ring_score += weights[17]
    
    # Endometriosis
    if arr[19] == 'no':
        pass
    else:
        ring_score += weights[18]
    
    # Top Gender Dysphoria
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        ring_score += weights[19][0]
    elif arr[20] == 'moderate':
        ring_score += weights[19][1]
    else:
        ring_score += weights[19][2]
    
    # Top Surgery
    if arr[21] == 'no':
        pass
    elif arr[21] == 'mild':
        ring_score += weights[20][0]
    elif arr[21] == 'moderate':
        ring_score += weights[20][1]
    else:
        ring_score += weights[20][2]

    # BGDP
    if arr[22] == 'no':
        pass
    else:
        ring_score += weights[21]

    # GDVI

    
    # GDP
    if arr[23] == 'no':
        pass
    else:
        ring_score += weights[22]

    # HRT
    if arr[24] == 'no':
        pass
    else:
        ring_score += weights[23]
    
    return ring_score
        
def score_shot(arr):
    shot_score = 3

    if arr[1] == "v_unp":
        shot_score -= 1.5
    elif arr[1] == "unp":
        shot_score -= 1
    elif arr[1] == "sl_unp":
        shot_score -= 0.5
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        shot_score += 0.5
    elif arr[1] == "imp":
        shot_score += 1
    else:
        shot_score += 1.5
    
    if arr[2] == "v_unp":
        shot_score -= 3
    elif arr[2] == "unp":
        shot_score -= 2
    elif arr[2] == "sl_unp":
        shot_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        shot_score += 1
    elif arr[2] == "imp":
        shot_score += 2
    else:
        shot_score += 3
    
    if arr[3] == "v_unp":
        shot_score += 3
    elif arr[3] == "unp":
        shot_score += 2
    elif arr[3] == "sl_unp":
        shot_score += 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        shot_score -= 1
    elif arr[3] == "imp":
        shot_score -= 2
    else:
        shot_score -= 3
    
    if arr[4] == "monthly":
        shot_score += 3
    
    if arr[5] == 'p':
        shot_score += 3
    elif arr[5] == 'ep':
        shot_score += 3
    else:
        pass

    if arr[6] == "v_unp":
        shot_score -= 3
    elif arr[6] == "unp":
        shot_score -= 2
    elif arr[6] == "sl_unp":
        shot_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        shot_score += 1
    elif arr[6] == "imp":
        shot_score += 2
    else:
        shot_score += 3
    
    if arr[7] == "v_unp":
        shot_score -= 3
    elif arr[7] == "unp":
        shot_score -= 2
    elif arr[7] == "sl_unp":
        shot_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        shot_score += 1
    elif arr[7] == "imp":
        shot_score += 2
    else:
        shot_score += 3
    
    if arr[8] == 'no':
        pass
    else:
        shot_score += 3
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        shot_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        shot_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        shot_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        shot_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        shot_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        shot_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        shot_score -= 7.5
    elif arr[10] == 'moderate' and arr[9] != 'no':
        shot_score -= 12.5
    elif arr[10] == 'severe' and arr[9] != 'no':
        shot_score -= 25
    elif arr[10] == 'mild' and arr[9] == 'no':
        shot_score -= 15
    elif arr[10] == 'moderate' and arr[9] == 'no':
        shot_score -= 25
    elif arr[10]== 'severe' and arr[9] == 'no':
        shot_score -= 50
    
    if arr[11] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[14] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[15] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[16] == 'no':
        pass
    else:
        shot_score -= 100
    
    if arr[17] == 'no':
        pass
    else:
        shot_score +=3

    if arr[18] == 'no':
        pass
    else:
        shot_score +=3
    
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        shot_score -= 15
    elif arr[19] == 'moderate':
        shot_score -= 25
    else:
        shot_score -= 50
    
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        shot_score -= 15
    elif arr[20] == 'moderate':
        shot_score -= 25
    else:
        shot_score -= 50
    
    if arr[21] == 'no':
        pass
    else:
        shot_score += 3
    
    if arr[22] == 'no':
        pass
    else:
        shot_score += 1.5
    
    if arr[23] == 'no':
        pass
    else:
        shot_score -= 100
    
    return shot_score

def change_score_shot(arr, weights):
    shot_score = 3

    # Pregnancy Prevention
    if arr[1] == "v_unp":
        shot_score += weights[0][0]
    elif arr[1] == "unp":
        shot_score += weights[0][1]
    elif arr[1] == "sl_unp":
        shot_score += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        shot_score += weights[0][3]
    elif arr[1] == "imp":
        shot_score += weights[0][4]
    else:
        shot_score += weights[0][5]
    
    # Management of Periods
    if arr[2] == "v_unp":
        shot_score += weights[1][0]
    elif arr[2] == "unp":
        shot_score += weights[1][1]
    elif arr[2] == "sl_unp":
        shot_score += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        shot_score += weights[1][3]
    elif arr[2] == "imp":
        shot_score += weights[1][4]
    else:
        shot_score += weights[1][5]
    
    # Weight Management
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
    
     # Maintainance
    if arr[4] == "monthly":
        shot_score += weights[3]
    
    # Hormones
    if arr[5] == 'p':
        shot_score += weights[4][0]
    elif arr[5] == 'ep':
        shot_score += weights[4][1]
    else:
        pass

    # Seeking consultation
    if arr[6] == "v_unp":
        shot_score += weights[5][0]
    elif arr[6] == "unp":
        shot_score += weights[5][1]
    elif arr[6] == "sl_unp":
        shot_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        shot_score += weights[5][3]
    elif arr[6] == "imp":
        shot_score += weights[5][4]
    else:
        shot_score += weights[5][5]
    
    # Medical Procedure
    if arr[7] == "v_unp":
        shot_score += weights[6][0]
    elif arr[7] == "unp":
        shot_score += weights[6][1]
    elif arr[7] == "sl_unp":
        shot_score += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        shot_score += weights[6][3]
    elif arr[7] == "imp":
        shot_score += weights[6][4]
    else:
        shot_score += weights[6][5]
    
    # Acne
    if arr[8] == 'no':
        pass
    else:
        shot_score += weights[7]
    
    # Anxiety
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        shot_score += weights[8][0]
    elif arr[9] == 'moderate' and arr[10] != 'no':
        shot_score += weights[8][1]
    elif arr[9]=='severe' and arr[10] != 'no':
        shot_score += weights[8][2]
    elif arr[9] == 'mild' and arr[10] == 'no':
        shot_score += weights[8][3]
    elif arr[9] == 'moderate' and arr[10] == 'no':
        shot_score += weights[8][4]
    elif arr[9]== 'severe' and arr[10] == 'no':
        shot_score += weights[8][5]
    
    # Depression
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        shot_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[9] != 'no':
        shot_score += weights[9][1]
    elif arr[10] == 'severe' and arr[9] != 'no':
        shot_score += weights[9][2]
    elif arr[10] == 'mild' and arr[9] == 'no':
        shot_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[9] == 'no':
        shot_score += weights[9][4]
    elif arr[10]== 'severe' and arr[9] == 'no':
        shot_score += weights[9][5]
    
    # Hyper
    if arr[11] == 'no':
        pass
    else:
        shot_score += weights[10]
    
    # Blood Clots
    if arr[12] == 'no':
        pass
    else:
        shot_score += weights[11]
    
    # CHF_CAD
    if arr[13] == 'no':
        pass
    else:
        shot_score += weights[12]
    
    # Breast
    if arr[14] == 'no':
        pass
    else:
        shot_score += weights[13]
    
    # Smoker
    if arr[15] == 'no':
        pass
    else:
        shot_score += weights[14]
    
    # Migraine
    if arr[16] == 'no':
        pass
    else:
        shot_score += weights[15]
    
    # PCOS
    if arr[17] == 'no':
        pass
    else:
        shot_score += weights[16]

    # Endometriosis
    if arr[18] == 'no':
        pass
    else:
        shot_score += weights[17]
    
    # Top gender dysphoria
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        shot_score += weights[18][0]
    elif arr[19] == 'moderate':
        shot_score += weights[18][1]
    else:
        shot_score += weights[18][2]
    
    # Top Surgery
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        shot_score += weights[19][0]
    elif arr[20] == 'moderate':
        shot_score += weights[19][1]
    else:
        shot_score += weights[19][2]
    
    # BGDP
    if arr[21] == 'no':
        pass
    else:
        shot_score += weights[20]
    
    # Gender Dypshoria Preganancy
    if arr[22] == 'no':
        pass
    else:
        shot_score += weights[21]
    
    # HRT
    if arr[23] == 'no':
        pass
    else:
        shot_score += weights[22]
    
    return shot_score

def score_combo_pill(arr):
    combo_pill_score = 3

    if arr[1] == "v_unp":
        combo_pill_score -= 3
    elif arr[1] == "unp":
        combo_pill_score -= 2
    elif arr[1] == "sl_unp":
        combo_pill_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        combo_pill_score += 1
    elif arr[1] == "imp":
        combo_pill_score += 2
    else:
        combo_pill_score += 3
    
    if arr[2] == "v_unp":
        combo_pill_score -= 1.5
    elif arr[2] == "unp":
        combo_pill_score -= 1
    elif arr[2] == "sl_unp":
        combo_pill_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        combo_pill_score += 0.5
    elif arr[2] == "imp":
        combo_pill_score += 1
    else:
        combo_pill_score += 1.5
    
    if arr[3] == "v_unp":
        combo_pill_score -= 3
    elif arr[3] == "unp":
        combo_pill_score -= 2
    elif arr[3] == "sl_unp":
        combo_pill_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        combo_pill_score += 1
    elif arr[3] == "imp":
        combo_pill_score += 2
    else:
        combo_pill_score += 3
    
    if arr[4] == "v_unp":
        combo_pill_score += 3
    elif arr[4] == "unp":
        combo_pill_score += 2
    elif arr[4] == "sl_unp":
        combo_pill_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        combo_pill_score -= 1
    elif arr[4] == "imp":
        combo_pill_score -= 2
    else:
        combo_pill_score -= 3
    
    if arr[5] == "daily":
        combo_pill_score += 3
    
    if arr[6] == 'ep':
        combo_pill_score += 3
    else:
        pass

    if arr[7] == "v_unp":
        combo_pill_score -= 3
    elif arr[7] == "unp":
        combo_pill_score -= 2
    elif arr[7] == "sl_unp":
        combo_pill_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        combo_pill_score+= 1
    elif arr[7] == "imp":
        combo_pill_score += 2
    else:
        combo_pill_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        combo_pill_score -= 15
    elif arr[8] == 'moderate':
        combo_pill_score -= 25
    else:
        combo_pill_score -= 50

    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        combo_pill_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        combo_pill_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        combo_pill_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        combo_pill_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        combo_pill_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        combo_pill_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        combo_pill_score -= 7.5
    elif arr[10] == 'moderate' and arr[9] != 'no':
        combo_pill_score -= 12.5
    elif arr[10] == 'severe' and arr[9] != 'no':
        combo_pill_score -= 25
    elif arr[10] == 'mild' and arr[9] == 'no':
        combo_pill_score -= 15
    elif arr[10] == 'moderate' and arr[9] == 'no':
        combo_pill_score -= 25
    elif arr[10]== 'severe' and arr[9] == 'no':
        combo_pill_score -= 50
    
    if arr[11] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[14] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[15] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[16] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    if arr[17] == 'no':
        pass
    else:
        combo_pill_score += 3
    
    if arr[18] == 'no':
        pass
    else:
        combo_pill_score += 3
    
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        combo_pill_score -= 15
    elif arr[19] == 'moderate':
        combo_pill_score -= 25
    else:
        combo_pill_score -= 50
    
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        combo_pill_score -= 15
    elif arr[20] == 'moderate':
        combo_pill_score -= 25
    else:
        combo_pill_score -= 50
    
    if arr[21] == 'no':
        pass
    else:
         combo_pill_score += 3
    
    if arr[22] == 'no':
        pass
    else:
         combo_pill_score += 1.5
    
    if arr[23] == 'no':
        pass
    else:
        combo_pill_score -= 100
    
    return combo_pill_score


def change_score_combo_pill(arr, weights):
    combo_pill_score = 3

    if arr[1] == "v_unp":
        combo_pill_score += weights[0][0]
    elif arr[1] == "unp":
        combo_pill_score += weights[0][1]
    elif arr[1] == "sl_unp":
        combo_pill_score += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        combo_pill_score += weights[0][3]
    elif arr[1] == "imp":
        combo_pill_score += weights[0][4]
    else:
        combo_pill_score += weights[0][5]
    
    if arr[2] == "v_unp":
        combo_pill_score += weights[1][0]
    elif arr[2] == "unp":
        combo_pill_score += weights[1][1]
    elif arr[2] == "sl_unp":
        combo_pill_score += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        combo_pill_score += weights[1][3]
    elif arr[2] == "imp":
        combo_pill_score += weights[1][4]
    else:
        combo_pill_score += weights[1][5]
    
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
    
    if arr[5] == "daily":
        combo_pill_score += weights[4]
    
    if arr[6] == 'ep':
        combo_pill_score += weights[5]
    else:
        pass

    if arr[7] == "v_unp":
        combo_pill_score += weights[6][0]
    elif arr[7] == "unp":
        combo_pill_score += weights[6][1]
    elif arr[7] == "sl_unp":
        combo_pill_score += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        combo_pill_score+= weights[6][3]
    elif arr[7] == "imp":
        combo_pill_score += weights[6][4]
    else:
        combo_pill_score += weights[6][5]
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        combo_pill_score += weights[7][0]
    elif arr[8] == 'moderate':
        combo_pill_score += weights[7][1]
    else:
        combo_pill_score += weights[7][2]

    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        combo_pill_score += weights[8][0]
    elif arr[9] == 'moderate' and arr[10] != 'no':
        combo_pill_score += weights[8][1]
    elif arr[9]=='severe' and arr[10] != 'no':
        combo_pill_score += weights[8][2]
    elif arr[9] == 'mild' and arr[10] == 'no':
        combo_pill_score += weights[8][3]
    elif arr[9] == 'moderate' and arr[10] == 'no':
        combo_pill_score += weights[8][4]
    elif arr[9]== 'severe' and arr[10] == 'no':
        combo_pill_score += weights[8][5]
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        combo_pill_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[9] != 'no':
        combo_pill_score += weights[9][1]
    elif arr[10] == 'severe' and arr[9] != 'no':
        combo_pill_score += weights[9][2]
    elif arr[10] == 'mild' and arr[9] == 'no':
        combo_pill_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[9] == 'no':
        combo_pill_score += weights[9][4]
    elif arr[10]== 'severe' and arr[9] == 'no':
        combo_pill_score += weights[9][5]
    
    if arr[11] == 'no':
        pass
    else:
        combo_pill_score += weights[10]
    
    if arr[12] == 'no':
        pass
    else:
        combo_pill_score += weights[11]
    
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
    elif arr[19] == 'mild':
        combo_pill_score += weights[18][0]
    elif arr[19] == 'moderate':
        combo_pill_score += weights[18][1]
    else:
        combo_pill_score += weights[18][2]
    
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        combo_pill_score += weights[19][0]
    elif arr[20] == 'moderate':
        combo_pill_score += weights[19][1]
    else:
        combo_pill_score += weights[19][2]
    
    if arr[21] == 'no':
        pass
    else:
         combo_pill_score += weights[20]
    
    if arr[22] == 'no':
        pass
    else:
         combo_pill_score += weights[21]
    
    if arr[23] == 'no':
        pass
    else:
        combo_pill_score += weights[22]
    
    return combo_pill_score

def score_patch(arr):
    patch_score = 3

    if arr[1] == "v_unp":
        patch_score -= 3
    elif arr[1] == "unp":
        patch_score -= 2
    elif arr[1] == "sl_unp":
        patch_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        patch_score += 1
    elif arr[1] == "imp":
        patch_score += 2
    else:
        patch_score += 3
    
    if arr[2] == "v_unp":
        patch_score -= 1.5
    elif arr[2] == "unp":
        patch_score -= 1
    elif arr[2] == "sl_unp":
        patch_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        patch_score += 0.5
    elif arr[2] == "imp":
        patch_score += 1
    else:
        patch_score += 1.5
    
    if arr[3] == "v_unp":
        patch_score -= 3
    elif arr[3] == "unp":
        patch_score -= 2
    elif arr[3] == "sl_unp":
        patch_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        patch_score += 1
    elif arr[3] == "imp":
        patch_score += 2
    else:
        patch_score += 3
    
    if arr[4] == "v_unp":
        patch_score += 3
    elif arr[4] == "unp":
        patch_score += 2
    elif arr[4] == "sl_unp":
        patch_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        patch_score -= 1
    elif arr[4] == "imp":
        patch_score -= 2
    else:
        patch_score -= 3
    
    if arr[5] == "weekly":
        patch_score += 3
    
    if arr[6] == 'ep':
        patch_score += 3
    else:
        pass

    if arr[7] == "v_unp":
        patch_score -= 3
    elif arr[7] == "unp":
        patch_score -= 2
    elif arr[7] == "sl_unp":
        patch_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        patch_score+= 1
    elif arr[7] == "imp":
        patch_score += 2
    else:
        patch_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        patch_score -= 15
    elif arr[8] == 'moderate':
        patch_score -= 25
    else:
        patch_score -= 50

    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        patch_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        patch_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        patch_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        patch_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        patch_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        patch_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        patch_score -= 7.5
    elif arr[10] == 'moderate' and arr[9] != 'no':
        patch_score -= 12.5
    elif arr[10] == 'severe' and arr[9] != 'no':
        patch_score -= 25
    elif arr[10] == 'mild' and arr[9] == 'no':
        patch_score -= 15
    elif arr[10] == 'moderate' and arr[9] == 'no':
        patch_score -= 25
    elif arr[10]== 'severe' and arr[9] == 'no':
        patch_score -= 50
    
    if arr[11] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[14] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[15] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[16] == 'no':
        pass
    else:
        patch_score -= 100
    
    if arr[17] == 'no':
        pass
    else:
        patch_score += 3
    
    if arr[18] == 'no':
        pass
    else:
        patch_score += 3
    
    if arr[19] == 'no':
        pass
    elif arr[19] == 'mild':
        patch_score -= 15
    elif arr[19] == 'moderate':
        patch_score -= 25
    else:
        patch_score -= 50
    
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        patch_score -= 15
    elif arr[20] == 'moderate':
        patch_score -= 25
    else:
        patch_score -= 50
    
    if arr[21] == 'no':
        pass
    else:
         patch_score += 3
    
    if arr[22] == 'no':
        pass
    else:
         patch_score += 1.5
    
    if arr[23] == 'no':
        pass
    else:
        patch_score -= 100
    
    return patch_score

def change_score_patch(arr, weights):
    patch_score = 3

    if arr[1] == "v_unp":
        patch_score += weights[0][0]
    elif arr[1] == "unp":
        patch_score += weights[0][1]
    elif arr[1] == "sl_unp":
        patch_score += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        patch_score += weights[0][3]
    elif arr[1] == "imp":
        patch_score += weights[0][4]
    else:
        patch_score += weights[0][5]
    
    if arr[2] == "v_unp":
        patch_score += weights[1][0]
    elif arr[2] == "unp":
        patch_score += weights[1][1]
    elif arr[2] == "sl_unp":
        patch_score += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        patch_score += weights[1][3]
    elif arr[2] == "imp":
        patch_score += weights[1][4]
    else:
        patch_score += weights[1][5]
    
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
    
    if arr[5] == "weekly":
        patch_score += weights[4]
    
    if arr[6] == 'ep':
        patch_score += weights[5]
    else:
        pass

    if arr[7] == "v_unp":
        patch_score += weights[6][0]
    elif arr[7] == "unp":
        patch_score += weights[6][1]
    elif arr[7] == "sl_unp":
        patch_score += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        patch_score+= weights[6][3]
    elif arr[7] == "imp":
        patch_score += weights[6][4]
    else:
        patch_score += weights[6][5]
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        patch_score += weights[7][0]
    elif arr[8] == 'moderate':
        patch_score += weights[7][1]
    else:
        patch_score += weights[7][2]

    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        patch_score += weights[8][0]
    elif arr[9] == 'moderate' and arr[10] != 'no':
        patch_score += weights[8][1]
    elif arr[9]=='severe' and arr[10] != 'no':
        patch_score += weights[8][2]
    elif arr[9] == 'mild' and arr[10] == 'no':
        patch_score += weights[8][3]
    elif arr[9] == 'moderate' and arr[10] == 'no':
        patch_score += weights[8][4]
    elif arr[9]== 'severe' and arr[10] == 'no':
        patch_score += weights[8][5]
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        patch_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[9] != 'no':
        patch_score += weights[9][1]
    elif arr[10] == 'severe' and arr[9] != 'no':
        patch_score += weights[9][2]
    elif arr[10] == 'mild' and arr[9] == 'no':
        patch_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[9] == 'no':
        patch_score += weights[9][4]
    elif arr[10]== 'severe' and arr[9] == 'no':
        patch_score += weights[9][5]
    
    if arr[11] == 'no':
        pass
    else:
        patch_score += weights[10]
    
    if arr[12] == 'no':
        pass
    else:
        patch_score += weights[11]
    
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
    elif arr[19] == 'mild':
        patch_score += weights[18][0]
    elif arr[19] == 'moderate':
        patch_score += weights[18][1]
    else:
        patch_score += weights[18][2]
    
    if arr[20] == 'no':
        pass
    elif arr[20] == 'mild':
        patch_score += weights[19][0]
    elif arr[20] == 'moderate':
        patch_score += weights[19][1]
    else:
        patch_score += weights[19][2]
    
    if arr[21] == 'no':
        pass
    else:
         patch_score += weights[20]
    
    if arr[22] == 'no':
        pass
    else:
         patch_score += weights[21]
    
    if arr[23] == 'no':
        pass
    else:
        patch_score += weights[22]
    
    return patch_score

def score_hormonal_iud(arr):
    hormonal_iud_score = 3
    if arr[1] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[1] == "unp":
        hormonal_iud_score -= 2
    elif arr[1] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[1] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[2] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[2] == "unp":
        hormonal_iud_score -= 2
    elif arr[2] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[2] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3

    if arr[3] == "v_unp":
        hormonal_iud_score += 3
    elif arr[3] == "unp":
        hormonal_iud_score += 2
    elif arr[3] == "sl_unp":
        hormonal_iud_score += 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        hormonal_iud_score -= 1
    elif arr[3] == "imp":
        hormonal_iud_score -= 2
    else:
        hormonal_iud_score -= 3
    
    if arr[4] == "yearly":
        hormonal_iud_score += 3
    
    if arr[5] == 'p':
        hormonal_iud_score += 3
    elif arr[5] == 'ep':
        hormonal_iud_score += 3
    else:
        pass
    
    if arr[6] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[6] == "unp":
        hormonal_iud_score -= 2
    elif arr[6] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[6] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[7] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[7] == "unp":
        hormonal_iud_score -= 2
    elif arr[7] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[7] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[8] == "v_unp":
        hormonal_iud_score -= 3
    elif arr[8] == "unp":
        hormonal_iud_score -= 2
    elif arr[8] == "sl_unp":
        hormonal_iud_score -= 1
    elif arr[8] == "neutral":
        pass
    elif arr[8] == "sl_imp":
        hormonal_iud_score += 1
    elif arr[8] == "imp":
        hormonal_iud_score += 2
    else:
        hormonal_iud_score += 3
    
    if arr[9] == 'no':
        pass
    elif arr[9]  == 'mild':
        hormonal_iud_score -= 15
    elif arr[9] == 'moderate':
        hormonal_iud_score -= 25
    else:
        hormonal_iud_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[11] != 'no':
        hormonal_iud_score -= 7.5
    elif arr[10] == 'moderate' and arr[11] != 'no':
        hormonal_iud_score -= 12.5
    elif arr[10]=='severe' and arr[11] != 'no':
        hormonal_iud_score -= 25
    elif arr[10] == 'mild' and arr[11] == 'no':
        hormonal_iud_score -= 15
    elif arr[10] == 'moderate' and arr[11] == 'no':
        hormonal_iud_score -= 25
    elif arr[10]== 'severe' and arr[11] == 'no':
        hormonal_iud_score -= 50
    
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        hormonal_iud_score -= 7.5
    elif arr[11] == 'moderate' and arr[10] != 'no':
        hormonal_iud_score -= 12.5
    elif arr[11] == 'severe' and arr[10] != 'no':
        hormonal_iud_score -= 25
    elif arr[11] == 'mild' and arr[10] == 'no':
        hormonal_iud_score -= 15
    elif arr[11] == 'moderate' and arr[10] == 'no':
        hormonal_iud_score -= 25
    elif arr[11]== 'severe' and arr[10] == 'no':
        hormonal_iud_score -= 50
    
    if arr[12] == 'no':
        pass
    else:
        hormonal_iud_score -= 100
    
    if arr[13] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    if arr[14] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    if arr[15] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    if arr[16] == 'no':
        pass
    elif arr[16]  == 'mild':
        hormonal_iud_score -= 15
    elif arr[16] == 'moderate':
        hormonal_iud_score -= 25
    else:
        hormonal_iud_score -= 50
    
    if arr[17] == 'no':
        pass
    else:
        hormonal_iud_score += 3
    
    return hormonal_iud_score 

def change_score_hormonal_iud(arr, weights):
    hormonal_iud_score = 3
    if arr[1] == "v_unp":
        hormonal_iud_score += weights[0][0]
    elif arr[1] == "unp":
        hormonal_iud_score += weights[0][1]
    elif arr[1] == "sl_unp":
        hormonal_iud_score += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        hormonal_iud_score += weights[0][3]
    elif arr[1] == "imp":
        hormonal_iud_score += weights[0][4]
    else:
        hormonal_iud_score += weights[0][5]
    
    if arr[2] == "v_unp":
        hormonal_iud_score += weights[1][0]
    elif arr[2] == "unp":
        hormonal_iud_score += weights[1][1]
    elif arr[2] == "sl_unp":
        hormonal_iud_score += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        hormonal_iud_score += weights[1][3]
    elif arr[2] == "imp":
        hormonal_iud_score += weights[1][4]
    else:
        hormonal_iud_score += weights[1][5]

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
    
    if arr[4] == "yearly":
        hormonal_iud_score += weights[3]
    
    if arr[5] == 'p':
        hormonal_iud_score += weights[4][0]
    elif arr[5] == 'ep':
        hormonal_iud_score += weights[4][1]
    else:
        pass
    
    if arr[6] == "v_unp":
        hormonal_iud_score += weights[5][0]
    elif arr[6] == "unp":
        hormonal_iud_score += weights[5][1]
    elif arr[6] == "sl_unp":
        hormonal_iud_score += weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        hormonal_iud_score += weights[5][3]
    elif arr[6] == "imp":
        hormonal_iud_score += weights[5][4]
    else:
        hormonal_iud_score += weights[5][5]
    
    if arr[7] == "v_unp":
        hormonal_iud_score += weights[6][0]
    elif arr[7] == "unp":
        hormonal_iud_score += weights[6][1]
    elif arr[7] == "sl_unp":
        hormonal_iud_score += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        hormonal_iud_score += weights[6][3]
    elif arr[7] == "imp":
        hormonal_iud_score += weights[6][4]
    else:
        hormonal_iud_score += weights[6][5]
    
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
    
    if arr[9] == 'no':
        pass
    elif arr[9]  == 'mild':
        hormonal_iud_score += weights[8][0]
    elif arr[9] == 'moderate':
        hormonal_iud_score += weights[8][1]
    else:
        hormonal_iud_score += weights[8][2]
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[11] != 'no':
        hormonal_iud_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[11] != 'no':
        hormonal_iud_score += weights[9][1]
    elif arr[10]=='severe' and arr[11] != 'no':
        hormonal_iud_score += weights[9][2]
    elif arr[10] == 'mild' and arr[11] == 'no':
        hormonal_iud_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[11] == 'no':
        hormonal_iud_score += weights[9][4]
    elif arr[10]== 'severe' and arr[11] == 'no':
        hormonal_iud_score += weights[9][5]
    
    if arr[11] == 'no':
        pass
    elif arr[11] == 'mild' and arr[10] != 'no':
        hormonal_iud_score += weights[10][0]
    elif arr[11] == 'moderate' and arr[10] != 'no':
        hormonal_iud_score += weights[10][1]
    elif arr[11] == 'severe' and arr[10] != 'no':
        hormonal_iud_score += weights[10][2]
    elif arr[11] == 'mild' and arr[10] == 'no':
        hormonal_iud_score += weights[10][3]
    elif arr[11] == 'moderate' and arr[10] == 'no':
        hormonal_iud_score += weights[10][4]
    elif arr[11]== 'severe' and arr[10] == 'no':
        hormonal_iud_score += weights[10][5]
    
    if arr[12] == 'no':
        pass
    else:
        hormonal_iud_score += weights[11]
    
    if arr[13] == 'no':
        pass
    else:
        hormonal_iud_score += weights[12]
    
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
    elif arr[16]  == 'mild':
        hormonal_iud_score += weights[15][0]
    elif arr[16] == 'moderate':
        hormonal_iud_score += weights[15][1]
    else:
        hormonal_iud_score += weights[15][2]
    
    if arr[17] == 'no':
        pass
    else:
        hormonal_iud_score += weights[16]
    
    return hormonal_iud_score 

# Condoms
print("Condoms Done")
def score_condoms(arr):
    score_condoms = 3
    if arr[1] == "v_unp":
        score_condoms -= 3
    elif arr[1] == "unp":
        score_condoms -= 2
    elif arr[1] == "sl_unp":
        score_condoms -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_condoms += 1
    elif arr[1] == "imp":
        score_condoms += 2
    else:
        score_condoms += 3
    
    if arr[2] == "v_unp":
        score_condoms -= 1.5
    elif arr[2] == "unp":
        score_condoms -= 1
    elif arr[2] == "sl_unp":
        score_condoms -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        score_condoms += 0.5
    elif arr[2] == "imp":
        score_condoms += 1
    else:
        score_condoms += 1.5
    
    if arr[3] == "daily":
        score_condoms += 3
    else:
        pass

    if arr[4] == "v_unp":
        score_condoms -= 3
    elif arr[4] == "unp":
        score_condoms -= 2
    elif arr[4] == "sl_unp":
        score_condoms -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_condoms += 1
    elif arr[4] == "imp":
        score_condoms += 2
    else:
        score_condoms += 3
    
    if arr[5] == "v_unp":
        score_condoms -= 3
    elif arr[5] == "unp":
        score_condoms -= 2
    elif arr[5] == "sl_unp":
        score_condoms -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        score_condoms += 1
    elif arr[5] == "imp":
        score_condoms += 2
    else:
        score_condoms += 3
    
    if arr[6] == "none":
        score_condoms += 3
    
    if arr[7] == 'no':
        pass
    else:
        score_condoms += 1.5

    return score_condoms

def change_score_condoms(arr, weights):
    score_condoms = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        score_condoms += 1 * weights[0][0]
    elif arr[1] == "unp":
        score_condoms += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        score_condoms += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_condoms += 1 * weights[0][3]
    elif arr[1] == "imp":
        score_condoms += 1 * weights[0][4]
    else:
        score_condoms += 1 * weights[0][5]
    
    # Pregnancy prevention
    if arr[2] == "v_unp":
        score_condoms += 1 * weights[1][0]
    elif arr[2] == "unp":
        score_condoms += 1  * weights[1][1]
    elif arr[2] == "sl_unp":
        score_condoms += 1 * weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        score_condoms += 1 * weights[1][3]
    elif arr[2] == "imp":
        score_condoms += 1 * weights[1][4]
    else:
        score_condoms += 1 * weights[1][5]
    
    # Maintainance
    if arr[3] == "daily":
        score_condoms += 1 * weights[2]
    else:
        pass

    # Partner Willingness
    if arr[4] == "v_unp":
        score_condoms += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_condoms += 1 * weights[3][1]
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
    
    # STI
    if arr[5] == "v_unp":
        score_condoms += 1 * weights[4][0]
    elif arr[5] == "unp":
        score_condoms += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        score_condoms += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        score_condoms += 1 * weights[4][3]
    elif arr[5] == "imp":
        score_condoms += 1 * weights[4][4]
    else:
        score_condoms += 1 * weights[4][5]
    
    # Bottom gender dysphoria pregnancy
    if arr[6] == "none":
        score_condoms += weights[5]

    if arr[7] == 'no':
        pass
    else:
        score_condoms += 1 * weights[6]
    
    return score_condoms

def score_internal_condoms(arr):
    internal_condom_score = 3

    if arr[1] == "v_unp":
        internal_condom_score -= 3
    elif arr[1] == "unp":
        internal_condom_score -= 2
    elif arr[1] == "sl_unp":
        internal_condom_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        internal_condom_score += 1
    elif arr[1] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3

    if arr[2] == "v_unp":
        internal_condom_score -= 1.5
    elif arr[2] == "unp":
        internal_condom_score -= 1
    elif arr[2] == "sl_unp":
        internal_condom_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        internal_condom_score += 0.5
    elif arr[2] == "imp":
        internal_condom_score += 1
    else:
        internal_condom_score += 1.5
    
    
    
    if arr[3] == 'daily':
        internal_condom_score += 3
    else:
        pass

    if arr[4] == "v_unp":
        internal_condom_score -= 3
    elif arr[4] == "unp":
        internal_condom_score -= 2
    elif arr[4] == "sl_unp":
        internal_condom_score -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        internal_condom_score += 1
    elif arr[4] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3
    
    if arr[5] == "v_unp":
        internal_condom_score -= 3
    elif arr[5] == "unp":
        internal_condom_score -= 2
    elif arr[5] == "sl_unp":
        internal_condom_score -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        internal_condom_score += 1
    elif arr[5] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3

    if arr[6] == "none":
        internal_condom_score += 3
    
    if arr[7] == "v_unp":
        internal_condom_score -= 3
    elif arr[7] == "unp":
        internal_condom_score -= 2
    elif arr[7] == "sl_unp":
        internal_condom_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        internal_condom_score += 1
    elif arr[7] == "imp":
        internal_condom_score += 2
    else:
        internal_condom_score += 3
    
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        internal_condom_score -= 15
    elif arr[8] == 'moderate':
        internal_condom_score -= 25
    else:
        internal_condom_score -= 50
    
    if arr[9] == 'no':
        pass
    else:
        internal_condom_score += 1.5
    
    return internal_condom_score

def change_internal_condoms(arr, weights):
    score_internal_condoms = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        score_internal_condoms += 1 * weights[0][0]
    elif arr[1] == "unp":
        score_internal_condoms += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        score_internal_condoms += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_internal_condoms += 1 * weights[0][3]
    elif arr[1] == "imp":
        score_internal_condoms += 1 * weights[0][4]
    else:
        score_internal_condoms += 1 * weights[0][5]
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        score_internal_condoms += 1 * weights[1][0]
    elif arr[2] == "unp":
        score_internal_condoms += 1  * weights[1][1]
    elif arr[2] == "sl_unp":
        score_internal_condoms += 1 * weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        score_internal_condoms += 1 * weights[1][3]
    elif arr[2] == "imp":
        score_internal_condoms += 1 * weights[1][4]
    else:
        score_internal_condoms += 1 * weights[1][5]
    
    # Maintainance
    if arr[3] == "daily":
        score_internal_condoms += 1 * weights[2]
    else:
        pass

    # Partner Willingness
    if arr[4] == "v_unp":
        score_internal_condoms += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_internal_condoms += 1 * weights[3][1]
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
    
    # Prevents STI
    if arr[5] == "v_unp":
        score_internal_condoms += 1 * weights[4][0]
    elif arr[5] == "unp":
        score_internal_condoms += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        score_internal_condoms += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        score_internal_condoms += 1 * weights[4][3]
    elif arr[5] == "imp":
        score_internal_condoms += 1 * weights[4][4]
    else:
        score_internal_condoms += 1 * weights[4][5]
    
    if arr[6] == "none":
        score_internal_condoms += weights[5]
    
    # Vaginal Insertion
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
    
    # Gender Dysphoria Vaginal Insertion
    if arr[8] == "no":
        pass
    elif arr[8] == "mild":
        score_internal_condoms += weights[7][0]
    elif arr[8] == "moderate":
        score_internal_condoms += weights[7][1]
    else:
        score_internal_condoms += weights[7][2]
    
    # Gender Dysphoria Pregnancy
    if arr[9] == "no":
        pass
    
    else:
        score_internal_condoms += weights[8]

    return score_internal_condoms
# Cervical Cap

def scoring_cervical_cap(arr):
    cervical_cap_score = 3

    if arr[1] == "v_unp":
        cervical_cap_score -= 3
    elif arr[1] == "unp":
        cervical_cap_score -= 2
    elif arr[1] == "sl_unp":
        cervical_cap_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        cervical_cap_score += 1
    elif arr[1] == "imp":
        cervical_cap_score += 2
    else:
        cervical_cap_score += 3
    
    if arr[2] == "daily":
        cervical_cap_score += 3
    
    if arr[3] == "none":
        cervical_cap_score += 3
    
    if arr[4] == "v_unp":
        cervical_cap_score -= 3
    elif arr[4] == "unp":
        cervical_cap_score -= 2
    elif arr[4] == "sl_unp":
        cervical_cap_score -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        cervical_cap_score += 1
    elif arr[4] == "imp":
        cervical_cap_score += 2
    else:
        cervical_cap_score += 3

    if arr[5] == "v_unp":
        cervical_cap_score -= 3
    elif arr[5] == "unp":
        cervical_cap_score -= 2
    elif arr[5] == "sl_unp":
        cervical_cap_score -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        cervical_cap_score += 1
    elif arr[5] == "imp":
        cervical_cap_score += 2
    else:
        cervical_cap_score += 3
    
    if arr[6] == 'no':
        pass
    elif arr[6] == 'mild':
        cervical_cap_score -= 15
    elif arr[6] == 'moderate':
        cervical_cap_score -= 25
    else:
        cervical_cap_score -= 50
    
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        cervical_cap_score -= 15
    elif arr[7] == 'moderate':
        cervical_cap_score -= 25
    else:
        cervical_cap_score -= 50
    
    return cervical_cap_score

def change_score_cervical_cap(arr, weights):
    score_cervical_cap = 3

    # Cost effectiveness
    if arr[1] == "v_unp":
        score_cervical_cap += 1 * weights[0][0]
    elif arr[1] == "unp":
        score_cervical_cap += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        score_cervical_cap += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_cervical_cap += 1 * weights[0][3]
    elif arr[1] == "imp":
        score_cervical_cap += 1 * weights[0][4]
    else:
        score_cervical_cap += 1 * weights[0][5]

    # Maintainance
    if arr[2] == "daily":
        score_cervical_cap += 1 * weights[1]
    else:
        pass

    if arr[3] == "none":
        score_cervical_cap += weights[2]

    # Vaginal insertion
    if arr[4] == "v_unp":
        score_cervical_cap += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_cervical_cap += 1 * weights[3][1]
    elif arr[4] == "sl_unp":
        score_cervical_cap += 1 * weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_cervical_cap += 1 * weights[3][3]
    elif arr[4] == "imp":
        score_cervical_cap += 1 * weights[3][4]
    else:
        score_cervical_cap += 1 * weights[3][5]
    
    # Seeking consultation
    if arr[5] == "v_unp":
        score_cervical_cap += 1 * weights[4][0]
    elif arr[5] == "unp":
        score_cervical_cap += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        score_cervical_cap += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        score_cervical_cap += 1 * weights[4][3]
    elif arr[5] == "imp":
        score_cervical_cap += 1 * weights[4][4]
    else:
        score_cervical_cap += 1 * weights[4][5]
    
    # Gender Dysphoria Vaginal Insertion
    if arr[6] == 'no':
        pass
    elif arr[6] == 'mild':
        score_cervical_cap += 1 * weights[5][0]
    elif arr[6] == 'moderate':
        score_cervical_cap += 1 * weights[5][1]
    else:
        score_cervical_cap += 1 * weights[5][2]
    
    # Gender dysphoria pregnancy
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        score_cervical_cap += 1 * weights[6][0]
    elif arr[7] == 'moderate':
        score_cervical_cap += 1 * weights[6][1]
    else:
        score_cervical_cap += 1 * weights[6][2]
    
    return score_cervical_cap


# FAM

def scoring_fam(arr):
    fam_score = 3

    if arr[1] == "v_unp":
        fam_score -= 3
    elif arr[1] == "unp":
        fam_score -= 2
    elif arr[1] == "sl_unp":
        fam_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        fam_score += 1
    elif arr[1] == "imp":
        fam_score += 2
    else:
        fam_score += 3
    
    if arr[2] == "daily":
        fam_score += 3
    
    if arr[3] == "none":
        fam_score += 3
    
    if arr[4] == "v_unp":
        fam_score -= 3
    elif arr[4] == "unp":
        fam_score -= 2
    elif arr[4] == "sl_unp":
        fam_score -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        fam_score += 1
    elif arr[4] == "imp":
        fam_score += 2
    else:
        fam_score += 3
    
    if arr[5] == 'no':
        pass
    elif arr[5] == 'mild':
        fam_score -= 15
    elif arr[5] == 'moderate':
        fam_score -= 25
    else:
        fam_score -= 50
    
    return fam_score

def change_fam(arr, weights):
    score_fam = 3

    # Cost effectiveness
    if arr[1] == "v_unp":
        score_fam += 1 * weights[0][0]
    elif arr[1] == "unp":
        score_fam += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        score_fam += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_fam += 1 * weights[0][3]
    elif arr[1] == "imp":
        score_fam += 1 * weights[0][4]
    else:
        score_fam += 1 * weights[0][5]
    
    # Maintainance
    if arr[2] == "daily":
        score_fam += 1 * weights[1]
    else:
        pass

    if arr[3] == "none":
        score_fam += weights[2]

    # Partner Willingness
    if arr[4] == "v_unp":
        score_fam += 1 * weights[3][0]
    elif arr[4] == "unp":
        score_fam += 1 * weights[3][1]
    elif arr[4] == "sl_unp":
        score_fam += 1 * weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        score_fam += 1 * weights[3][3]
    elif arr[4] == "imp":
        score_fam += 1 * weights[3][4]
    else:
        score_fam += 1 * weights[3][5]
    
    # Gender Dysphoria Pregnancy
    if arr[5] == "no":
        pass
    elif arr[5] == "mild":
        score_fam += 1 * weights[4][0]
    elif arr[5] == "moderate":
        score_fam += 1 * weights[4][1]
    else:
        score_fam += 1 * weights[4][2]
    
    return score_fam

'''
# Arm Implant
'''

def scoring_arm_implant(arr):
    arm_implant_score = 3

    if arr[1] == "v_unp":
        arm_implant_score -= 3
    elif arr[1] == "unp":
        arm_implant_score -= 2
    elif arr[1] == "sl_unp":
        arm_implant_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        arm_implant_score += 1
    elif arr[1] == "imp":
        arm_implant_score += 2
    else:
        arm_implant_score += 3
    
    if arr[2] == "v_unp":
        arm_implant_score -= 3
    elif arr[2] == "unp":
        arm_implant_score -= 2
    elif arr[2] == "sl_unp":
        arm_implant_score -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        arm_implant_score += 1
    elif arr[2] == "imp":
        arm_implant_score += 2
    else:
        arm_implant_score += 3
    
    if arr[3] == "v_unp":
        arm_implant_score += 3
    elif arr[3] == "unp":
        arm_implant_score += 2
    elif arr[3] == "sl_unp":
        arm_implant_score += 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        arm_implant_score -= 1
    elif arr[3] == "imp":
        arm_implant_score -= 2
    else:
        arm_implant_score -= 3
    
    if arr[4] == 'yearly':
        arm_implant_score += 3
    
    if arr[5] == 'p':
        arm_implant_score += 3
    elif arr[5] == 'ep':
        arm_implant_score += 3
    else:
        pass

    if arr[6] == "v_unp":
        arm_implant_score -= 3
    elif arr[6] == "unp":
        arm_implant_score -= 2
    elif arr[6] == "sl_unp":
        arm_implant_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        arm_implant_score += 1
    elif arr[6] == "imp":
        arm_implant_score += 2
    else:
        arm_implant_score += 3

    if arr[7] == "v_unp":
        arm_implant_score -= 3
    elif arr[7] == "unp":
        arm_implant_score -= 2
    elif arr[7] == "sl_unp":
        arm_implant_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        arm_implant_score += 1
    elif arr[7] == "imp":
        arm_implant_score += 2
    else:
        arm_implant_score += 3

    if arr[8] == 'no':
        pass
    else:
        arm_implant_score += 3
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        arm_implant_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        arm_implant_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        arm_implant_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        arm_implant_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        arm_implant_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        arm_implant_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        arm_implant_score -= 7.5
    elif arr[10] == 'moderate' and arr[9] != 'no':
        arm_implant_score -= 12.5
    elif arr[10] == 'severe' and arr[9] != 'no':
        arm_implant_score -= 25
    elif arr[10] == 'mild' and arr[9] == 'no':
        arm_implant_score -= 15
    elif arr[10] == 'moderate' and arr[9] == 'no':
        arm_implant_score -= 25
    elif arr[10]== 'severe' and arr[9] == 'no':
        arm_implant_score -= 50
    
    if arr[11] == 'no':
        pass
    else:
        arm_implant_score += 3
    
    if arr[12] == 'no':
        pass
    else:
        arm_implant_score += 3
    
    return arm_implant_score

def change_arm_implant(arr, weights):
    score_arm_implant = 3

    # Pregnancy Prevention
    if arr[1] == "v_unp":
        score_arm_implant += 1 * weights[0][0]
    elif arr[1] == "unp":
        score_arm_implant += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        score_arm_implant += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        score_arm_implant += 1 * weights[0][3]
    elif arr[1] == "imp":
        score_arm_implant += 1 * weights[0][4]
    else:
        score_arm_implant += 1 * weights[0][5]
    
    # Lessens Periods
    if arr[2] == "v_unp":
        score_arm_implant += 1 * weights[1][0]
    elif arr[2] == "unp":
        score_arm_implant += 1  * weights[1][1]
    elif arr[2] == "sl_unp":
        score_arm_implant += 1 * weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        score_arm_implant += 1 * weights[1][3]
    elif arr[2] == "imp":
        score_arm_implant += 1 * weights[1][4]
    else:
        score_arm_implant += 1 * weights[1][5]
    
    # Maintains Weight
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
    
    # Maintainance
    if arr[4] == "yearly":
        score_arm_implant += 1 * weights[3]
    else:
        pass

    # Hormones Used
    if arr[5] == "p":
        score_arm_implant += 1 * weights[4][0]
    elif arr[5] == "ep":
        score_arm_implant += 1 * weights[4][1]
    else:
        pass

    # Seeking consultation
    if arr[6] == "v_unp":
        score_arm_implant += 1 * weights[5][0]
    elif arr[6] == "unp":
        score_arm_implant += 1 * weights[5][1]
    elif arr[6] == "sl_unp":
        score_arm_implant += 1 * weights[5][2]
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        score_arm_implant += 1 * weights[5][3]
    elif arr[6] == "imp":
        score_arm_implant += 1 * weights[5][4]
    else:
        score_arm_implant += 1 * weights[5][5]
    
    # Medical procedure
    if arr[7] == "v_unp":
        score_arm_implant += 1 * weights[6][0]
    elif arr[7] == "unp":
        score_arm_implant += 1 * weights[6][1]
    elif arr[7] == "sl_unp":
        score_arm_implant += 1 * weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        score_arm_implant += 1 * weights[6][3]
    elif arr[7] == "imp":
        score_arm_implant += 1 * weights[6][4]
    else:
        score_arm_implant += 1 * weights[6][5]
    
    # Acne
    if arr[8] == "no":
        pass
    else:
        score_arm_implant += 1 * weights[7]
    
    # Anxiety 
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        score_arm_implant += weights[8][0]
    elif arr[9] == 'moderate' and arr[10] != 'no':
        score_arm_implant += weights[8][1]
    elif arr[9]=='severe' and arr[10] != 'no':
        score_arm_implant += weights[8][2]
    elif arr[9] == 'mild' and arr[10] == 'no':
        score_arm_implant += weights[8][3]
    elif arr[9] == 'moderate' and arr[10] == 'no':
        score_arm_implant += weights[8][4]
    elif arr[9]== 'severe' and arr[10] == 'no':
        score_arm_implant += weights[8][5]
    
    # Depression
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        score_arm_implant += weights[9][0]
    elif arr[10] == 'moderate' and arr[9] != 'no':
        score_arm_implant += weights[9][1]
    elif arr[10] == 'severe' and arr[9] != 'no':
        score_arm_implant += weights[9][2]
    elif arr[10] == 'mild' and arr[9] == 'no':
        score_arm_implant += weights[9][3]
    elif arr[10] == 'moderate' and arr[9] == 'no':
        score_arm_implant += weights[9][4]
    elif arr[10]== 'severe' and arr[9] == 'no':
        score_arm_implant += weights[9][5]
    
    # Gender dysphoria period
    if arr[11] == 'no':
        pass
    else:
        score_arm_implant += weights[10]
    
    # Gender dysphoria pregnancy
    if arr[12] == 'no':
        pass
    else:
        score_arm_implant += weights[11]
    
    return score_arm_implant



# Copper IUD
def scoring_copper_iud(arr):
    copper_iud_score = 3

    if arr[1] == "v_unp":
        copper_iud_score -= 3
    elif arr[1] == "unp":
        copper_iud_score -= 2
    elif arr[1] == "sl_unp":
        copper_iud_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        copper_iud_score += 1
    elif arr[1] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[2] == 'yearly':
        copper_iud_score += 3
    
    if arr[3] == "none":
        copper_iud_score += 3
    
    if arr[4] == "v_unp":
        copper_iud_score -= 3
    elif arr[4] == "unp":
        copper_iud_score -= 2
    elif arr[4] == "sl_unp":
        copper_iud_score -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        copper_iud_score += 1
    elif arr[4] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[5] == "v_unp":
        copper_iud_score -= 3
    elif arr[5] == "unp":
        copper_iud_score -= 2
    elif arr[5] == "sl_unp":
        copper_iud_score -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        copper_iud_score += 1
    elif arr[5] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[6] == "v_unp":
        copper_iud_score -= 3
    elif arr[6] == "unp":
        copper_iud_score -= 2
    elif arr[6] == "sl_unp":
        copper_iud_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        copper_iud_score += 1
    elif arr[6] == "imp":
        copper_iud_score += 2
    else:
        copper_iud_score += 3
    
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        copper_iud_score -= 15
    elif arr[7] == 'moderate':
        copper_iud_score -= 25
    else:
        copper_iud_score -= 50
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        copper_iud_score -= 15
    elif arr[8] == 'moderate':
        copper_iud_score -= 25
    else:
        copper_iud_score -= 50
    
    if arr[9] == 'no':
        pass
    else:
        copper_iud_score += 3
    
    return copper_iud_score

def change_copper_iud(arr, weights):
    copper_iud_score = 3

    # Pregnancy Prevention
    if arr[1] == "v_unp":
        copper_iud_score += 1 * weights[0][0]
    elif arr[1] == "unp":
        copper_iud_score += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        copper_iud_score += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        copper_iud_score += 1 * weights[0][3]
    elif arr[1] == "imp":
        copper_iud_score += 1 * weights[0][4]
    else:
        copper_iud_score += 1 * weights[0][5]
    
    # Maintainance
    if arr[2] == 'yearly':
        copper_iud_score += weights[1]
    
    if arr[3] == "none":
        copper_iud_score += weights[2]
    
    # Vaginal insertion
    if arr[4] == "v_unp":
        copper_iud_score += weights[3][0]
    elif arr[4] == "unp":
        copper_iud_score += weights[3][1]
    elif arr[4] == "sl_unp":
        copper_iud_score += weights[3][2]
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        copper_iud_score += weights[3][3]
    elif arr[4] == "imp":
        copper_iud_score += weights[3][4]
    else:
        copper_iud_score += weights[3][5]
    
    # Seeking consultation
    if arr[5] == "v_unp":
        copper_iud_score += 1 * weights[4][0]
    elif arr[5] == "unp":
        copper_iud_score += 1 * weights[4][1]
    elif arr[5] == "sl_unp":
        copper_iud_score += 1 * weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        copper_iud_score += 1 * weights[4][3]
    elif arr[5] == "imp":
        copper_iud_score += 1 * weights[4][4]
    else:
        copper_iud_score += 1 * weights[4][5]
    
    # Medical Procedure
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
    
    # Gender dysphoria period
    if arr[7] == 'no':
        pass
    elif arr[7] == 'mild':
        copper_iud_score += weights[6][0]
    elif arr[7] == 'moderate':
        copper_iud_score += weights[6][1]
    else:
        copper_iud_score += weights[6][2]
    
    # Gender Dysphoria Vaginal Insertion
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild':
        copper_iud_score += weights[7][0] 
    elif arr[8] == 'moderate':
        copper_iud_score += weights[7][1]
    else:
        copper_iud_score += weights[7][2]
    
    # Gender Dysphoria Pregnancy
    if arr[9] == 'no':
        pass
    else:
        copper_iud_score += weights[7]
    
    return copper_iud_score
# Sterilization

def scoring_sterilization(arr):
    sterilization_scores = 3

    if arr[1] == "v_unp":
        sterilization_scores -= 3
    elif arr[1] == "unp":
        sterilization_scores -= 2
    elif arr[1] == "sl_unp":
        sterilization_scores -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        sterilization_scores += 1
    elif arr[1] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[2] == "v_unp":
        sterilization_scores -= 3
    elif arr[2] == "unp":
        sterilization_scores -= 2
    elif arr[2] == "sl_unp":
        sterilization_scores -= 1
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        sterilization_scores += 1
    elif arr[2] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[3] == "none":
        sterilization_scores += 3
    
    if arr[4] == "v_unp":
        sterilization_scores -= 3
    elif arr[4] == "unp":
        sterilization_scores -= 2
    elif arr[4] == "sl_unp":
        sterilization_scores -= 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        sterilization_scores += 1
    elif arr[4] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[5] == "v_unp":
        sterilization_scores -= 3
    elif arr[5] == "unp":
        sterilization_scores -= 2
    elif arr[5] == "sl_unp":
        sterilization_scores -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        sterilization_scores += 1
    elif arr[5] == "imp":
        sterilization_scores += 2
    else:
        sterilization_scores += 3
    
    if arr[6] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    if arr[7] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    if arr[8] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    if arr[9] == 'no':
        pass
    else:
        sterilization_scores += 3
    
    return sterilization_scores

def change_score_sterilization(arr, weights):
    sterilization_scores = 3

    # Pregnancy prevention
    if arr[1] == "v_unp":
        sterilization_scores += weights[0][0]
    elif arr[1] == "unp":
        sterilization_scores += weights[0][1]
    elif arr[1] == "sl_unp":
        sterilization_scores += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        sterilization_scores += weights[0][3]
    elif arr[1] == "imp":
        sterilization_scores += weights[0][4]
    else:
        sterilization_scores += weights[0][5]
    
    # Lessens periods
    if arr[2] == "v_unp":
        sterilization_scores += weights[1][0]
    elif arr[2] == "unp":
        sterilization_scores += weights[1][1]
    elif arr[2] == "sl_unp":
        sterilization_scores += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        sterilization_scores += weights[1][3]
    elif arr[2] == "imp":
        sterilization_scores += weights[1][4]
    else:
        sterilization_scores += weights[1][5]
    
    if arr[3] == "none":
        sterilization_scores += weights[2]
    
    # Seeking consultation
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
    
    # Medical Procedure
    if arr[5] == "v_unp":
        sterilization_scores += weights[4][0]
    elif arr[5] == "unp":
        sterilization_scores += weights[4][1]
    elif arr[5] == "sl_unp":
        sterilization_scores += weights[4][2]
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        sterilization_scores += weights[4][3]
    elif arr[5] == "imp":
        sterilization_scores += weights[4][4]
    else:
        sterilization_scores += weights[4][5]
    
    # PCOS
    if arr[6] == 'no':
        pass
    else:
        sterilization_scores += weights[4]
    
    # ENDMT
    if arr[7] == 'no':
        pass
    else:
        sterilization_scores += weights[5]
    
    # Gender Dypsphoria Period
    if arr[8] == 'no':
        pass
    else:
        sterilization_scores += weights[6]
    
    # Gender Dysphoria Pregnancy
    if arr[9] == 'no':
        pass
    else:
        sterilization_scores += weights[7]
    
    return sterilization_scores

def scoring_gel(arr):

    gel_score = 3

    if arr[1] == "v_unp":
        gel_score -= 3
    elif arr[1] == "unp":
        gel_score -= 2
    elif arr[1] == "sl_unp":
        gel_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        gel_score += 1
    elif arr[1] == "imp":
        gel_score += 2
    else:
        gel_score += 3
    
    if arr[2] == "daily":
        gel_score += 3
    
    if arr[3] == "v_unp":
        gel_score -= 3
    elif arr[3] == "unp":
        gel_score -= 2
    elif arr[3] == "sl_unp":
        gel_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        gel_score += 1
    elif arr[3] == "imp":
        gel_score += 2
    else:
        gel_score += 3

    if arr[4] == "none":
        gel_score += 3
    
    if arr[5] == "v_unp":
        gel_score -= 3
    elif arr[5] == "unp":
        gel_score -= 2
    elif arr[5] == "sl_unp":
        gel_score -= 1
    elif arr[5] == "neutral":
        pass
    elif arr[5] == "sl_imp":
        gel_score += 1
    elif arr[5] == "imp":
        gel_score += 2
    else:
        gel_score += 3
    
    return gel_score

def change_score_gel(arr, weights):
    gel_score = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        gel_score += 1 * weights[0][0]
    elif arr[1] == "unp":
        gel_score += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        gel_score += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        gel_score += 1 * weights[0][3]
    elif arr[1] == "imp":
        gel_score += 1 * weights[0][4]
    else:
        gel_score += 1 * weights[0][5]
    
    # Maintainance
    if arr[2] == "daily":
        gel_score += weights[1]
    else:
        pass
    
    # Partner Willingness 
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
    
    if arr[4] == "none":
        gel_score += weights[3]
    
    # Vaginal Insertion
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
    
    return gel_score


def scoring_withdrawal(arr):

    withdrawal_score = 3

    if arr[1] == "v_unp":
        withdrawal_score -= 3
    elif arr[1] == "unp":
        withdrawal_score -= 2
    elif arr[1] == "sl_unp":
        withdrawal_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        withdrawal_score += 1
    elif arr[1] == "imp":
        withdrawal_score += 2
    else:
        withdrawal_score += 3

    if arr[2] == "daily":
        withdrawal_score += 3
    
    if arr[3] == "v_unp":
        withdrawal_score -= 3
    elif arr[3] == "unp":
        withdrawal_score -= 2
    elif arr[3] == "sl_unp":
        withdrawal_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        withdrawal_score += 1
    elif arr[3] == "imp":
        withdrawal_score += 2
    else:
        withdrawal_score += 3
    
    if arr[4] == "none":
        withdrawal_score += 3
    
    if arr[5] == 'no':
        pass
    elif arr[5] == 'mild':
        withdrawal_score -= 15
    elif arr[5]== 'moderate':
        withdrawal_score -= 25
    else:
        withdrawal_score -= 50
    
    return withdrawal_score

def change_score_withdrawal(arr, weights):
    withdrawal_score = 3

    # Cost Effectivess
    if arr[1] == "v_unp":
        withdrawal_score += 1 * weights[0][0]
    elif arr[1] == "unp":
        withdrawal_score += 1 * weights[0][1]
    elif arr[1] == "sl_unp":
        withdrawal_score += 1 * weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        withdrawal_score += 1 * weights[0][3]
    elif arr[1] == "imp":
        withdrawal_score += 1 * weights[0][4]
    else:
        withdrawal_score += 1 * weights[0][5]

    # Maintainance
    if arr[2] == "daily":
        withdrawal_score += weights[1]
    
    # Partner Willingness
    if arr[3] == "v_unp":
        withdrawal_score += weights[2][0]
    elif arr[3] == "unp":
        withdrawal_score += weights[2][1]
    elif arr[3] == "sl_unp":
        withdrawal_score += weights[2][2]
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        withdrawal_score += weights[2][3]
    elif arr[3] == "imp":
        withdrawal_score += weights[2][4]
    else:
        withdrawal_score += weights[2][5]
    
    if arr[4] == "none":
        withdrawal_score += weights[3]
    
    # Gender Dysphoria Pregnancy
    if arr[5] == 'no':
        pass
    elif arr[5] == 'mild':
        withdrawal_score += weights[4][0]
    elif arr[5]== 'moderate':
        withdrawal_score += weights[4][1]
    else:
        withdrawal_score += weights[4][2]
    
    return withdrawal_score

def scoring_mini_pill_original(arr):
    mini_pill_score = 3

    if arr[1] == "v_unp":
        mini_pill_score -= 3
    elif arr[1] == "unp":
        mini_pill_score -= 2
    elif arr[1] == "sl_unp":
        mini_pill_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        mini_pill_score += 1
    elif arr[1] == "imp":
        mini_pill_score += 2
    else:
        mini_pill_score += 3
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        mini_pill_score -= 1.5
    elif arr[2] == "unp":
        mini_pill_score -= 1
    elif arr[2] == "sl_unp":
        mini_pill_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        mini_pill_score += 0.5
    elif arr[2] == "imp":
        mini_pill_score += 1
    else:
        mini_pill_score += 1.5
    
    # Management of Periods 
    if arr[3] == "v_unp":
        mini_pill_score -= 3
    elif arr[3] == "unp":
        mini_pill_score -= 2
    elif arr[3] == "sl_unp":
        mini_pill_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        mini_pill_score += 1
    elif arr[3] == "imp":
        mini_pill_score += 2
    else:
        mini_pill_score += 3
    
    # Weight Management
    if arr[4] == "v_unp":
        mini_pill_score += 3
    elif arr[4] == "unp":
        mini_pill_score += 2
    elif arr[4] == "sl_unp":
        mini_pill_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        mini_pill_score -= 1
    elif arr[4] == "imp":
        mini_pill_score -= 2
    else:
        mini_pill_score -= 3
    
    if arr[5] == "daily":
        mini_pill_score += 3
    
    if arr[6] == 'p':
        mini_pill_score += 3
    elif arr[6] == 'ep':
        mini_pill_score += 3
    else:
        pass
    
    if arr[7] == "v_unp":
        mini_pill_score -= 3
    elif arr[7] == "unp":
        mini_pill_score -= 2
    elif arr[7] == "sl_unp":
        mini_pill_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        mini_pill_score += 1
    elif arr[7] == "imp":
        mini_pill_score += 2
    else:
        mini_pill_score += 3
    
    if arr[8] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        mini_pill_score -= 7.5
    elif arr[9] == 'moderate' and arr[10] != 'no':
        mini_pill_score -= 12.5
    elif arr[9]=='severe' and arr[10] != 'no':
        mini_pill_score -= 25
    elif arr[9] == 'mild' and arr[10] == 'no':
        mini_pill_score -= 15
    elif arr[9] == 'moderate' and arr[10] == 'no':
        mini_pill_score -= 25
    elif arr[9]== 'severe' and arr[10] == 'no':
        mini_pill_score -= 50
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        mini_pill_score -= 7.5
    elif arr[10] == 'moderate' and arr[9] != 'no':
        mini_pill_score -= 12.5
    elif arr[10] == 'severe' and arr[9] != 'no':
        mini_pill_score -= 25
    elif arr[10] == 'mild' and arr[9] == 'no':
        mini_pill_score -= 15
    elif arr[10] == 'moderate' and arr[9] == 'no':
        mini_pill_score -= 25
    elif arr[10]== 'severe' and arr[9] == 'no':
        mini_pill_score -= 50
    
    if arr[11] == 'no':
        pass
    else:
        mini_pill_score -= 100
    
    if arr[12] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[13] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[14] == 'no':
        pass
    else:
        mini_pill_score += 3
    
    if arr[15] == 'no':
        pass
    else:
        mini_pill_score += 1.5
    
    return mini_pill_score

def change_scoring_mini_pill(arr, weights):
    mini_pill_score = 3

    # Cost Effectiveness
    if arr[1] == "v_unp":
        mini_pill_score += weights[0][0]
    elif arr[1] == "unp":
        mini_pill_score += weights[0][1]
    elif arr[1] == "sl_unp":
        mini_pill_score += weights[0][2]
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        mini_pill_score += weights[0][3]
    elif arr[1] == "imp":
        mini_pill_score += weights[0][4]
    else:
        mini_pill_score += weights[0][5]
    
    # Pregnancy Prevention
    if arr[2] == "v_unp":
        mini_pill_score += weights[1][0]
    elif arr[2] == "unp":
        mini_pill_score += weights[1][1]
    elif arr[2] == "sl_unp":
        mini_pill_score += weights[1][2]
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        mini_pill_score += weights[1][3]
    elif arr[2] == "imp":
        mini_pill_score += weights[1][4]
    else:
        mini_pill_score += weights[1][5]
    
    # Management of Periods 
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
    
    # Weight Management
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
    
    # Maintainance
    if arr[5] == "daily":
        mini_pill_score += weights[4] 
    
    # Hormones 
    if arr[6] == 'p':
        mini_pill_score += weights[5][0]
    elif arr[6] == 'ep':
        mini_pill_score += weights[5][1]
    else:   
        pass
    
    # Seeking consultations
    if arr[7] == "v_unp":
        mini_pill_score += weights[6][0]
    elif arr[7] == "unp":
        mini_pill_score += weights[6][1]
    elif arr[7] == "sl_unp":
        mini_pill_score += weights[6][2]
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        mini_pill_score += weights[6][3]
    elif arr[7] == "imp":
        mini_pill_score += weights[6][4]
    else:
        mini_pill_score += weights[6][5]
    
    # Acne
    if arr[8] == 'no':
        pass
    else:
        mini_pill_score += weights[7]
    
    # Anxiety
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild' and arr[10] != 'no':
        mini_pill_score += weights[8][0]
    elif arr[9] == 'moderate' and arr[10] != 'no':
        mini_pill_score += weights[8][1]
    elif arr[9]=='severe' and arr[10] != 'no':
        mini_pill_score += weights[8][2]
    elif arr[9] == 'mild' and arr[10] == 'no':
        mini_pill_score += weights[8][3]
    elif arr[9] == 'moderate' and arr[10] == 'no':
        mini_pill_score += weights[8][4]
    elif arr[9]== 'severe' and arr[10] == 'no':
        mini_pill_score += weights[8][5]
    
    # Depression
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[9] != 'no':
        mini_pill_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[9] != 'no':
        mini_pill_score += weights[9][1]
    elif arr[10] == 'severe' and arr[9] != 'no':
        mini_pill_score += weights[9][2]
    elif arr[10] == 'mild' and arr[9] == 'no':
        mini_pill_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[9] == 'no':
        mini_pill_score += weights[9][4]
    elif arr[10]== 'severe' and arr[9] == 'no':
        mini_pill_score += weights[9][5]
    
    # Breast
    if arr[11] == 'no':
        pass
    else:
        mini_pill_score += weights[10]
    
    # PCOS
    if arr[12] == 'no':
        pass
    else:
        mini_pill_score += weights[11]
    
    # ENDMT
    if arr[13] == 'no':
        pass
    else:
        mini_pill_score += weights[12]
    
    # Gender dysphoria period
    if arr[14] == 'no':
        pass
    else:
        mini_pill_score += weights[13]
    
    # Gender dysphoria pregnancy
    if arr[15] == 'no':
        pass
    else:
        mini_pill_score += weights[14]
    
    return mini_pill_score