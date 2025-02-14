import numpy as np
from mayavi import mlab

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
x_values = [-60, -40, -20, 0, 20, 40, 60]

# Define y values and labels
severity_map = {
    'severe': -50,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60
y_values = list(severity_map.values()) + positive_values

# Create coordinate matrices using actual numerical values
X, Y = np.meshgrid(x_values, y_values)

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
    "Condom", "Internal Condom", "Cervical Cap", "FAM", "Copper IUD",
    "Hormonal IUD", "Patch", "Combination Pill", "Sterilization",
    "Spermicide Gel", "Withdrawal"
]

full_range_methods = [
    "Arm Implant", "Mini Pill", "Ring", "Shot"
]

# Combined list for color assignment
all_methods = negative_only_methods + full_range_methods

# Create distinct color scale
distinct_colors = [
    (1, 0, 0), (0, 0, 1), (1, 0.84, 0), (1, 0.08, 0.58), (0, 1, 0), (0.55, 0, 0.55), (1, 0.55, 0),
    (0, 1, 1), (0.5, 0, 0), (0, 0, 0.5), (0.5, 0.5, 0), (1, 0, 1), (0, 0.5, 0.5), (1, 0.65, 0), (0.29, 0, 0.51)
]

# Create the 3D visualization
fig = mlab.figure(size=(1200, 800))

# Process negative-only methods
for method_idx, method in enumerate(negative_only_methods):
    Z = np.zeros((len(y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _ = preference_dicts[x_label]

        for severity, y_pos in severity_map.items():
            y_idx = y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    
    mlab.surf(X, Y, Z, color=distinct_colors[method_idx], opacity=0.7, name=method)

# Process full-range methods
for method_idx, method in enumerate(full_range_methods, start=len(negative_only_methods)):
    Z = np.zeros((len(y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, pos_dict = preference_dicts[x_label]

        for severity, y_pos in severity_map.items():
            y_idx = y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
        
        for y_value in positive_values:
            y_idx = y_values.index(y_value)
            if str(y_value) in pos_dict and method in pos_dict[str(y_value)]:
                Z[y_idx, x_idx] = pos_dict[str(y_value)][method]

    mlab.surf(X, Y, Z, color=distinct_colors[method_idx], opacity=0.7, name=method)

# Add labels and title
mlab.xlabel('Preference Level')
mlab.ylabel('Acne Severity/Positive Weight')
mlab.zlabel('Score')
mlab.title('3D Visualization of Contraceptive Scores')

# Show the plot
mlab.show()