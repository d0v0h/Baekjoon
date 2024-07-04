from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def BFS():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 치즈 발견시
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                # 치즈가 아닌 경우
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

ans = 0
is_check_cheese = True
while is_check_cheese:
    visited = [[0] * m for _ in range(n)]
    BFS()
    ans += 1
    is_check_cheese = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                is_check_cheese = True
            elif graph[i][j] == 2:
                graph[i][j] = 1

print(ans - 1)