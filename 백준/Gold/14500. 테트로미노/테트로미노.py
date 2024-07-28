import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
def DFS(x, y, cnt, total):
    global result
    if cnt == 3:
        result = max(result, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if cnt == 1:
                DFS(x, y, cnt+1, total + graph[nx][ny])
            DFS(nx, ny, cnt+1, total + graph[nx][ny])
            visited[nx][ny] = False

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        DFS(x, y, 0, graph[x][y])
        visited[x][y] = False
print(result)