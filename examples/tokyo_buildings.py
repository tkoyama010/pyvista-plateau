import json
from pyvista_plateau import convert_to_pyvista, filter_by_height, plot_mesh

# Create a simple demo GeoJSON dataset with building data
demo_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [139.7, 35.6, 0],
                    [139.7, 35.601, 0],
                    [139.701, 35.601, 0],
                    [139.701, 35.6, 0],
                    [139.7, 35.6, 0]
                ]]
            },
            "properties": {
                "measuredHeight": 50.0,
                "name": "Building 1"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [139.702, 35.6, 0],
                    [139.702, 35.601, 0],
                    [139.703, 35.601, 0],
                    [139.703, 35.6, 0],
                    [139.702, 35.6, 0]
                ]]
            },
            "properties": {
                "measuredHeight": 25.0,
                "name": "Building 2"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [139.704, 35.6, 0],
                    [139.704, 35.601, 0],
                    [139.705, 35.601, 0],
                    [139.705, 35.6, 0],
                    [139.704, 35.6, 0]
                ]]
            },
            "properties": {
                "measuredHeight": 75.0,
                "name": "Building 3"
            }
        }
    ]
}

print("Creating demo dataset...")

# Convert demo data to PyVista mesh
print("Converting to PyVista mesh...")
mesh = convert_to_pyvista(demo_geojson)

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
