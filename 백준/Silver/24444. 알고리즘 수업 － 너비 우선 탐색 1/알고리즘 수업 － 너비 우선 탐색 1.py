from collections import deque
import sys; input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def bfs(node):
    queue = deque([node])
    cnt = 1
    visited[node] = cnt

    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)
                cnt += 1
                visited[next_node] = cnt

    print(*visited[1:], sep='\n')

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름 차순 정렬
for item in graph:
    item.sort()

bfs(r)
