import pyvista as pv
import numpy as np


def plot_mesh(mesh: pv.PolyData, title: str = "CityGML View", **kwargs):
    """
    Plot a PyVista mesh with building data.
    
    Parameters
    ----------
    mesh : pv.PolyData
        PyVista mesh to visualize
    title : str, optional
        Title for the plot window (default: "CityGML View")
    **kwargs
        Additional keyword arguments passed to the plotter
    """
    if mesh.n_points == 0:
        print("Warning: Empty mesh provided. Nothing to plot.")
        return
    
    # Create plotter
    plotter = pv.Plotter(title=title)
    
    # Add mesh to plotter
    if 'height' in mesh.point_data:
        # Color by height if available
        plotter.add_mesh(
            mesh, 
            scalars='height',
            cmap='viridis',
            show_edges=True,
            edge_color='white',
            line_width=0.5,
            **kwargs
        )
        plotter.add_scalar_bar(title="Height (m)")
    else:
        # Default coloring
        plotter.add_mesh(
            mesh,
            color='lightblue',
            show_edges=True,
            edge_color='white',
            line_width=0.5,
            **kwargs
        )
    
    # Set up camera and lighting
    plotter.camera_position = 'iso'
    plotter.enable_anti_aliasing()
    
    # Show the plot
    plotter.show()
