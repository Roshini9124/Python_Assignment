import numpy as np
from src.MeanVarStd.util import calculate_statistics


def test_calculate_statistics():
    arr = np.array([
        [1, 2],
        [3, 4]
    ])

    mean, var, std = calculate_statistics(arr)

    assert np.array_equal(mean, np.array([1.5, 3.5]))
    assert np.array_equal(var, np.array([1.0, 1.0]))
    assert np.isclose(std, 1.118033988749895)