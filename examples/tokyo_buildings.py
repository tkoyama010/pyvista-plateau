from pyvista_plateau.loader import load_citygml
from pyvista_plateau.filter import filter_by_height
from pyvista_plateau.plotter import plot_mesh

# Fix code to load gml file from internet like pyvista load functions AI!
mesh = load_citygml("Tokyo_23ku_Building.gml")
filtered = filter_by_height(mesh, min_height=30)
plot_mesh(filtered, title="Tokyo Buildings taller than 30m")
