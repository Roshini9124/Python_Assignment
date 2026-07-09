from util import runner_up_score

n = int(input())
scores = list(map(int, input().split()))

print(runner_up_score(scores))