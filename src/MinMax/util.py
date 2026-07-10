import numpy

def min_max(arr):
    return numpy.max(numpy.min(arr, axis=1))