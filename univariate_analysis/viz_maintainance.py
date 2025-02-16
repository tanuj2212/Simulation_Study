import matplotlib.pyplot as plt
import copy
from correct_original_weights import *
from functions_simulation_diff_weight import *

# Define the input data
inputs = [
    ['neutral', 'neutral', 'neutral', 'neutral', 'daily', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     
    ['neutral', 'neutral', 'neutral', 'neutral', 'weekly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'monthly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],

     ['neutral', 'neutral', 'neutral', 'neutral', 'yearly', 'neutral', 'neutral', 'none', 'neutral', 'neutral', 'neutral', 'moderate',
     'moderate', 'moderate', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'moderate', 'moderate', 'no', 'yes'],
     ]


# Define the weight multipliers
n = 20
weight_multipliers = [i + 1 for i in range(n)]

# Define a function to calculate scores for a given input and weight multiplier
def calculate_scores(input_arr, multiplier):
    current_weights = 3 * multiplier

    # Update weights for each method
    weights_dict = {
            'arm_implant': copy.deepcopy(original_weight_arm_implant),
            'hormonal_iud': copy.deepcopy(original_weight_hormonal_IUD),
            'patch': copy.deepcopy(original_weight_patch),
            'combo_pill': copy.deepcopy(original_weight_combo_pill),
            'mini_pill': copy.deepcopy(original_weight_mini_pill),
            'ring': copy.deepcopy(original_weight_ring),
            'shot': copy.deepcopy(original_weight_shot),
            'copper_iud': copy.deepcopy(original_weight_copper_IUD),
            'internal_condoms': copy.deepcopy(original_weight_internal_condoms),
            'condoms': copy.deepcopy(original_weight_condoms),
            "cervical_cap": copy.deepcopy(original_weight_cervical_cap),
            "FAM": copy.deepcopy(original_weight_FAM),
            "spermicide": copy.deepcopy(original_weight_spermicide),
            "withdrawal": copy.deepcopy(original_weight_withdrawl)
        }

    original_weights = {
            'sterilization': copy.deepcopy(original_weight_sterilization),
            
        }

        # Update the cost effectiveness weights
    for method in weights_dict:
            if method == 'condoms':
                weights_dict[method][2] = current_weights
            elif method == 'internal_condoms':
                weights_dict[method][2] = current_weights
            elif method == 'cervical_cap':
                weights_dict[method][1] = current_weights
            elif method == 'FAM':
                weights_dict[method][1] = current_weights
            elif method == 'arm_implant':
                weights_dict[method][3] = current_weights
            elif method == 'copper_iud':
                weights_dict[method][1] = current_weights
            elif method == 'hormonal_iud':
                weights_dict[method][3] = current_weights
            elif method == 'patch':
                weights_dict[method][4] = current_weights
            elif method == 'combo_pill':
                weights_dict[method][4] = current_weights
            elif method == 'mini_pill':
                weights_dict[method][4] = current_weights
            elif method == 'ring':
                weights_dict[method][4] = current_weights
            elif method == 'shot':
                weights_dict[method][3] = current_weights
            elif method == 'spermicide':
                weights_dict[method][1] = current_weights
            elif method == 'withdrawal':
                weights_dict[method][1] = current_weights
            else:
                pass


    # Calculate scores
    condom_arr = ["condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[26]]
    internal_condom_arr = ["int_condom", input_arr[0], input_arr[1], input_arr[4], input_arr[5], input_arr[6], input_arr[8], input_arr[25], input_arr[26]]
    cervical_cap_arr = ["cervical_cap", input_arr[0], input_arr[4], input_arr[8], input_arr[9], input_arr[25], input_arr[26]]
    fam_arr = ["fam", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    arm_implant_arr = ["arm_implant", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[24], input_arr[26]]
    copper_iud_arr = ["copper_iud", input_arr[1], input_arr[4], input_arr[8], input_arr[9], input_arr[10], input_arr[24], input_arr[25], input_arr[26]]
    hormonal_iud_arr = ["hormonal_iud", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[8], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[25], input_arr[26]]
    patch_arr = ["patch", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    combo_pill_arr = ["combo_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    mini_pill_arr = ["mini_pill", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[11], input_arr[12], input_arr[13], input_arr[17], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    ring_arr = ["ring", input_arr[0], input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    shot_arr = ["shot", input_arr[1], input_arr[2], input_arr[3], input_arr[4], input_arr[7], input_arr[9], input_arr[10], input_arr[11], input_arr[12], input_arr[13], input_arr[14], input_arr[15], input_arr[16], input_arr[17], input_arr[18], input_arr[19], input_arr[20], input_arr[21], input_arr[22], input_arr[23], input_arr[24], input_arr[26], input_arr[27]]
    sterilization_arr = ["sterilization", input_arr[1], input_arr[2], input_arr[9], input_arr[10], input_arr[20], input_arr[21], input_arr[24], input_arr[26]]
    gel_arr = ["gel", input_arr[0], input_arr[4], input_arr[5], input_arr[8]]
    withdrawal_arr = ["withdrawal", input_arr[0], input_arr[4], input_arr[5], input_arr[26]]
    # Calculate scores using the updated weights
    condom_score = change_score_condoms(condom_arr, weights_dict['condoms'])
    internal_condom_score = change_internal_condoms(internal_condom_arr, weights_dict['internal_condoms'])
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, weights_dict['cervical_cap'])
    fam_score = change_fam(fam_arr, weights_dict['FAM'])
    arm_implant_score = change_arm_implant(arm_implant_arr, weights_dict['arm_implant'])
    copper_iud_score = change_copper_iud(copper_iud_arr, weights_dict['copper_iud'])
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, weights_dict['hormonal_iud'])
    patch_score = change_score_patch(patch_arr, weights_dict['patch'])
    combo_pill_score = change_score_combo_pill(combo_pill_arr, weights_dict['combo_pill'])
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, weights_dict['mini_pill'])
    ring_score = score_ring(ring_arr, weights_dict['ring'])
    shot_score = change_score_shot(shot_arr, weights_dict['shot'])
    sterilization_score = change_score_sterilization(sterilization_arr, original_weights['sterilization'])
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

'''
# Plot the scores for each contraceptive method
plt.figure(figsize=(12, 8))

# Choose one input to plot
input_to_plot = inputs[0]

# Calculate scores for each weight multiplier
scores_over_weights = {method: [] for method in calculate_scores(input_to_plot, 1).keys()}
for multiplier in weight_multipliers:
    scores = calculate_scores(input_to_plot, multiplier)
    for method, score in scores.items():
        scores_over_weights[method].append(score)

# Create x-axis labels showing the actual weight ranges
x_labels = [f"(-{3*m}, +{3*m})" for m in weight_multipliers]

# Plot each method's scores
for method, scores in scores_over_weights.items():
    plt.plot(range(len(weight_multipliers)), scores, label=method, marker='o')

# Customize the plot
plt.xlabel('Weight Range')
plt.ylabel('Contraceptive Score')
plt.title('Contraceptive Scores vs Weight Range for Pregnancy Prevention')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Set x-axis ticks and labels
plt.xticks(range(len(weight_multipliers)), x_labels, rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
'''

import matplotlib.pyplot as plt
# Define a list of very distinct colors
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

input_labels = ['daily', 'weekly', 'monthly', 'yearly']

# Create separate plots for each input
for input_arr, input_label in zip(inputs, input_labels):
    # Create a new figure for each input
    plt.figure(figsize=(12, 8))
    
    # Calculate scores for each weight multiplier
    scores_over_weights = {method: [] for method in calculate_scores(input_arr, 1).keys()}
    for multiplier in weight_multipliers:
        scores = calculate_scores(input_arr, multiplier)
        for method, score in scores.items():
            scores_over_weights[method].append(score)

    # Create x-axis labels showing the actual weight ranges
    x_labels = [f"({3*m})" for m in weight_multipliers]

    # Plot each method's scores with manually chosen distinct colors
    for (method, scores), color in zip(scores_over_weights.items(), distinct_colors):
        plt.plot(range(len(weight_multipliers)), scores, label=method, marker='o', color=color, linewidth=2)

    # Customize the plot
    plt.xlabel('Weight Range')
    plt.ylabel('Contraceptive Score')
    plt.title(f'Contraceptive Scores vs Weight Range for maintainance (Input: {input_label})')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Set x-axis ticks and labels
    plt.xticks(range(len(weight_multipliers)), x_labels, rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    filename = f'maintainance_{input_label}_viz.png'  # or .pdf, .jpg, etc.
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    
    # Show each plot
    #plt.show()

# Define a function to group overlapping contraceptives
def group_overlapping_scores(scores_dict):
    grouped_scores = {}
    for method, scores in scores_dict.items():
        scores_tuple = tuple(scores)
        if scores_tuple in grouped_scores:
            grouped_scores[scores_tuple].append(method)
        else:
            grouped_scores[scores_tuple] = [method]
    return grouped_scores

# Create separate plots for each input
for input_arr, input_label in zip(inputs, input_labels):
    # Create a new figure for each input
    plt.figure(figsize=(12, 8))
    
    # Calculate scores for each weight multiplier
    scores_over_weights = {method: [] for method in calculate_scores(input_arr, 1).keys()}
    for multiplier in weight_multipliers:
        scores = calculate_scores(input_arr, multiplier)
        for method, score in scores.items():
            scores_over_weights[method].append(score)

    # Group overlapping scores
    grouped_scores = group_overlapping_scores(scores_over_weights)

    # Create x-axis labels showing the actual weight ranges
    x_labels = [f"({3*m})" for m in weight_multipliers]

    # Plot each group of overlapping scores with manually chosen distinct colors
    for (scores, methods), color in zip(grouped_scores.items(), distinct_colors):
        label = '+'.join(methods)
        plt.plot(range(len(weight_multipliers)), scores, label=label, marker='o', color=color, linewidth=2)

    # Customize the plot
    plt.xlabel('Weight Range')
    plt.ylabel('Contraceptive Score')
    plt.title(f'Contraceptive Scores vs Weight Range for maintainance (Input: {input_label})')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Set x-axis ticks and labels
    plt.xticks(range(len(weight_multipliers)), x_labels, rotation=45)
    plt.ylim(-550, 100)
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    filename = f'univariate_analysis/visualizations_univariate/personal_preferences/maintainance_{input_label}_viz.png'  # or .pdf, .jpg, etc.
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    
    # Show each plot
    #plt.show()