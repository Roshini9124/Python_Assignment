from util import calculate_happiness

n, m = map(int, input().split())
values = input().split()
a = set(input().split())
b = set(input().split())

result = calculate_happiness(values, a, b)
print(result)