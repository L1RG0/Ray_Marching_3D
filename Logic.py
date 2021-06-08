import math
import numpy as np
from numba import jit

@jit
def length(x, y, z):
    return np.sqrt(x ** 2 + y ** 2 + z ** 2)

@jit
def Ray(x, y, z, angle_x, angle_y, col, dist):
    closest_distance = DistanceToSphere(x, y, z, .15)
    # closest_distance = DistanceToSphere(x, y, z, 150)
    if closest_distance < .002:
        return 0
    elif closest_distance > 1.5 or col > 255 or dist > 2:
        return col
    else:
        radius = closest_distance
        x += radius * math.cos(angle_y) * math.sin(angle_x)
        y += radius * math.sin(angle_y)
        z += radius * math.cos(angle_y) * math.cos(angle_x)
        return Ray(x, y, z, angle_x, angle_y, col + 1, closest_distance)

@jit
def DistanceToSphere(x, y, z, radius):
    return length(x, y, z) - radius

@jit
def DistanceToBox(x1, y1, z1, x2, y2, z2):
    xq, yq, zq = abs(x1) - x2, abs(y1) - y2, abs(z1) - z2
    xp, yp, zp = max(xq, 0), max(yq, 0), max(zq, 0)
    return length(xp, yp, zp) + min(max(xq, yq, zq), 0.0)
