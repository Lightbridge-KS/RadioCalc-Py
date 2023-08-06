# Ellipsoid Volume

def print_vol_ellipsoid(d1, d2, d3):
    """Print ellipsoid volume from 3 perpendicular **diameters**"""
    v = round(vol_ellipsoid(d1, d2, d3), 3)
    print(f"Volume: {v}")
    return(v)

def vol_ellipsoid(d1, d2, d3):
    """Calculate ellipsoid volume from 3 perpendicular **diameters**"""
    import math
    volume = (4/3) * math.pi * d1/2 * d2/2 * d3/2
    return volume
