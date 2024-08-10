from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 아기 상어 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

def BFS(x, y, size):
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    dist[x][y] = 0
    info = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

                    if 0 < graph[nx][ny] < size:
                        # 먹을 수 있는 물고기까지의 거리와 좌표를 저장
                        info.append((dist[nx][ny], nx, ny))
    
    info.sort()
    return info

size = 2
eat = 0
time = 0

prob = len(BFS(x, y, size))

while prob:
    result = BFS(x, y, size)
    prob = len(result)
    if len(result) != 0:
        time += result[0][0]
        eat_x, eat_y = result[0][1], result[0][2]
        x, y = eat_x, eat_y
        eat += 1
        graph[eat_x][eat_y] = 0
    
    if eat >= size:
        size += 1
        eat = 0

print(time)