"""
PyVista Plateau - A package for plateau functionality with PyVista
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
        
        # Convert to PolyData for smoothing if it's a StructuredGrid
        if hasattr(self.mesh, 'extract_surface'):
            poly_mesh = self.mesh.extract_surface()
        else:
            poly_mesh = self.mesh
        
        # Apply smoothing
        self.mesh = poly_mesh.smooth(n_iter=iterations)
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


def demo():
    """Run a demonstration of the plateau functionality."""
    print("Creating PyVista Plateau demo...")
    
    # Create a plateau
    plateau = PlateauMesh()
    mesh = plateau.create_plateau(width=15, height=15, plateau_height=3)
    
    # Add some noise for realism
    plateau.add_noise(amplitude=0.2)
    
    # Smooth the surface
    plateau.smooth_plateau(iterations=50)
    
    print(f"Created plateau mesh with {mesh.n_points} points and {mesh.n_cells} cells")
    
    # Visualize (commented out for non-interactive environments)
    # plateau.visualize()
    
    return plateau


def main():
    """Main entry point for the package."""
    print("PyVista Plateau Package")
    print("======================")
    print("A package for creating and manipulating plateau-like mesh structures with PyVista")
    print("\nExample usage:")
    print("from main import PlateauMesh")
    print("plateau = PlateauMesh()")
    print("mesh = plateau.create_plateau()")
    print("plateau.visualize()")
    
    # Run demo
    demo()


if __name__ == "__main__":
    main()
