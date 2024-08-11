from collections import deque
import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def various(graph):
    queue = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = 2
    
    return graph

max_val = -1

def well(cnt):
    global max_val
    if cnt == 3:
        new_graph = various(copy.deepcopy(graph))
        result = 0
        for i in range(n):
            for j in range(m):
                if new_graph[i][j] == 0:
                    result += 1
        if result > max_val:
            max_val = result
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                well(cnt+1)
                graph[i][j] = 0

well(0)
print(max_val)