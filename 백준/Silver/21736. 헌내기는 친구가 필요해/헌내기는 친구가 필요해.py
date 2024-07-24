from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

queue = deque()
def BFS(x,y):
    meet = 0
    queue.append((x,y))
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'P' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    meet += 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 'O' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    if meet:
        return meet
    else:
        return 'TT'

for x in range(n):
    for y in range(m):
        if graph[x][y] == 'I':
            print(BFS(x,y))