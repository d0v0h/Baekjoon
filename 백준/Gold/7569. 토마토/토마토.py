from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[] for _ in range(h)]

for z in range(h):
    for y in range(n):
        graph[z].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append((x, y, z))

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nx, ny, nz))

def day_cal(tomatos):
    max_day = 0
    for tomato in tomatos:
        for item in tomato:
            if 0 in item:
                return -1
            else:
                if max_day < max(item):
                    max_day = max(item)
    return max_day - 1

print(day_cal(graph))