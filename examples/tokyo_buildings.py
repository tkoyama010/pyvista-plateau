import plateaukit as pk
from pyvista_plateau import convert_to_pyvista, filter_by_height, plot_mesh

# Install Tokyo 23 wards dataset if not already installed
try:
    dataset = pk.datasets.load("tokyo23ku")
except:
    print("Installing Tokyo 23ku dataset...")
    pk.datasets.install("tokyo23ku")
    dataset = pk.datasets.load("tokyo23ku")

# Convert PLATEAU dataset to PyVista mesh
print("Converting to PyVista mesh...")
mesh = convert_to_pyvista(dataset)

# Filter buildings taller than 30 meters
print("Filtering buildings by height...")
filtered = filter_by_height(mesh, min_height=30)

# Visualize the results
print("Plotting results...")
plot_mesh(filtered, title="Tokyo Buildings taller than 30m")
