import numpy

def calculate_statistics(arr):
    mean = numpy.mean(arr, axis=1)
    var = numpy.var(arr, axis=0)
    std = numpy.std(arr)
    return mean, var, std