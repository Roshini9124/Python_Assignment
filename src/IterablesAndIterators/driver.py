from util import calculate_probability

n = int(input())
letters = input().split()
k = int(input())

print(calculate_probability(letters, k))