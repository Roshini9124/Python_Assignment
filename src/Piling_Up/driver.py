from util import can_stack

t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(can_stack(blocks))