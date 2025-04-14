from functions_simulation_diff_weight_hor import *
import copy
from correct_original_weights_hor import *

inputs = [
    ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'moderate', 'moderate', 'no', 'yes'],
]



def calculate_scores_negative(input_arr):
    #weights_negative = -100
    weights_dict = {
        'patch': copy.deepcopy(original_weight_patch),
        "combo_pill": copy.deepcopy(original_weight_combo_pill),
        "ring": copy.deepcopy(original_weight_ring),
        "shot": copy.deepcopy(original_weight_shot),
        }
    '''
    for method in weights_dict:
            if method == 'patch':
                weights_dict[method][-1] = weights_negative
            elif method == "combo_pill":
                weights_dict[method][-1] = weights_negative
            elif method == "ring":
                weights_dict[method][-1] = weights_negative
            elif method == "shot":
                weights_dict[method][-1] = weights_negative
            '''
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    # Calculate scores using the updated weights
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    contraceptive_scores = {
        "Patch": patch_score,
        "Combo Pill": combo_pill_score,
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
        "arm_implant": copy.deepcopy(original_weight_arm_implant),
        "copper_iud": copy.deepcopy(original_weight_copper_IUD),
        "hormonal_iud": copy.deepcopy(original_weight_hormonal_IUD),
        "mini_pill": copy.deepcopy(original_weight_mini_pill),
        "sterilization": copy.deepcopy(original_weight_sterilization),
        "spermicide": copy.deepcopy(original_weight_spermicide),
        "withdrawal": copy.deepcopy(original_weight_withdrawl)
        }
    
    #condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    #internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    #cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    #fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    #copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
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
    condom_score = change_score_condoms(condom_arr, original_weights['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, original_weights['internal_condoms'])
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, original_weights['cervical_cap'])
    fam_score = change_fam(fam_arr, original_weights['fam'])
    arm_implant_score = change_arm_implant(arm_implant_arr, original_weights['arm_implant'])
    copper_iud_score = change_copper_iud(copper_iud_arr, original_weights['copper_iud'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, original_weights['hormonal_iud'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, original_weights['mini_pill'])
    sterilization_score = change_score_sterilization(sterilization_arr, original_weights['sterilization'])
    gel_score = change_score_gel(gel_arr, original_weights['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, original_weights['withdrawal'])
    contraceptive_scores = {
        "Condom": condom_score,
        "Internal Condom": internal_condom_score,
        "Cervical Cap": cervical_cap_score,
        "FAM": fam_score,
        "Arm Implant": arm_implant_score,
        "Copper IUD": copper_iud_score,
        "Hormonal IUD": hormonal_iud_score,
        "Mini Pill": mini_pill_score,
        "Sterilization": sterilization_score,
        "Gel": gel_score,
        "Withdrawal": withdrawal_score
    }
    return contraceptive_scores


neg_scores = {

}
for arr in inputs:
    score_neg = calculate_scores_negative(arr)
    if arr[-1] == "yes":
        neg_scores["yes"] = score_neg

n_pos = 21


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

def plot_contraceptive_scores(neg_scores, zero_scores):
    plt.figure(figsize=(15, 10))
    
    # Define two separate sets of weight labels and multipliers
    # First set for negative to zero range
    #neg_weight_labels = ['-100', '0']
    #neg_weight_multipliers = [-100, 0]
    
    # Second set for positive range
    pos_weight_labels = [str(i*3) for i in range(1, 21)]  # Start from 0 to maintain continuity
    pos_weight_multipliers = list(range(1, 21))
    
    # Combine both sets
    weight_labels = pos_weight_labels
    
    # Create a non-linear mapping for x-axis values
    #x_values = neg_weight_multipliers[:-1] + pos_weight_multipliers
    x_values = pos_weight_multipliers
    
    # Prepare data and identify overlapping scores
    all_scores = {}
    score_to_methods = {}
    
    # Process hormone-based methods with negative weights
    for method in neg_scores['yes'].keys():
        score = neg_scores['yes'][method]
        score_key = f"{score}"
        if score_key in score_to_methods:
            score_to_methods[score_key].append(method)
        else:
            score_to_methods[score_key] = [method]
            # Calculate scores for all x values
            all_scores[score_key] = [score] * len(x_values)
    
    # Process other methods from zero_scores
    for method in zero_scores['1'].keys():
        score = zero_scores['1'][method]
        score_key = f"{score}"
        if score_key in score_to_methods:
            score_to_methods[score_key].append(method)
        else:
            score_to_methods[score_key] = [method]
            all_scores[score_key] = [score] * len(x_values)

    # Define distinct colors with better visibility
    distinct_colors = [
        '#FF0000', '#0000FF', '#00FF00', '#FF8C00', '#800080',
        '#008080', '#FF1493', '#FFD700', '#4B0082', '#00FFFF',
        '#FF4500', '#32CD32', '#BA55D3', '#20B2AA', '#FF69B4'
    ]

    # Add thick axes at y=0 and x=0 BEFORE plotting the data
    plt.axhline(y=1, color='black', linewidth=1.5)  # Thicker horizontal line at y=0
    plt.axvline(x=0, color='black', linewidth=1.5)  # Thicker vertical line at x=0 (corresponding to value 0)

    # Plot each unique score line with combined method names
    for i, (score_key, scores) in enumerate(all_scores.items()):
        methods = score_to_methods[score_key]
        max_methods_per_line = 4
        if len(methods) > max_methods_per_line:
            chunks = [methods[i:i + max_methods_per_line] for i in range(0, len(methods), max_methods_per_line)]
            combined_label = '\n'.join([' + '.join(chunk) for chunk in chunks])
        else:
            combined_label = ' + '.join(methods)
        color = contraceptive_colors[methods[0]]
            
        plt.plot(range(len(x_values)), scores,
                label=combined_label,
                marker='o',
                linewidth=2,
                markersize=6,
                color=color)

    # Customize the plot
    plt.xlabel('Weights', fontsize=12)
    plt.ylabel('Contraceptive Score', fontsize=12)
    plt.title('Contraceptive Scores across weights for Top surgery', fontsize=14, pad=20)
    
    # Improve legend
    plt.legend(bbox_to_anchor=(1.05, 1), 
              loc='upper left', 
              fontsize=10,
              frameon=True,
              edgecolor='black')
    
    # Enhance grid
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # Set y-axis limits with some padding
    plt.ylim(-550, 100)
    
    # Set x-axis ticks and labels
    plt.xticks(range(len(x_values)), 
               weight_labels,
               rotation=45,
               ha='right',
               fontsize=10)
    
    # Add subtle background grid
    plt.grid(True, which='both', linestyle='--', alpha=0.2)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return plt

plt = plot_contraceptive_scores(neg_scores, zero_scores)
filename = f'univariate_analysis/visualizations_univariate/medical_conditions/ts_univ_viz.png'  # or .pdf, .jpg, etc.
plt.savefig(filename, dpi=300, bbox_inches='tight')
#plt.show()


