import numpy as np
import plotly.graph_objects as go

# Define different planes with coefficients (a, b)
planes = [
    {"a": 2, "b": 3, "color": "red"},
    {"a": -1, "b": 4, "color": "blue"},
    {"a": 1, "b": -2, "color": "green"},
    {"a": 3, "b": -1, "color": "purple"}
]

# Define X, Y range
x_values = np.linspace(-10, 10, 20)
y_values = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x_values, y_values)

# Create figure
fig = go.Figure()

# Plot each plane as a surface
for plane in planes:
    Z = plane["a"] * X + plane["b"] * Y  # Compute Z using ax + by = z
    
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z, colorscale=[[0, plane["color"]], [1, plane["color"]]],
        opacity=0.6, name=f"Plane {plane['a']}x + {plane['b']}y = z"
    ))

# Update layout for better visualization
fig.update_layout(
    title="Interactive 3D Visualization of Intersecting Planes",
    scene=dict(
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        zaxis_title="Z-axis",
        aspectmode="cube"  # Keeps axes proportional
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Show figure
fig.show()
