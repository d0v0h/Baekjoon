from collections import deque
import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(n):
    visited[n] = 1
    for node in graph[n]:
        if visited[node] == 0:
            DFS(node)

DFS(1)
print(sum(visited)-1)