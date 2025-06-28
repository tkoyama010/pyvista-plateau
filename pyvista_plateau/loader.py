import pyvista as pv
import xml.etree.ElementTree as ET
import numpy as np
from pathlib import Path


def load_citygml(file_path):
    """
    Load a CityGML file and convert building surfaces to a PyVista PolyData mesh.
    This basic version assumes triangulated surfaces and limited metadata.
    """
    file_path = Path(file_path)
    tree = ET.parse(file_path)
    root = tree.getroot()

    ns = {
        "gml": "http://www.opengis.net/gml",
        "bldg": "http://www.opengis.net/citygml/building/2.0",
    }

    all_points = []
    faces = []
    heights = []

    for surface in root.findall(".//gml:Polygon", ns):
        pos_list = surface.find(".//gml:posList", ns)
        if pos_list is None:
            continue
        coords = list(map(float, pos_list.text.strip().split()))
        coords = np.array(coords).reshape(-1, 3)

        start_idx = len(all_points)
        all_points.extend(coords)
        faces.append([len(coords)] + list(range(start_idx, start_idx + len(coords))))

        # Dummy height (use real measuredHeight in real version)
        avg_height = np.mean(coords[:, 2])
        heights.append(avg_height)

    points = np.array(all_points)
    faces_flat = np.hstack(faces)
    mesh = pv.PolyData(points, faces_flat)
    mesh["measuredHeight"] = np.array(heights).repeat([f[0] for f in faces])

    return mesh
