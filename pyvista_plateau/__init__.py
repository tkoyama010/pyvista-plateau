"""
PyVista Plateau - A package for plateau functionality with PyVista
"""

from .converter import convert_to_pyvista
from .filter import filter_by_height
from .plotter import plot_mesh

__version__ = "0.1.0"
__all__ = ["convert_to_pyvista", "filter_by_height", "plot_mesh"]
