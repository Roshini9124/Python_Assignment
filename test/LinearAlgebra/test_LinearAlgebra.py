import numpy as np
from src.LinearAlgebra.util import determinant


def test_determinant():
    matrix = np.array([
        [1.1, 1.1],
        [1.1, 1.1]
    ])

    assert determinant(matrix) == 0.0