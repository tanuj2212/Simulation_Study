from functions_simulation_diff_weight_hor import *
import copy
from correct_original_weights_hor import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

inputs = [
    ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'mild', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'severe', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'moderate', 'mild', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'moderate', 'moderate', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'mild', 'moderate', 'severe', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'mild', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'moderate', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'severe', 'yes'],



     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'moderate', 'mild', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'moderate', 'moderate', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'severe', 'moderate', 'severe', 'yes'],


     
]

def zero_pos(input_arr, pos):

    weights_dict = {

        "condoms": copy.deepcopy(original_weight_condoms),
        "internal_condoms": copy.deepcopy(original_weight_internal_condoms),
    }

    for method in weights_dict:
        if method == "condoms":
            weights_dict[method][-1] = pos * 0.5
        elif method == "internal_condoms":
            weights_dict[method][-1] = pos * 0.5
    
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[7], input_arr[8], input_arr[25], input_arr[26]]

    condom_score = change_score_condoms(condom_arr, weights_dict['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, weights_dict['internal_condoms'])

    return {
        "Condoms": condom_score,
        "Internal Condoms": internal_condom_score
    }

def zero_neg(input_arr):

    weights_dict = {
        "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
        "fam": copy.deepcopy(original_weight_FAM),
        "withdrawal": copy.deepcopy(original_weight_withdrawl)
    }

    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[26]]

    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_dict['cervical_cap'])
    fam_score = change_fam(fam_arr, weights_dict['fam'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, weights_dict['withdrawal'])

    return {
        "Cervical Cap": cervical_cap_score,
        "FAM": fam_score,
        "Withdrawal": withdrawal_score
    }



def pos_pos(input_arr, pos_gdper, pos_gdp):
    weights_dict = {
        "arm_implant": copy.deepcopy(original_weight_arm_implant),
        "hormonal_iud": copy.deepcopy(original_weight_hormonal_IUD),
        "patch": copy.deepcopy(original_weight_patch),
        "combo_pill": copy.deepcopy(original_weight_combo_pill),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
        "ring": copy.deepcopy(original_weight_ring),
        "shot": copy.deepcopy(original_weight_shot),
        "sterilization": copy.deepcopy(original_weight_sterilization)
    }

    for method in weights_dict:
        if method == "arm_implant":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp
        elif method == "hormonal_iud":
            weights_dict[method][-3] = pos_gdper 
            weights_dict[method][-1] = pos_gdp
        elif method == "patch":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp * 0.5
        elif method == "combo_pill":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp * 0.5
        elif method == "mini_pill":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp * 0.5
        elif method == "ring":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp * 0.5
        elif method == "shot":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp * 0.5
        elif method == "sterilization":
            weights_dict[method][-2] = pos_gdper 
            weights_dict[method][-1] = pos_gdp 
        
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[7], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]

    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    sterilization_score = change_score_sterilization(sterilization_arr, weights_dict['sterilization'])

    return {
        "Arm Implant": arm_implant_score,
        "Hormonal IUD": hormonal_iud_score,
        "Patch": patch_score,
        "Combination Pill": combo_pill_score,
        "Mini Pill": mini_pill_score,
        "Ring": ring_score,
        "Shot": shot_score,
        "Sterilization": sterilization_score
    }

def neg_pos(input_arr, pos):
    weights_dict = {
        "copper_iud": copy.deepcopy(original_weight_copper_IUD),
    }
    for method in weights_dict:
        if method == "copper_iud":
            weights_dict[method][-1] = pos
    
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    copper_iud_score = change_copper_iud(copper_iud_arr, weights_dict['copper_iud'])

    return {
        "Copper IUD": copper_iud_score
    }

def zero_zero(input_arr):
    weights_dict = {
        "spermicide": copy.deepcopy(original_weight_spermicide)
    }

    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[7], input_arr[8]]
    gel_score = change_score_gel(gel_arr, weights_dict['spermicide'])

    return {
        "Spermicide": gel_score
    }

gel_scores_no = {

}

