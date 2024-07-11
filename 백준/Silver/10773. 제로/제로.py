from collections import deque

n = int(input())

result = deque()
for _ in range(n):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        result.pop()

print(sum(result))