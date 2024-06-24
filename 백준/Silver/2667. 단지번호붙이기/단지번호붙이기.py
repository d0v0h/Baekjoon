from collections import deque
import sys
input = sys.stdin.readline

t = int(input().strip())

graph = []
for _ in range(t):
    line = list(map(int, input().strip()))
    graph.append(line)

def BFS(x, y):
    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < t) and (0 <= ny < t) and (graph[nx][ny] == 1):
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1

    return count

results = []
for i in range(t):
    for j in range(t):
        if graph[i][j] == 1:
            results.append(BFS(i,j))

results.sort()
print(len(results))
for result in results:
    print(result)