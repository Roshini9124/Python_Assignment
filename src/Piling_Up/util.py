from collections import deque

def can_stack(blocks):
    cubes = deque(blocks)
    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            return "No"

        last = current

    return "Yes"