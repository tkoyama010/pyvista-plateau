def filter_by_height(mesh, min_height=10.0):
    return mesh.threshold(value=min_height, scalars="measuredHeight")
