import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

visitied = [False] * (n+1)
def DFS(node):
    visitied[node] = True

    for next_node in graph[node]:
        if not visitied[next_node]:
            DFS(next_node)

count = 0
for node in range(1, n+1):
    if not visitied[node]:
        DFS(node)
        count += 1

print(count)