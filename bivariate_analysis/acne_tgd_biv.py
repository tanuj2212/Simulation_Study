import copy
from functions_simulation_diff_weight_hor import *
from correct_original_weights_hor import *
import plotly.graph_objects as go
import numpy as np

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
condoms_6 = {}
condoms_9 = {}
condoms_12 = {}
condoms_15 = {}
condoms_18 = {}
condoms_21 = {}
condoms_24 = {}
condoms_27 = {}
condoms_30 = {}
condoms_33 = {}
condoms_36 = {}
condoms_39 = {}
condoms_42 = {}
condoms_45 = {}
condoms_48 = {}
condoms_51 = {}
condoms_54 = {}
condoms_57 = {}
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
condoms_3["6"] = zero_zero(inputs[0])["Condoms"]
condoms_3["9"] = zero_zero(inputs[0])["Condoms"]
condoms_3["3"] = zero_zero(inputs[0])["Condoms"]
condoms_3["6"] = zero_zero(inputs[0])["Condoms"]
condoms_3["9"] = zero_zero(inputs[0])["Condoms"]
condoms_3["12"] = zero_zero(inputs[0])["Condoms"]
condoms_3["15"] = zero_zero(inputs[0])["Condoms"]
condoms_3["18"] = zero_zero(inputs[0])["Condoms"]
condoms_3["21"] = zero_zero(inputs[0])["Condoms"]
condoms_3["24"] = zero_zero(inputs[0])["Condoms"]
condoms_3["27"] = zero_zero(inputs[0])["Condoms"]
condoms_3["30"] = zero_zero(inputs[0])["Condoms"]
condoms_3["33"] = zero_zero(inputs[0])["Condoms"]
condoms_3["36"] = zero_zero(inputs[0])["Condoms"]
condoms_3["39"] = zero_zero(inputs[0])["Condoms"]
condoms_3["42"] = zero_zero(inputs[0])["Condoms"]
condoms_3["45"] = zero_zero(inputs[0])["Condoms"]
condoms_3["48"] = zero_zero(inputs[0])["Condoms"]
condoms_3["51"] = zero_zero(inputs[0])["Condoms"]
condoms_3["54"] = zero_zero(inputs[0])["Condoms"]
condoms_3["57"] = zero_zero(inputs[0])["Condoms"]
condoms_3["60"] = zero_zero(inputs[0])["Condoms"]


condoms_6["3"] = zero_zero(inputs[0])["Condoms"]
condoms_6["6"] = zero_zero(inputs[0])["Condoms"]
condoms_6["9"] = zero_zero(inputs[0])["Condoms"]
condoms_6["12"] = zero_zero(inputs[0])["Condoms"]
condoms_6["15"] = zero_zero(inputs[0])["Condoms"]
condoms_6["18"] = zero_zero(inputs[0])["Condoms"]
condoms_6["21"] = zero_zero(inputs[0])["Condoms"]
condoms_6["24"] = zero_zero(inputs[0])["Condoms"]
condoms_6["27"] = zero_zero(inputs[0])["Condoms"]
condoms_6["30"] = zero_zero(inputs[0])["Condoms"]
condoms_6["33"] = zero_zero(inputs[0])["Condoms"]
condoms_6["36"] = zero_zero(inputs[0])["Condoms"]
condoms_6["39"] = zero_zero(inputs[0])["Condoms"]
condoms_6["42"] = zero_zero(inputs[0])["Condoms"]
condoms_6["45"] = zero_zero(inputs[0])["Condoms"]
condoms_6["48"] = zero_zero(inputs[0])["Condoms"]
condoms_6["51"] = zero_zero(inputs[0])["Condoms"]
condoms_6["54"] = zero_zero(inputs[0])["Condoms"]
condoms_6["57"] = zero_zero(inputs[0])["Condoms"]
condoms_6["60"] = zero_zero(inputs[0])["Condoms"]

condoms_9["3"] = zero_zero(inputs[0])["Condoms"]
condoms_9["6"] = zero_zero(inputs[0])["Condoms"]
condoms_9["9"] = zero_zero(inputs[0])["Condoms"]
condoms_9["12"] = zero_zero(inputs[0])["Condoms"]
condoms_9["15"] = zero_zero(inputs[0])["Condoms"]
condoms_9["18"] = zero_zero(inputs[0])["Condoms"]
condoms_9["21"] = zero_zero(inputs[0])["Condoms"]
condoms_9["24"] = zero_zero(inputs[0])["Condoms"]
condoms_9["27"] = zero_zero(inputs[0])["Condoms"]
condoms_9["30"] = zero_zero(inputs[0])["Condoms"]
condoms_9["33"] = zero_zero(inputs[0])["Condoms"]
condoms_9["36"] = zero_zero(inputs[0])["Condoms"]
condoms_9["39"] = zero_zero(inputs[0])["Condoms"]
condoms_9["42"] = zero_zero(inputs[0])["Condoms"]
condoms_9["45"] = zero_zero(inputs[0])["Condoms"]
condoms_9["48"] = zero_zero(inputs[0])["Condoms"]
condoms_9["51"] = zero_zero(inputs[0])["Condoms"]
condoms_9["54"] = zero_zero(inputs[0])["Condoms"]
condoms_9["57"] = zero_zero(inputs[0])["Condoms"]
condoms_9["60"] = zero_zero(inputs[0])["Condoms"]

condoms_12["3"] = zero_zero(inputs[0])["Condoms"]
condoms_12["6"] = zero_zero(inputs[0])["Condoms"]
condoms_12["9"] = zero_zero(inputs[0])["Condoms"]
condoms_12["12"] = zero_zero(inputs[0])["Condoms"]
condoms_12["15"] = zero_zero(inputs[0])["Condoms"]
condoms_12["18"] = zero_zero(inputs[0])["Condoms"]
condoms_12["21"] = zero_zero(inputs[0])["Condoms"]
condoms_12["24"] = zero_zero(inputs[0])["Condoms"]
condoms_12["27"] = zero_zero(inputs[0])["Condoms"]
condoms_12["30"] = zero_zero(inputs[0])["Condoms"]
condoms_12["33"] = zero_zero(inputs[0])["Condoms"]
condoms_12["36"] = zero_zero(inputs[0])["Condoms"]
condoms_12["39"] = zero_zero(inputs[0])["Condoms"]
condoms_12["42"] = zero_zero(inputs[0])["Condoms"]
condoms_12["45"] = zero_zero(inputs[0])["Condoms"]
condoms_12["48"] = zero_zero(inputs[0])["Condoms"]
condoms_12["51"] = zero_zero(inputs[0])["Condoms"]
condoms_12["54"] = zero_zero(inputs[0])["Condoms"]
condoms_12["57"] = zero_zero(inputs[0])["Condoms"]
condoms_12["60"] = zero_zero(inputs[0])["Condoms"]


condoms_15["3"] = zero_zero(inputs[0])["Condoms"]
condoms_15["6"] = zero_zero(inputs[0])["Condoms"]
condoms_15["9"] = zero_zero(inputs[0])["Condoms"]
condoms_15["12"] = zero_zero(inputs[0])["Condoms"]
condoms_15["15"] = zero_zero(inputs[0])["Condoms"]
condoms_15["18"] = zero_zero(inputs[0])["Condoms"]
condoms_15["21"] = zero_zero(inputs[0])["Condoms"]
condoms_15["24"] = zero_zero(inputs[0])["Condoms"]
condoms_15["27"] = zero_zero(inputs[0])["Condoms"]  
condoms_15["30"] = zero_zero(inputs[0])["Condoms"]
condoms_15["33"] = zero_zero(inputs[0])["Condoms"]
condoms_15["36"] = zero_zero(inputs[0])["Condoms"]
condoms_15["39"] = zero_zero(inputs[0])["Condoms"]
condoms_15["42"] = zero_zero(inputs[0])["Condoms"]
condoms_15["45"] = zero_zero(inputs[0])["Condoms"]
condoms_15["48"] = zero_zero(inputs[0])["Condoms"]
condoms_15["51"] = zero_zero(inputs[0])["Condoms"]
condoms_15["54"] = zero_zero(inputs[0])["Condoms"]
condoms_15["57"] = zero_zero(inputs[0])["Condoms"]
condoms_15["60"] = zero_zero(inputs[0])["Condoms"]

condoms_18["3"] = zero_zero(inputs[0])["Condoms"]
condoms_18["6"] = zero_zero(inputs[0])["Condoms"]
condoms_18["9"] = zero_zero(inputs[0])["Condoms"]
condoms_18["12"] = zero_zero(inputs[0])["Condoms"]
condoms_18["15"] = zero_zero(inputs[0])["Condoms"]
condoms_18["18"] = zero_zero(inputs[0])["Condoms"]
condoms_18["21"] = zero_zero(inputs[0])["Condoms"]
condoms_18["24"] = zero_zero(inputs[0])["Condoms"]
condoms_18["27"] = zero_zero(inputs[0])["Condoms"]
condoms_18["30"] = zero_zero(inputs[0])["Condoms"]
condoms_18["33"] = zero_zero(inputs[0])["Condoms"]
condoms_18["36"] = zero_zero(inputs[0])["Condoms"]
condoms_18["39"] = zero_zero(inputs[0])["Condoms"]
condoms_18["42"] = zero_zero(inputs[0])["Condoms"]
condoms_18["45"] = zero_zero(inputs[0])["Condoms"]
condoms_18["48"] = zero_zero(inputs[0])["Condoms"]
condoms_18["51"] = zero_zero(inputs[0])["Condoms"]
condoms_18["54"] = zero_zero(inputs[0])["Condoms"]
condoms_18["57"] = zero_zero(inputs[0])["Condoms"]
condoms_18["60"] = zero_zero(inputs[0])["Condoms"]



condoms_21["3"] = zero_zero(inputs[0])["Condoms"]
condoms_21["6"] = zero_zero(inputs[0])["Condoms"]
condoms_21["9"] = zero_zero(inputs[0])["Condoms"]
condoms_21["12"] = zero_zero(inputs[0])["Condoms"]
condoms_21["15"] = zero_zero(inputs[0])["Condoms"]
condoms_21["18"] = zero_zero(inputs[0])["Condoms"]
condoms_21["21"] = zero_zero(inputs[0])["Condoms"]
condoms_21["24"] = zero_zero(inputs[0])["Condoms"]
condoms_21["27"] = zero_zero(inputs[0])["Condoms"]
condoms_21["30"] = zero_zero(inputs[0])["Condoms"]
condoms_21["33"] = zero_zero(inputs[0])["Condoms"]
condoms_21["36"] = zero_zero(inputs[0])["Condoms"]
condoms_21["39"] = zero_zero(inputs[0])["Condoms"]
condoms_21["42"] = zero_zero(inputs[0])["Condoms"]
condoms_21["45"] = zero_zero(inputs[0])["Condoms"]
condoms_21["48"] = zero_zero(inputs[0])["Condoms"]
condoms_21["51"] = zero_zero(inputs[0])["Condoms"]
condoms_21["54"] = zero_zero(inputs[0])["Condoms"]
condoms_21["57"] = zero_zero(inputs[0])["Condoms"]
condoms_21["60"] = zero_zero(inputs[0])["Condoms"]






condoms_24["3"] = zero_zero(inputs[0])["Condoms"]
condoms_24["6"] = zero_zero(inputs[0])["Condoms"]
condoms_24["9"] = zero_zero(inputs[0])["Condoms"]
condoms_24["12"] = zero_zero(inputs[0])["Condoms"]
condoms_24["15"] = zero_zero(inputs[0])["Condoms"]
condoms_24["18"] = zero_zero(inputs[0])["Condoms"]
condoms_24["21"] = zero_zero(inputs[0])["Condoms"]
condoms_24["24"] = zero_zero(inputs[0])["Condoms"]
condoms_24["27"] = zero_zero(inputs[0])["Condoms"]
condoms_24["30"] = zero_zero(inputs[0])["Condoms"]
condoms_24["33"] = zero_zero(inputs[0])["Condoms"]
condoms_24["36"] = zero_zero(inputs[0])["Condoms"]
condoms_24["39"] = zero_zero(inputs[0])["Condoms"]
condoms_24["42"] = zero_zero(inputs[0])["Condoms"]
condoms_24["45"] = zero_zero(inputs[0])["Condoms"]
condoms_24["48"] = zero_zero(inputs[0])["Condoms"]
condoms_24["51"] = zero_zero(inputs[0])["Condoms"]
condoms_24["54"] = zero_zero(inputs[0])["Condoms"]
condoms_24["57"] = zero_zero(inputs[0])["Condoms"]
condoms_24["60"] = zero_zero(inputs[0])["Condoms"]





condoms_27["3"] = zero_zero(inputs[0])["Condoms"]
condoms_27["6"] = zero_zero(inputs[0])["Condoms"]
condoms_27["9"] = zero_zero(inputs[0])["Condoms"]
condoms_27["12"] = zero_zero(inputs[0])["Condoms"]
condoms_27["15"] = zero_zero(inputs[0])["Condoms"]
condoms_27["18"] = zero_zero(inputs[0])["Condoms"]
condoms_27["21"] = zero_zero(inputs[0])["Condoms"]
condoms_27["24"] = zero_zero(inputs[0])["Condoms"]
condoms_27["27"] = zero_zero(inputs[0])["Condoms"]
condoms_27["30"] = zero_zero(inputs[0])["Condoms"]
condoms_27["33"] = zero_zero(inputs[0])["Condoms"]
condoms_27["36"] = zero_zero(inputs[0])["Condoms"]
condoms_27["39"] = zero_zero(inputs[0])["Condoms"]
condoms_27["42"] = zero_zero(inputs[0])["Condoms"]
condoms_27["45"] = zero_zero(inputs[0])["Condoms"]
condoms_27["48"] = zero_zero(inputs[0])["Condoms"]
condoms_27["51"] = zero_zero(inputs[0])["Condoms"]
condoms_27["54"] = zero_zero(inputs[0])["Condoms"]
condoms_27["57"] = zero_zero(inputs[0])["Condoms"]
condoms_27["60"] = zero_zero(inputs[0])["Condoms"]




