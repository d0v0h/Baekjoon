from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    route = list(map(int, input().strip()))
    graph.append(route)

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

def BFS(x, y, is_break):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y, is_break))
    visited[x][y][is_break] = 1

    while queue:
        x, y, is_break = queue.popleft()

        # 도착지점에 방문한 경우
        if x == n-1 and y == m-1:
            return visited[x][y][is_break]
    
        # 상,하,좌,우 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # n, m을 벗어나지 않는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 지점이 벽이고 벽을 한번도 안부신 경우
                if not is_break and graph[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1   # 이전 방문 경로 값에 + 1
                    queue.append((nx, ny, 1))
                
                # 이동 경로 지점이 단순하게 방문 가능한 지점이고 방문하지 않은 경우
                elif graph[nx][ny] == 0 and not visited[nx][ny][is_break]:
                    visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                    queue.append((nx, ny, is_break))
    return -1

print(BFS(0, 0, 0))