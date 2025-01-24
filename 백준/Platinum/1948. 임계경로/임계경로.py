from collections import deque
import sys; input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))         # 위상정렬에 사용
    r_graph[b].append((a, c))       # 역추적에 사용
    in_degree[b] += 1               # 진입차수 설정

# 진입차수 0인 노드 설정
queue = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

start, end = map(int, input().split())

distance = [0] * (n+1)
while queue:
    cur = queue.popleft()
    for next_node, cost in graph[cur]:
        if distance[next_node] < distance[cur] + cost:
            # 거리 갱신
            distance[next_node] = distance[cur] + cost
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(distance[end])

# 역추적 도로 찾기
visited = [False] * (n+1)
queue = deque([end])
result = 0

while queue:
    cur = queue.popleft()
    for prev_node, cost in r_graph[cur]:
        if distance[prev_node] + cost == distance[cur]:
            result += 1
            if not visited[prev_node]:
                visited[prev_node] = True
                queue.append(prev_node)

print(result)