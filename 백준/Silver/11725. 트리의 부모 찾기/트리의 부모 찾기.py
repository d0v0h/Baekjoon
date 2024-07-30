from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
result = {}
def BFS(node):
    queue.append(node)
    visited[node] = True

    while queue:
        x = queue.popleft()
        vertex = graph[x]

        for next_node in vertex:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                result[next_node] = x

BFS(1)
for i in range(2, n+1):
    print(result[i])