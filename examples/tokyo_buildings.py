from pyvista_plateau.loader import load_citygml
from pyvista_plateau.filter import filter_by_height
from pyvista_plateau.plotter import plot_mesh

mesh = load_citygml("https://www.geospatial.jp/ckan/dataset/plateau-tokyo23ku-citygml-2020/resource/d6140914-8035-4eae-b187-6dc5b5e33974")
filtered = filter_by_height(mesh, min_height=30)
plot_mesh(filtered, title="Tokyo Buildings taller than 30m")
