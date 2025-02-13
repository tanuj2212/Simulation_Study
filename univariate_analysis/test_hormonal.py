
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

    print("PRE ACNE", hormonal_iud_score)
    
    
    if arr[9] == 'no':
        print("input is no")
        print("POST NO", hormonal_iud_score)
        pass
    elif arr[9]  == 'mild':
        print("input is mild")
        hormonal_iud_score += weights[8][0]
        print(weights[8][0])
        print("POST MILD", hormonal_iud_score)
    elif arr[9] == 'moderate':
        hormonal_iud_score += weights[8][1]
    else:
        hormonal_iud_score += weights[8][2]
    
    if arr[10] == 'no':
        pass
    elif arr[10] == 'mild' and arr[10] != 'no':
        hormonal_iud_score += weights[9][0]
    elif arr[10] == 'moderate' and arr[10] != 'no':
        hormonal_iud_score += weights[9][1]
    elif arr[10]=='severe' and arr[10] != 'no':
        hormonal_iud_score += weights[9][2]
    elif arr[10] == 'mild' and arr[10] == 'no':
        hormonal_iud_score += weights[9][3]
    elif arr[10] == 'moderate' and arr[10] == 'no':
        hormonal_iud_score += weights[9][4]
    elif arr[10]== 'severe' and arr[10] == 'no':
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

inputs = [
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'mild',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'severe',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ]

input_arr = inputs[1]
hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
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

print(change_score_hormonal_iud(hormonal_iud_arr, original_weight_hormonal_IUD))
    