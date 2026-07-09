import numpy as np
import math

def floor_values(numbers):
    return np.array([math.floor(num) for num in numbers], float)

def ceil_values(numbers):
    return np.array([math.ceil(num) for num in numbers], float)

def rint_values(numbers):
    return np.array([np.rint(num) for num in numbers])