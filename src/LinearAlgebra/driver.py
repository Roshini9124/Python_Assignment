import numpy
from util import determinant

n = int(input())

matrix = numpy.array([list(map(float, input().split())) for _ in range(n)])

print(determinant(matrix))