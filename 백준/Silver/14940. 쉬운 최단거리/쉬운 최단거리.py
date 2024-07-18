from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
queue = deque()

for i in range(n):
    graph[i] = (list(map(int, input().split())))

visitied = [[False]*m for _ in range(n)]
answers = [[0]*m for _ in range(n)]
def BFS(x, y):
    visitied[x][y] = True
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visitied[nx][ny] and graph[nx][ny] == 1:
                    visitied[nx][ny] = True
                    answers[nx][ny] = answers[x][y] + 1
                    queue.append((nx, ny))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            i, j = x, y

BFS(i, j)

for x in range(n):
    for y in range(m):
        if not visitied[x][y] and graph[x][y] == 1:
            answers[x][y] = -1

for answer in answers:
    print(*answer)