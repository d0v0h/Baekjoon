from collections import deque
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]


def diffusion():
    new_graph = [[0] * c for _ in range(r)]

    # 공기 청정기 위치 보존
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                new_graph[i][j] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                cnt = 0 
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < r and 0 <= ny < c and new_graph[nx][ny] != -1:
                        new_graph[nx][ny] += graph[x][y] // 5
                        cnt += 1
                new_graph[x][y] += graph[x][y] - graph[x][y] // 5 * cnt
    
    return new_graph

def purifier():
    top = bottom = 0
    for i in range(r):
        if graph[i][0] == -1:
            top = i
            bottom = i + 1
            break

    # 위쪽 공기 순환 (반시계)
    for i in range(top-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(c-1):
        graph[0][i] = graph[0][i+1]
    for i in range(top):
        graph[i][c-1] = graph[i+1][c-1]
    for i in range(c-1, 0, -1):
        graph[top][i] = graph[top][i-1]
    graph[top][1] = 0

    # 아래쪽 공기 순환 (시계)
    for i in range(bottom+1, r-1):
        graph[i][0] = graph[i+1][0]
    for i in range(c-1):
        graph[r-1][i] = graph[r-1][i+1]
    for i in range(r-1, bottom, -1):
        graph[i][c-1] = graph[i-1][c-1]
    for i in range(c-1, 0, -1):
        graph[bottom][i] = graph[bottom][i-1]
    graph[bottom][1] = 0

for i in range(t):
    graph = diffusion()
    purifier()

result = 0
for x in range(r):
    for y in range(c):
        if graph[x][y] > 0:
            result += graph[x][y]

print(result)