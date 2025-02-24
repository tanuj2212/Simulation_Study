import numpy as np
from mayavi import mlab
'''

# Create matrices from the actual dictionaries
def create_full_matrix(method_dicts):
    no_dict, mild_dict, mod_dict, sev_dict, t3_dict, t6_dict, t9_dict = method_dicts
    return np.array([
        [no_dict['no'], no_dict['mild'], no_dict['moderate'], no_dict['severe'], t3_dict['3'], t3_dict['6'], t3_dict['9']],
        [mild_dict['no'], mild_dict['mild'], mild_dict['moderate'], mild_dict['severe'], t3_dict['3'], t3_dict['6'], t3_dict['9']],
        [mod_dict['no'], mod_dict['mild'], mod_dict['moderate'], mod_dict['severe'], t3_dict['3'], t3_dict['6'], t3_dict['9']],
        [sev_dict['no'], sev_dict['mild'], sev_dict['moderate'], sev_dict['severe'], t3_dict['3'], t3_dict['6'], t3_dict['9']],
        [t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['3'], t3_dict['6'], t3_dict['9']],
        [t6_dict['3'], t6_dict['3'], t6_dict['3'], t6_dict['3'], t6_dict['3'], t6_dict['6'], t6_dict['9']],
        [t9_dict['3'], t9_dict['3'], t9_dict['3'], t9_dict['3'], t9_dict['3'], t9_dict['6'], t9_dict['9']]
    ])

# Create all matrices
z_condoms = create_full_matrix([condom_no, condoms_mild, condoms_moderate, condoms_severe, condoms_3, condoms_6, condoms_9])
z_internal_condoms = create_full_matrix([internal_condom_no, internal_condom_mild, internal_condom_moderate, internal_condom_severe, internal_condom_3, internal_condom_6, internal_condom_9])
z_cervical_cap = create_full_matrix([cervical_cap_no, cervical_cap_mild, cervical_cap_moderate, cervical_cap_severe, cervical_cap_3, cervical_cap_6, cervical_cap_9])
z_fam = create_full_matrix([fam_no, fam_mild, fam_moderate, fam_severe, fam_3, fam_6, fam_9])
z_copper_iud = create_full_matrix([copper_iud_no, copper_iud_mild, copper_iud_moderate, copper_iud_severe, copper_iud_3, copper_iud_6, copper_iud_9])
z_sterilization = create_full_matrix([sterilization_no, sterilization_mild, sterilization_moderate, sterilization_severe, sterilization_3, sterilization_6, sterilization_9])
z_spermicide = create_full_matrix([spermicide_no, spermicide_mild, spermicide_moderate, spermicide_severe, spermicide_3, spermicide_6, spermicide_9])
z_withdrawal = create_full_matrix([withdrawal_no, withdrawal_mild, withdrawal_moderate, withdrawal_severe, withdrawal_3, withdrawal_6, withdrawal_9])

x_full = ['no', 'mild', 'moderate', 'severe', '3', '6', '9']
y_full = ['no', 'mild', 'moderate', 'severe', '3', '6', '9']

# Create partial matrix for arm implant (only 3,6,9 values)
x_partial = ['3', '6', '9']
y_partial = ['3', '6', '9']
z_arm_implant = np.array([
    [arm_implant_3['3'], arm_implant_3['6'], arm_implant_3['9']],
    [arm_implant_6['3'], arm_implant_6['6'], arm_implant_6['9']],
    [arm_implant_9['3'], arm_implant_9['6'], arm_implant_9['9']]
])

# Create hormonal IUD matrix (4x7 matrix)
z_hormonal_iud = np.array([
    [hormonal_iud_no['no'], hormonal_iud_no['mild'], hormonal_iud_no['moderate'], hormonal_iud_no['severe'], hormonal_iud_no['3'], hormonal_iud_no['6'], hormonal_iud_no['9']],
    [hormonal_iud_mild['no'], hormonal_iud_mild['mild'], hormonal_iud_mild['moderate'], hormonal_iud_mild['severe'], hormonal_iud_mild['3'], hormonal_iud_mild['6'], hormonal_iud_mild['9']],
    [hormonal_iud_moderate['no'], hormonal_iud_moderate['mild'], hormonal_iud_moderate['moderate'], hormonal_iud_moderate['severe'], hormonal_iud_moderate['3'], hormonal_iud_moderate['6'], hormonal_iud_moderate['9']],
    [hormonal_iud_severe['no'], hormonal_iud_severe['mild'], hormonal_iud_severe['moderate'], hormonal_iud_severe['severe'], hormonal_iud_severe['3'], hormonal_iud_severe['6'], hormonal_iud_severe['9']],
])

# Create ring matrix (4x3 matrix)
z_ring = np.array([
    [ring_3['no'], ring_3['mild'], ring_3['moderate'], ring_3['severe']],
    [ring_6['no'], ring_6['mild'], ring_6['moderate'], ring_6['severe']],
    [ring_9['no'], ring_9['mild'], ring_9['moderate'], ring_9['severe']]
])

# Create shot matrix (4x3 matrix)
z_shot = np.array([
    [shot_3['no'], shot_3['mild'], shot_3['moderate'], shot_3['severe']],
    [shot_6['no'], shot_6['mild'], shot_6['moderate'], shot_6['severe']],
    [shot_9['no'], shot_9['mild'], shot_9['moderate'], shot_9['severe']]
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

# Add ring surface with its specific axes
x_ring_shot = ['no', 'mild', 'moderate', 'severe']
y_ring_shot = ['3', '6', '9']

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
x_hormonal = ['no', 'mild', 'moderate', 'severe', '3', '6', '9']

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
    ('Arm Implant', z_arm_implant, x_partial, y_partial)
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

# Update layout with improved legend
fig.update_layout(
    title='Contraceptive Methods Scores - 3D Surface Plot',
    scene=dict(
        xaxis_title='Severity Level/Time Period',
        yaxis_title='Severity Level/Time Period',
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

fig.show()

'''