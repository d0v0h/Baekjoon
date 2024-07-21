from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = []
graph_2 = []
queue = deque()

for _ in range(n):
    color = input().strip()
    graph.append(list(color))
    graph_2.append(list(color.replace('R', 'G')))

def BFS(x, y):
    queue.append((x, y))
    visited[x][y] = True
    color = graph[x][y]

    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return 1

result = 0
visited = [[False] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            result += BFS(x, y)
print(result, end=' ')

result = 0
graph = graph_2
visited = [[False] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            result += BFS(x, y)
print(result)