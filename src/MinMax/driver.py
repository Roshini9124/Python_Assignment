import numpy
from util import min_max
n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(min_max(arr))