condoms_30["3"] = zero_zero(inputs[0])["Condoms"]
condoms_30["6"] = zero_zero(inputs[0])["Condoms"]
condoms_30["9"] = zero_zero(inputs[0])["Condoms"]
condoms_30["12"] = zero_zero(inputs[0])["Condoms"]
condoms_30["15"] = zero_zero(inputs[0])["Condoms"]
condoms_30["18"] = zero_zero(inputs[0])["Condoms"]
condoms_30["21"] = zero_zero(inputs[0])["Condoms"]
condoms_30["24"] = zero_zero(inputs[0])["Condoms"]
condoms_30["27"] = zero_zero(inputs[0])["Condoms"]  
condoms_30["30"] = zero_zero(inputs[0])["Condoms"]
condoms_30["33"] = zero_zero(inputs[0])["Condoms"]
condoms_30["36"] = zero_zero(inputs[0])["Condoms"]
condoms_30["39"] = zero_zero(inputs[0])["Condoms"]
condoms_30["42"] = zero_zero(inputs[0])["Condoms"]
condoms_30["45"] = zero_zero(inputs[0])["Condoms"]
condoms_30["48"] = zero_zero(inputs[0])["Condoms"]
condoms_30["51"] = zero_zero(inputs[0])["Condoms"]
condoms_30["54"] = zero_zero(inputs[0])["Condoms"]
condoms_30["57"] = zero_zero(inputs[0])["Condoms"]
condoms_30["60"] = zero_zero(inputs[0])["Condoms"]

condoms_33["3"] = zero_zero(inputs[0])["Condoms"]
condoms_33["6"] = zero_zero(inputs[0])["Condoms"]
condoms_33["9"] = zero_zero(inputs[0])["Condoms"]
condoms_33["12"] = zero_zero(inputs[0])["Condoms"]
condoms_33["15"] = zero_zero(inputs[0])["Condoms"]
condoms_33["18"] = zero_zero(inputs[0])["Condoms"]
condoms_33["21"] = zero_zero(inputs[0])["Condoms"]
condoms_33["24"] = zero_zero(inputs[0])["Condoms"]
condoms_33["27"] = zero_zero(inputs[0])["Condoms"]
condoms_33["30"] = zero_zero(inputs[0])["Condoms"]
condoms_33["33"] = zero_zero(inputs[0])["Condoms"]
condoms_33["36"] = zero_zero(inputs[0])["Condoms"]
condoms_33["39"] = zero_zero(inputs[0])["Condoms"]
condoms_33["42"] = zero_zero(inputs[0])["Condoms"]
condoms_33["45"] = zero_zero(inputs[0])["Condoms"]
condoms_33["48"] = zero_zero(inputs[0])["Condoms"]
condoms_33["51"] = zero_zero(inputs[0])["Condoms"]
condoms_33["54"] = zero_zero(inputs[0])["Condoms"]
condoms_33["57"] = zero_zero(inputs[0])["Condoms"]
condoms_33["60"] = zero_zero(inputs[0])["Condoms"]


condoms_36["3"] = zero_zero(inputs[0])["Condoms"]
condoms_36["6"] = zero_zero(inputs[0])["Condoms"]
condoms_36["9"] = zero_zero(inputs[0])["Condoms"]
condoms_36["12"] = zero_zero(inputs[0])["Condoms"]
condoms_36["15"] = zero_zero(inputs[0])["Condoms"]
condoms_36["18"] = zero_zero(inputs[0])["Condoms"]
condoms_36["21"] = zero_zero(inputs[0])["Condoms"]
condoms_36["24"] = zero_zero(inputs[0])["Condoms"]
condoms_36["27"] = zero_zero(inputs[0])["Condoms"]
condoms_36["30"] = zero_zero(inputs[0])["Condoms"]
condoms_36["33"] = zero_zero(inputs[0])["Condoms"]
condoms_36["36"] = zero_zero(inputs[0])["Condoms"]
condoms_36["39"] = zero_zero(inputs[0])["Condoms"]
condoms_36["42"] = zero_zero(inputs[0])["Condoms"]
condoms_36["45"] = zero_zero(inputs[0])["Condoms"]
condoms_36["48"] = zero_zero(inputs[0])["Condoms"]
condoms_36["51"] = zero_zero(inputs[0])["Condoms"]
condoms_36["54"] = zero_zero(inputs[0])["Condoms"]
condoms_36["57"] = zero_zero(inputs[0])["Condoms"]
condoms_36["60"] = zero_zero(inputs[0])["Condoms"]






condoms_39["3"] = zero_zero(inputs[0])["Condoms"]
condoms_39["6"] = zero_zero(inputs[0])["Condoms"]
condoms_39["9"] = zero_zero(inputs[0])["Condoms"]
condoms_39["12"] = zero_zero(inputs[0])["Condoms"]
condoms_39["15"] = zero_zero(inputs[0])["Condoms"]
condoms_39["18"] = zero_zero(inputs[0])["Condoms"]
condoms_39["21"] = zero_zero(inputs[0])["Condoms"]
condoms_39["24"] = zero_zero(inputs[0])["Condoms"]
condoms_39["27"] = zero_zero(inputs[0])["Condoms"]
condoms_39["30"] = zero_zero(inputs[0])["Condoms"]
condoms_39["33"] = zero_zero(inputs[0])["Condoms"]
condoms_39["36"] = zero_zero(inputs[0])["Condoms"]
condoms_39["39"] = zero_zero(inputs[0])["Condoms"]
condoms_39["42"] = zero_zero(inputs[0])["Condoms"]
condoms_39["45"] = zero_zero(inputs[0])["Condoms"]
condoms_39["48"] = zero_zero(inputs[0])["Condoms"]
condoms_39["51"] = zero_zero(inputs[0])["Condoms"]
condoms_39["54"] = zero_zero(inputs[0])["Condoms"]
condoms_39["57"] = zero_zero(inputs[0])["Condoms"]
condoms_39["60"] = zero_zero(inputs[0])["Condoms"]





condoms_42["3"] = zero_zero(inputs[0])["Condoms"]
condoms_42["6"] = zero_zero(inputs[0])["Condoms"]
condoms_42["9"] = zero_zero(inputs[0])["Condoms"]
condoms_42["12"] = zero_zero(inputs[0])["Condoms"]
condoms_42["15"] = zero_zero(inputs[0])["Condoms"]
condoms_42["18"] = zero_zero(inputs[0])["Condoms"]
condoms_42["21"] = zero_zero(inputs[0])["Condoms"]
condoms_42["24"] = zero_zero(inputs[0])["Condoms"]
condoms_42["27"] = zero_zero(inputs[0])["Condoms"]
condoms_42["30"] = zero_zero(inputs[0])["Condoms"]
condoms_42["33"] = zero_zero(inputs[0])["Condoms"]
condoms_42["36"] = zero_zero(inputs[0])["Condoms"]
condoms_42["39"] = zero_zero(inputs[0])["Condoms"]
condoms_42["42"] = zero_zero(inputs[0])["Condoms"]
condoms_42["45"] = zero_zero(inputs[0])["Condoms"]
condoms_42["48"] = zero_zero(inputs[0])["Condoms"]
condoms_42["51"] = zero_zero(inputs[0])["Condoms"]
condoms_42["54"] = zero_zero(inputs[0])["Condoms"]
condoms_42["57"] = zero_zero(inputs[0])["Condoms"]
condoms_42["60"] = zero_zero(inputs[0])["Condoms"]





condoms_45["3"] = zero_zero(inputs[0])["Condoms"]
condoms_45["6"] = zero_zero(inputs[0])["Condoms"]
condoms_45["9"] = zero_zero(inputs[0])["Condoms"]
condoms_45["12"] = zero_zero(inputs[0])["Condoms"]
condoms_45["15"] = zero_zero(inputs[0])["Condoms"]
condoms_45["18"] = zero_zero(inputs[0])["Condoms"]
condoms_45["21"] = zero_zero(inputs[0])["Condoms"]
condoms_45["24"] = zero_zero(inputs[0])["Condoms"]
condoms_45["27"] = zero_zero(inputs[0])["Condoms"]  
condoms_45["30"] = zero_zero(inputs[0])["Condoms"]
condoms_45["33"] = zero_zero(inputs[0])["Condoms"]
condoms_45["36"] = zero_zero(inputs[0])["Condoms"]
condoms_45["39"] = zero_zero(inputs[0])["Condoms"]
condoms_45["42"] = zero_zero(inputs[0])["Condoms"]
condoms_45["45"] = zero_zero(inputs[0])["Condoms"]
condoms_45["48"] = zero_zero(inputs[0])["Condoms"]
condoms_45["51"] = zero_zero(inputs[0])["Condoms"]
condoms_45["54"] = zero_zero(inputs[0])["Condoms"]
condoms_45["57"] = zero_zero(inputs[0])["Condoms"]
condoms_45["60"] = zero_zero(inputs[0])["Condoms"]

condoms_48["3"] = zero_zero(inputs[0])["Condoms"]
condoms_48["6"] = zero_zero(inputs[0])["Condoms"]
condoms_48["9"] = zero_zero(inputs[0])["Condoms"]
condoms_48["12"] = zero_zero(inputs[0])["Condoms"]
condoms_48["15"] = zero_zero(inputs[0])["Condoms"]
condoms_48["18"] = zero_zero(inputs[0])["Condoms"]
condoms_48["21"] = zero_zero(inputs[0])["Condoms"]
condoms_48["24"] = zero_zero(inputs[0])["Condoms"]
condoms_48["27"] = zero_zero(inputs[0])["Condoms"]
condoms_48["30"] = zero_zero(inputs[0])["Condoms"]
condoms_48["33"] = zero_zero(inputs[0])["Condoms"]
condoms_48["36"] = zero_zero(inputs[0])["Condoms"]
condoms_48["39"] = zero_zero(inputs[0])["Condoms"]
condoms_48["42"] = zero_zero(inputs[0])["Condoms"]
condoms_48["45"] = zero_zero(inputs[0])["Condoms"]
condoms_48["48"] = zero_zero(inputs[0])["Condoms"]
condoms_48["51"] = zero_zero(inputs[0])["Condoms"]
condoms_48["54"] = zero_zero(inputs[0])["Condoms"]
condoms_48["57"] = zero_zero(inputs[0])["Condoms"]
condoms_48["60"] = zero_zero(inputs[0])["Condoms"]

condoms_51["3"] = zero_zero(inputs[0])["Condoms"]
condoms_51["6"] = zero_zero(inputs[0])["Condoms"]
condoms_51["9"] = zero_zero(inputs[0])["Condoms"]
condoms_51["12"] = zero_zero(inputs[0])["Condoms"]  
condoms_51["15"] = zero_zero(inputs[0])["Condoms"]
condoms_51["18"] = zero_zero(inputs[0])["Condoms"]
condoms_51["21"] = zero_zero(inputs[0])["Condoms"]
condoms_51["24"] = zero_zero(inputs[0])["Condoms"]
condoms_51["27"] = zero_zero(inputs[0])["Condoms"]
condoms_51["30"] = zero_zero(inputs[0])["Condoms"]
condoms_51["33"] = zero_zero(inputs[0])["Condoms"]
condoms_51["36"] = zero_zero(inputs[0])["Condoms"]
condoms_51["39"] = zero_zero(inputs[0])["Condoms"]
condoms_51["42"] = zero_zero(inputs[0])["Condoms"]
condoms_51["45"] = zero_zero(inputs[0])["Condoms"]
condoms_51["48"] = zero_zero(inputs[0])["Condoms"]
condoms_51["51"] = zero_zero(inputs[0])["Condoms"]
condoms_51["54"] = zero_zero(inputs[0])["Condoms"]
condoms_51["57"] = zero_zero(inputs[0])["Condoms"]
condoms_51["60"] = zero_zero(inputs[0])["Condoms"]


condoms_54["3"] = zero_zero(inputs[0])["Condoms"]
condoms_54["6"] = zero_zero(inputs[0])["Condoms"]
condoms_54["9"] = zero_zero(inputs[0])["Condoms"]
condoms_54["12"] = zero_zero(inputs[0])["Condoms"]
condoms_54["15"] = zero_zero(inputs[0])["Condoms"]
condoms_54["18"] = zero_zero(inputs[0])["Condoms"]
condoms_54["21"] = zero_zero(inputs[0])["Condoms"]
condoms_54["24"] = zero_zero(inputs[0])["Condoms"]
condoms_54["27"] = zero_zero(inputs[0])["Condoms"]  
condoms_54["30"] = zero_zero(inputs[0])["Condoms"]
condoms_54["33"] = zero_zero(inputs[0])["Condoms"]
condoms_54["36"] = zero_zero(inputs[0])["Condoms"]
condoms_54["39"] = zero_zero(inputs[0])["Condoms"]
condoms_54["42"] = zero_zero(inputs[0])["Condoms"]
condoms_54["45"] = zero_zero(inputs[0])["Condoms"]
condoms_54["48"] = zero_zero(inputs[0])["Condoms"]
condoms_54["51"] = zero_zero(inputs[0])["Condoms"]
condoms_54["54"] = zero_zero(inputs[0])["Condoms"]
condoms_54["57"] = zero_zero(inputs[0])["Condoms"]
condoms_54["60"] = zero_zero(inputs[0])["Condoms"]

condoms_57["3"] = zero_zero(inputs[0])["Condoms"]
condoms_57["6"] = zero_zero(inputs[0])["Condoms"]
condoms_57["9"] = zero_zero(inputs[0])["Condoms"]
condoms_57["12"] = zero_zero(inputs[0])["Condoms"]  
condoms_57["15"] = zero_zero(inputs[0])["Condoms"]
condoms_57["18"] = zero_zero(inputs[0])["Condoms"]
condoms_57["21"] = zero_zero(inputs[0])["Condoms"]
condoms_57["24"] = zero_zero(inputs[0])["Condoms"]
condoms_57["27"] = zero_zero(inputs[0])["Condoms"]
condoms_57["30"] = zero_zero(inputs[0])["Condoms"]
condoms_57["33"] = zero_zero(inputs[0])["Condoms"]
condoms_57["36"] = zero_zero(inputs[0])["Condoms"]
condoms_57["39"] = zero_zero(inputs[0])["Condoms"]
condoms_57["42"] = zero_zero(inputs[0])["Condoms"]
condoms_57["45"] = zero_zero(inputs[0])["Condoms"]
condoms_57["48"] = zero_zero(inputs[0])["Condoms"]
condoms_57["51"] = zero_zero(inputs[0])["Condoms"]
condoms_57["54"] = zero_zero(inputs[0])["Condoms"]
condoms_57["57"] = zero_zero(inputs[0])["Condoms"]
condoms_57["60"] = zero_zero(inputs[0])["Condoms"]



