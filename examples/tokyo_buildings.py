import json
from pyvista_plateau import convert_to_pyvista, filter_by_height, plot_mesh

from plateaukit import load_dataset

dataset = load_dataset("plateau-tokyo23ku-2022")

area = dataset.area_from_landmark("田町駅")

area.show()
print("Creating demo dataset...")

# Convert demo data to PyVista mesh
print("Converting to PyVista mesh...")
mesh = convert_to_pyvista(dataset)

# Filter buildings taller than 30 meters
print("Filtering buildings by height...")
filtered = filter_by_height(mesh, min_height=30)

# Visualize the results
print("Plotting results...")
# Note: This will open an interactive 3D window
# Uncomment the line below to visualize:
# plot_mesh(filtered, title="Demo Buildings taller than 30m")

# Alternative: Save to file
import pyvista as pv
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(
    filtered, 
    scalars='height',
    cmap='viridis',
    show_edges=True,
    edge_color='white',
    line_width=0.5
)
plotter.add_scalar_bar(title="Height (m)")
plotter.camera_position = 'iso'
plotter.screenshot('demo_buildings.png')
print("Saved visualization to demo_buildings.png")

# Print summary
print(f"\nSummary:")
print(f"Total buildings: 3")
print(f"Buildings taller than 30m: {filtered.n_cells // 10}")  # Each building has ~10 faces
print(f"Mesh points: {filtered.n_points}")
print(f"Mesh faces: {filtered.n_cells}")
