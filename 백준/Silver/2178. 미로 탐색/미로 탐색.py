from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        moved_x = x + dx[i]
        moved_y = y + dy[i]
        
        if (0 <= moved_x < n) and (0 <= moved_y < m) and (graph[moved_x][moved_y]) == 1:
            queue.append([moved_x, moved_y])
            graph[moved_x][moved_y] = graph[x][y] + 1

print(graph[n-1][m-1])