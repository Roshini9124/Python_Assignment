import numpy as np
from src.MinMax.util import min_max


def test_min_max():
    arr = np.array([
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ])
    assert min_max(arr) == 3