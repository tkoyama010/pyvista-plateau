import pyvista as pv
import numpy as np


def filter_by_height(mesh: pv.PolyData, min_height: float = 10.0) -> pv.PolyData:
    """
    Filter a PyVista mesh to only include buildings above a minimum height.
    
    Parameters
    ----------
    mesh : pv.PolyData
        Input PyVista mesh with building data
    min_height : float, optional
        Minimum height threshold in meters (default: 10.0)
        
    Returns
    -------
    pv.PolyData
        Filtered mesh containing only buildings above min_height
    """
    if 'height' not in mesh.point_data:
        print("Warning: No height data found in mesh. Returning original mesh.")
        return mesh
    
    # Get height data
    heights = mesh.point_data['height']
    
    # Create mask for points above minimum height
    height_mask = heights >= min_height
    
    if not np.any(height_mask):
        print(f"No buildings found above {min_height}m height.")
        return pv.PolyData()  # Return empty mesh
    
    # Extract subset of mesh based on height criteria
    # This is a simplified approach - in practice you might want more sophisticated filtering
    filtered_mesh = mesh.extract_points(height_mask)
    
    return filtered_mesh
