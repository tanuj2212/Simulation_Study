from functions_simulation_diff_weight_hor import *
import copy
from correct_original_weights_hor import *


inputs = [
    ['v_unp', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['v_unp', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_unp', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['unp', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['unp', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['unp', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['sl_unp', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['sl_unp', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['neutral', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['neutral', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['sl_imp', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['sl_imp', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['imp', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['imp', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],


     ['v_imp', 'v_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['v_imp', 'unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'sl_unp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

    ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'sl_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'v_imp', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
]


def score_ce_preg_biv(input_arr):
    ce_weights = [-60, -40, -20, 20, 40, 60]
    preg_weights = [-60, -40, -20, 20, 40, 60]

    weights_dict = {
        "condoms": copy.deepcopy(original_weight_condoms),
        "internal_condoms": copy.deepcopy(original_weight_internal_condoms),
        "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
        "fam": copy.deepcopy(original_weight_FAM),
        'arm_implant': copy.deepcopy(original_weight_arm_implant),
        'copper_iud': copy.deepcopy(original_weight_copper_IUD),
        'hormonal_iud': copy.deepcopy(original_weight_hormonal_IUD),
        "patch": copy.deepcopy(original_weight_patch),
        "combo_pill": copy.deepcopy(original_weight_combo_pill),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
        "ring": copy.deepcopy(original_weight_ring),
        'shot': copy.deepcopy(original_weight_shot),
        'sterilization': copy.deepcopy(original_weight_sterilization),
        "spermicide": copy.deepcopy(original_weight_spermicide),
        "withdrawal": copy.deepcopy(original_weight_withdrawl) 
    }

   
    for method in weights_dict:
        if method == "condoms":
            weights_dict[method][0] = ce_weights
            weights_dict[method][1] = [i * 0.5 for i in preg_weights]
        elif method == "internal_condoms":
            weights_dict[method][0] = ce_weights
            weights_dict[method][1] = [i * 0.5 for i in preg_weights]
        elif method == "cervical_cap":
            weights_dict[method][0] = ce_weights
        elif method == "fam":
            weights_dict[method][0] = ce_weights
        elif method == "arm_implant":
            weights_dict[method][0] = preg_weights
        elif method == "copper_iud":
            weights_dict[method][0] = preg_weights
        elif method == "hormonal_iud":
            weights_dict[method][0] = preg_weights
        elif method == "patch":
            weights_dict[method][0] = ce_weights
            weights_dict[method][1] = [i * 0.5 for i in preg_weights]
        elif method == "combo_pill":
            weights_dict[method][0] = ce_weights
            weights_dict[method][1] = [i * 0.5 for i in preg_weights]
        elif method == "mini_pill":
            weights_dict[method][0] = ce_weights
            weights_dict[method][1] = [i * 0.5 for i in preg_weights]
        elif method == "ring":
            weights_dict[method][0] = ce_weights
            weights_dict[method][1] = [i * 0.5 for i in preg_weights]
        elif method == "shot":
            weights_dict[method][0] =  [i * 0.5 for i in preg_weights]
        elif method == "sterilization":
            weights_dict[method][0] = preg_weights
        elif method == "spermicide":
            weights_dict[method][0] = ce_weights
        elif method == "withdrawal":
            weights_dict[method][0] = ce_weights

    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
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
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    copper_iud_score = change_copper_iud(copper_iud_arr, weights_dict['copper_iud'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    sterilization_score = change_score_sterilization(sterilization_arr, weights_dict['sterilization'])
    gel_score = change_score_gel(gel_arr, weights_dict['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, weights_dict['withdrawal'])
    
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

    return contraceptive_scores

v_unp_dict = {}

for arr in inputs[0:7]:
    if arr[1] == "v_unp":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        v_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other v_unp")

unp_dict = {}

for arr in inputs[7:14]:
    if arr[1] == "v_unp":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        unp_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other unp")

sl_unp_dict = {}
for arr in inputs[14:21]:
    if arr[1] == "v_unp":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        sl_unp_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other sl_unp")

neutral_dict = {}
for arr in inputs[21:28]:
    if arr[1] == "v_unp":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        neutral_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other neutral")
sl_imp_dict = {}
for arr in inputs[28:35]:
    if arr[1] == "v_unp":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        sl_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other sl_imp")
imp_dict = {}
for arr in inputs[35:42]:
    if arr[1] == "v_unp":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        imp_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other imp")
v_imp_dict = {}
for arr in inputs[42:]:
    if arr[1] == "v_unp":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "unp":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_unp":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "neutral":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "sl_imp":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "imp":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    elif arr[1] == "v_imp":
        v_imp_dict[arr[1]] = score_ce_preg_biv(arr)
    else:
        print("Other v_imp")


print(v_unp_dict)


import plotly.graph_objects as go
import numpy as np

# Create the x and y coordinate ranges
x_range = np.array([-60, -40, -20, 0, 20, 40, 60])
y_range = np.array([-60, -40, -20, 0, 20, 40, 60])

# Create meshgrid for 3D surface
X, Y = np.meshgrid(x_range, y_range)

# Define methods and their colors
methods = {
    "Condom": "#FF0000",
    "Internal Condom": "#0000FF",
    "Cervical Cap": "#FFD700",
    "FAM": "#FF1493",
    "Arm Implant": "#00FF00",
    "Copper IUD": "#8B008B",
    "Hormonal IUD": "#FF8C00",
    "Patch": "#00FFFF",
    "Combination Pill": "#800000",
    "Mini Pill": "#000080",
    "Ring": "#808000",
    "Shot": "#FF00FF",
    "Sterilization": "#008080",
    "Spermicide Gel": "#FFA500",
    "Withdrawal": "#4B0082"
}
# Create the 3D visualization
import plotly.graph_objects as go
import numpy as np
import plotly.graph_objects as go
import numpy as np

# Create mapping dictionaries for preference levels to numerical values
pref_to_num = {
    'v_unp': -60,
    'unp': -40,
    'sl_unp': -20,
    'neutral': 0,
    'sl_imp': 20,
    'imp': 40,
    'v_imp': 60
}

num_to_pref = {v: k for k, v in pref_to_num.items()}

# Create the x and y coordinate ranges
x_range = np.array([-60, -40, -20, 0, 20, 40, 60])
y_range = np.array([-60, -40, -20, 0, 20, 40, 60])

# Create meshgrid for 3D surface
X, Y = np.meshgrid(x_range, y_range)

# Define methods and their colors (same as before)
methods = {
    "Condom": "#FF0000",
    "Internal Condom": "#0000FF",
    "Cervical Cap": "#FFD700",
    "FAM": "#FF1493",
    "Arm Implant": "#00FF00",
    "Copper IUD": "#8B008B",
    "Hormonal IUD": "#FF8C00",
    "Patch": "#00FFFF",
    "Combination Pill": "#800000",
    "Mini Pill": "#000080",
    "Ring": "#808000",
    "Shot": "#FF00FF",
    "Sterilization": "#008080",
    "Spermicide Gel": "#FFA500",
    "Withdrawal": "#4B0082"
}

# Create the 3D visualization
fig = go.Figure()

# Add a surface for each contraceptive method
for method, color in methods.items():
    # Initialize the Z matrix for this method
    Z = np.zeros((len(y_range), len(x_range)))
    
    # Populate the Z matrix using the original input arrays
    for input_arr in inputs:
        # Get x and y coordinates from the first two elements of input array
        x_coord = pref_to_num[input_arr[0]]  # First preference
        y_coord = pref_to_num[input_arr[1]]  # Second preference
        
        # Find the corresponding indices in our grid
        x_idx = np.where(x_range == x_coord)[0][0]
        y_idx = np.where(y_range == y_coord)[0][0]
        
        # Calculate score using the original input array
        scores = score_ce_preg_biv(input_arr)
        Z[y_idx, x_idx] = scores[method]
    
    # Add surface plot for this method
    fig.add_trace(go.Surface(
        x=X,
        y=Y,
        z=Z,
        name=method,
        showscale=False,
        colorscale=[[0, color], [1, color]],
        opacity=0.7,
        showlegend=True
    ))

# Update layout (same as before)
fig.update_layout(
    title='3D Visualization of Contraceptive Scores',
    scene=dict(
        xaxis=dict(
            title='First Preference Level',
            #ticktext=['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp'],
            ticktext=['-60', '-40', '-20', '0', '20', '40', '60'],
            tickvals=[-60, -40, -20, 0, 20, 40, 60],
            range=[-70, 70]
        ),
        yaxis=dict(
            title='Second Preference Level',
            #ticktext=['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp'],
            ticktext=['-60', '-40', '-20', '0', '20', '40', '60'],
            tickvals=[-60, -40, -20, 0, 20, 40, 60],
            range=[-70, 70]
        ),
        zaxis=dict(
            title='Final Score'
        )
    ),
    showlegend=True,
    legend=dict(
        x=1.1,
        y=0.5,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='rgba(0, 0, 0, 0.2)',
        borderwidth=1
    ),
    width=1200,
    height=800
)

# Add dropdown menu (same as before)
buttons = []
for method in methods:
    visible = [True if m == method else False for m in methods]
    buttons.append(dict(
        label=method,
        method='update',
        args=[{'visible': visible}]
    ))

buttons.append(dict(
    label="Show All",
    method='update',
    args=[{'visible': [True] * len(methods)}]
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

# Show the figure
fig.show()
#fig.write_html("bivariate_analysis/ce_preg_3d.html")