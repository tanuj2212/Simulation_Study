from functions_simulation_diff_weight import *
import copy
from correct_original_weights import *

inputs = [
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes'],
     
    ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'mild', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'moderate', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes'],

     ['imp', 'neutral', 'sl_imp', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'no',
     'severe', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes'],
]


def calculate_scores_negative(input_arr):
    weights_negative = [-15, -25, -50]
    weights_dict = {
        'arm_implant': copy.deepcopy(original_weight_arm_implant),
        "hormonal_iud": copy.deepcopy(original_weight_hormonal_IUD),
        "patch": copy.deepcopy(original_weight_patch),
        "combo_pill": copy.deepcopy(original_weight_combo_pill),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
        "ring": copy.deepcopy(original_weight_ring),
        "shot": copy.deepcopy(original_weight_shot) 
        }
    '''
    for method in weights_dict:
            if method == 'arm_implant':
                weights_dict[method][-4] = weights_negative
            elif method == "hormonal_iud":
                weights_dict[method][-8] = weights_negative
            elif method == "patch":
                weights_dict[method][-15] = weights_negative
            elif method == "combo_pill":
                weights_dict[method][-15] = weights_negative
            elif method == "mini_pill":
                weights_dict[method][-7] = weights_negative
            elif method == "ring":
                weights_dict[method][-15] = weights_negative
            elif method == "shot":
                weights_dict[method][-15] = weights_negative
        '''
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    # Calculate scores using the updated weights
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    contraceptive_scores = {
        "Arm Implant": arm_implant_score,
        "Hormonal IUD": hormonal_iud_score,
        "Patch": patch_score,
        "Combination Pill": combo_pill_score,
        "Mini Pill": mini_pill_score,
        "Ring": ring_score,
        "Shot": shot_score,
    }
    return contraceptive_scores

 

def calculate_scores_zero(input_arr):

    original_weights = {
        "condoms": copy.deepcopy(original_weight_condoms),
        "internal_condoms": copy.deepcopy(original_weight_internal_condoms),
        "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
        "fam": copy.deepcopy(original_weight_FAM),
        "copper_iud": copy.deepcopy(original_weight_copper_IUD),
        "sterilization": copy.deepcopy(original_weight_sterilization),
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
    fam_score = change_fam(fam_arr, original_weights['fam'])
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
        "Sterilization": sterilization_score,
        "Spermicide Gel": gel_score,
        "Withdrawal": withdrawal_score
    }
    return contraceptive_scores


neg_scores = {

}
for arr in inputs:
    score_neg = calculate_scores_negative(arr)
    if arr[12] == "no":
        neg_scores["no"] = score_neg
    elif arr[12] == "mild":
        neg_scores["mild"] = score_neg
    elif arr[12] == "moderate":
        neg_scores["moderate"] = score_neg
    elif arr[12] == "severe":
        neg_scores["severe"] = score_neg

n_pos = 21

'''
pos_scores = {

}


for i in range(1, n_pos):
    positive_weight = 3 * i
    for arr in inputs:
        score_pos = calculate_scores_positive(arr, positive_weight)
        pos_scores[f"{positive_weight}"] = score_pos
zero_scores = {

}

'''
zero_scores = {

}
for i in range(1, 25):
    for arr in inputs:
        zero_scores[f"{i}"] = calculate_scores_zero(arr)




# Plotting the graph
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


print(neg_scores)

def plot_contraceptive_scores(neg_scores, zero_scores):
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
    
    '''
    for method in pos_scores['3'].keys():
        scores = [None] * 4  # Pad with None for negative range
        method_scores = [pos_scores[str(weight)][method] for weight in range(3, 63, 3)]
        scores.extend(method_scores)
        all_scores[method] = scores
'''
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
        max_methods_per_line = 4
        if len(methods) > max_methods_per_line:
    # Split the methods into chunks of 4 and join with a newline
            chunks = [methods[i:i + max_methods_per_line] for i in range(0, len(methods), max_methods_per_line)]
            combined_label = '\n'.join([' + '.join(chunk) for chunk in chunks])
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
    plt.title('Contraceptive Scores across weights for Anxiety or Depression')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
    plt.ylim(-550, 100)

    # Set x-ticks
    plt.xticks(weight_multipliers, weight_labels, rotation=45)

    # Add axes at y=0 and x=0
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Adjust layout
    plt.tight_layout()
    
    return plt

# Example usage:
plt = plot_contraceptive_scores(neg_scores, zero_scores)
filename = f'univariate_analysis/visualizations_univariate/medical_conditions/anxiety_dep_univ_viz.png'  # or .pdf, .jpg, etc.
plt.savefig(filename, dpi=300, bbox_inches='tight')
#plt.show()
