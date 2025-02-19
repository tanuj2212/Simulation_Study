import copy
from matplotlib import pyplot as plt
from correct_original_weights_hor import *


from functions_simulation_diff_weight_hor import *

# Define the input data

inputs = [
    ['v_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    ['unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_unp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['sl_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['v_imp', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes']
]


# Define the weight multipliers
n = 20
weight_multipliers = [i + 1 for i in range(n)]

# Define a function to calculate scores for a given input and weight multiplier
def calculate_scores(input_arr, multiplier):
    weights = [-3 * multiplier, -2 * multiplier, -1 * multiplier,
               1 * multiplier, 2 * multiplier, 3 * multiplier]

    # Update weights for each method
    weights_dict = {
            'condoms': copy.deepcopy(original_weight_condoms),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'cervical_cap': copy.deepcopy(original_weight_cervical_cap),
            'FAM': copy.deepcopy(original_weight_FAM),
            'patch': copy.deepcopy(original_weight_patch),
            'combo_pill': copy.deepcopy(original_weight_combo_pill),
            'mini_pill': copy.deepcopy(original_weight_mini_pill),
            'ring': copy.deepcopy(original_weight_ring),
            'spermicide': copy.deepcopy(original_weight_spermicide),
            'withdrawal': copy.deepcopy(original_weight_withdrawl)
        }

    original_weights = {
    'arm_implant': original_weight_arm_implant,
    'copper_iud': original_weight_copper_IUD,
    'hormonal_iud': original_weight_hormonal_IUD,
    'shot': original_weight_shot,
    'sterilization': original_weight_sterilization
} 

    # Update the cost effectiveness weights
    for method in weights_dict:
        weights_dict[method][0] = weights

    # Calculate scores
    #condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    #internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    #cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    #fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    #copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
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
    arm_implant_score = change_arm_implant(arm_implant_arr, original_weights['arm_implant'])
    copper_iud_score = change_copper_iud(copper_iud_arr, original_weights['copper_iud'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, original_weights['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, original_weights['shot'])
    sterilization_score = change_score_sterilization(sterilization_arr, original_weights['sterilization'])
    gel_score = change_score_gel(gel_arr, weights_dict['spermicide'])
    withdrawal_score = change_score_withdrawal(withdrawal_arr, weights_dict['withdrawal'])
    return {
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

weight_multipliers = [-60, -40, -20, 0, 20, 40, 60]
weight_labels = [-60, -40, -20, 0, 20, 40, 60]

plt.figure(figsize=(12, 8))

# Calculate scores for each input
scores_over_inputs = {method: [] for method in calculate_scores(inputs[0], 1).keys()}
for input_arr in inputs:
   scores = calculate_scores(input_arr, 20)
   for method, score in scores.items():
       scores_over_inputs[method].append(score)

# Group methods with identical score patterns
grouped_methods = {}
for method, scores in scores_over_inputs.items():
   scores_tuple = tuple(scores)  # Convert scores list to tuple for hashing
   if scores_tuple in grouped_methods:
       grouped_methods[scores_tuple].append(method)
   else:
       grouped_methods[scores_tuple] = [method]

# Plot each unique score pattern with combined labels using distinct colors
for i, (scores_tuple, methods) in enumerate(grouped_methods.items()):
   combined_label = ' + '.join(methods)
   plt.plot(weight_multipliers, scores_tuple, label=combined_label, marker='o', 
            color=distinct_colors[i % len(distinct_colors)])  # Use modulo to cycle through colors

plt.xlabel('Weight for Cost Effectiveness')
plt.ylabel('Contraceptive Score')
plt.title('Contraceptive Scores vs Weight for Cost Effectiveness')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(weight_multipliers, weight_labels, rotation=45)
plt.tight_layout()
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.ylim(-550, 100)

filename = f'univariate_analysis/visualizations_univariate/personal_preferences/cost_effectiveness_univ_viz.png'  # or .pdf, .jpg, etc.
plt.savefig(filename, dpi=300, bbox_inches='tight')
#plt.show()