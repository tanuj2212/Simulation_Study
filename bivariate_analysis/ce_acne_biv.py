from functions_simulation_diff_weight_hor import *
import copy
from correct_original_weights_hor import *

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
    'severe': -50,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-50", "-25", "-15", "0"]
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
x_values = [-60, -40, -20, 0, 20, 40, 60]
x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]

# Define y values and labels for negative and positive ranges
severity_map = {
    'severe': -50,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity

negative_y_labels = ["-50", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values]

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

# Create coordinate matrices for negative methods
X_neg, Y_neg = np.meshgrid(x_values, negative_y_values)

# Create coordinate matrices for positive methods
X_pos, Y_pos = np.meshgrid(x_values, positive_y_values)

# Create coordinate matrices for zero methods (using negative y-values for consistency)
X_zero, Y_zero = np.meshgrid(x_values, negative_y_values)

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
for method_idx, method in enumerate(all_methods["zero"], 
                                  start=len(all_methods["negative_only"]) + len(all_methods["positive"])):
    Z = np.zeros((len(negative_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, _, zero_dict = preference_dicts[x_label]
        
        for severity, y_pos in severity_map.items():
            y_idx = negative_y_values.index(y_pos)
            if severity in zero_dict and method in zero_dict[severity]:
                Z[y_idx, x_idx] = zero_dict[severity][method]
    
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
        xaxis=dict(title='Preference Level', ticktext=x_labels, tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne Effect', ticktext=negative_y_labels + positive_y_labels[1:], 
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

fig.show()
'''

# Working code, but no checkboxes. Shows everything
import numpy as np
import plotly.graph_objects as go

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
x_values = [-60, -40, -20, 0, 20, 40, 60]
x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]

# Define y values and labels for negative and positive ranges
severity_map = {
    'severe': -50,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60

# Create separate y_values arrays for negative and positive methods
negative_y_values = list(severity_map.values())
positive_y_values = [0] + positive_values  # Include 0 for continuity
all_y_values = negative_y_values + positive_values[1:]  # Combined y-values for zero correlation methods

negative_y_labels = ["-50", "-25", "-15", "0"]
positive_y_labels = ["0"] + [str(i) for i in positive_values]
all_y_labels = negative_y_labels + [str(i) for i in positive_values[1:]]

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

# Methods classification
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

# Create coordinate matrices for zero correlation methods (spanning full range)
X_zero, Y_zero = np.meshgrid(x_values, all_y_values)

# Process negative-only methods
for method_idx, method in enumerate(negative_only_methods):
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
for method_idx, method in enumerate(positive_methods, start=len(negative_only_methods)):
    Z = np.zeros((len(positive_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        _, pos_dict, _ = preference_dicts[x_label]
        
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

# Process zero correlation methods
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
    title='3D Visualization of Contraceptive Scores',
    scene=dict(
        xaxis=dict(title='Preference Level', ticktext=x_labels, tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne Severity/Positive Weight', ticktext=all_y_labels, 
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

# Add buttons to show/hide individual surfaces
buttons = []
all_methods = negative_only_methods + positive_methods + zero_correlation_methods
for method_idx, method in enumerate(all_methods):
    visible = [False] * len(all_methods)
    visible[method_idx] = True
    buttons.append(dict(
        label=method,
        method='update',
        args=[{'visible': visible}]
    ))

# Add category buttons
buttons.append(dict(
    label="Show Negative Correlation Methods",
    method='update',
    args=[{'visible': [i < len(negative_only_methods) for i in range(len(all_methods))]}]
))

buttons.append(dict(
    label="Show Positive Correlation Methods",
    method='update',
    args=[{'visible': [(i >= len(negative_only_methods) and i < len(negative_only_methods) + len(positive_methods)) for i in range(len(all_methods))]}]
))

buttons.append(dict(
    label="Show Zero Correlation Methods",
    method='update',
    args=[{'visible': [i >= len(negative_only_methods) + len(positive_methods) for i in range(len(all_methods))]}]
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
# Save the figure as an HTML file
#fig.write_html("ce_acne_3d.html")

import numpy as np
import vtk

import vtk
import numpy as np

# Create renderer and window
renderer = vtk.vtkRenderer()
renderer.SetBackground(1.0, 1.0, 1.0)  # White background

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(1250, 800)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Create axes
axes = vtk.vtkAxesActor()
axes.SetTotalLength(140, 140, 140)
axes.SetXAxisLabelText("Preference Level")
axes.SetYAxisLabelText("Acne Severity/Positive Weight")
axes.SetZAxisLabelText("Score")

# Create distinct colors for methods
distinct_colors = [
    (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.84, 0.0),
    (1.0, 0.08, 0.58), (0.0, 1.0, 0.0), (0.55, 0.0, 0.55),
    (1.0, 0.55, 0.0), (0.0, 1.0, 1.0), (0.5, 0.0, 0.0),
    (0.0, 0.0, 0.5), (0.5, 0.5, 0.0), (1.0, 0.0, 1.0),
    (0.0, 0.5, 0.5), (1.0, 0.65, 0.0), (0.29, 0.0, 0.51)
]

def create_surface(x_values, y_values, z_values, color):
    # Create points
    points = vtk.vtkPoints()
    nx, ny = len(x_values), len(y_values)
    
    # Create cells
    polygons = vtk.vtkCellArray()
    
    # Create scalars for coloring
    scalars = vtk.vtkFloatArray()
    
    # Fill points and scalars
    for j in range(ny):
        for i in range(nx):
            points.InsertNextPoint(x_values[i], y_values[j], z_values[j][i])
            scalars.InsertNextValue(z_values[j][i])
    
    # Create polygons
    for j in range(ny-1):
        for i in range(nx-1):
            polygon = vtk.vtkPolygon()
            polygon.GetPointIds().SetNumberOfIds(4)
            
            polygon.GetPointIds().SetId(0, i + j*nx)
            polygon.GetPointIds().SetId(1, (i+1) + j*nx)
            polygon.GetPointIds().SetId(2, (i+1) + (j+1)*nx)
            polygon.GetPointIds().SetId(3, i + (j+1)*nx)
            
            polygons.InsertNextCell(polygon)
    
    # Create polydata
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetPolys(polygons)
    polydata.GetPointData().SetScalars(scalars)
    
    # Create mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color)
    actor.GetProperty().SetOpacity(0.7)
    
    return actor

# Process negative-only methods
for method_idx, method in enumerate(negative_only_methods):
    Z = np.zeros((len(negative_y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _, _ = preference_dicts[x_label]
        
        for severity, y_pos in severity_map.items():
            y_idx = negative_y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    
    actor = create_surface(x_values, negative_y_values, Z, distinct_colors[method_idx])
    renderer.AddActor(actor)

# Process positive methods
for method_idx, method in enumerate(positive_methods, start=len(negative_only_methods)):
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
    
    actor = create_surface(x_values, positive_y_values, Z, distinct_colors[method_idx])
    renderer.AddActor(actor)

# Process zero correlation methods
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
    
    actor = create_surface(x_values, all_y_values, Z, distinct_colors[method_idx])
    renderer.AddActor(actor)

# Add axes to renderer
renderer.AddActor(axes)

# Set up camera
camera = renderer.GetActiveCamera()
camera.SetPosition(200, 200, 200)
camera.SetFocalPoint(0, 0, 0)
camera.SetViewUp(0, 0, 1)

# Add text labels for methods
legend_actors = []
y_offset = 20
for idx, method in enumerate(negative_only_methods + positive_methods + zero_correlation_methods):
    text_actor = vtk.vtkTextActor()
    text_actor.SetInput(method)
    text_actor.GetTextProperty().SetColor(distinct_colors[idx])
    text_actor.SetPosition(10, 800 - y_offset)
    renderer.AddActor2D(text_actor)
    legend_actors.append(text_actor)
    y_offset += 20

# Initialize and start interaction
interactor.Initialize()
render_window.Render()
interactor.Start()
'''