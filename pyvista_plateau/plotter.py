import pyvista as pv

def plot_mesh(mesh, title="CityGML View"):
    p = pv.Plotter()
    p.add_mesh(mesh, scalars="measuredHeight", show_scalar_bar=True)
    p.add_title(title)
    p.show()
