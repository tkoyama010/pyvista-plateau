# PyVista Plateau

A Python package that combines PyVista 3D visualization with PlateauKit for working with MLIT Project PLATEAU 3D city models.

## Features

- Load PLATEAU CityGML datasets using PlateauKit
- Convert CityGML to PyVista meshes for 3D visualization
- Filter buildings by height and other criteria
- Create and manipulate plateau-like mesh structures
- Interactive 3D visualization of urban building models
- Support for PLATEAU dataset management and conversion

## Installation

```bash
pip install pyvista-plateau
```

This package depends on:
- `plateaukit[all]` - For PLATEAU data handling and CityGML processing
- `pyvista` - For 3D mesh visualization
- `numpy` - For numerical operations

## Quick Start

```python
import plateaukit as pk
from pyvista_plateau import convert_to_pyvista, filter_by_height, plot_mesh

# Install and load PLATEAU dataset
pk.datasets.install("tokyo23ku")
dataset = pk.datasets.load("tokyo23ku")

# Convert to PyVista mesh
mesh = convert_to_pyvista(dataset)

# Filter buildings by minimum height
filtered = filter_by_height(mesh, min_height=30)

# Visualize the results
plot_mesh(filtered, title="Tokyo Buildings > 30m")
```

## Examples

See the `examples/` directory for more detailed usage examples including:
- Loading Tokyo building data from PLATEAU datasets
- Filtering and visualizing urban structures
- Creating custom plateau meshes

## About PLATEAU

This package leverages the [MLIT Project PLATEAU](https://www.mlit.go.jp/plateau/) 3D city model datasets through the excellent [PlateauKit](https://github.com/ozekik/plateaukit) library. PLATEAU provides high-quality 3D city models for Japanese cities.
