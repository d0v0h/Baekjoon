from collections import deque

n = int(input())
queue = deque(enumerate(list(map(int, input().split()))))

result = []
while queue:
    idx, r = queue.popleft()
    result.append(idx + 1)

    queue.rotate(-(r-1)) if r > 0 else queue.rotate(-r)

print(*result)