from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 출발점은 익은 토마토
for x in range(m):
    for y in range(n):
        if graph[y][x] == 1:
            queue.append((x, y))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 탐색 범위 확인
        if 0 <= nx < m and 0 <= ny < n:
            # 익지 않은 토마토라면
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1       # 익은 토마토로 변경 + 변경된 날짜 반영
                queue.append((nx, ny))                # 익은 토마토이므로 추가

def cal_day(tomatos):
    max_day = 0
    for tomato in tomatos:
        if 0 in tomato:
            return -1
        else:
            if max_day < max(tomato):
                max_day = max(tomato)
    return max_day - 1

print(cal_day(graph))