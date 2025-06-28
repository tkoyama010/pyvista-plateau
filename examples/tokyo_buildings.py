import plateaukit as pk
from pyvista_plateau import convert_to_pyvista, filter_by_height, plot_mesh

# Load a sample CityGML file using PlateauKit
# For this example, we'll create a simple demo dataset
print("Creating demo dataset...")

# Create a simple demo with some building polygons
demo_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [139.7, 35.7, 0],
                    [139.71, 35.7, 0], 
                    [139.71, 35.71, 0],
                    [139.7, 35.71, 0],
                    [139.7, 35.7, 0]
                ]]
            },
            "properties": {
                "measuredHeight": 45.0
            }
        },
        {
            "type": "Feature", 
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [139.72, 35.7, 0],
                    [139.73, 35.7, 0],
                    [139.73, 35.71, 0], 
                    [139.72, 35.71, 0],
                    [139.72, 35.7, 0]
                ]]
            },
            "properties": {
                "measuredHeight": 25.0
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon", 
                "coordinates": [[
                    [139.705, 35.705, 0],
                    [139.715, 35.705, 0],
                    [139.715, 35.715, 0],
                    [139.705, 35.715, 0], 
                    [139.705, 35.705, 0]
                ]]
            },
            "properties": {
                "measuredHeight": 60.0
            }
        }
    ]
}

# Convert demo data to PyVista mesh
print("Converting to PyVista mesh...")
mesh = convert_to_pyvista(demo_geojson)

# Filter buildings taller than 30 meters
print("Filtering buildings by height...")
filtered = filter_by_height(mesh, min_height=30)

# Visualize the results
print("Plotting results...")
plot_mesh(filtered, title="Demo Buildings taller than 30m")
