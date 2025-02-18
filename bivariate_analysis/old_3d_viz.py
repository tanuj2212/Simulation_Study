'''
import plotly.graph_objects as go
import numpy as np

# Define categorical labels for x-axis
x_category_labels = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', 'v_imp']
x_values = [-60, -40, -20, 0, 20, 40, 60]
x_labels = ["-60", "-40", "-20", "0", "20", "40", "60"]  # Display labels

# Define y values and labels
severity_map = {
    'severe': -50,
    'moderate': -25,
    'mild': -15,
    'no': 0
}

positive_values = [i * 3 for i in range(1, 21)]  # Positive values from 3 to 60
y_values = list(severity_map.values()) + positive_values
y_labels = ["-50", "-25", "-15", "0"] + [str(i) for i in positive_values]

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
    '#FF0000', '#0000FF', '#FFD700', '#FF1493', '#00FF00', '#8B008B', '#FF8C00',
    '#00FFFF', '#800000', '#000080', '#808000', '#FF00FF', '#008080', '#FFA500', '#4B0082'
]
# Create the 3D visualization
fig = go.Figure()

# Process negative-only methods
for method_idx, method in enumerate(negative_only_methods):
    Z = np.zeros((len(y_values), len(x_values)))
    
    for x_idx, x_label in enumerate(x_category_labels):
        neg_dict, _ = preference_dicts[x_label]

        for severity, y_pos in severity_map.items():
            y_idx = y_values.index(y_pos)
            if severity in neg_dict and method in neg_dict[severity]:
                Z[y_idx, x_idx] = neg_dict[severity][method]
    
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

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

    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        name=method, showscale=False,
        colorscale=[[0, distinct_colors[method_idx]], [1, distinct_colors[method_idx]]],
        opacity=0.7, showlegend=True, legendgroup=method
    ))

# Update layout with modified legend positioning
fig.update_layout(
    title='3D Visualization of Contraceptive Scores',
    scene=dict(
        xaxis=dict(title='Preference Level', ticktext=x_labels, tickvals=x_values, range=[-70, 70]),
        yaxis=dict(title='Acne Severity/Positive Weight', ticktext=y_labels, tickvals=y_values, range=[-60, 60]),
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
#fig.write_html("/Users/sanyamshah/Simulation_Study/bivariate_analysis/ce_acne_3d.html")
'''