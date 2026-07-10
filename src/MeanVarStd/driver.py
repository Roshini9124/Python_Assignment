import numpy
from util import calculate_statistics

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

mean, var, std = calculate_statistics(arr)

print(mean)
print(var)
print(std)