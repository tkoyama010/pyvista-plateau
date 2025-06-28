# PyVista Plateau

A Python package for loading, filtering, and visualizing CityGML building data using PyVista.

## Features

- Load CityGML files containing building data
- Filter buildings by height and other criteria
- Create and manipulate plateau-like mesh structures
- 3D visualization of urban building models

## Installation

```bash
pip install pyvista-plateau
```

## Quick Start

```python
from pyvista_plateau import load_citygml, filter_by_height, plot_mesh

# Load CityGML data
mesh = load_citygml("Tokyo_23ku_Building.gml")

# Filter buildings by minimum height
filtered = filter_by_height(mesh, min_height=30)

# Visualize the results
plot_mesh(filtered, title="Tokyo Buildings > 30m")
```

## Examples

See the `examples/` directory for more detailed usage examples.
