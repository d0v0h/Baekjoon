import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

order = 1
def DFS(node):
    global order
    visited[node] = order

    for next_node in graph[node]:
        if not visited[next_node]:
            order += 1
            DFS(next_node)

DFS(r)

print(*visited[1:], sep='\n')