for arr in inputs[0:4]:
    if arr[-2] == "no":
        gel_scores_no["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "mild":
        gel_scores_no["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "moderate":
        gel_scores_no["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "severe":
        gel_scores_no["severe"] = zero_zero(arr)["Spermicide"]

gel_scores_mild = {}

for arr in inputs[4:8]:
    score = zero_zero(arr)
    if arr[-2] == "no":
        gel_scores_mild["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "mild":
        gel_scores_mild["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "moderate":
        gel_scores_mild["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "severe":
        gel_scores_mild["severe"] = zero_zero(arr)["Spermicide"]

gel_scores_moderate = {}

for arr in inputs[8:12]:
    score = zero_zero(arr)
    if arr[-2] == "no":
        gel_scores_moderate["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "mild":
        gel_scores_moderate["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "moderate":
        gel_scores_moderate["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "severe":
        gel_scores_moderate["severe"] = zero_zero(arr)["Spermicide"]
gel_scores_severe = {}
for arr in inputs[12:16]:
    score = zero_zero(arr)
    if arr[-2] == "no":
        gel_scores_severe["no"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "mild":
        gel_scores_severe["mild"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "moderate":
        gel_scores_severe["moderate"] = zero_zero(arr)["Spermicide"]
    elif arr[-2] == "severe":
        gel_scores_severe["severe"] = zero_zero(arr)["Spermicide"]
    
condom_no = {}
int_condom_no = {}
condom_no["severe"] = []
int_condom_no["severe"] = []
condom_no["moderate"] = []
int_condom_no["moderate"] = []
condom_no["mild"] = []
int_condom_no["mild"] = []
condom_no["no"] = []
int_condom_no["no"] = []
for arr in inputs[0:4]:
    if arr[-2] == "no":
        condom_no["no"] = []
        int_condom_no["no"] = []
        for i in range(1, 21):
            condom_no["no"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_no["no"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "mild":
        condom_no["mild"] = []
        int_condom_no["mild"] = []
        for i in range(1, 21):
            condom_no["mild"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_no["mild"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "moderate":
        condom_no["moderate"] = []
        int_condom_no["moderate"] = []
        for i in range(1, 21):
            condom_no["moderate"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_no["moderate"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "severe":
        condom_no["severe"] = []
        int_condom_no["severe"] = []
        for i in range(1, 21):
            condom_no["severe"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_no["severe"].append(zero_pos(arr, i*3)["Internal Condoms"])

condom_mild = {}
int_condom_mild = {}
condom_mild["no"] = []
int_condom_mild["no"] = []
condom_mild["mild"] = []
int_condom_mild["mild"] = []
condom_mild["moderate"] = []
int_condom_mild["moderate"] = []
condom_mild["severe"] = []
int_condom_mild["severe"] = []
for arr in inputs[4:8]:
    if arr[-2] == "no":
        for i in range(1, 21):
            condom_mild["no"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_mild["no"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            condom_mild["mild"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_mild["mild"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            condom_mild["moderate"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_mild["moderate"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            condom_mild["severe"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_mild["severe"].append(zero_pos(arr, i*3)["Internal Condoms"])

condom_moderate = {}
int_condom_moderate = {}
condom_moderate["no"] = []
int_condom_moderate["no"] = []
condom_moderate["mild"] = []
int_condom_moderate["mild"] = []
condom_moderate["moderate"] = []
int_condom_moderate["moderate"] = []
condom_moderate["severe"] = []
int_condom_moderate["severe"] = []
for arr in inputs[8:12]:
    if arr[-2] == "no":
        for i in range(1, 21):
            condom_moderate["no"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_moderate["no"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            condom_moderate["mild"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_moderate["mild"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            condom_moderate["moderate"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_moderate["moderate"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            condom_moderate["severe"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_moderate["severe"].append(zero_pos(arr, i*3)["Internal Condoms"])
condom_severe = {}
int_condom_severe = {}
condom_severe["no"] = []
int_condom_severe["no"] = []
condom_severe["mild"] = []
int_condom_severe["mild"] = []
condom_severe["moderate"] = []
int_condom_severe["moderate"] = []
condom_severe["severe"] = []
int_condom_severe["severe"] = []
condom_severe["no"] = []
int_condom_severe["no"] = []
condom_severe["mild"] = []
int_condom_severe["mild"] = []
condom_severe["moderate"] = []
int_condom_severe["moderate"] = []
condom_severe["severe"] = []
int_condom_severe["severe"] = []

for arr in inputs[12:16]:
    if arr[-2] == "no":
        for i in range(1, 21):
            condom_severe["no"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_severe["no"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            condom_severe["mild"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_severe["mild"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            condom_severe["moderate"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_severe["moderate"].append(zero_pos(arr, i*3)["Internal Condoms"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            condom_severe["severe"].append(zero_pos(arr, i*3)["Condoms"])
            int_condom_severe["severe"].append(zero_pos(arr, i*3)["Internal Condoms"])

cervical_cap_no = {}
fam_no = {}
withdrawal_no = {}

for arr in inputs[0:4]:
    if arr[-2] == "no":
            cervical_cap_no["no"] = zero_neg(arr)["Cervical Cap"]
            fam_no["no"] = zero_neg(arr)["FAM"]
            withdrawal_no["no"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "mild":
            cervical_cap_no["mild"] = zero_neg(arr)["Cervical Cap"]
            fam_no["mild"] = zero_neg(arr)["FAM"]
            withdrawal_no["mild"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "moderate":
            cervical_cap_no["moderate"] = zero_neg(arr)["Cervical Cap"]
            fam_no["moderate"] = zero_neg(arr)["FAM"]
            withdrawal_no["moderate"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "severe":
            cervical_cap_no["severe"] = zero_neg(arr)["Cervical Cap"]
            fam_no["severe"] = zero_neg(arr)["FAM"]
            withdrawal_no["severe"] = zero_neg(arr)["Withdrawal"]

cervical_cap_mild = {}
fam_mild = {}
withdrawal_mild = {}
for arr in inputs[4:8]:
    if arr[-2] == "no":
            cervical_cap_mild["no"] = zero_neg(arr)["Cervical Cap"]
            fam_mild["no"] = zero_neg(arr)["FAM"]
            withdrawal_mild["no"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "mild":
            cervical_cap_mild["mild"] = zero_neg(arr)["Cervical Cap"]
            fam_mild["mild"] = zero_neg(arr)["FAM"]
            withdrawal_mild["mild"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "moderate":
            cervical_cap_mild["moderate"] = zero_neg(arr)["Cervical Cap"]
            fam_mild["moderate"] = zero_neg(arr)["FAM"]
            withdrawal_mild["moderate"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "severe":
            cervical_cap_mild["severe"] = zero_neg(arr)["Cervical Cap"]
            fam_mild["severe"] = zero_neg(arr)["FAM"]
            withdrawal_mild["severe"] = zero_neg(arr)["Withdrawal"]

cervical_cap_moderate = {}
fam_moderate = {}
withdrawal_moderate = {}
for arr in inputs[8:12]:
    if arr[-2] == "no":
            cervical_cap_moderate["no"] = zero_neg(arr)["Cervical Cap"]
            fam_moderate["no"] = zero_neg(arr)["FAM"]
            withdrawal_moderate["no"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "mild":
            cervical_cap_moderate["mild"] = zero_neg(arr)["Cervical Cap"]
            fam_moderate["mild"] = zero_neg(arr)["FAM"]
            withdrawal_moderate["mild"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "moderate":
            cervical_cap_moderate["moderate"] = zero_neg(arr)["Cervical Cap"]
            fam_moderate["moderate"] = zero_neg(arr)["FAM"]
            withdrawal_moderate["moderate"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "severe":
            cervical_cap_moderate["severe"] = zero_neg(arr)["Cervical Cap"]
            fam_moderate["severe"] = zero_neg(arr)["FAM"]
            withdrawal_moderate["severe"] = zero_neg(arr)["Withdrawal"]

cervical_cap_severe = {}
fam_severe = {}
withdrawal_severe = {}
for arr in inputs[12:16]:
    if arr[-2] == "no":
            cervical_cap_severe["no"] = zero_neg(arr)["Cervical Cap"]
            fam_severe["no"] = zero_neg(arr)["FAM"]
            withdrawal_severe["no"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "mild":
            cervical_cap_severe["mild"] = zero_neg(arr)["Cervical Cap"]
            fam_severe["mild"] = zero_neg(arr)["FAM"]
            withdrawal_severe["mild"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "moderate":
            cervical_cap_severe["moderate"] = zero_neg(arr)["Cervical Cap"]
            fam_severe["moderate"] = zero_neg(arr)["FAM"]
            withdrawal_severe["moderate"] = zero_neg(arr)["Withdrawal"]
    elif arr[-2] == "severe":
            cervical_cap_severe["severe"] = zero_neg(arr)["Cervical Cap"]
            fam_severe["severe"] = zero_neg(arr)["FAM"]
            withdrawal_severe["severe"] = zero_neg(arr)["Withdrawal"]

copper_iud_no = {}
copper_iud_mild = {}
copper_iud_moderate = {}
copper_iud_severe = {}

copper_iud_no["no"] = []
copper_iud_no["mild"] = []
copper_iud_no["moderate"] = []
copper_iud_no["severe"] = []

copper_iud_mild["no"] = []
copper_iud_mild["mild"] = []
copper_iud_mild["moderate"] = []
copper_iud_mild["severe"] = []

copper_iud_moderate["no"] = []
copper_iud_moderate["mild"] = []
copper_iud_moderate["moderate"] = []
copper_iud_moderate["severe"] = []

copper_iud_severe["no"] = []
copper_iud_severe["mild"] = []
copper_iud_severe["moderate"] = []
copper_iud_severe["severe"] = []
for arr in inputs[0:4]:

    if arr[-2] == "no":
        for i in range(1, 21):
            copper_iud_no["no"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            copper_iud_no["mild"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            copper_iud_no["moderate"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            copper_iud_no["severe"].append(neg_pos(arr, i*3)["Copper IUD"])
for arr in inputs[4:8]:
    if arr[-2] == "no":
        for i in range(1, 21):
            copper_iud_mild["no"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            copper_iud_mild["mild"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            copper_iud_mild["moderate"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            copper_iud_mild["severe"].append(neg_pos(arr, i*3)["Copper IUD"])
for arr in inputs[8:12]:
    if arr[-2] == "no":
        for i in range(1, 21):
            copper_iud_moderate["no"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            copper_iud_moderate["mild"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            copper_iud_moderate["moderate"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            copper_iud_moderate["severe"].append(neg_pos(arr, i*3)["Copper IUD"])
for arr in inputs[12:16]:
    if arr[-2] == "no":
        for i in range(1, 21):
            copper_iud_severe["no"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            copper_iud_severe["mild"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            copper_iud_severe["moderate"].append(neg_pos(arr, i*3)["Copper IUD"])
    elif arr[-2] == "severe":
        for i in range(1, 21):
            copper_iud_severe["severe"].append(neg_pos(arr, i*3)["Copper IUD"])



arm_no = {}
hormonal_iud_no = {}
patch_no = {}
combo_pill_no = {}
mini_pill_no = {}
ring_no = {}
shot_no = {}
sterilization_no = {}

arm_mild = {}
hormonal_iud_mild = {}
patch_mild = {}
combo_pill_mild = {}
mini_pill_mild = {}
ring_mild = {}
shot_mild = {}
sterilization_mild = {}

arm_moderate = {}
hormonal_iud_moderate = {}
patch_moderate = {}
combo_pill_moderate = {}
mini_pill_moderate = {}
ring_moderate = {}
shot_moderate = {}
sterilization_moderate = {}

arm_severe = {}
hormonal_iud_severe = {}
patch_severe = {}
combo_pill_severe = {}
mini_pill_severe = {}
ring_severe = {}
shot_severe = {}
sterilization_severe = {}

arm_no["no"] = []
hormonal_iud_no["no"] = []
patch_no["no"] = []
combo_pill_no["no"] = []
mini_pill_no["no"] = []
ring_no["no"] = []
shot_no["no"] = []
sterilization_no["no"] = []

arm_no["mild"] = []
hormonal_iud_no["mild"] = []
patch_no["mild"] = []
combo_pill_no["mild"] = []
mini_pill_no["mild"] = []
ring_no["mild"] = []
shot_no["mild"] = []
sterilization_no["mild"] = []

arm_no["moderate"] = []
hormonal_iud_no["moderate"] = []
patch_no["moderate"] = []
combo_pill_no["moderate"] = []
mini_pill_no["moderate"] = []
ring_no["moderate"] = []
shot_no["moderate"] = []
sterilization_no["moderate"] = []

arm_no["severe"] = []
hormonal_iud_no["severe"] = []
patch_no["severe"] = []
combo_pill_no["severe"] = []
mini_pill_no["severe"] = []
ring_no["severe"] = []
shot_no["severe"] = []
sterilization_no["severe"] = []


for arr in inputs[0:4]:
    if arr[-2] == "no":
        for i in range(1, 21):
            arm_no["no"].append(pos_pos(arr, 0, i*3)["Arm Implant"])
            hormonal_iud_no["no"].append(pos_pos(arr, 0, i*3)["Hormonal IUD"])
            patch_no["no"].append(pos_pos(arr, 0, i*3)["Patch"])
            combo_pill_no["no"].append(pos_pos(arr, 0, i*3)["Combination Pill"])
            mini_pill_no["no"].append(pos_pos(arr, 0, i*3)["Mini Pill"])
            ring_no["no"].append(pos_pos(arr, 0, i*3)["Ring"])
            shot_no["no"].append(pos_pos(arr, 0, i*3)["Shot"])
            sterilization_no["no"].append(pos_pos(arr, 0, i*3)["Sterilization"])
    elif arr[-2] == "mild":
        for i in range(1, 21):
            arm_no["mild"].append(pos_pos(arr, 0, i*3)["Arm Implant"])
            hormonal_iud_no["mild"].append(pos_pos(arr, 0, i*3)["Hormonal IUD"])
            patch_no["mild"].append(pos_pos(arr, 0, i*3)["Patch"])
            combo_pill_no["mild"].append(pos_pos(arr, 0, i*3)["Combination Pill"])
            mini_pill_no["mild"].append(pos_pos(arr, 0, i*3)["Mini Pill"])
            ring_no["mild"].append(pos_pos(arr, 0, i*3)["Ring"])
            shot_no["mild"].append(pos_pos(arr, 0, i*3)["Shot"])
            sterilization_no["mild"].append(pos_pos(arr, 0, i*3)["Sterilization"])
    elif arr[-2] == "moderate":
        for i in range(1, 21):
            arm_no["moderate"].append(pos_pos(arr, 0, i*3)["Arm Implant"])
            hormonal_iud_no["moderate"].append(pos_pos(arr, 0, i*3)["Hormonal IUD"])
            patch_no["moderate"].append(pos_pos(arr, 0, i*3)["Patch"])
            combo_pill_no["moderate"].append(pos_pos(arr, 0, i*3)["Combination Pill"])
            mini_pill_no["moderate"].append(pos_pos(arr, 0, i*3)["Mini Pill"])
            ring_no["moderate"].append(pos_pos(arr, 0, i*3)["Ring"])
            shot_no["moderate"].append(pos_pos(arr, 0, i*3)["Shot"])
            sterilization_no["moderate"].append(pos_pos(arr, 0, i*3)["Sterilization"])
    elif arr[-2] == "severe":

        for i in range(1, 21):
            arm_no["severe"].append(pos_pos(arr, 0, i*3)["Arm Implant"])
            hormonal_iud_no["severe"].append(pos_pos(arr, 0, i*3)["Hormonal IUD"])
            patch_no["severe"].append(pos_pos(arr, 0, i*3)["Patch"])
            combo_pill_no["severe"].append(pos_pos(arr, 0, i*3)["Combination Pill"])
            mini_pill_no["severe"].append(pos_pos(arr, 0, i*3)["Mini Pill"])
            ring_no["severe"].append(pos_pos(arr, 0, i*3)["Ring"])
            shot_no["severe"].append(pos_pos(arr, 0, i*3)["Shot"])
            sterilization_no["severe"].append(pos_pos(arr, 0, i*3)["Sterilization"])