condoms_60["3"] = zero_zero(inputs[0])["Condoms"]
condoms_60["6"] = zero_zero(inputs[0])["Condoms"]
condoms_60["9"] = zero_zero(inputs[0])["Condoms"]
condoms_60["12"] = zero_zero(inputs[0])["Condoms"]
condoms_60["15"] = zero_zero(inputs[0])["Condoms"]
condoms_60["18"] = zero_zero(inputs[0])["Condoms"]
condoms_60["21"] = zero_zero(inputs[0])["Condoms"]
condoms_60["24"] = zero_zero(inputs[0])["Condoms"]
condoms_60["27"] = zero_zero(inputs[0])["Condoms"]
condoms_60["30"] = zero_zero(inputs[0])["Condoms"]
condoms_60["33"] = zero_zero(inputs[0])["Condoms"]
condoms_60["36"] = zero_zero(inputs[0])["Condoms"]
condoms_60["39"] = zero_zero(inputs[0])["Condoms"]
condoms_60["42"] = zero_zero(inputs[0])["Condoms"]
condoms_60["45"] = zero_zero(inputs[0])["Condoms"]
condoms_60["48"] = zero_zero(inputs[0])["Condoms"]
condoms_60["51"] = zero_zero(inputs[0])["Condoms"]
condoms_60["54"] = zero_zero(inputs[0])["Condoms"]
condoms_60["57"] = zero_zero(inputs[0])["Condoms"]
condoms_60["60"] = zero_zero(inputs[0])["Condoms"]






