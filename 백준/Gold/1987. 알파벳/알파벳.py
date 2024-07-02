import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
for i in range(r):
    route = list(input().strip())
    graph.append(route)

check = set()
ans = 0

def DFS(x, y, count):
    global ans
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = max(ans, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in check:
                # 방문한 알파벳 체크를 위해 add
                check.add(graph[nx][ny])
                # 방문한 지점 기준 상,하,좌,우 탐색
                DFS(nx, ny, count+1)
                # 방문 지점으로부터 돌아올 때 방문 지점 삭제
                check.remove(graph[nx][ny])

check.add(graph[0][0])
DFS(0, 0, 1)
print(ans)