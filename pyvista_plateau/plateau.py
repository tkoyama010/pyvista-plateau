"""
Core plateau functionality for PyVista meshes.
"""

import pyvista as pv
import numpy as np
from scipy.spatial import ConvexHull


class PlateauMesh:
    """A class for creating and manipulating plateau-like mesh structures."""
    
    def __init__(self, mesh=None):
        """Initialize with an optional PyVista mesh."""
        self.mesh = mesh
    
    def create_plateau(self, width=10, height=10, plateau_height=2, base_height=0):
        """Create a basic plateau mesh structure."""
        # Create a grid for the base
        x = np.linspace(-width/2, width/2, 50)
        y = np.linspace(-height/2, height/2, 50)
        X, Y = np.meshgrid(x, y)
        
        # Create plateau shape (elevated center region)
        center_mask = (X**2 + Y**2) <= (min(width, height)/4)**2
        Z = np.where(center_mask, plateau_height, base_height)
        
        # Create PyVista structured grid
        self.mesh = pv.StructuredGrid(X, Y, Z)
        return self.mesh
    
    def smooth_plateau(self, iterations=100):
        """Apply smoothing to the plateau mesh."""
        if self.mesh is None:
            raise ValueError("No mesh available. Create or load a mesh first.")
        
        self.mesh = self.mesh.smooth(n_iter=iterations)
        return self.mesh
    
    def add_noise(self, amplitude=0.1):
        """Add random noise to the plateau surface."""
        if self.mesh is None:
            raise ValueError("No mesh available. Create or load a mesh first.")
        
        points = self.mesh.points.copy()
        noise = np.random.normal(0, amplitude, points.shape[0])
        points[:, 2] += noise  # Add noise to Z coordinates
        self.mesh.points = points
        return self.mesh
    
    def visualize(self, show_edges=True, color='terrain'):
        """Visualize the plateau mesh using PyVista."""
        if self.mesh is None:
            raise ValueError("No mesh available. Create or load a mesh first.")
        
        plotter = pv.Plotter()
        plotter.add_mesh(self.mesh, show_edges=show_edges, cmap=color)
        plotter.show_grid()
        plotter.show()


def create_simple_plateau():
    """Create and return a simple plateau mesh."""
    plateau = PlateauMesh()
    return plateau.create_plateau()
