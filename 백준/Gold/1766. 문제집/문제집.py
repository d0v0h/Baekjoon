import heapq
import sys; input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

# 진입 차수 0인 노드를 우선순위 큐에 입력 (선행 문제)
queue = []
for i in range(n + 1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)

# 위상 정렬
result = []
while queue:
    cur = heapq.heappop(queue)
    result.append(cur)
    for neighbor in graph[cur]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(queue, neighbor)

print(*result[1:])