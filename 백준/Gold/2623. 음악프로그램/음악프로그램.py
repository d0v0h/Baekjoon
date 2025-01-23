from collections import deque
import sys; input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

# 그래프 설정
for _ in range(m):
    arr = list(map(int, input().split()))[1:]
    for i in range(len(arr) - 1):
        graph[arr[i]].append(arr[i+1])
        in_degree[arr[i+1]] += 1

# 진입 차수 0인 노드 설정
queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

# 위상 정렬
result = []
while queue:
    cur = queue.popleft()
    result.append(cur)
    for neighbor in graph[cur]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(result) == n:
    print(*result, sep='\n')
else:
    print(0)