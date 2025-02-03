import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(node):
    global cnt
    visited[node] = cnt
    cnt += 1
    graph[node].sort(reverse=True)

    for next_node in graph[node]:
        if not visited[next_node]:
            bfs(next_node)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(r)
print(*visited[1:], sep='\n')