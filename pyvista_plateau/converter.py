import pyvista as pv
import numpy as np
import plateaukit as pk
from typing import Union


def convert_to_pyvista(data) -> pv.PolyData:
    """
    Convert GeoJSON or PlateauKit data to a PyVista mesh.
    
    Parameters
    ----------
    data : dict or plateaukit dataset
        The data to convert (GeoJSON dict or PLATEAU dataset)
        
    Returns
    -------
    pv.PolyData
        PyVista mesh representation of the dataset
    """
    # Handle different input types
    if isinstance(data, dict):
        geojson_data = data
    else:
        # Try to convert using PlateauKit
        try:
            geojson_data = pk.convert.to_geojson(data)
        except:
            raise ValueError("Unable to convert input data to GeoJSON format")
    
    # Extract building geometries and create mesh
    points = []
    faces = []
    heights = []
    
    point_offset = 0
    
    for feature in geojson_data.get('features', []):
        geometry = feature.get('geometry', {})
        properties = feature.get('properties', {})
        
        if geometry.get('type') == 'Polygon':
            coords = geometry.get('coordinates', [[]])[0]  # Get exterior ring
            
            # Get building height from properties
            height = properties.get('measuredHeight', 10.0)  # Default 10m if not specified
            heights.extend([height] * len(coords))
            
            # Create base points (ground level)
            base_points = []
            for coord in coords[:-1]:  # Skip last point (same as first)
                points.append([coord[0], coord[1], 0.0])
                base_points.append(point_offset)
                point_offset += 1
            
            # Create top points (at building height)
            top_points = []
            for coord in coords[:-1]:
                points.append([coord[0], coord[1], height])
                top_points.append(point_offset)
                point_offset += 1
            
            # Create faces for the building
            n_points = len(base_points)
            
            # Bottom face
            bottom_face = [n_points] + base_points
            faces.extend(bottom_face)
            
            # Top face (reversed for correct normal)
            top_face = [n_points] + top_points[::-1]
            faces.extend(top_face)
            
            # Side faces
            for i in range(n_points):
                next_i = (i + 1) % n_points
                # Create quad face
                quad = [4, base_points[i], base_points[next_i], 
                       top_points[next_i], top_points[i]]
                faces.extend(quad)
    
    if not points:
        # Return empty mesh if no data
        return pv.PolyData()
    
    # Create PyVista mesh
    mesh = pv.PolyData(np.array(points), faces=faces)
    
    # Add height data as point data
    if heights:
        mesh.point_data['height'] = np.array(heights)
    
    return mesh