# Internal Condoms
internal_condom_no = {}
internal_condom_mild = {}
internal_condom_moderate = {}
internal_condom_severe = {}
internal_condom_3 = {}
internal_condom_6 = {}
internal_condom_9 = {}
internal_condom_12 = {}
internal_condom_15 = {}
internal_condom_18 = {}
internal_condom_21 = {}
internal_condom_24 = {}
internal_condom_27 = {} 
internal_condom_30 = {}
internal_condom_33 = {}
internal_condom_36 = {}
internal_condom_39 = {}
internal_condom_42 = {}
internal_condom_45 = {} 
internal_condom_48 = {}
internal_condom_51 = {}
internal_condom_54 = {}
internal_condom_57 = {}
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
internal_condom_3["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_3["60"] = zero_zero(inputs[0])["Internal Condoms"]





internal_condom_6["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_6["60"] = zero_zero(inputs[0])["Internal Condoms"]


internal_condom_9["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_9["60"] = zero_zero(inputs[0])["Internal Condoms"]




internal_condom_12["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_12["60"] = zero_zero(inputs[0])["Internal Condoms"]


internal_condom_15["3"] = zero_zero(inputs[0])["Internal Condoms"]  
internal_condom_15["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_15["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_18["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["9"] = zero_zero(inputs[0])["Internal Condoms"] 
internal_condom_18["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["24"] = zero_zero(inputs[0])["Internal Condoms"] 
internal_condom_18["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_18["60"] = zero_zero(inputs[0])["Internal Condoms"]





internal_condom_21["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_21["60"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_24["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_24["60"] = zero_zero(inputs[0])["Internal Condoms"]






internal_condom_27["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_27["60"] = zero_zero(inputs[0])["Internal Condoms"]




internal_condom_30["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_30["60"] = zero_zero(inputs[0])["Internal Condoms"]




internal_condom_33["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_33["60"] = zero_zero(inputs[0])["Internal Condoms"]


internal_condom_36["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["15"] = zero_zero(inputs[0])["Internal Condoms"]

internal_condom_36["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_36["60"] = zero_zero(inputs[0])["Internal Condoms"]




internal_condom_39["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_39["60"] = zero_zero(inputs[0])["Internal Condoms"]


internal_condom_42["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["30"] = zero_zero(inputs[0])["Internal Condoms"] 
internal_condom_42["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_42["60"] = zero_zero(inputs[0])["Internal Condoms"]


internal_condom_45["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_45["60"] = zero_zero(inputs[0])["Internal Condoms"]



internal_condom_48["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_48["60"] = zero_zero(inputs[0])["Internal Condoms"]




internal_condom_51["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_51["60"] = zero_zero(inputs[0])["Internal Condoms"]


internal_condom_54["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_54["60"] = zero_zero(inputs[0])["Internal Condoms"]






internal_condom_57["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["12"] = zero_zero(inputs[0])["Internal Condoms"] 
internal_condom_57["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_57["60"] = zero_zero(inputs[0])["Internal Condoms"]





internal_condom_60["3"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["6"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["9"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["12"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["15"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["18"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["21"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["24"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["27"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["30"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["33"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["36"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["39"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["42"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["45"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["48"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["51"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["54"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["57"] = zero_zero(inputs[0])["Internal Condoms"]
internal_condom_60["60"] = zero_zero(inputs[0])["Internal Condoms"]







# Cervical Cap
cervical_cap_no = {}
cervical_cap_mild = {}
cervical_cap_moderate = {}
cervical_cap_severe = {}
cervical_cap_3 = {}
cervical_cap_6 = {}
cervical_cap_9 = {}
cervical_cap_12 = {}
cervical_cap_15 = {}
cervical_cap_18 = {}
cervical_cap_21 = {}
cervical_cap_24 = {}
cervical_cap_27 = {}
cervical_cap_30 = {}
cervical_cap_33 = {}
cervical_cap_36 = {}
cervical_cap_39 = {}
cervical_cap_42 = {}
cervical_cap_45 = {}
cervical_cap_48 = {}
cervical_cap_51 = {}
cervical_cap_54 = {}
cervical_cap_57 = {}
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
cervical_cap_3["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_3["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_6["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_6["60"] = zero_zero(inputs[0])["Cervical Cap"]

cervical_cap_9["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_9["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_12["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_12["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_15["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_15["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_18["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_18["60"] = zero_zero(inputs[0])["Cervical Cap"]




cervical_cap_21["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_21["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_24["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_24["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_27["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_27["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_30["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_30["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_33["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_33["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_36["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_36["60"] = zero_zero(inputs[0])["Cervical Cap"]




cervical_cap_39["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_39["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_42["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_42["60"] = zero_zero(inputs[0])["Cervical Cap"]


cervical_cap_45["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_45["60"] = zero_zero(inputs[0])["Cervical Cap"]




cervical_cap_48["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_48["60"] = zero_zero(inputs[0])["Cervical Cap"]




cervical_cap_51["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_51["60"] = zero_zero(inputs[0])["Cervical Cap"]




cervical_cap_54["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_54["60"] = zero_zero(inputs[0])["Cervical Cap"]





cervical_cap_57["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["27"] = zero_zero(inputs[0])["Cervical Cap"]    
cervical_cap_57["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_57["60"] = zero_zero(inputs[0])["Cervical Cap"]



cervical_cap_60["3"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["6"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["9"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["12"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["15"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["18"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["21"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["24"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["27"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["30"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["33"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["36"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["39"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["42"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["45"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["48"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["51"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["54"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["57"] = zero_zero(inputs[0])["Cervical Cap"]
cervical_cap_60["60"] = zero_zero(inputs[0])["Cervical Cap"]



# FAM
fam_no = {}
fam_mild = {}
fam_moderate = {}
fam_severe = {}
fam_3 = {}
fam_6 = {}
fam_9 = {}
fam_12 = {}
fam_15 = {}
fam_18 = {}
fam_21 = {}
fam_24 = {}
fam_27 = {}
fam_30 = {}
fam_33 = {}
fam_36 = {}
fam_39 = {}
fam_42 = {}
fam_45 = {}
fam_48 = {}
fam_51 = {}
fam_54 = {}
fam_57 = {}
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
fam_3["6"] = zero_zero(inputs[0])["FAM"]
fam_3["9"] = zero_zero(inputs[0])["FAM"]
fam_3["12"] = zero_zero(inputs[0])["FAM"]
fam_3["15"] = zero_zero(inputs[0])["FAM"]
fam_3["18"] = zero_zero(inputs[0])["FAM"]
fam_3["21"] = zero_zero(inputs[0])["FAM"]
fam_3["24"] = zero_zero(inputs[0])["FAM"]
fam_3["27"] = zero_zero(inputs[0])["FAM"]
fam_3["30"] = zero_zero(inputs[0])["FAM"]
fam_3["33"] = zero_zero(inputs[0])["FAM"]
fam_3["36"] = zero_zero(inputs[0])["FAM"]
fam_3["39"] = zero_zero(inputs[0])["FAM"]
fam_3["42"] = zero_zero(inputs[0])["FAM"]
fam_3["45"] = zero_zero(inputs[0])["FAM"]
fam_3["48"] = zero_zero(inputs[0])["FAM"]
fam_3["51"] = zero_zero(inputs[0])["FAM"]
fam_3["54"] = zero_zero(inputs[0])["FAM"]
fam_3["57"] = zero_zero(inputs[0])["FAM"]
fam_3["60"] = zero_zero(inputs[0])["FAM"]


fam_6["3"] = zero_zero(inputs[0])["FAM"]
fam_6["6"] = zero_zero(inputs[0])["FAM"]
fam_6["9"] = zero_zero(inputs[0])["FAM"]
fam_6["12"] = zero_zero(inputs[0])["FAM"]
fam_6["15"] = zero_zero(inputs[0])["FAM"]
fam_6["18"] = zero_zero(inputs[0])["FAM"]
fam_6["21"] = zero_zero(inputs[0])["FAM"]
fam_6["24"] = zero_zero(inputs[0])["FAM"]
fam_6["27"] = zero_zero(inputs[0])["FAM"]
fam_6["30"] = zero_zero(inputs[0])["FAM"]
fam_6["33"] = zero_zero(inputs[0])["FAM"]
fam_6["36"] = zero_zero(inputs[0])["FAM"]
fam_6["39"] = zero_zero(inputs[0])["FAM"]
fam_6["42"] = zero_zero(inputs[0])["FAM"]
fam_6["45"] = zero_zero(inputs[0])["FAM"]
fam_6["48"] = zero_zero(inputs[0])["FAM"]
fam_6["51"] = zero_zero(inputs[0])["FAM"]
fam_6["54"] = zero_zero(inputs[0])["FAM"]
fam_6["57"] = zero_zero(inputs[0])["FAM"]
fam_6["60"] = zero_zero(inputs[0])["FAM"]


fam_9["3"] = zero_zero(inputs[0])["FAM"]
fam_9["6"] = zero_zero(inputs[0])["FAM"]
fam_9["9"] = zero_zero(inputs[0])["FAM"]
fam_9["12"] = zero_zero(inputs[0])["FAM"]
fam_9["15"] = zero_zero(inputs[0])["FAM"]
fam_9["18"] = zero_zero(inputs[0])["FAM"]
fam_9["21"] = zero_zero(inputs[0])["FAM"]
fam_9["24"] = zero_zero(inputs[0])["FAM"]
fam_9["27"] = zero_zero(inputs[0])["FAM"]
fam_9["30"] = zero_zero(inputs[0])["FAM"]
fam_9["33"] = zero_zero(inputs[0])["FAM"]
fam_9["36"] = zero_zero(inputs[0])["FAM"]
fam_9["39"] = zero_zero(inputs[0])["FAM"]
fam_9["42"] = zero_zero(inputs[0])["FAM"]
fam_9["45"] = zero_zero(inputs[0])["FAM"]
fam_9["48"] = zero_zero(inputs[0])["FAM"]
fam_9["51"] = zero_zero(inputs[0])["FAM"]
fam_9["54"] = zero_zero(inputs[0])["FAM"]
fam_9["57"] = zero_zero(inputs[0])["FAM"]
fam_9["60"] = zero_zero(inputs[0])["FAM"]

fam_12["3"] = zero_zero(inputs[0])["FAM"]
fam_12["6"] = zero_zero(inputs[0])["FAM"]
fam_12["9"] = zero_zero(inputs[0])["FAM"]
fam_12["12"] = zero_zero(inputs[0])["FAM"]
fam_12["15"] = zero_zero(inputs[0])["FAM"]
fam_12["18"] = zero_zero(inputs[0])["FAM"]
fam_12["21"] = zero_zero(inputs[0])["FAM"]
fam_12["24"] = zero_zero(inputs[0])["FAM"]
fam_12["27"] = zero_zero(inputs[0])["FAM"]
fam_12["30"] = zero_zero(inputs[0])["FAM"]
fam_12["33"] = zero_zero(inputs[0])["FAM"]
fam_12["36"] = zero_zero(inputs[0])["FAM"]
fam_12["39"] = zero_zero(inputs[0])["FAM"]
fam_12["42"] = zero_zero(inputs[0])["FAM"]
fam_12["45"] = zero_zero(inputs[0])["FAM"]
fam_12["48"] = zero_zero(inputs[0])["FAM"]
fam_12["51"] = zero_zero(inputs[0])["FAM"]
fam_12["54"] = zero_zero(inputs[0])["FAM"]
fam_12["57"] = zero_zero(inputs[0])["FAM"]
fam_12["60"] = zero_zero(inputs[0])["FAM"]

fam_15["3"] = zero_zero(inputs[0])["FAM"]
fam_15["6"] = zero_zero(inputs[0])["FAM"]
fam_15["9"] = zero_zero(inputs[0])["FAM"]
fam_15["12"] = zero_zero(inputs[0])["FAM"]
fam_15["15"] = zero_zero(inputs[0])["FAM"]
fam_15["18"] = zero_zero(inputs[0])["FAM"]
fam_15["21"] = zero_zero(inputs[0])["FAM"]
fam_15["24"] = zero_zero(inputs[0])["FAM"]
fam_15["27"] = zero_zero(inputs[0])["FAM"]
fam_15["30"] = zero_zero(inputs[0])["FAM"]
fam_15["33"] = zero_zero(inputs[0])["FAM"]
fam_15["36"] = zero_zero(inputs[0])["FAM"]
fam_15["39"] = zero_zero(inputs[0])["FAM"]
fam_15["42"] = zero_zero(inputs[0])["FAM"]
fam_15["45"] = zero_zero(inputs[0])["FAM"]
fam_15["48"] = zero_zero(inputs[0])["FAM"]
fam_15["51"] = zero_zero(inputs[0])["FAM"]
fam_15["54"] = zero_zero(inputs[0])["FAM"]
fam_15["57"] = zero_zero(inputs[0])["FAM"]
fam_15["60"] = zero_zero(inputs[0])["FAM"]


fam_18["3"] = zero_zero(inputs[0])["FAM"]
fam_18["6"] = zero_zero(inputs[0])["FAM"]
fam_18["9"] = zero_zero(inputs[0])["FAM"]
fam_18["12"] = zero_zero(inputs[0])["FAM"]
fam_18["15"] = zero_zero(inputs[0])["FAM"]
fam_18["18"] = zero_zero(inputs[0])["FAM"]
fam_18["21"] = zero_zero(inputs[0])["FAM"]
fam_18["24"] = zero_zero(inputs[0])["FAM"]
fam_18["27"] = zero_zero(inputs[0])["FAM"]
fam_18["30"] = zero_zero(inputs[0])["FAM"]
fam_18["33"] = zero_zero(inputs[0])["FAM"]
fam_18["36"] = zero_zero(inputs[0])["FAM"]
fam_18["39"] = zero_zero(inputs[0])["FAM"]
fam_18["42"] = zero_zero(inputs[0])["FAM"]
fam_18["45"] = zero_zero(inputs[0])["FAM"]
fam_18["48"] = zero_zero(inputs[0])["FAM"]
fam_18["51"] = zero_zero(inputs[0])["FAM"]
fam_18["54"] = zero_zero(inputs[0])["FAM"]
fam_18["57"] = zero_zero(inputs[0])["FAM"]
fam_18["60"] = zero_zero(inputs[0])["FAM"]


fam_21["3"] = zero_zero(inputs[0])["FAM"]
fam_21["6"] = zero_zero(inputs[0])["FAM"]
fam_21["9"] = zero_zero(inputs[0])["FAM"]
fam_21["12"] = zero_zero(inputs[0])["FAM"]
fam_21["15"] = zero_zero(inputs[0])["FAM"]
fam_21["18"] = zero_zero(inputs[0])["FAM"]
fam_21["21"] = zero_zero(inputs[0])["FAM"]
fam_21["24"] = zero_zero(inputs[0])["FAM"]
fam_21["27"] = zero_zero(inputs[0])["FAM"]
fam_21["30"] = zero_zero(inputs[0])["FAM"]
fam_21["33"] = zero_zero(inputs[0])["FAM"]
fam_21["36"] = zero_zero(inputs[0])["FAM"]
fam_21["39"] = zero_zero(inputs[0])["FAM"]
fam_21["42"] = zero_zero(inputs[0])["FAM"]
fam_21["45"] = zero_zero(inputs[0])["FAM"]
fam_21["48"] = zero_zero(inputs[0])["FAM"]
fam_21["51"] = zero_zero(inputs[0])["FAM"]
fam_21["54"] = zero_zero(inputs[0])["FAM"]
fam_21["57"] = zero_zero(inputs[0])["FAM"]
fam_21["60"] = zero_zero(inputs[0])["FAM"]


fam_24["3"] = zero_zero(inputs[0])["FAM"]
fam_24["6"] = zero_zero(inputs[0])["FAM"]
fam_24["9"] = zero_zero(inputs[0])["FAM"]
fam_24["12"] = zero_zero(inputs[0])["FAM"]
fam_24["15"] = zero_zero(inputs[0])["FAM"]
fam_24["18"] = zero_zero(inputs[0])["FAM"]
fam_24["21"] = zero_zero(inputs[0])["FAM"]
fam_24["24"] = zero_zero(inputs[0])["FAM"]
fam_24["27"] = zero_zero(inputs[0])["FAM"]
fam_24["30"] = zero_zero(inputs[0])["FAM"]
fam_24["33"] = zero_zero(inputs[0])["FAM"]
fam_24["36"] = zero_zero(inputs[0])["FAM"]
fam_24["39"] = zero_zero(inputs[0])["FAM"]
fam_24["42"] = zero_zero(inputs[0])["FAM"]
fam_24["45"] = zero_zero(inputs[0])["FAM"]
fam_24["48"] = zero_zero(inputs[0])["FAM"]
fam_24["51"] = zero_zero(inputs[0])["FAM"]
fam_24["54"] = zero_zero(inputs[0])["FAM"]
fam_24["57"] = zero_zero(inputs[0])["FAM"]
fam_24["60"] = zero_zero(inputs[0])["FAM"]


fam_27["3"] = zero_zero(inputs[0])["FAM"]
fam_27["6"] = zero_zero(inputs[0])["FAM"]
fam_27["9"] = zero_zero(inputs[0])["FAM"]
fam_27["12"] = zero_zero(inputs[0])["FAM"]
fam_27["15"] = zero_zero(inputs[0])["FAM"]
fam_27["18"] = zero_zero(inputs[0])["FAM"]
fam_27["21"] = zero_zero(inputs[0])["FAM"]
fam_27["24"] = zero_zero(inputs[0])["FAM"]
fam_27["27"] = zero_zero(inputs[0])["FAM"]
fam_27["30"] = zero_zero(inputs[0])["FAM"]
fam_27["33"] = zero_zero(inputs[0])["FAM"]
fam_27["36"] = zero_zero(inputs[0])["FAM"]
fam_27["39"] = zero_zero(inputs[0])["FAM"]
fam_27["42"] = zero_zero(inputs[0])["FAM"]
fam_27["45"] = zero_zero(inputs[0])["FAM"]
fam_27["48"] = zero_zero(inputs[0])["FAM"]
fam_27["51"] = zero_zero(inputs[0])["FAM"]
fam_27["54"] = zero_zero(inputs[0])["FAM"]
fam_27["57"] = zero_zero(inputs[0])["FAM"]
fam_27["60"] = zero_zero(inputs[0])["FAM"]


fam_30["3"] = zero_zero(inputs[0])["FAM"]
fam_30["6"] = zero_zero(inputs[0])["FAM"]
fam_30["9"] = zero_zero(inputs[0])["FAM"]
fam_30["12"] = zero_zero(inputs[0])["FAM"]
fam_30["15"] = zero_zero(inputs[0])["FAM"]
fam_30["18"] = zero_zero(inputs[0])["FAM"]
fam_30["21"] = zero_zero(inputs[0])["FAM"]
fam_30["24"] = zero_zero(inputs[0])["FAM"]
fam_30["27"] = zero_zero(inputs[0])["FAM"]
fam_30["30"] = zero_zero(inputs[0])["FAM"]
fam_30["33"] = zero_zero(inputs[0])["FAM"]
fam_30["36"] = zero_zero(inputs[0])["FAM"]
fam_30["39"] = zero_zero(inputs[0])["FAM"]
fam_30["42"] = zero_zero(inputs[0])["FAM"]
fam_30["45"] = zero_zero(inputs[0])["FAM"]
fam_30["48"] = zero_zero(inputs[0])["FAM"]
fam_30["51"] = zero_zero(inputs[0])["FAM"]
fam_30["54"] = zero_zero(inputs[0])["FAM"]
fam_30["57"] = zero_zero(inputs[0])["FAM"]
fam_30["60"] = zero_zero(inputs[0])["FAM"]

fam_33["3"] = zero_zero(inputs[0])["FAM"]
fam_33["6"] = zero_zero(inputs[0])["FAM"]
fam_33["9"] = zero_zero(inputs[0])["FAM"]
fam_33["12"] = zero_zero(inputs[0])["FAM"]
fam_33["15"] = zero_zero(inputs[0])["FAM"]
fam_33["18"] = zero_zero(inputs[0])["FAM"]
fam_33["21"] = zero_zero(inputs[0])["FAM"]
fam_33["24"] = zero_zero(inputs[0])["FAM"]
fam_33["27"] = zero_zero(inputs[0])["FAM"]
fam_33["30"] = zero_zero(inputs[0])["FAM"]
fam_33["33"] = zero_zero(inputs[0])["FAM"]
fam_33["36"] = zero_zero(inputs[0])["FAM"]
fam_33["39"] = zero_zero(inputs[0])["FAM"]
fam_33["42"] = zero_zero(inputs[0])["FAM"]
fam_33["45"] = zero_zero(inputs[0])["FAM"]
fam_33["48"] = zero_zero(inputs[0])["FAM"]
fam_33["51"] = zero_zero(inputs[0])["FAM"]
fam_33["54"] = zero_zero(inputs[0])["FAM"]
fam_33["57"] = zero_zero(inputs[0])["FAM"]
fam_33["60"] = zero_zero(inputs[0])["FAM"]

fam_36["3"] = zero_zero(inputs[0])["FAM"]
fam_36["6"] = zero_zero(inputs[0])["FAM"]
fam_36["9"] = zero_zero(inputs[0])["FAM"]
fam_36["12"] = zero_zero(inputs[0])["FAM"]
fam_36["15"] = zero_zero(inputs[0])["FAM"]
fam_36["18"] = zero_zero(inputs[0])["FAM"]
fam_36["21"] = zero_zero(inputs[0])["FAM"]
fam_36["24"] = zero_zero(inputs[0])["FAM"]
fam_36["27"] = zero_zero(inputs[0])["FAM"]
fam_36["30"] = zero_zero(inputs[0])["FAM"]
fam_36["33"] = zero_zero(inputs[0])["FAM"]
fam_36["36"] = zero_zero(inputs[0])["FAM"]
fam_36["39"] = zero_zero(inputs[0])["FAM"]
fam_36["42"] = zero_zero(inputs[0])["FAM"]
fam_36["45"] = zero_zero(inputs[0])["FAM"]
fam_36["48"] = zero_zero(inputs[0])["FAM"]
fam_36["51"] = zero_zero(inputs[0])["FAM"]
fam_36["54"] = zero_zero(inputs[0])["FAM"]
fam_36["57"] = zero_zero(inputs[0])["FAM"]
fam_36["60"] = zero_zero(inputs[0])["FAM"]


fam_39["3"] = zero_zero(inputs[0])["FAM"]
fam_39["6"] = zero_zero(inputs[0])["FAM"]
fam_39["9"] = zero_zero(inputs[0])["FAM"]
fam_39["12"] = zero_zero(inputs[0])["FAM"]
fam_39["15"] = zero_zero(inputs[0])["FAM"]
fam_39["18"] = zero_zero(inputs[0])["FAM"]
fam_39["21"] = zero_zero(inputs[0])["FAM"]
fam_39["24"] = zero_zero(inputs[0])["FAM"]
fam_39["27"] = zero_zero(inputs[0])["FAM"]
fam_39["30"] = zero_zero(inputs[0])["FAM"]
fam_39["33"] = zero_zero(inputs[0])["FAM"]
fam_39["36"] = zero_zero(inputs[0])["FAM"]
fam_39["39"] = zero_zero(inputs[0])["FAM"]
fam_39["42"] = zero_zero(inputs[0])["FAM"]
fam_39["45"] = zero_zero(inputs[0])["FAM"]
fam_39["48"] = zero_zero(inputs[0])["FAM"]
fam_39["51"] = zero_zero(inputs[0])["FAM"]
fam_39["54"] = zero_zero(inputs[0])["FAM"]
fam_39["57"] = zero_zero(inputs[0])["FAM"]
fam_39["60"] = zero_zero(inputs[0])["FAM"]


fam_42["3"] = zero_zero(inputs[0])["FAM"]
fam_42["6"] = zero_zero(inputs[0])["FAM"]
fam_42["9"] = zero_zero(inputs[0])["FAM"]
fam_42["12"] = zero_zero(inputs[0])["FAM"]
fam_42["15"] = zero_zero(inputs[0])["FAM"]
fam_42["18"] = zero_zero(inputs[0])["FAM"]
fam_42["21"] = zero_zero(inputs[0])["FAM"]
fam_42["24"] = zero_zero(inputs[0])["FAM"]
fam_42["27"] = zero_zero(inputs[0])["FAM"]
fam_42["30"] = zero_zero(inputs[0])["FAM"]
fam_42["33"] = zero_zero(inputs[0])["FAM"]
fam_42["36"] = zero_zero(inputs[0])["FAM"]
fam_42["39"] = zero_zero(inputs[0])["FAM"]
fam_42["42"] = zero_zero(inputs[0])["FAM"]
fam_42["45"] = zero_zero(inputs[0])["FAM"]
fam_42["48"] = zero_zero(inputs[0])["FAM"]
fam_42["51"] = zero_zero(inputs[0])["FAM"]
fam_42["54"] = zero_zero(inputs[0])["FAM"]
fam_42["57"] = zero_zero(inputs[0])["FAM"]
fam_42["60"] = zero_zero(inputs[0])["FAM"]

fam_45["3"] = zero_zero(inputs[0])["FAM"]
fam_45["6"] = zero_zero(inputs[0])["FAM"]
fam_45["9"] = zero_zero(inputs[0])["FAM"]
fam_45["12"] = zero_zero(inputs[0])["FAM"]
fam_45["15"] = zero_zero(inputs[0])["FAM"]
fam_45["18"] = zero_zero(inputs[0])["FAM"]
fam_45["21"] = zero_zero(inputs[0])["FAM"]
fam_45["24"] = zero_zero(inputs[0])["FAM"]
fam_45["27"] = zero_zero(inputs[0])["FAM"]
fam_45["30"] = zero_zero(inputs[0])["FAM"]
fam_45["33"] = zero_zero(inputs[0])["FAM"]
fam_45["36"] = zero_zero(inputs[0])["FAM"]
fam_45["39"] = zero_zero(inputs[0])["FAM"]
fam_45["42"] = zero_zero(inputs[0])["FAM"]
fam_45["45"] = zero_zero(inputs[0])["FAM"]
fam_45["48"] = zero_zero(inputs[0])["FAM"]
fam_45["51"] = zero_zero(inputs[0])["FAM"]
fam_45["54"] = zero_zero(inputs[0])["FAM"]
fam_45["57"] = zero_zero(inputs[0])["FAM"]
fam_45["60"] = zero_zero(inputs[0])["FAM"]


fam_48["3"] = zero_zero(inputs[0])["FAM"]
fam_48["6"] = zero_zero(inputs[0])["FAM"]
fam_48["9"] = zero_zero(inputs[0])["FAM"]
fam_48["12"] = zero_zero(inputs[0])["FAM"]
fam_48["15"] = zero_zero(inputs[0])["FAM"]
fam_48["18"] = zero_zero(inputs[0])["FAM"]
fam_48["21"] = zero_zero(inputs[0])["FAM"]
fam_48["24"] = zero_zero(inputs[0])["FAM"]
fam_48["27"] = zero_zero(inputs[0])["FAM"]
fam_48["30"] = zero_zero(inputs[0])["FAM"]
fam_48["33"] = zero_zero(inputs[0])["FAM"]
fam_48["36"] = zero_zero(inputs[0])["FAM"]
fam_48["39"] = zero_zero(inputs[0])["FAM"]
fam_48["42"] = zero_zero(inputs[0])["FAM"]
fam_48["45"] = zero_zero(inputs[0])["FAM"]
fam_48["48"] = zero_zero(inputs[0])["FAM"]
fam_48["51"] = zero_zero(inputs[0])["FAM"]
fam_48["54"] = zero_zero(inputs[0])["FAM"]
fam_48["57"] = zero_zero(inputs[0])["FAM"]
fam_48["60"] = zero_zero(inputs[0])["FAM"]


fam_51["3"] = zero_zero(inputs[0])["FAM"]
fam_51["6"] = zero_zero(inputs[0])["FAM"]
fam_51["9"] = zero_zero(inputs[0])["FAM"]
fam_51["12"] = zero_zero(inputs[0])["FAM"]
fam_51["15"] = zero_zero(inputs[0])["FAM"]
fam_51["18"] = zero_zero(inputs[0])["FAM"]
fam_51["21"] = zero_zero(inputs[0])["FAM"]
fam_51["24"] = zero_zero(inputs[0])["FAM"]
fam_51["27"] = zero_zero(inputs[0])["FAM"]
fam_51["30"] = zero_zero(inputs[0])["FAM"]
fam_51["33"] = zero_zero(inputs[0])["FAM"]
fam_51["36"] = zero_zero(inputs[0])["FAM"]
fam_51["39"] = zero_zero(inputs[0])["FAM"]
fam_51["42"] = zero_zero(inputs[0])["FAM"]
fam_51["45"] = zero_zero(inputs[0])["FAM"]
fam_51["48"] = zero_zero(inputs[0])["FAM"]
fam_51["51"] = zero_zero(inputs[0])["FAM"]
fam_51["54"] = zero_zero(inputs[0])["FAM"]
fam_51["57"] = zero_zero(inputs[0])["FAM"]
fam_51["60"] = zero_zero(inputs[0])["FAM"]


fam_54["3"] = zero_zero(inputs[0])["FAM"]
fam_54["6"] = zero_zero(inputs[0])["FAM"]
fam_54["9"] = zero_zero(inputs[0])["FAM"]
fam_54["12"] = zero_zero(inputs[0])["FAM"]
fam_54["15"] = zero_zero(inputs[0])["FAM"]
fam_54["18"] = zero_zero(inputs[0])["FAM"]
fam_54["21"] = zero_zero(inputs[0])["FAM"]
fam_54["24"] = zero_zero(inputs[0])["FAM"]
fam_54["27"] = zero_zero(inputs[0])["FAM"]
fam_54["30"] = zero_zero(inputs[0])["FAM"]
fam_54["33"] = zero_zero(inputs[0])["FAM"]
fam_54["36"] = zero_zero(inputs[0])["FAM"]
fam_54["39"] = zero_zero(inputs[0])["FAM"]
fam_54["42"] = zero_zero(inputs[0])["FAM"]
fam_54["45"] = zero_zero(inputs[0])["FAM"]
fam_54["48"] = zero_zero(inputs[0])["FAM"]
fam_54["51"] = zero_zero(inputs[0])["FAM"]
fam_54["54"] = zero_zero(inputs[0])["FAM"]
fam_54["57"] = zero_zero(inputs[0])["FAM"]
fam_54["60"] = zero_zero(inputs[0])["FAM"]


fam_57["3"] = zero_zero(inputs[0])["FAM"]
fam_57["6"] = zero_zero(inputs[0])["FAM"]
fam_57["9"] = zero_zero(inputs[0])["FAM"]
fam_57["12"] = zero_zero(inputs[0])["FAM"]
fam_57["15"] = zero_zero(inputs[0])["FAM"]
fam_57["18"] = zero_zero(inputs[0])["FAM"]
fam_57["21"] = zero_zero(inputs[0])["FAM"]
fam_57["24"] = zero_zero(inputs[0])["FAM"]
fam_57["27"] = zero_zero(inputs[0])["FAM"]
fam_57["30"] = zero_zero(inputs[0])["FAM"]
fam_57["33"] = zero_zero(inputs[0])["FAM"]
fam_57["36"] = zero_zero(inputs[0])["FAM"]
fam_57["39"] = zero_zero(inputs[0])["FAM"]
fam_57["42"] = zero_zero(inputs[0])["FAM"]
fam_57["45"] = zero_zero(inputs[0])["FAM"]
fam_57["48"] = zero_zero(inputs[0])["FAM"]
fam_57["51"] = zero_zero(inputs[0])["FAM"]
fam_57["54"] = zero_zero(inputs[0])["FAM"]
fam_57["57"] = zero_zero(inputs[0])["FAM"]
fam_57["60"] = zero_zero(inputs[0])["FAM"]


fam_60["3"] = zero_zero(inputs[0])["FAM"]
fam_60["6"] = zero_zero(inputs[0])["FAM"]
fam_60["9"] = zero_zero(inputs[0])["FAM"]
fam_60["12"] = zero_zero(inputs[0])["FAM"]
fam_60["15"] = zero_zero(inputs[0])["FAM"]
fam_60["18"] = zero_zero(inputs[0])["FAM"]
fam_60["21"] = zero_zero(inputs[0])["FAM"]
fam_60["24"] = zero_zero(inputs[0])["FAM"]
fam_60["27"] = zero_zero(inputs[0])["FAM"]
fam_60["30"] = zero_zero(inputs[0])["FAM"]
fam_60["33"] = zero_zero(inputs[0])["FAM"]
fam_60["36"] = zero_zero(inputs[0])["FAM"]
fam_60["39"] = zero_zero(inputs[0])["FAM"]
fam_60["42"] = zero_zero(inputs[0])["FAM"]
fam_60["45"] = zero_zero(inputs[0])["FAM"]
fam_60["48"] = zero_zero(inputs[0])["FAM"]
fam_60["51"] = zero_zero(inputs[0])["FAM"]
fam_60["54"] = zero_zero(inputs[0])["FAM"]
fam_60["57"] = zero_zero(inputs[0])["FAM"]
fam_60["60"] = zero_zero(inputs[0])["FAM"]



# Copper IUD
copper_iud_no = {}
copper_iud_mild = {}
copper_iud_moderate = {}
copper_iud_severe = {}
copper_iud_3 = {}
copper_iud_6 = {}
copper_iud_9 = {}
copper_iud_12 = {}
copper_iud_15 = {}
copper_iud_18 = {}
copper_iud_21 = {}
copper_iud_24 = {}
copper_iud_27 = {}
copper_iud_30 = {}
copper_iud_33 = {}
copper_iud_36 = {}
copper_iud_39 = {}
copper_iud_42 = {}
copper_iud_45 = {}
copper_iud_48 = {}
copper_iud_51 = {}
copper_iud_54 = {}
copper_iud_57 = {}
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
copper_iud_3["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_3["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_6["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_6["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_9["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_9["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_12["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_12["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_15["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_15["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_18["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_18["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_21["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_21["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_24["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_24["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_27["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_27["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_30["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_30["60"] = zero_zero(inputs[0])["Copper IUD"]

copper_iud_33["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_33["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_36["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_36["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_39["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_39["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_42["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_42["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_45["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_45["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_48["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_48["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_51["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_51["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_54["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_54["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_57["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_57["60"] = zero_zero(inputs[0])["Copper IUD"]


copper_iud_60["3"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["6"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["9"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["12"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["15"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["18"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["21"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["24"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["27"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["30"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["33"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["36"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["39"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["42"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["45"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["48"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["51"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["54"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["57"] = zero_zero(inputs[0])["Copper IUD"]
copper_iud_60["60"] = zero_zero(inputs[0])["Copper IUD"]


# Sterilization
sterilization_no = {}
sterilization_mild = {}
sterilization_moderate = {}
sterilization_severe = {}
sterilization_3 = {}
sterilization_6 = {}
sterilization_9 = {}
sterilization_12 = {}
sterilization_15 = {}
sterilization_18 = {}
sterilization_21 = {}
sterilization_24 = {}
sterilization_27 = {}
sterilization_30 = {}
sterilization_33 = {}
sterilization_36 = {}
sterilization_39 = {}
sterilization_42 = {}
sterilization_45 = {}
sterilization_48 = {}
sterilization_51 = {}
sterilization_54 = {}
sterilization_57 = {}
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
sterilization_3["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_3["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_6["3"] = zero_zero(inputs[0])["Sterilization"]    
sterilization_6["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_6["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_9["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_9["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_12["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_12["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_15["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_15["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_18["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_18["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_21["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_21["60"] = zero_zero(inputs[0])["Sterilization"]

sterilization_24["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_24["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_27["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_27["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_30["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_30["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_33["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_33["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_36["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_36["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_39["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_39["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_42["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_42["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_45["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_45["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_48["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_48["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_51["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_51["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_54["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_54["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_57["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_57["60"] = zero_zero(inputs[0])["Sterilization"]


sterilization_60["3"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["6"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["9"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["12"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["15"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["18"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["21"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["24"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["27"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["30"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["33"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["36"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["39"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["42"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["45"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["48"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["51"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["54"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["57"] = zero_zero(inputs[0])["Sterilization"]
sterilization_60["60"] = zero_zero(inputs[0])["Sterilization"]


# Spermicide
spermicide_no = {}
spermicide_mild = {}
spermicide_moderate = {}
spermicide_severe = {}
spermicide_3 = {}
spermicide_6 = {}
spermicide_9 = {}
spermicide_12 = {}
spermicide_15 = {}
spermicide_18 = {}
spermicide_21 = {}
spermicide_24 = {}
spermicide_27 = {}
spermicide_30 = {}
spermicide_33 = {}
spermicide_36 = {}
spermicide_39 = {}
spermicide_42 = {}
spermicide_45 = {}
spermicide_48 = {}
spermicide_51 = {}
spermicide_54 = {}
spermicide_57 = {}
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
spermicide_3["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["9"] = zero_zero(inputs[0])["Spermicide"]

spermicide_3["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_3["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_6["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_6["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_9["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_9["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_12["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_12["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_15["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_15["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_18["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_18["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_21["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_21["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_24["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_24["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_27["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_27["60"] = zero_zero(inputs[0])["Spermicide"]

spermicide_30["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_30["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_33["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_33["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_36["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_36["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_39["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_39["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_42["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_42["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_45["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_45["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_48["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_48["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_51["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_51["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_54["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_54["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_57["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_57["60"] = zero_zero(inputs[0])["Spermicide"]


spermicide_60["3"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["6"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["9"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["12"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["15"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["18"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["21"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["24"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["27"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["30"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["33"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["36"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["39"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["42"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["45"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["48"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["51"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["54"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["57"] = zero_zero(inputs[0])["Spermicide"]
spermicide_60["60"] = zero_zero(inputs[0])["Spermicide"]




# Withdrawal
withdrawal_no = {}
withdrawal_mild = {}
withdrawal_moderate = {}
withdrawal_severe = {}
withdrawal_3 = {}
withdrawal_6 = {}
withdrawal_9 = {}
withdrawal_12 = {}
withdrawal_15 = {}
withdrawal_18 = {}
withdrawal_21 = {}
withdrawal_24 = {}
withdrawal_27 = {}
withdrawal_30 = {}
withdrawal_33 = {}
withdrawal_36 = {}
withdrawal_39 = {}
withdrawal_42 = {}
withdrawal_45 = {}
withdrawal_48 = {}
withdrawal_51 = {}
withdrawal_54 = {}
withdrawal_57 = {}
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
withdrawal_3["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_3["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_6["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_6["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_9["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_9["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_12["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_12["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_15["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_15["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_18["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_18["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_21["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_21["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_24["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_24["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_27["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_27["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_30["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_30["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_33["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_33["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_36["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_36["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_39["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_39["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_42["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_42["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_45["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_45["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_48["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_48["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_51["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_51["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_54["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_54["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_57["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_57["60"] = zero_zero(inputs[0])["Withdrawal"]


withdrawal_60["3"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["6"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["9"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["12"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["15"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["18"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["21"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["24"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["27"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["30"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["33"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["36"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["39"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["42"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["45"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["48"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["51"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["54"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["57"] = zero_zero(inputs[0])["Withdrawal"]
withdrawal_60["60"] = zero_zero(inputs[0])["Withdrawal"]



# Arm Implant

arm_implant_3 = {}
arm_implant_6 = {}
arm_implant_9 = {}
arm_implant_12 = {}
arm_implant_15 = {}
arm_implant_18 = {}
arm_implant_21 = {}
arm_implant_24 = {}
arm_implant_27 = {}
arm_implant_30 = {}
arm_implant_33 = {}
arm_implant_36 = {}
arm_implant_39 = {}
arm_implant_42 = {}
arm_implant_45 = {}
arm_implant_48 = {}
arm_implant_51 = {}
arm_implant_54 = {}
arm_implant_57 = {}
arm_implant_60 = {}

arr_arm = inputs[5]
arm_implant_3["3"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["6"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["9"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["12"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["15"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["18"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["21"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["24"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["27"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["30"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["33"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["36"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["39"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["42"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["45"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["48"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["51"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["54"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["57"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["60"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["no"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["mild"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["moderate"] = pos_zero(arr_arm, 3)["Arm Implant"]
arm_implant_3["severe"] = pos_zero(arr_arm, 3)["Arm Implant"]

arm_implant_6["3"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["6"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["9"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["12"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["15"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["18"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["21"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["24"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["27"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["30"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["33"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["36"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["39"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["42"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["45"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["48"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["51"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["54"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["57"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["60"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["no"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["mild"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["moderate"] = pos_zero(arr_arm, 6)["Arm Implant"]
arm_implant_6["severe"] = pos_zero(arr_arm, 6)["Arm Implant"]

arm_implant_9["3"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["6"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["9"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["12"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["15"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["18"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["21"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["24"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["27"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["30"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["33"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["36"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["39"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["42"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["45"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["48"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["51"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["54"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["57"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["60"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["no"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["mild"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["moderate"] = pos_zero(arr_arm, 9)["Arm Implant"]
arm_implant_9["severe"] = pos_zero(arr_arm, 9)["Arm Implant"]

arm_implant_12["3"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["6"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["9"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["12"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["15"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["18"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["21"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["24"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["27"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["30"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["33"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["36"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["39"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["42"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["45"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["48"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["51"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["54"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["57"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["60"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["no"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["mild"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["moderate"] = pos_zero(arr_arm, 12)["Arm Implant"]
arm_implant_12["severe"] = pos_zero(arr_arm, 12)["Arm Implant"]

arm_implant_15["3"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["6"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["9"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["12"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["15"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["18"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["21"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["24"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["27"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["30"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["33"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["36"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["39"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["42"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["45"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["48"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["51"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["54"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["57"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["60"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["no"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["mild"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["moderate"] = pos_zero(arr_arm, 15)["Arm Implant"]
arm_implant_15["severe"] = pos_zero(arr_arm, 15)["Arm Implant"]

arm_implant_18["3"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["6"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["9"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["12"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["15"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["18"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["21"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["24"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["27"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["30"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["33"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["36"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["39"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["42"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["45"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["48"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["51"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["54"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["57"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["60"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["no"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["mild"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["moderate"] = pos_zero(arr_arm, 18)["Arm Implant"]
arm_implant_18["severe"] = pos_zero(arr_arm, 18)["Arm Implant"]

arm_implant_21["3"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["6"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["9"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["12"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["15"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["18"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["21"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["24"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["27"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["30"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["33"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["36"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["39"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["42"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["45"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["48"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["51"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["54"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["57"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["60"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["no"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["mild"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["moderate"] = pos_zero(arr_arm, 21)["Arm Implant"]
arm_implant_21["severe"] = pos_zero(arr_arm, 21)["Arm Implant"]

arm_implant_24["3"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["6"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["9"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["12"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["15"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["18"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["21"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["24"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["27"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["30"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["33"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["36"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["39"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["42"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["45"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["48"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["51"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["54"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["57"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["60"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["no"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["mild"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["moderate"] = pos_zero(arr_arm, 24)["Arm Implant"]
arm_implant_24["severe"] = pos_zero(arr_arm, 24)["Arm Implant"]

arm_implant_27["3"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["6"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["9"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["12"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["15"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["18"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["21"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["24"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["27"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["30"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["33"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["36"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["39"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["42"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["45"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["48"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["51"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["54"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["57"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["60"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["no"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["mild"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["moderate"] = pos_zero(arr_arm, 27)["Arm Implant"]
arm_implant_27["severe"] = pos_zero(arr_arm, 27)["Arm Implant"]

arm_implant_30["3"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["6"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["9"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["12"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["15"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["18"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["21"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["24"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["27"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["30"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["33"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["36"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["39"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["42"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["45"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["48"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["51"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["54"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["57"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["60"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["no"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["mild"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["moderate"] = pos_zero(arr_arm, 30)["Arm Implant"]
arm_implant_30["severe"] = pos_zero(arr_arm, 30)["Arm Implant"]

arm_implant_33["3"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["6"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["9"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["12"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["15"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["18"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["21"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["24"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["27"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["30"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["33"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["36"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["39"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["42"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["45"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["48"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["51"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["54"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["57"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["60"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["no"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["mild"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["moderate"] = pos_zero(arr_arm, 33)["Arm Implant"]
arm_implant_33["severe"] = pos_zero(arr_arm, 33)["Arm Implant"]

arm_implant_36["3"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["6"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["9"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["12"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["15"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["18"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["21"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["24"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["27"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["30"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["33"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["36"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["39"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["42"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["45"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["48"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["51"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["54"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["57"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["60"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["no"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["mild"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["moderate"] = pos_zero(arr_arm, 36)["Arm Implant"]
arm_implant_36["severe"] = pos_zero(arr_arm, 36)["Arm Implant"]

arm_implant_39["3"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["6"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["9"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["12"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["15"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["18"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["21"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["24"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["27"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["30"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["33"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["36"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["39"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["42"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["45"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["48"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["51"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["54"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["57"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["60"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["no"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["mild"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["moderate"] = pos_zero(arr_arm, 39)["Arm Implant"]
arm_implant_39["severe"] = pos_zero(arr_arm, 39)["Arm Implant"]

arm_implant_42["3"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["6"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["9"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["12"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["15"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["18"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["21"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["24"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["27"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["30"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["33"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["36"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["39"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["42"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["45"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["48"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["51"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["54"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["57"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["60"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["no"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["mild"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["moderate"] = pos_zero(arr_arm, 42)["Arm Implant"]
arm_implant_42["severe"] = pos_zero(arr_arm, 42)["Arm Implant"]

arm_implant_45["3"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["6"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["9"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["12"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["15"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["18"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["21"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["24"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["27"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["30"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["33"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["36"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["39"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["42"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["45"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["48"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["51"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["54"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["57"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["60"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["no"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["mild"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["moderate"] = pos_zero(arr_arm, 45)["Arm Implant"]
arm_implant_45["severe"] = pos_zero(arr_arm, 45)["Arm Implant"]

arm_implant_48["3"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["6"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["9"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["12"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["15"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["18"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["21"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["24"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["27"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["30"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["33"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["36"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["39"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["42"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["45"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["48"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["51"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["54"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["57"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["60"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["no"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["mild"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["moderate"] = pos_zero(arr_arm, 48)["Arm Implant"]
arm_implant_48["severe"] = pos_zero(arr_arm, 48)["Arm Implant"]

arm_implant_51["3"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["6"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["9"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["12"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["15"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["18"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["21"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["24"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["27"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["30"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["33"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["36"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["39"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["42"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["45"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["48"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["51"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["54"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["57"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["60"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["no"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["mild"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["moderate"] = pos_zero(arr_arm, 51)["Arm Implant"]
arm_implant_51["severe"] = pos_zero(arr_arm, 51)["Arm Implant"]

arm_implant_54["3"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["6"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["9"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["12"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["15"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["18"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["21"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["24"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["27"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["30"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["33"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["36"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["39"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["42"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["45"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["48"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["51"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["54"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["57"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["60"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["no"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["mild"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["moderate"] = pos_zero(arr_arm, 54)["Arm Implant"]
arm_implant_54["severe"] = pos_zero(arr_arm, 54)["Arm Implant"]

arm_implant_57["3"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["6"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["9"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["12"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["15"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["18"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["21"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["24"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["27"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["30"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["33"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["36"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["39"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["42"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["45"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["48"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["51"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["54"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["57"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["60"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["no"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["mild"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["moderate"] = pos_zero(arr_arm, 57)["Arm Implant"]
arm_implant_57["severe"] = pos_zero(arr_arm, 57)["Arm Implant"]

arm_implant_60["3"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["6"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["9"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["12"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["15"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["18"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["21"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["24"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["27"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["30"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["33"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["36"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["39"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["42"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["45"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["48"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["51"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["54"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["57"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["60"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["no"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["mild"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["moderate"] = pos_zero(arr_arm, 60)["Arm Implant"]
arm_implant_60["severe"] = pos_zero(arr_arm, 60)["Arm Implant"]



    
# Mini Pill

mini_pill_3 = {}
mini_pill_6 = {}
mini_pill_9 = {}
mini_pill_12 = {}
mini_pill_15 = {}
mini_pill_18 = {}
mini_pill_21 = {}
mini_pill_24 = {}
mini_pill_27 = {}
mini_pill_30 = {}
mini_pill_33 = {}
mini_pill_36 = {}
mini_pill_39 = {}
mini_pill_42 = {}
mini_pill_45 = {}
mini_pill_48 = {}
mini_pill_51 = {}
mini_pill_54 = {}
mini_pill_57 = {}
mini_pill_60 = {}

arr_mini = inputs[6]
mini_pill_3["3"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["6"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["9"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["12"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["15"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["18"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["21"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["24"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["27"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["30"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["33"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["36"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["39"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["42"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["45"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["48"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["51"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["54"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["57"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["60"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["no"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["mild"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["moderate"] = pos_zero(arr_mini, 3)["Mini Pill"]
mini_pill_3["severe"] = pos_zero(arr_mini, 3)["Mini Pill"]

mini_pill_6["3"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["6"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["9"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["12"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["15"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["18"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["21"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["24"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["27"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["30"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["33"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["36"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["39"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["42"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["45"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["48"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["51"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["54"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["57"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["60"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["no"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["mild"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["moderate"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_6["severe"] = pos_zero(arr_mini, 6)["Mini Pill"]
mini_pill_9["3"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["6"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["9"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["12"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["15"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["18"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["21"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["24"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["27"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["30"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["33"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["36"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["39"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["42"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["45"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["48"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["51"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["54"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["57"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["60"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["no"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["mild"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["moderate"] = pos_zero(arr_mini, 9)["Mini Pill"]
mini_pill_9["severe"] = pos_zero(arr_mini, 9)["Mini Pill"]

mini_pill_12["3"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["6"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["9"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["12"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["15"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["18"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["21"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["24"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["27"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["30"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["33"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["36"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["39"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["42"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["45"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["48"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["51"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["54"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["57"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["60"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["no"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["mild"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["moderate"] = pos_zero(arr_mini, 12)["Mini Pill"]
mini_pill_12["severe"] = pos_zero(arr_mini, 12)["Mini Pill"]

mini_pill_15["3"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["6"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["9"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["12"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["15"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["18"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["21"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["24"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["27"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["30"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["33"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["36"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["39"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["42"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["45"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["48"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["51"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["54"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["57"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["60"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["no"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["mild"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["moderate"] = pos_zero(arr_mini, 15)["Mini Pill"]
mini_pill_15["severe"] = pos_zero(arr_mini, 15)["Mini Pill"]

mini_pill_18["3"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["6"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["9"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["12"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["15"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["18"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["21"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["24"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["27"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["30"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["33"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["36"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["39"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["42"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["45"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["48"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["51"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["54"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["57"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["60"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["no"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["mild"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["moderate"] = pos_zero(arr_mini, 18)["Mini Pill"]
mini_pill_18["severe"] = pos_zero(arr_mini, 18)["Mini Pill"]

mini_pill_21["3"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["6"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["9"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["12"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["15"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["18"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["21"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["24"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["27"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["30"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["33"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["36"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["39"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["42"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["45"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["48"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["51"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["54"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["57"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["60"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["no"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["mild"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["moderate"] = pos_zero(arr_mini, 21)["Mini Pill"]
mini_pill_21["severe"] = pos_zero(arr_mini, 21)["Mini Pill"]

mini_pill_24["3"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["6"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["9"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["12"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["15"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["18"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["21"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["24"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["27"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["30"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["33"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["36"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["39"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["42"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["45"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["48"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["51"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["54"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["57"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["60"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["no"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["mild"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["moderate"] = pos_zero(arr_mini, 24)["Mini Pill"]
mini_pill_24["severe"] = pos_zero(arr_mini, 24)["Mini Pill"]

mini_pill_27["3"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["6"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["9"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["12"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["15"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["18"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["21"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["24"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["27"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["30"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["33"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["36"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["39"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["42"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["45"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["48"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["51"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["54"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["57"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["60"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["no"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["mild"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["moderate"] = pos_zero(arr_mini, 27)["Mini Pill"]
mini_pill_27["severe"] = pos_zero(arr_mini, 27)["Mini Pill"]

mini_pill_30["3"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["6"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["9"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["12"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["15"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["18"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["21"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["24"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["27"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["30"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["33"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["36"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["39"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["42"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["45"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["48"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["51"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["54"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["57"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["60"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["no"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["mild"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["moderate"] = pos_zero(arr_mini, 30)["Mini Pill"]
mini_pill_30["severe"] = pos_zero(arr_mini, 30)["Mini Pill"]

mini_pill_33["3"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["6"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["9"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["12"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["15"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["18"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["21"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["24"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["27"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["30"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["33"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["36"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["39"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["42"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["45"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["48"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["51"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["54"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["57"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["60"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["no"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["mild"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["moderate"] = pos_zero(arr_mini, 33)["Mini Pill"]
mini_pill_33["severe"] = pos_zero(arr_mini, 33)["Mini Pill"]

mini_pill_36["3"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["6"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["9"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["12"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["15"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["18"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["21"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["24"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["27"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["30"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["33"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["36"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["39"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["42"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["45"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["48"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["51"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["54"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["57"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["60"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["no"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["mild"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["moderate"] = pos_zero(arr_mini, 36)["Mini Pill"]
mini_pill_36["severe"] = pos_zero(arr_mini, 36)["Mini Pill"]

mini_pill_39["3"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["6"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["9"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["12"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["15"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["18"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["21"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["24"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["27"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["30"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["33"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["36"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["39"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["42"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["45"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["48"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["51"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["54"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["57"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["60"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["no"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["mild"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["moderate"] = pos_zero(arr_mini, 39)["Mini Pill"]
mini_pill_39["severe"] = pos_zero(arr_mini, 39)["Mini Pill"]

mini_pill_42["3"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["6"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["9"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["12"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["15"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["18"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["21"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["24"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["27"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["30"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["33"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["36"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["39"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["42"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["45"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["48"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["51"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["54"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["57"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["60"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["no"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["mild"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["moderate"] = pos_zero(arr_mini, 42)["Mini Pill"]
mini_pill_42["severe"] = pos_zero(arr_mini, 42)["Mini Pill"]

mini_pill_45["3"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["6"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["9"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["12"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["15"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["18"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["21"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["24"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["27"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["30"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["33"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["36"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["39"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["42"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["45"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["48"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["51"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["54"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["57"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["60"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["no"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["mild"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["moderate"] = pos_zero(arr_mini, 45)["Mini Pill"]
mini_pill_45["severe"] = pos_zero(arr_mini, 45)["Mini Pill"]

mini_pill_48["3"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["6"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["9"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["12"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["15"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["18"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["21"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["24"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["27"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["30"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["33"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["36"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["39"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["42"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["45"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["48"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["51"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["54"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["57"] = pos_zero(arr_mini, 48)["Mini Pill"]

mini_pill_48["60"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["no"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["mild"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["moderate"] = pos_zero(arr_mini, 48)["Mini Pill"]
mini_pill_48["severe"] = pos_zero(arr_mini, 48)["Mini Pill"]

mini_pill_51["3"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["6"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["9"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["12"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["15"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["18"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["21"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["24"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["27"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["30"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["33"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["36"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["39"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["42"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["45"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["48"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["51"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["54"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["57"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["60"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["no"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["mild"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["moderate"] = pos_zero(arr_mini, 51)["Mini Pill"]
mini_pill_51["severe"] = pos_zero(arr_mini, 51)["Mini Pill"]

mini_pill_54["3"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["6"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["9"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["12"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["15"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["18"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["21"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["24"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["27"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["30"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["33"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["36"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["39"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["42"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["45"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["48"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["51"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["54"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["57"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["60"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["no"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["mild"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["moderate"] = pos_zero(arr_mini, 54)["Mini Pill"]
mini_pill_54["severe"] = pos_zero(arr_mini, 54)["Mini Pill"]

mini_pill_57["3"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["6"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["9"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["12"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["15"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["18"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["21"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["24"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["27"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["30"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["33"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["36"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["39"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["42"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["45"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["48"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["51"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["54"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["57"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["60"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["no"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["mild"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["moderate"] = pos_zero(arr_mini, 57)["Mini Pill"]
mini_pill_57["severe"] = pos_zero(arr_mini, 57)["Mini Pill"]

mini_pill_60["3"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["6"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["9"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["12"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["15"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["18"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["21"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["24"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["27"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["30"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["33"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["36"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["39"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["42"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["45"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["48"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["51"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["54"] = pos_zero(arr_mini, 60)["Mini Pill"]
mini_pill_60["57"] = pos_zero(arr_mini, 60)["Mini Pill"]
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
    hormonal_iud_no["6"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["9"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["12"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["15"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["18"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["24"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["27"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["30"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["33"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["36"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["39"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["45"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["48"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["51"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["54"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_no["57"] = neg_zero(arr)["Hormonal IUD"]
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
    hormonal_iud_mild["6"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["9"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["12"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["15"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["18"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["24"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["27"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["30"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["33"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["36"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["39"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["45"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["48"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["51"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["54"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_mild["57"] = neg_zero(arr)["Hormonal IUD"]
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
    hormonal_iud_moderate["6"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["9"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["12"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["15"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["18"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["24"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["27"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["30"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["33"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["36"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["39"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["45"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["48"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["51"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["54"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_moderate["57"] = neg_zero(arr)["Hormonal IUD"]
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
    hormonal_iud_severe["6"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["9"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["12"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["15"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["18"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["21"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["24"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["27"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["30"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["33"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["36"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["39"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["42"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["45"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["48"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["51"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["54"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["57"] = neg_zero(arr)["Hormonal IUD"]
    hormonal_iud_severe["60"] = neg_zero(arr)["Hormonal IUD"]
    
    

# Ring
ring_3 = {}
ring_6 = {}
ring_9 = {}
ring_12 = {}
ring_15 = {}
ring_18 = {}
ring_21 = {}
ring_24 = {}
ring_27 = {}
ring_30 = {}
ring_33 = {}
ring_36 = {}
ring_39 = {}
ring_42 = {}
ring_45 = {}
ring_48 = {}
ring_51 = {}
ring_54 = {}
ring_57 = {}
ring_60 = {}

for arr in inputs[4:8]:
    if arr[-6] == "no":
        ring_3["no"] = pos_neg(arr, 3)["Ring"]
        ring_6["no"] = pos_neg(arr, 6)["Ring"]
        ring_9["no"] = pos_neg(arr, 9)["Ring"]
        ring_12["no"] = pos_neg(arr, 12)["Ring"]
        ring_15["no"] = pos_neg(arr, 15)["Ring"]
        ring_18["no"] = pos_neg(arr, 18)["Ring"]
        ring_21["no"] = pos_neg(arr, 21)["Ring"]
        ring_24["no"] = pos_neg(arr, 24)["Ring"]
        ring_27["no"] = pos_neg(arr, 27)["Ring"]
        ring_30["no"] = pos_neg(arr, 30)["Ring"]
        ring_33["no"] = pos_neg(arr, 33)["Ring"]
        ring_36["no"] = pos_neg(arr, 36)["Ring"]
        ring_39["no"] = pos_neg(arr, 39)["Ring"]
        ring_42["no"] = pos_neg(arr, 42)["Ring"]
        ring_45["no"] = pos_neg(arr, 45)["Ring"]
        ring_48["no"] = pos_neg(arr, 48)["Ring"]
        ring_51["no"] = pos_neg(arr, 51)["Ring"]
        ring_54["no"] = pos_neg(arr, 54)["Ring"]
        ring_57["no"] = pos_neg(arr, 57)["Ring"]
        ring_60["no"] = pos_neg(arr, 60)["Ring"]
        
    elif arr[-6] == "mild":
        ring_3["mild"] = pos_neg(arr, 3)["Ring"]
        ring_6["mild"] = pos_neg(arr, 6)["Ring"]
        ring_9["mild"] = pos_neg(arr, 9)["Ring"]
        ring_12["mild"] = pos_neg(arr, 12)["Ring"]
        ring_15["mild"] = pos_neg(arr, 15)["Ring"]
        ring_18["mild"] = pos_neg(arr, 18)["Ring"]
        ring_21["mild"] = pos_neg(arr, 21)["Ring"]
        ring_24["mild"] = pos_neg(arr, 24)["Ring"]
        ring_27["mild"] = pos_neg(arr, 27)["Ring"]
        ring_30["mild"] = pos_neg(arr, 30)["Ring"]
        ring_33["mild"] = pos_neg(arr, 33)["Ring"]
        ring_36["mild"] = pos_neg(arr, 36)["Ring"]
        ring_39["mild"] = pos_neg(arr, 39)["Ring"]
        ring_42["mild"] = pos_neg(arr, 42)["Ring"]
        ring_45["mild"] = pos_neg(arr, 45)["Ring"]
        ring_48["mild"] = pos_neg(arr, 48)["Ring"]
        ring_51["mild"] = pos_neg(arr, 51)["Ring"]
        ring_54["mild"] = pos_neg(arr, 54)["Ring"]
        ring_57["mild"] = pos_neg(arr, 57)["Ring"]
        ring_60["mild"] = pos_neg(arr, 60)["Ring"]
        
    elif arr[-6] == "moderate":
        ring_3["moderate"] = pos_neg(arr, 3)["Ring"]
        ring_6["moderate"] = pos_neg(arr, 6)["Ring"]
        ring_9["moderate"] = pos_neg(arr, 9)["Ring"]
        ring_12["moderate"] = pos_neg(arr, 12)["Ring"]
        ring_15["moderate"] = pos_neg(arr, 15)["Ring"]
        ring_18["moderate"] = pos_neg(arr, 18)["Ring"]
        ring_21["moderate"] = pos_neg(arr, 21)["Ring"]
        ring_24["moderate"] = pos_neg(arr, 24)["Ring"]
        ring_27["moderate"] = pos_neg(arr, 27)["Ring"]
        ring_30["moderate"] = pos_neg(arr, 30)["Ring"]
        ring_33["moderate"] = pos_neg(arr, 33)["Ring"]
        ring_36["moderate"] = pos_neg(arr, 36)["Ring"]
        ring_39["moderate"] = pos_neg(arr, 39)["Ring"]
        ring_42["moderate"] = pos_neg(arr, 42)["Ring"]
        ring_45["moderate"] = pos_neg(arr, 45)["Ring"]
        ring_48["moderate"] = pos_neg(arr, 48)["Ring"]
        ring_51["moderate"] = pos_neg(arr, 51)["Ring"]
        ring_54["moderate"] = pos_neg(arr, 54)["Ring"]
        ring_57["moderate"] = pos_neg(arr, 57)["Ring"]
        ring_60["moderate"] = pos_neg(arr, 60)["Ring"]
        
    elif arr[-6] == "severe":
        ring_3["severe"] = pos_neg(arr, 3)["Ring"]
        ring_6["severe"] = pos_neg(arr, 6)["Ring"]
        ring_9["severe"] = pos_neg(arr, 9)["Ring"]
        ring_12["severe"] = pos_neg(arr, 12)["Ring"]
        ring_15["severe"] = pos_neg(arr, 15)["Ring"]
        ring_18["severe"] = pos_neg(arr, 18)["Ring"]
        ring_21["severe"] = pos_neg(arr, 21)["Ring"]
        ring_24["severe"] = pos_neg(arr, 24)["Ring"]
        ring_27["severe"] = pos_neg(arr, 27)["Ring"]
        ring_30["severe"] = pos_neg(arr, 30)["Ring"]
        ring_33["severe"] = pos_neg(arr, 33)["Ring"]
        ring_36["severe"] = pos_neg(arr, 36)["Ring"]
        ring_39["severe"] = pos_neg(arr, 39)["Ring"]
        ring_42["severe"] = pos_neg(arr, 42)["Ring"]
        ring_45["severe"] = pos_neg(arr, 45)["Ring"]
        ring_48["severe"] = pos_neg(arr, 48)["Ring"]
        ring_51["severe"] = pos_neg(arr, 51)["Ring"]
        ring_54["severe"] = pos_neg(arr, 54)["Ring"]
        ring_57["severe"] = pos_neg(arr, 57)["Ring"]
        ring_60["severe"] = pos_neg(arr, 60)["Ring"]

        
        
        

# Shot
shot_3 = {}
shot_6 = {}
shot_9 = {}
shot_12 = {}
shot_15 = {}
shot_18 = {}
shot_21 = {}
shot_24 = {}
shot_27 = {}
shot_30 = {}
shot_33 = {}
shot_36 = {}
shot_39 = {}
shot_42 = {}
shot_45 = {}
shot_48 = {}
shot_51 = {}
shot_54 = {}
shot_57 = {}
shot_60 = {}


for arr in inputs[4:8]:
    if arr[-6] == "no":
        shot_3["no"] = pos_neg(arr, 3)["Shot"]
        shot_6["no"] = pos_neg(arr, 6)["Shot"]
        shot_9["no"] = pos_neg(arr, 9)["Shot"]
        shot_12["no"] = pos_neg(arr, 12)["Shot"]
        shot_15["no"] = pos_neg(arr, 15)["Shot"]
        shot_18["no"] = pos_neg(arr, 18)["Shot"]
        shot_21["no"] = pos_neg(arr, 21)["Shot"]
        shot_24["no"] = pos_neg(arr, 24)["Shot"]
        shot_27["no"] = pos_neg(arr, 27)["Shot"]
        shot_30["no"] = pos_neg(arr, 30)["Shot"]
        shot_33["no"] = pos_neg(arr, 33)["Shot"]
        shot_36["no"] = pos_neg(arr, 36)["Shot"]
        shot_39["no"] = pos_neg(arr, 39)["Shot"]
        shot_42["no"] = pos_neg(arr, 42)["Shot"]
        shot_45["no"] = pos_neg(arr, 45)["Shot"]
        shot_48["no"] = pos_neg(arr, 48)["Shot"]
        shot_51["no"] = pos_neg(arr, 51)["Shot"]
        shot_54["no"] = pos_neg(arr, 54)["Shot"]
        shot_57["no"] = pos_neg(arr, 57)["Shot"]
        shot_60["no"] = pos_neg(arr, 60)["Shot"]
        
        
        
    elif arr[-6] == "mild":
        shot_3["mild"] = pos_neg(arr, 3)["Shot"]
        shot_6["mild"] = pos_neg(arr, 6)["Shot"]
        shot_9["mild"] = pos_neg(arr, 9)["Shot"]
        shot_12["mild"] = pos_neg(arr, 12)["Shot"]
        shot_15["mild"] = pos_neg(arr, 15)["Shot"]
        shot_18["mild"] = pos_neg(arr, 18)["Shot"]
        shot_21["mild"] = pos_neg(arr, 21)["Shot"]
        shot_24["mild"] = pos_neg(arr, 24)["Shot"]
        shot_27["mild"] = pos_neg(arr, 27)["Shot"]
        shot_30["mild"] = pos_neg(arr, 30)["Shot"]
        shot_33["mild"] = pos_neg(arr, 33)["Shot"]
        shot_36["mild"] = pos_neg(arr, 36)["Shot"]
        shot_39["mild"] = pos_neg(arr, 39)["Shot"]
        shot_42["mild"] = pos_neg(arr, 42)["Shot"]
        shot_45["mild"] = pos_neg(arr, 45)["Shot"]
        shot_48["mild"] = pos_neg(arr, 48)["Shot"]
        shot_51["mild"] = pos_neg(arr, 51)["Shot"]
        shot_54["mild"] = pos_neg(arr, 54)["Shot"]
        shot_57["mild"] = pos_neg(arr, 57)["Shot"]
        shot_60["mild"] = pos_neg(arr, 60)["Shot"]

        
        
        
    elif arr[-6] == "moderate":
        shot_3["moderate"] = pos_neg(arr, 3)["Shot"]
        shot_6["moderate"] = pos_neg(arr, 6)["Shot"]
        shot_9["moderate"] = pos_neg(arr, 9)["Shot"]
        shot_12["moderate"] = pos_neg(arr, 12)["Shot"]
        shot_15["moderate"] = pos_neg(arr, 15)["Shot"]
        shot_18["moderate"] = pos_neg(arr, 18)["Shot"]
        shot_21["moderate"] = pos_neg(arr, 21)["Shot"]
        shot_24["moderate"] = pos_neg(arr, 24)["Shot"]
        shot_27["moderate"] = pos_neg(arr, 27)["Shot"]
        shot_30["moderate"] = pos_neg(arr, 30)["Shot"]
        shot_33["moderate"] = pos_neg(arr, 33)["Shot"]
        shot_36["moderate"] = pos_neg(arr, 36)["Shot"]
        shot_39["moderate"] = pos_neg(arr, 39)["Shot"]
        shot_42["moderate"] = pos_neg(arr, 42)["Shot"]
        shot_45["moderate"] = pos_neg(arr, 45)["Shot"]
        shot_48["moderate"] = pos_neg(arr, 48)["Shot"]
        shot_51["moderate"] = pos_neg(arr, 51)["Shot"]
        shot_54["moderate"] = pos_neg(arr, 54)["Shot"]
        shot_57["moderate"] = pos_neg(arr, 57)["Shot"]
        shot_60["moderate"] = pos_neg(arr, 60)["Shot"]
        
    elif arr[-6] == "severe":
        shot_3["severe"] = pos_neg(arr, 3)["Shot"]
        shot_6["severe"] = pos_neg(arr, 6)["Shot"]
        shot_9["severe"] = pos_neg(arr, 9)["Shot"]
        shot_12["severe"] = pos_neg(arr, 12)["Shot"]
        shot_15["severe"] = pos_neg(arr, 15)["Shot"]
        shot_18["severe"] = pos_neg(arr, 18)["Shot"]
        shot_21["severe"] = pos_neg(arr, 21)["Shot"]
        shot_24["severe"] = pos_neg(arr, 24)["Shot"]
        shot_27["severe"] = pos_neg(arr, 27)["Shot"]
        shot_30["severe"] = pos_neg(arr, 30)["Shot"]
        shot_33["severe"] = pos_neg(arr, 33)["Shot"]
        shot_36["severe"] = pos_neg(arr, 36)["Shot"]
        shot_39["severe"] = pos_neg(arr, 39)["Shot"]
        shot_42["severe"] = pos_neg(arr, 42)["Shot"]
        shot_45["severe"] = pos_neg(arr, 45)["Shot"]
        shot_48["severe"] = pos_neg(arr, 48)["Shot"]
        shot_51["severe"] = pos_neg(arr, 51)["Shot"]
        shot_54["severe"] = pos_neg(arr, 54)["Shot"]
        shot_57["severe"] = pos_neg(arr, 57)["Shot"]
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
    
    # Define the labels we want to use
    severity = ['no', 'mild', 'moderate', 'severe']
    times = ['3', '21', '42', '60']
    
    return np.array([
        # Severity rows
        [no_dict['no'], no_dict['mild'], no_dict['moderate'], no_dict['severe'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        [mild_dict['no'], mild_dict['mild'], mild_dict['moderate'], mild_dict['severe'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        [mod_dict['no'], mod_dict['mild'], mod_dict['moderate'], mod_dict['severe'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        [sev_dict['no'], sev_dict['mild'], sev_dict['moderate'], sev_dict['severe'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        # Time rows
        [t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        [t21_dict['21'], t21_dict['21'], t21_dict['21'], t21_dict['21'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        [t42_dict['42'], t42_dict['42'], t42_dict['42'], t42_dict['42'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']],
        [t60_dict['60'], t60_dict['60'], t60_dict['60'], t60_dict['60'], t3_dict['3'], t21_dict['21'], t42_dict['42'], t60_dict['60']]
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

x_full = ['no', 'mild', 'moderate', 'severe', '3', '21', '42', '60']
y_full = ['no', 'mild', 'moderate', 'severe', '3', '21', '42', '60']

# Create partial matrix for arm implant (only 3,6,9 values)
x_partial = ['3', '21', '42', '60', 'no', 'mild', 'moderate', 'severe']
y_partial = ['3', '21', '42', '60', 'no', 'mild', 'moderate', 'severe']
z_arm_implant = np.array([
    [arm_implant_3['3'], arm_implant_3['21'], arm_implant_3['42'],  arm_implant_3['60'], arm_implant_3['no'], arm_implant_3['mild'], arm_implant_3['moderate'], arm_implant_3['severe']],
    [arm_implant_21['3'], arm_implant_21['21'], arm_implant_21['42'],  arm_implant_21['60'], arm_implant_21['no'], arm_implant_21['mild'], arm_implant_21['moderate'], arm_implant_21['severe']],
    [arm_implant_42['3'], arm_implant_42['21'], arm_implant_42['42'],  arm_implant_42['60'], arm_implant_42['no'], arm_implant_42['mild'], arm_implant_42['moderate'], arm_implant_42['severe']],
    [arm_implant_60['3'], arm_implant_60['21'], arm_implant_60['42'],  arm_implant_60['60'], arm_implant_60['no'], arm_implant_60['mild'], arm_implant_60['moderate'], arm_implant_60['severe']]
])

x_partial_mini = ['3', '21', '42', '60', 'no', 'mild', 'moderate', 'severe']
y_partial_mini = ['3', '21', '42', '60']
z_mini = np.array([
    [mini_pill_3['3'], mini_pill_3['21'], mini_pill_3['42'], mini_pill_3['60'], mini_pill_3['no'], mini_pill_3['mild'], mini_pill_3['moderate'], mini_pill_3['severe']],
    [mini_pill_21['3'], mini_pill_21['21'], mini_pill_21['42'], mini_pill_21['60'], mini_pill_21['no'], mini_pill_21['mild'], mini_pill_21['moderate'], mini_pill_21['severe']],
    [mini_pill_42['3'], mini_pill_42['21'], mini_pill_42['42'], mini_pill_42['60'], mini_pill_42['no'], mini_pill_42['mild'], mini_pill_42['moderate'], mini_pill_42['severe']],
    [mini_pill_60['3'], mini_pill_60['21'], mini_pill_60['42'], mini_pill_60['60'], mini_pill_60['no'], mini_pill_60['mild'], mini_pill_60['moderate'], mini_pill_60['severe']],
])

# Create hormonal IUD matrix (4x7 matrix)
z_hormonal_iud = np.array([
    [hormonal_iud_no['no'], hormonal_iud_no['mild'], hormonal_iud_no['moderate'], hormonal_iud_no['severe'], hormonal_iud_no['3'], hormonal_iud_no['21'],  hormonal_iud_no['42'],  hormonal_iud_no['60']],
    [hormonal_iud_mild['no'], hormonal_iud_mild['mild'], hormonal_iud_mild['moderate'], hormonal_iud_mild['severe'], hormonal_iud_mild['3'],  hormonal_iud_mild['21'],hormonal_iud_mild['42'],  hormonal_iud_mild['60']],
    [hormonal_iud_moderate['no'], hormonal_iud_moderate['mild'], hormonal_iud_moderate['moderate'], hormonal_iud_moderate['severe'], hormonal_iud_moderate['3'],  hormonal_iud_moderate['21'],  hormonal_iud_moderate['42'], hormonal_iud_moderate['60']],
    [hormonal_iud_severe['no'], hormonal_iud_severe['mild'], hormonal_iud_severe['moderate'], hormonal_iud_severe['severe'], hormonal_iud_severe['3'], hormonal_iud_severe['21'], hormonal_iud_severe['42'], hormonal_iud_severe['60']],
])

# Create ring matrix (4x3 matrix)
z_ring = np.array([
    [ring_3['no'], ring_3['mild'], ring_3['moderate'], ring_3['severe']],

    [ring_21['no'], ring_21['mild'], ring_21['moderate'], ring_21['severe']],

    [ring_42['no'], ring_42['mild'], ring_42['moderate'], ring_42['severe']],

    [ring_60['no'], ring_60['mild'], ring_60['moderate'], ring_60['severe']]
])

# Create shot matrix (4x3 matrix)
z_shot = np.array([
    [shot_3['no'], shot_3['mild'], shot_3['moderate'], shot_3['severe']],
    [shot_21['no'], shot_21['mild'], shot_21['moderate'], shot_21['severe']],
    [shot_42['no'], shot_42['mild'], shot_42['moderate'], shot_42['severe']],
    [shot_60['no'], shot_60['mild'], shot_60['moderate'], shot_60['severe']]
])

# Create patch matrix (4x4 matrix)
z_patch = np.array([
    [patch_no['no'], patch_no['mild'], patch_no['moderate'], patch_no['severe']],
    [patch_mild['no'], patch_mild['mild'], patch_mild['moderate'], patch_mild['severe']],
    [patch_moderate['no'], patch_moderate['mild'], patch_moderate['moderate'], patch_moderate['severe']],
    [patch_severe['no'], patch_severe['mild'], patch_severe['moderate'], patch_severe['severe']]
    
])

# Create combo pill matrix (4x4 matrix)
z_combo_pill = np.array([
    [combo_no['no'], combo_no['mild'], combo_no['moderate'], combo_no['severe']],
    [combo_mild['no'], combo_mild['mild'], combo_mild['moderate'], combo_mild['severe']],
    [combo_moderate['no'], combo_moderate['mild'], combo_moderate['moderate'], combo_moderate['severe']],
    [combo_severe['no'], combo_severe['mild'], combo_severe['moderate'], combo_severe['severe']]
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

# Create figure
fig = go.Figure()

# Add patch surface with its specific axes
x_patch_combo = ['no', 'mild', 'moderate', 'severe']
y_patch_combo = ['no', 'mild', 'moderate', 'severe']

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
x_ring_shot = ['no', 'mild', 'moderate', 'severe']
y_ring_shot = ['3', '20', '40', '60']

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
y_hormonal = ['no', 'mild', 'moderate', 'severe']
x_hormonal = ['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60']

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

# Add hormonal IUD surface


# Add all other surfaces with different colors and opacity
surfaces = [
    ('Condoms', z_condoms, x_full, y_full),
    ('Internal Condoms', z_internal_condoms, x_full, y_full),
    ('Cervical Cap', z_cervical_cap, x_full, y_full),
    ('FAM', z_fam, x_full, y_full),
    ('Copper IUD', z_copper_iud, x_full, y_full),
    ('Sterilization', z_sterilization, x_full, y_full),
    ('Spermicide', z_spermicide, x_full, y_full),
    ('Withdrawal', z_withdrawal, x_full, y_full),
    ('Arm Implant', z_arm_implant, x_partial, y_partial),
  
]

for i, (name, z, x, y) in enumerate(surfaces):
    fig.add_trace(go.Surface(
        x=x,
        y=y,
        z=z,
        name=name,
        colorscale=[[0, distinct_colors[i]], [1, distinct_colors[i]]],
        showscale=False,
        opacity=0.7,
        showlegend=True,
        legendgroup=name,
        hoverinfo='name+z'
    ))

'''
# Update layout with improved legend
fig.update_layout(
    title='Contraceptive Methods Scores - 3D Surface Plot',
    scene=dict(
        xaxis_title='TGD',
        yaxis_title='Acne',
        zaxis_title='Score',
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.2)
        )
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
'''

# Update the layout section of your code:
# Update the layout section of your code:
# Update the layout section with specific time points
fig.update_layout(
    title=dict(
        text='Contraceptive Methods Scores - 3D Surface Plot',
        x=0.5,
        xanchor='center',
        y=0.95
    ),
    scene=dict(
        xaxis=dict(
            title='TGD',
            ticktext=['no', 'mild', 'moderate', 'severe', '3', '21', '42', '60'],
            tickvals= [1, 2, 3, 5, 6, 7, 8, 9],  # 8 values total
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        yaxis=dict(
            title='Acne',
            ticktext=['no', 'mild', 'moderate', 'severe', '3', '21', '42', '60'],
            tickvals=[1, 2, 3, 5, 6, 7, 8, 9],  # 8 values total
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        zaxis=dict(
            title='Score',
            titlefont=dict(size=12),
            tickfont=dict(size=10)
        ),
        camera=dict(
            eye=dict(x=2, y=2, z=1.5)
        )
    ),
    width=1500,
    height=1200,
    autosize=False,
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='rgba(0, 0, 0, 0.5)',
        borderwidth=2,
        font=dict(size=14, color='black'),
        itemsizing='constant',
        itemwidth=30,
        orientation="v",
        title=dict(
            text="Contraceptive Methods",
            font=dict(size=16, color='black')
        )
    ),
    margin=dict(
        l=50, r=50, t=100, b=50,
        pad=4
    )
)

# Update hover template
for trace in fig.data:
    trace.update(
        hovertemplate=(
            "<b>%{fullData.name}</b><br>" +
            "TGD: %{x}<br>" +
            "Acne: %{y}<br>" +
            "Score: %{z}<br>" +
            "<extra></extra>"
        )
    )

fig.show()


# tickvals= [1, 2, 3, 7, 8, 10, 14, 20],

'''
fig.update_layout(
    title=dict(
        text='Contraceptive Methods Scores - 3D Surface Plot',
        x=0.5,
        xanchor='center',
        y=0.95
    ),
    scene=dict(
        xaxis=dict(
            title='TGD',
            ticktext=['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60'],
            tickvals=[1, 2, 3, 7, 8, 10, 14, 20],  # 8 values total
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        yaxis=dict(
            title='Acne',
            ticktext=['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60'],
            tickvals=[1, 2, 3, 7, 8, 10, 14, 20],  # 8 values total
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        zaxis=dict(
            title='Score',
            titlefont=dict(size=12),
            tickfont=dict(size=10)
        ),
        camera=dict(
            eye=dict(x=2, y=2, z=1.5)
        )
    ),
    width=1500,
    height=1200,
    autosize=False,
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='rgba(0, 0, 0, 0.5)',
        borderwidth=2,
        font=dict(size=14, color='black'),
        itemsizing='constant',
        itemwidth=30,
        orientation="v",
        title=dict(
            text="Contraceptive Methods",
            font=dict(size=16, color='black')
        )
    ),
    margin=dict(
        l=50, r=50, t=100, b=50,
        pad=4
    )
)

# Update hover template
for trace in fig.data:
    trace.update(
        hovertemplate=(
            "<b>%{fullData.name}</b><br>" +
            "TGD: %{x}<br>" +
            "Acne: %{y}<br>" +
            "Score: %{z}<br>" +
            "<extra></extra>"
        )
    )

#fig.show()

fig.update_layout(
    title=dict(
        text='Contraceptive Methods Scores - 3D Surface Plot',
        x=0.5,
        xanchor='center',
        y=0.95
    ),
    scene=dict(
        xaxis=dict(
            title='TGD',
            ticktext=['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60'],
            tickvals=list(range(len(['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60']))),
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        yaxis=dict(
            title='Acne',
            ticktext=['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60'],
            tickvals=list(range(len(['no', 'mild', 'moderate', 'severe', '3', '20', '40', '60']))),
            tickangle=45,
            tickmode='array',
            titlefont=dict(size=12),
            tickfont=dict(size=10),
            showticklabels=True
        ),
        zaxis=dict(
            title='Score',
            titlefont=dict(size=12),
            tickfont=dict(size=10)
        ),
        camera=dict(
            eye=dict(x=2, y=2, z=1.5)
        )
    ),
    width=1500,
    height=1200,
    autosize=False,
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='rgba(0, 0, 0, 0.5)',
        borderwidth=2,
        font=dict(size=14, color='black'),
        itemsizing='constant',
        itemwidth=30,
        orientation="v",
        title=dict(
            text="Contraceptive Methods",
            font=dict(size=16, color='black')
        )
    ),
    margin=dict(
        l=50, r=50, t=100, b=50,
        pad=4
    )
)
# Update hover template
for trace in fig.data:
    trace.update(
        hovertemplate=(
            "<b>%{fullData.name}</b><br>" +
            "TGD: %{x}<br>" +
            "Acne: %{y}<br>" +
            "Score: %{z}<br>" +
            "<extra></extra>"
        )
    )

fig.show()






'''