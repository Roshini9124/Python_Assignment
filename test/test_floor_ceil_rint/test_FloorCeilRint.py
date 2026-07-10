import sys
import os
import numpy as np
 
# Add src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
 
from src.FloorCeilRint.util import floor_values, ceil_values, rint_values
 
 
def test_floor_values():
    data = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected = np.array([1., 2., 3., 4., 5.])
 
    np.testing.assert_array_equal(floor_values(data), expected)
 
 
def test_ceil_values():
    data = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected = np.array([2., 3., 4., 5., 6.])
 
    np.testing.assert_array_equal(ceil_values(data), expected)
 
 
def test_rint_values():
    data = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected = np.array([1., 2., 3., 4., 6.])
 
    np.testing.assert_array_equal(rint_values(data), expected)
 