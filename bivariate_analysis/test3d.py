import numpy as np
import pyvista as pv

# Generate grid data with proper dimensions
x = np.linspace(-60, 60, 50)  # Increased resolution for smoother surface
y = np.linspace(-60, 60, 50)
X, Y = np.meshgrid(x, y)

# Create surface data with proper broadcasting
Z = (
    np.exp(-((X + 20)**2 / 1000)) * np.exp(-((Y - 15)**2 / 800)) * 40 +  # Peak 1
    np.exp(-((X - 30)**2 / 1200)) * np.exp(-((Y + 30)**2 / 900)) * 30 +  # Peak 2
    np.exp(-((X - 10)**2 / 500)) * np.exp(-((Y - 10)**2 / 500)) * 50     # Peak 3
)

# Ensure Z is properly shaped
Z = np.asarray(Z).reshape(X.shape)

# Create PyVista surface
grid = pv.StructuredGrid(X, Y, Z)

# Create plotter with improved settings
plotter = pv.Plotter()
plotter.add_mesh(
    grid,
    scalars=Z.ravel(),  # Flatten the array for scalar mapping
    cmap="viridis",
    smooth_shading=True,
    specular=0.5,
    show_edges=False,
    scalar_bar_args={'title': "Score Value"}
)

# Add labels with better positioning
plotter.add_axes(
    xlabel="X Variable",
    ylabel="Y Variable",
    zlabel="Z Score",
    line_width=5,
    labels_off=False
)

# Adjust camera position for better initial view
plotter.camera_position = 'xy'
plotter.show(window_size=[1000, 800], title="3D Surface Plot")