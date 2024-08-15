import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def DFS(x, y, shape):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return

    if 0 <= x < n and 0 <= y < n:
        # 파이프가 가로인 경우 (-> 가로, 대각선 이동 가능)
        if shape == 0:
            # 가로 이동
            if y+1 < n and graph[x][y+1] != 1:
                DFS(x, y+1, 0)
            # 대각선 이동
            if x+1 < n and y+1 < n and graph[x][y+1] != 1 and graph[x+1][y] != 1 and graph[x+1][y+1] != 1:
                DFS(x+1, y+1, 2)
        # 파이프가 세로인 경우
        elif shape == 1:
            # 세로 이동
            if x+1 < n and graph[x+1][y] != 1:
                DFS(x+1, y, 1)
            # 대각선 이동
            if x+1 < n and y+1 < n and graph[x][y+1] != 1 and graph[x+1][y] != 1 and graph[x+1][y+1] != 1:
                DFS(x+1, y+1, 2)
        else:
            # 가로 이동
            if y+1 < n and graph[x][y+1] != 1:
                DFS(x, y+1, 0)
            # 세로 이동
            if x+1 < n and graph[x+1][y] != 1:
                DFS(x+1, y, 1)
            # 대각선 이동
            if x+1 < n and y+1 < n and graph[x][y+1] != 1 and graph[x+1][y] != 1 and graph[x+1][y+1] != 1:
                DFS(x+1, y+1, 2)

cnt = 0
# 0: 가로, 1: 세로, 2: 대각선
DFS(0, 1, 0)
print(cnt)